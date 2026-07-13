#!/usr/bin/env python3
"""
learn — black-box verb: headless claude writes the 原文结构精读 + step-annotated
whiteboard diagram for one raw/ source; the shell verifies from disk.

Pattern identical to ingest_url.py (agent inside, contract outside): the spawned
agent does only the generative part via the /learn-note command; everything
deterministic lives here — idempotency precheck (jingdu + steps.json both
present → no-op, never burns tokens), disk verification, thesis extraction
(gate-packet Hook), cleanup of invalid files created by this run, envelope.

Envelope / exit codes: contract 1.0, same shape as obsidian_content.py.
Error tokens (errors[0]): usage | source_missing | agent_failed |
jingdu_missing | jingdu_invalid | visual_incomplete.

Test seam: LEARN_CLAUDE_CMD substitutes the spawned binary
(tests/test_learn_note.py drives it with FAKE_MODE, offline).

Stdlib only — Python 3.11+.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

CONTRACT_VERSION = "1.0"
VERB = "learn"

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "raw"
WIKI_DIR = REPO_ROOT / "wiki"
VISUALS_DIR = REPO_ROOT / "visuals"
EVENTS_FILE = REPO_ROOT / "events" / "ingest-events.jsonl"

MIN_JINGDU_BYTES = 1500
DEFAULT_TIMEOUT = 2400
DEFAULT_MAX_TURNS = 60
# The render→view→fix loop needs Bash (uv run render_excalidraw.py).
ALLOWED_TOOLS = "Read,Write,Edit,Glob,Grep,Bash"
THESIS_RE = re.compile(r"^\*\*一句话主旨\*\*：(.+)$", re.MULTILINE)
SLUG_RE = re.compile(r"^(?:\d{4}-\d{2}-\d{2}-)?([a-z0-9][a-z0-9-]*)$")


def emit(ok: bool, artifacts: dict, warnings: list[str], errors: list[str]) -> int:
    print(json.dumps({
        "contract_version": CONTRACT_VERSION,
        "ok": ok,
        "verb": VERB,
        "artifacts": artifacts,
        "warnings": warnings,
        "errors": errors,
    }, ensure_ascii=False, indent=2))
    return 0 if ok else 1


# ── deterministic helpers ─────────────────────────────────────────────────────

def sha16(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def event_id_for(source_path: str) -> str:
    norm = source_path.strip().replace("\\", "/")
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]


def slug_for(source_rel: str) -> str | None:
    stem = Path(source_rel).stem
    m = SLUG_RE.match(stem)
    return m.group(1) if m else None


def resolve_source_from_event(event_id: str) -> str | None:
    if not EVENTS_FILE.exists():
        return None
    for ln in EVENTS_FILE.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        try:
            r = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if r.get("type") == "ingest" and r.get("event_id") == event_id:
            return r.get("source_path")
    return None


def jingdu_state(jingdu: Path) -> dict:
    """What the shell can verify about the 精读 file. Disk is the only witness."""
    out = {"exists": False, "has_section": False, "thesis": None, "bytes": 0}
    if not jingdu.exists():
        return out
    text = jingdu.read_text(encoding="utf-8", errors="replace")
    out["exists"] = True
    out["bytes"] = len(text.encode("utf-8"))
    out["has_section"] = "## 精读" in text
    m = THESIS_RE.search(text)
    if m:
        out["thesis"] = m.group(1).strip()
    return out


def visual_state(vdir: Path, slug: str) -> dict:
    """Verify the visual bundle: steps.json parses, every layer exists, png exists."""
    out = {"complete": False, "steps": None, "missing": [], "dir": None,
           "png": None, "excalidraw": None, "steps_json_hash": None}
    steps_json = vdir / "steps.json"
    png = vdir / f"{slug}-diagram.png"
    exc = vdir / f"{slug}-diagram.excalidraw"
    if not steps_json.exists():
        out["missing"].append("steps.json")
        return out
    try:
        meta = json.loads(steps_json.read_text(encoding="utf-8"))
        steps = meta.get("steps") or []
    except (json.JSONDecodeError, OSError) as e:
        out["missing"].append(f"steps.json unparseable: {e}")
        return out
    if not steps:
        out["missing"].append("steps.json has no steps")
    for s in steps:
        f = vdir / (s.get("file") or "")
        if not f.exists():
            out["missing"].append(s.get("file") or "<unnamed layer>")
    if not png.exists():
        out["missing"].append(png.name)
    if not exc.exists():
        out["missing"].append(exc.name)
    if not out["missing"]:
        out.update({
            "complete": True, "steps": len(steps),
            "dir": vdir.relative_to(REPO_ROOT).as_posix(),
            "png": png.relative_to(REPO_ROOT).as_posix(),
            "excalidraw": exc.relative_to(REPO_ROOT).as_posix(),
            "steps_json_hash": sha16(steps_json),
        })
    return out


# ── agent spawn ───────────────────────────────────────────────────────────────

def claude_argv(prompt: str, max_turns: int) -> list[str]:
    override = os.environ.get("LEARN_CLAUDE_CMD")
    base = shlex.split(override) if override else ["claude"]
    return base + ["-p", prompt,
                   "--allowedTools", ALLOWED_TOOLS,
                   "--max-turns", str(max_turns),
                   "--output-format", "json"]


def spawn_agent(source_rel: str, slug: str, skip_visual: bool,
                max_turns: int, timeout: int) -> tuple[dict, list[str]]:
    env = dict(os.environ)
    # claude / uv are not on PATH in VPS cron contexts — extend defensively.
    extra = f"{Path.home()}/.npm-global/bin:{Path.home()}/.local/bin"
    env["PATH"] = f"{env.get('PATH', '')}:{extra}"
    prompt = f"/learn-note {source_rel} {slug}" + (" skip-visual" if skip_visual else "")
    meta: dict = {"timed_out": False, "exit_code": None,
                  "num_turns": None, "duration_ms": None, "result_tail": None}
    warnings: list[str] = []
    try:
        proc = subprocess.run(claude_argv(prompt, max_turns),
                              capture_output=True, text=True, cwd=REPO_ROOT,
                              timeout=timeout, env=env)
        meta["exit_code"] = proc.returncode
        try:
            payload = json.loads(proc.stdout)
            meta["num_turns"] = payload.get("num_turns")
            meta["duration_ms"] = payload.get("duration_ms")
            meta["total_cost_usd"] = payload.get("total_cost_usd")
            meta["result_tail"] = (payload.get("result") or "")[-400:]
        except json.JSONDecodeError:
            meta["result_tail"] = (proc.stdout or proc.stderr)[-400:]
            warnings.append("agent stdout was not JSON; verifying from disk only")
    except subprocess.TimeoutExpired:
        meta["timed_out"] = True
        warnings.append(f"agent timed out after {timeout}s; verifying from disk anyway")
    except FileNotFoundError as e:
        meta["result_tail"] = f"spawn failed: {e}"
        meta["exit_code"] = -1
    return meta, warnings


# ── main verb ─────────────────────────────────────────────────────────────────

def cmd_learn(args) -> int:
    warnings: list[str] = []

    source_rel = (args.source or "").strip()
    if not source_rel and args.event_id:
        source_rel = resolve_source_from_event(args.event_id.strip()) or ""
        if not source_rel:
            return emit(False, {"event_id": args.event_id}, warnings,
                        ["usage", f"unknown event_id: {args.event_id}"])
    if not source_rel:
        return emit(False, {}, warnings, ["usage", "--source or --event-id is required"])

    src = REPO_ROOT / source_rel
    if not src.exists():
        return emit(False, {"source_path": source_rel}, warnings,
                    ["source_missing", source_rel])

    slug = slug_for(source_rel)
    if not slug:
        return emit(False, {"source_path": source_rel}, warnings,
                    ["usage", f"cannot derive slug from {source_rel}"])

    jingdu = WIKI_DIR / f"source-{slug}.md"
    vdir = VISUALS_DIR / slug
    jd = jingdu_state(jingdu)
    vs = visual_state(vdir, slug)

    def artifacts(jd: dict, vs: dict, agent: dict | None,
                  no_visual_reason: str | None = None) -> dict:
        return {
            "source_path": source_rel,
            "slug": slug,
            "event_id": event_id_for(source_rel),
            "jingdu_path": jingdu.relative_to(REPO_ROOT).as_posix(),
            "jingdu_hash": sha16(jingdu) if jd["exists"] else None,
            "jingdu_bytes": jd["bytes"],
            "thesis": jd["thesis"],
            "visual": {k: vs[k] for k in
                       ("dir", "png", "excalidraw", "steps", "steps_json_hash")}
                      if vs["complete"] else None,
            "no_visual_reason": no_visual_reason,
            "agent": agent,
        }

    # 1. Idempotency precheck — both artifacts already present → no-op.
    if not args.force and jd["exists"] and jd["has_section"] and vs["complete"]:
        warnings.append(f"learn artifacts already exist for {slug}; no-op — agent not spawned")
        return emit(True, artifacts(jd, vs, None), warnings, [])

    if args.dry_run:
        warnings.append("dry-run: agent not spawned, nothing written")
        return emit(True, {"source_path": source_rel, "slug": slug,
                           "would_spawn": True,
                           "jingdu_exists": jd["exists"],
                           "visual_complete": vs["complete"]}, warnings, [])

    # 2. Snapshot → spawn → verify from disk.
    jingdu_preexisting = jd["exists"]
    vdir_preexisting = vdir.exists()
    meta, spawn_warnings = spawn_agent(source_rel, slug, args.skip_visual,
                                       args.max_turns, args.timeout)
    warnings.extend(spawn_warnings)
    tail = meta.get("result_tail") or ""

    def cleanup_this_run() -> None:
        """Remove invalid artifacts created by this run; never touch pre-existing."""
        removed = []
        if not jingdu_preexisting and jingdu.exists():
            jingdu.unlink()
            removed.append(jingdu.name)
        if not vdir_preexisting and vdir.exists():
            import shutil
            shutil.rmtree(vdir, ignore_errors=True)
            removed.append(f"{vdir.name}/")
        if removed:
            warnings.append(f"deleted invalid artifact(s) created by this run: {', '.join(removed)}")

    m = re.search(r"LEARN_FAILED=(.+)", tail)
    if m:
        cleanup_this_run()
        return emit(False, {"source_path": source_rel, "slug": slug, "agent": meta},
                    warnings, ["agent_failed", m.group(1).strip()])

    jd = jingdu_state(jingdu)
    if not jd["exists"]:
        if meta["timed_out"] or (meta["exit_code"] not in (0, None)):
            return emit(False, {"source_path": source_rel, "slug": slug, "agent": meta},
                        warnings, ["agent_failed",
                                   f"exit={meta['exit_code']} timed_out={meta['timed_out']}"])
        return emit(False, {"source_path": source_rel, "slug": slug, "agent": meta},
                    warnings, ["jingdu_missing"])

    problems = []
    if not jd["has_section"]:
        problems.append("missing '## 精读' section")
    if not jd["thesis"]:
        problems.append("missing '**一句话主旨**：' line")
    if jd["bytes"] < MIN_JINGDU_BYTES:
        problems.append(f"{jd['bytes']} bytes < {MIN_JINGDU_BYTES}")
    if problems:
        cleanup_this_run()
        return emit(False, {"source_path": source_rel, "slug": slug, "agent": meta},
                    warnings, ["jingdu_invalid", "; ".join(problems)])

    # 3. Visual verification (unless skipped or agent declared not diagrammable).
    no_visual_reason = None
    nv = re.search(r"LEARN_NO_VISUAL=(.+)", tail)
    if args.skip_visual:
        no_visual_reason = "skip-visual requested"
    elif nv:
        no_visual_reason = nv.group(1).strip()
        warnings.append(f"agent judged source not diagrammable: {no_visual_reason}")

    vs = visual_state(vdir, slug)
    if no_visual_reason is None and not vs["complete"]:
        cleanup_this_run()
        return emit(False, {"source_path": source_rel, "slug": slug, "agent": meta,
                            "missing": vs["missing"]},
                    warnings, ["visual_incomplete", ", ".join(vs["missing"])])

    if vs["complete"] and f"![[{slug}-diagram.png]]" not in jingdu.read_text(encoding="utf-8"):
        warnings.append("diagram produced but not embedded in the 精读 note")

    return emit(True, artifacts(jd, vs, meta, no_visual_reason), warnings, [])


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="obsidian-content learn",
        description="Black-box verb: headless claude writes 精读 + whiteboard diagram; shell verifies.",
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--source", help="Raw source path, e.g. raw/2026-07-05-founder-mode.md")
    src.add_argument("--event-id", help="Ingest event_id to resolve the source from")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                   help=f"Agent wall-clock budget in seconds (default {DEFAULT_TIMEOUT})")
    p.add_argument("--max-turns", type=int, default=DEFAULT_MAX_TURNS,
                   help=f"Agent turn budget (default {DEFAULT_MAX_TURNS})")
    p.add_argument("--dry-run", action="store_true",
                   help="Idempotency precheck only; never spawns the agent")
    p.add_argument("--force", action="store_true",
                   help="Revision re-run even when artifacts already exist")
    p.add_argument("--skip-visual", action="store_true",
                   help="精读 only; skip the whiteboard diagram")
    return p


def main(argv: list[str] | None = None) -> int:
    # 内层 headless claude 会继承本进程 env；若带着会话的 TELEGRAM_STATE_DIR，
    # 其 telegram 插件会抢走 bot poller、瘫痪回话通道（07-05/07-13 事故根因）。
    os.environ.pop("TELEGRAM_STATE_DIR", None)
    args = build_parser().parse_args(argv)
    return cmd_learn(args)


if __name__ == "__main__":
    sys.exit(main())
