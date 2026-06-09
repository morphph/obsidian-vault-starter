#!/usr/bin/env python3
"""
obsidian-content — agent-native CLI for the Obsidian source layer.

This repo (`obsidian-vault-starter`) is the human-curated Tier-1 source layer of
an autonomous content system. The Hermes orchestration agent does NOT understand
this repo's internals; instead it calls this CLI, which exposes a stable contract.

Design contract (see docs/obsidian-content-cli.md):
- Every verb prints a single JSON envelope to stdout:
    { contract_version, ok, verb, artifacts, warnings, errors }
- Exit codes: 0 = ok, 1 = handled failure (ok:false), 2 = usage error (argparse).
- Verbs are idempotent where possible.
- Pure local file I/O. No SQLite writes, no git push, no network, no LLM calls.
- The source of truth is events/ingest-events.jsonl (append-only), NOT a raw/ scan
  (raw/ is full of auto-flushed session noise that is not Tier-1 curated material).

Stdlib only — runs on Python 3.11+ with no dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CONTRACT_VERSION = "1.0"
SCHEMA_VERSION = 1

REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_FILE = REPO_ROOT / "events" / "ingest-events.jsonl"
LOG_FILE = REPO_ROOT / "wiki" / "log.md"


# ── helpers ──────────────────────────────────────────────────────────────────

def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def event_id_for(source_path: str) -> str:
    """Stable id derived from the source path → re-recording is idempotent."""
    norm = source_path.strip().replace("\\", "/")
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]


def split_pages(value: str | None) -> list[str]:
    """Extract wiki page filenames from a free-text 'pages-created' string.

    Handles comma-separated lists with parenthetical annotations, e.g.
    'foo.md (entity), bar.md (updated X)' -> ['foo.md', 'bar.md'].
    """
    if not value:
        return []
    found = re.findall(r"[\w./-]+\.md", value)
    # de-dup while preserving order
    seen, out = set(), []
    for p in found:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def read_events() -> list[dict]:
    if not EVENTS_FILE.exists():
        return []
    records = []
    for ln in EVENTS_FILE.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        try:
            records.append(json.loads(ln))
        except json.JSONDecodeError:
            # tolerate a single corrupt line rather than failing the whole CLI
            continue
    return records


def append_event(record: dict) -> None:
    EVENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with EVENTS_FILE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def fold_state(records: list[dict]) -> dict[str, dict]:
    """Fold the append-only event log into current per-ingest state.

    'ingest' records create/refresh a state row; 'routed' records mark it routed.
    Folding is idempotent: replaying the same records yields the same state.
    """
    state: dict[str, dict] = {}
    for r in records:
        eid = r.get("event_id")
        if not eid:
            continue
        rtype = r.get("type")
        if rtype == "ingest":
            row = state.get(eid, {})
            row.update({
                "event_id": eid,
                "ts": r.get("ts"),
                "source_path": r.get("source_path"),
                "title": r.get("title"),
                "fetch_method": r.get("fetch_method"),
                "tier": r.get("tier", 1),
                "pages_created": r.get("pages_created", []),
                "pages_updated": r.get("pages_updated", []),
            })
            row.setdefault("routed", False)
            row.setdefault("routed_ts", None)
            row.setdefault("routed_by", None)
            row.setdefault("task_ref", None)
            state[eid] = row
        elif rtype == "routed":
            row = state.get(eid)
            if row is None:
                # routed before ingest seen — keep a stub so state is consistent
                row = {"event_id": eid, "pages_created": [], "pages_updated": []}
                state[eid] = row
            row["routed"] = True
            row["routed_ts"] = r.get("ts")
            row["routed_by"] = r.get("routed_by")
            row["task_ref"] = r.get("task_ref")
    return state


def ordered_state(state: dict[str, dict]) -> list[dict]:
    return sorted(state.values(), key=lambda r: (r.get("ts") or "", r.get("event_id")))


def emit(verb: str, ok: bool, artifacts: dict, warnings: list[str], errors: list[str]) -> int:
    print(json.dumps({
        "contract_version": CONTRACT_VERSION,
        "ok": ok,
        "verb": verb,
        "artifacts": artifacts,
        "warnings": warnings,
        "errors": errors,
    }, ensure_ascii=False, indent=2))
    return 0 if ok else 1


# ── verb: record-ingest ───────────────────────────────────────────────────────

def cmd_record_ingest(args) -> int:
    warnings: list[str] = []
    errors: list[str] = []

    source = (args.source or "").strip()
    if not source:
        errors.append("--source is required")
        return emit("record-ingest", False, {}, warnings, errors)

    eid = event_id_for(source)
    state = fold_state(read_events())

    # Idempotency: do not append a duplicate ingest record for the same source.
    if eid in state and state[eid].get("source_path"):
        warnings.append(f"ingest already recorded for {source} (event_id={eid}); no-op")
        return emit("record-ingest", True, {"event_id": eid, "recorded": False,
                                            "ingest": state[eid]}, warnings, errors)

    src_file = (REPO_ROOT / source).resolve()
    if not str(src_file).startswith(str(REPO_ROOT)):
        errors.append(f"--source must be inside the repo: {source}")
        return emit("record-ingest", False, {}, warnings, errors)
    if not src_file.exists():
        warnings.append(f"source file does not exist yet: {source}")

    record = {
        "type": "ingest",
        "schema_version": SCHEMA_VERSION,
        "event_id": eid,
        "ts": args.ts or now_iso(),
        "source_path": source,
        "title": args.title or src_file.stem,
        "fetch_method": args.fetch_method,
        "tier": args.tier,
        "pages_created": split_pages(args.pages_created),
        "pages_updated": split_pages(args.pages_updated),
    }

    if args.dry_run:
        warnings.append("dry-run: nothing written")
        return emit("record-ingest", True, {"event_id": eid, "recorded": False,
                                            "would_record": record}, warnings, errors)

    append_event(record)
    new_state = fold_state(read_events())
    return emit("record-ingest", True, {"event_id": eid, "recorded": True,
                                        "ingest": new_state.get(eid, record)}, warnings, errors)


# ── verb: list-ingests ────────────────────────────────────────────────────────

def cmd_list_ingests(args) -> int:
    warnings: list[str] = []
    errors: list[str] = []
    rows = ordered_state(fold_state(read_events()))

    if args.status == "new":
        rows = [r for r in rows if not r.get("routed")]
    elif args.status == "routed":
        rows = [r for r in rows if r.get("routed")]

    if args.since:
        rows = [r for r in rows if (r.get("ts") or "") >= args.since]

    total_matched = len(rows)
    if args.limit and args.limit > 0:
        rows = rows[-args.limit:] if args.newest else rows[:args.limit]

    return emit("list-ingests", True, {
        "status_filter": args.status,
        "count": len(rows),
        "total_matched": total_matched,
        "ingests": rows,
    }, warnings, errors)


# ── verb: export-source ───────────────────────────────────────────────────────

def cmd_export_source(args) -> int:
    warnings: list[str] = []
    errors: list[str] = []
    state = fold_state(read_events())
    row = state.get(args.id)
    if row is None:
        errors.append(f"unknown event_id: {args.id}")
        return emit("export-source", False, {}, warnings, errors)

    source = row.get("source_path")
    if not source:
        errors.append(f"event {args.id} has no source_path")
        return emit("export-source", False, {}, warnings, errors)

    src_file = (REPO_ROOT / source).resolve()
    if not src_file.exists():
        errors.append(f"source file missing: {source}")
        return emit("export-source", False, {"event_id": args.id, "source_path": source},
                    warnings, errors)

    content = src_file.read_text(encoding="utf-8")
    nbytes = len(content.encode("utf-8"))

    artifacts = {
        "event_id": args.id,
        "source_path": source,
        "title": row.get("title"),
        "bytes": nbytes,
    }

    if args.out:
        out_path = Path(args.out)
        if not out_path.is_absolute():
            out_path = (REPO_ROOT / out_path)
        if args.dry_run:
            warnings.append("dry-run: nothing written")
            artifacts["would_write_to"] = str(out_path)
        else:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            artifacts["written_to"] = str(out_path)
    else:
        artifacts["content"] = content

    return emit("export-source", True, artifacts, warnings, errors)


# ── verb: mark-routed ─────────────────────────────────────────────────────────

def cmd_mark_routed(args) -> int:
    warnings: list[str] = []
    errors: list[str] = []
    state = fold_state(read_events())
    row = state.get(args.id)
    if row is None or not row.get("source_path"):
        errors.append(f"unknown event_id: {args.id}")
        return emit("mark-routed", False, {}, warnings, errors)

    if row.get("routed"):
        warnings.append(f"event {args.id} already routed; no-op")
        return emit("mark-routed", True, {"event_id": args.id, "routed": True,
                                          "changed": False, "ingest": row}, warnings, errors)

    record = {
        "type": "routed",
        "schema_version": SCHEMA_VERSION,
        "event_id": args.id,
        "ts": now_iso(),
        "routed_by": args.by,
        "task_ref": args.task_ref,
    }

    if args.dry_run:
        warnings.append("dry-run: nothing written")
        return emit("mark-routed", True, {"event_id": args.id, "routed": False,
                                          "changed": False, "would_record": record},
                    warnings, errors)

    append_event(record)
    new_row = fold_state(read_events()).get(args.id)
    return emit("mark-routed", True, {"event_id": args.id, "routed": True,
                                      "changed": True, "ingest": new_row}, warnings, errors)


# ── verb: backfill-from-log ───────────────────────────────────────────────────

_HEADER_RE = re.compile(r"^##\s*\[(\d{4}-\d{2}-\d{2})\]\s*ingest\s*\|\s*(.+?)\s*$")


def parse_log_ingests() -> list[dict]:
    """Parse wiki/log.md ingest blocks into provisional ingest records.

    Handles both `source:` (single) and `sources:` (multi-line `  - raw/...`) forms.
    One emitted record per source file.
    """
    if not LOG_FILE.exists():
        return []
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()

    # split into blocks starting at each '## ' header
    blocks: list[list[str]] = []
    cur: list[str] | None = None
    for ln in lines:
        if ln.startswith("## "):
            if cur is not None:
                blocks.append(cur)
            cur = [ln]
        elif cur is not None:
            cur.append(ln)
    if cur is not None:
        blocks.append(cur)

    out: list[dict] = []
    for block in blocks:
        m = _HEADER_RE.match(block[0])
        if not m:
            continue
        date, title = m.group(1), m.group(2)
        ts = f"{date}T00:00:00+00:00"
        fetch_method = None
        sources: list[str] = []
        pages_created = ""
        pages_updated = ""
        in_sources = False
        for ln in block[1:]:
            s = ln.strip()
            if s.startswith("source:"):
                sources.append(s[len("source:"):].strip())
                in_sources = False
            elif s.startswith("sources:"):
                in_sources = True
            elif in_sources and s.startswith("-"):
                sources.append(s.lstrip("- ").strip())
            elif s.startswith("fetch-method:"):
                fetch_method = s[len("fetch-method:"):].strip()
                in_sources = False
            elif s.startswith("pages-created:"):
                pages_created = s[len("pages-created:"):].strip()
                in_sources = False
            elif s.startswith("pages-updated:"):
                pages_updated = s[len("pages-updated:"):].strip()
                in_sources = False
        for raw_src in sources:
            # strip trailing parenthetical annotations like '(Raj Pathak + ...)'
            src = re.sub(r"\s*\(.*\)\s*$", "", raw_src).strip()
            tok = re.search(r"[\w./-]+\.md", src)
            src = tok.group(0) if tok else src
            if not src:
                continue
            out.append({
                "ts": ts,
                "title": title,
                "fetch_method": fetch_method,
                "source_path": src,
                "pages_created": split_pages(pages_created),
                "pages_updated": split_pages(pages_updated),
            })
    return out


def cmd_backfill_from_log(args) -> int:
    warnings: list[str] = []
    errors: list[str] = []
    if not LOG_FILE.exists():
        errors.append(f"log not found: {LOG_FILE}")
        return emit("backfill-from-log", False, {}, warnings, errors)

    parsed = parse_log_ingests()
    state = fold_state(read_events())

    added, skipped, skipped_missing = [], [], []
    for p in parsed:
        eid = event_id_for(p["source_path"])
        if eid in state and state[eid].get("source_path"):
            skipped.append(eid)
            continue
        # Historical seed: only backfill ingests whose curated source still exists.
        # A missing path means the raw file was later renamed/removed (see log
        # `raw-renamed:` corrections); seeding it would create a permanently
        # unexportable 'new' item in Hermes's queue.
        if not (REPO_ROOT / p["source_path"]).exists():
            skipped_missing.append(p["source_path"])
            continue
        record = {
            "type": "ingest",
            "schema_version": SCHEMA_VERSION,
            "event_id": eid,
            "ts": p["ts"],
            "source_path": p["source_path"],
            "title": p["title"],
            "fetch_method": p["fetch_method"],
            "tier": 1,
            "pages_created": p["pages_created"],
            "pages_updated": p["pages_updated"],
            "backfilled": True,
        }
        if not args.dry_run:
            append_event(record)
            state[eid] = {"source_path": p["source_path"]}  # mark seen within this run
        added.append(eid)

    if args.dry_run:
        warnings.append("dry-run: nothing written")

    if skipped_missing:
        warnings.append(
            f"{len(skipped_missing)} log source(s) skipped — file no longer exists "
            f"(renamed/removed): {', '.join(skipped_missing)}"
        )

    return emit("backfill-from-log", True, {
        "scanned": len(parsed),
        "added": len(added),
        "skipped_existing": len(skipped),
        "skipped_missing": len(skipped_missing),
        "added_ids": added,
    }, warnings, errors)


# ── argparse ──────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="obsidian-content",
        description="Agent-native CLI for the Obsidian Tier-1 source layer.",
    )
    p.add_argument("--version", action="version",
                   version=f"obsidian-content contract {CONTRACT_VERSION} schema {SCHEMA_VERSION}")
    sub = p.add_subparsers(dest="verb", required=True)

    pr = sub.add_parser("record-ingest", help="Append a Tier-1 ingest event (called by /ingest).")
    pr.add_argument("--source", required=True, help="Path to the curated source, e.g. raw/2026-...md")
    pr.add_argument("--title")
    pr.add_argument("--fetch-method")
    pr.add_argument("--pages-created", help="Comma-separated wiki pages created")
    pr.add_argument("--pages-updated", help="Comma-separated wiki pages updated")
    pr.add_argument("--tier", type=int, default=1)
    pr.add_argument("--ts", help="ISO8601 timestamp override (default: now)")
    pr.add_argument("--dry-run", action="store_true")
    pr.set_defaults(func=cmd_record_ingest)

    pl = sub.add_parser("list-ingests", help="List ingests for Hermes discovery.")
    pl.add_argument("--status", choices=["new", "routed", "all"], default="new")
    pl.add_argument("--since", help="ISO date/datetime lower bound, e.g. 2026-05-01")
    pl.add_argument("--limit", type=int, default=0)
    pl.add_argument("--newest", action="store_true",
                    help="With --limit, take the newest N instead of the oldest N")
    pl.set_defaults(func=cmd_list_ingests)

    pe = sub.add_parser("export-source", help="Emit clean curated markdown for a given ingest.")
    pe.add_argument("--id", required=True, help="event_id from list-ingests")
    pe.add_argument("--out", help="Write content to this path instead of returning it inline")
    pe.add_argument("--dry-run", action="store_true")
    pe.set_defaults(func=cmd_export_source)

    pm = sub.add_parser("mark-routed", help="Mark an ingest routed (idempotent).")
    pm.add_argument("--id", required=True, help="event_id from list-ingests")
    pm.add_argument("--by", default="hermes")
    pm.add_argument("--task-ref", help="Optional downstream task reference")
    pm.add_argument("--dry-run", action="store_true")
    pm.set_defaults(func=cmd_mark_routed)

    pb = sub.add_parser("backfill-from-log",
                        help="One-time idempotent seed of events from wiki/log.md.")
    pb.add_argument("--dry-run", action="store_true")
    pb.set_defaults(func=cmd_backfill_from_log)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
