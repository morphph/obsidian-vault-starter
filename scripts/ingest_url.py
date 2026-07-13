#!/usr/bin/env python3
"""
ingest-url — black-box verb: headless claude fetches a URL into raw/, the shell verifies.

Pattern (content-ops plan §1 v2.6): agent inside, contract outside. The spawned
agent does ONLY the non-deterministic part — fetch the URL (smart fetch chain)
and write raw/{date}-{slug}.md. Everything else is deterministic and lives here:
idempotency precheck (by URL, so a repeat call never burns tokens), raw/ diff
verification, event recording via the record-ingest verb, hashing, envelope.
The shell trusts artifacts on disk, never the agent's self-report.

Envelope / exit codes are identical in shape to obsidian_content.py (contract 1.0):
  { contract_version, ok, verb, artifacts, warnings, errors }
  0 = ok, 1 = handled failure (ok:false), 2 = usage error (argparse).

Error tokens (errors[0]): fetch_failed | raw_missing | multiple_new_files |
header_mismatch | content_too_small | event_record_failed.
Invalid files created by the current run are deleted so they cannot poison a
later idempotency precheck; files from earlier runs are never touched.

Test seam: set INGEST_URL_CLAUDE_CMD to substitute the spawned binary (used by
tests/test_ingest_url.py to exercise all paths offline, without claude/Max).

Stdlib only — Python 3.11+.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

CONTRACT_VERSION = "1.0"
VERB = "ingest-url"

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "raw"
OBSIDIAN_CONTENT = REPO_ROOT / "scripts" / "obsidian_content.py"

MIN_BYTES = 500
DEFAULT_TIMEOUT = 420
DEFAULT_MAX_TURNS = 15
ALLOWED_TOOLS = "WebFetch,Read,Write,mcp__playwright__*"
FILENAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*\.md$")

# Proven recipe — identical to the 2026-07-05 golden-sample run (7 turns, 91s,
# WebFetch → Playwright MCP fallback verified live). Keep changes deliberate.
RECIPE = """You are running headlessly inside the obsidian-vault-starter repo (cwd = repo root). Task: capture ONE web article as a Tier-1 raw source file. Do ONLY this — no wiki pages, no index/log updates, no record-ingest call, no git.

URL: {url}

Steps:
1. Fetch the URL content using the smart fetch chain:
   - twitter.com / x.com / youtube.com / reddit.com / linkedin.com / instagram.com URLs → use Playwright MCP directly (browser_navigate, wait for load, browser_snapshot, extract main content, close browser when done).
   - All other URLs → try WebFetch first. If WebFetch fails or returns empty/partial/unusable content, fall back to Playwright MCP as above.
2. Write the full article to raw/{{YYYY-MM-DD}}-{{slug}}.md where {{YYYY-MM-DD}} is today's date and {{slug}} is a short kebab-case slug derived from the article title. The file MUST start with exactly this header block:

# {{Article Title}}

**Source:** {url}
**Fetch method:** {{the method you actually used, e.g. WebFetch or Playwright MCP}}

followed by the article content in clean markdown: preserve headings, paragraphs, lists and code blocks; keep images as URL references (do not download anything); no commentary of your own.
3. Do not create or modify any other file.
4. If you could not obtain usable article content after both methods, do NOT write a file; output the single line INGEST_FAILED={{one-line reason}} and stop.
5. On success your final output line must be exactly: INGEST_RAW_PATH=raw/{{filename}}.md
"""


# ── envelope ──────────────────────────────────────────────────────────────────

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

def content_hash_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]

def event_id_for(source_path: str) -> str:
    # Must mirror obsidian_content.event_id_for (verified by tests).
    norm = source_path.strip().replace("\\", "/")
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]

def header_fields(path: Path) -> dict:
    """Extract title / source url / fetch method from the raw-file header block."""
    out = {"title": None, "url": None, "fetch_method": None}
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[:8]
    except OSError:
        return out
    for ln in lines:
        s = ln.strip()
        if s.startswith("# ") and out["title"] is None:
            out["title"] = s[2:].strip()
        elif s.startswith("**Source:**"):
            out["url"] = s[len("**Source:**"):].strip()
        elif s.startswith("**Fetch method:**"):
            out["fetch_method"] = s[len("**Fetch method:**"):].strip()
    return out

def find_existing_capture(url: str) -> Path | None:
    """Idempotency precheck: is there already a raw file whose header cites this URL?"""
    if not RAW_DIR.is_dir():
        return None
    for f in sorted(RAW_DIR.glob("*.md")):
        try:
            if f.stat().st_size < MIN_BYTES:
                continue
        except OSError:
            continue
        if header_fields(f)["url"] == url:
            return f
    return None

def run_record_ingest(source_rel: str, title: str | None, fetch_method: str | None) -> dict:
    """Record the ingest event through the real verb (same boundary /ingest uses)."""
    cmd = [sys.executable, str(OBSIDIAN_CONTENT), "record-ingest", "--source", source_rel]
    if title:
        cmd += ["--title", title]
    if fetch_method:
        cmd += ["--fetch-method", fetch_method]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    try:
        env = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "_raw": proc.stdout[-500:], "_stderr": proc.stderr[-500:]}
    return env


# ── agent spawn ───────────────────────────────────────────────────────────────

def claude_argv(prompt: str, max_turns: int) -> list[str]:
    override = os.environ.get("INGEST_URL_CLAUDE_CMD")
    if override:
        base = shlex.split(override)
    else:
        base = ["claude"]
    return base + ["-p", prompt,
                   "--allowedTools", ALLOWED_TOOLS,
                   "--max-turns", str(max_turns),
                   "--output-format", "json"]

def spawn_agent(url: str, max_turns: int, timeout: int) -> tuple[dict, list[str]]:
    """Run the headless agent. Returns (meta, warnings). Never raises."""
    env = dict(os.environ)
    # claude is not on PATH in VPS cron/scripts contexts — extend defensively.
    extra = f"{Path.home()}/.npm-global/bin:{Path.home()}/.local/bin"
    env["PATH"] = f"{env.get('PATH', '')}:{extra}"
    meta: dict = {"timed_out": False, "exit_code": None,
                  "num_turns": None, "duration_ms": None, "result_tail": None}
    warnings: list[str] = []
    try:
        proc = subprocess.run(claude_argv(RECIPE.format(url=url), max_turns),
                              capture_output=True, text=True, cwd=REPO_ROOT,
                              timeout=timeout, env=env)
        meta["exit_code"] = proc.returncode
        try:
            payload = json.loads(proc.stdout)
            meta["num_turns"] = payload.get("num_turns")
            meta["duration_ms"] = payload.get("duration_ms")
            meta["total_cost_usd"] = payload.get("total_cost_usd")
            meta["result_tail"] = (payload.get("result") or "")[-300:]
        except json.JSONDecodeError:
            meta["result_tail"] = (proc.stdout or proc.stderr)[-300:]
            warnings.append("agent stdout was not JSON; verifying from disk only")
    except subprocess.TimeoutExpired:
        meta["timed_out"] = True
        warnings.append(f"agent timed out after {timeout}s; verifying from disk anyway")
    except FileNotFoundError as e:
        meta["result_tail"] = f"spawn failed: {e}"
        meta["exit_code"] = -1
    return meta, warnings


# ── main verb ─────────────────────────────────────────────────────────────────

def cmd_ingest_url(args) -> int:
    warnings: list[str] = []
    url = (args.url or "").strip()
    if not url.startswith(("http://", "https://")):
        return emit(False, {"url": url}, warnings, ["usage", "--url must be an http(s) URL"])

    # 1. Idempotency precheck — never burn tokens for a URL we already hold.
    existing = find_existing_capture(url)
    if existing is not None:
        rel = existing.relative_to(REPO_ROOT).as_posix()
        eid = event_id_for(rel)
        fields = header_fields(existing)
        env = run_record_ingest(rel, fields["title"], fields["fetch_method"])
        if not env.get("ok"):
            return emit(False, {"url": url, "source_path": rel}, warnings,
                        ["event_record_failed", json.dumps(env)[:500]])
        recorded = bool(env.get("artifacts", {}).get("recorded"))
        if recorded:
            warnings.append("raw file existed without an ingest event; event backfilled")
        else:
            warnings.append(f"already ingested (event_id={eid}); no-op — agent not spawned")
        return emit(True, {
            "url": url, "source_path": rel,
            "title": fields["title"], "fetch_method": fields["fetch_method"],
            "event_id": env.get("artifacts", {}).get("event_id", eid),
            "content_hash": content_hash_of(existing),
            "bytes": existing.stat().st_size,
            "recorded": recorded,
            "agent": None,
        }, warnings, [])

    if args.dry_run:
        warnings.append("dry-run: agent not spawned, nothing written")
        return emit(True, {"url": url, "would_spawn": True, "recorded": False},
                    warnings, [])

    # 2. Snapshot → spawn → diff. Disk is the only witness we accept.
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    before = {f.name for f in RAW_DIR.glob("*.md")}
    meta, spawn_warnings = spawn_agent(url, args.max_turns, args.timeout)
    warnings.extend(spawn_warnings)
    new_names = sorted({f.name for f in RAW_DIR.glob("*.md")} - before)

    def cleanup(names: list[str]) -> None:
        for n in names:
            try:
                (RAW_DIR / n).unlink()
            except OSError:
                pass
        if names:
            warnings.append(f"deleted invalid file(s) created by this run: {', '.join(names)}")

    if not new_names:
        tail = meta.get("result_tail") or ""
        m = re.search(r"INGEST_FAILED=(.+)", tail)
        if m:
            return emit(False, {"url": url, "agent": meta}, warnings,
                        ["fetch_failed", m.group(1).strip()])
        if meta["timed_out"] or (meta["exit_code"] not in (0, None)):
            return emit(False, {"url": url, "agent": meta}, warnings,
                        ["fetch_failed", f"agent exit={meta['exit_code']} timed_out={meta['timed_out']}"])
        return emit(False, {"url": url, "agent": meta}, warnings, ["raw_missing"])

    if len(new_names) > 1:
        cleanup(new_names)
        return emit(False, {"url": url, "agent": meta, "new_files": new_names},
                    warnings, ["multiple_new_files", ", ".join(new_names)])

    name = new_names[0]
    path = RAW_DIR / name
    rel = f"raw/{name}"
    if not FILENAME_RE.match(name):
        warnings.append(f"filename does not match raw/{{date}}-{{slug}}.md pattern: {name}")

    size = path.stat().st_size
    if size < MIN_BYTES:
        cleanup([name])
        return emit(False, {"url": url, "agent": meta, "source_path": rel},
                    warnings, ["content_too_small", f"{size} bytes < {MIN_BYTES}"])

    fields = header_fields(path)
    if fields["url"] != url:
        cleanup([name])
        return emit(False, {"url": url, "agent": meta, "source_path": rel},
                    warnings, ["header_mismatch", f"header Source is {fields['url']!r}"])

    # 3. Record the event and answer with verified facts only.
    env = run_record_ingest(rel, fields["title"], fields["fetch_method"])
    if not env.get("ok"):
        return emit(False, {"url": url, "agent": meta, "source_path": rel},
                    warnings, ["event_record_failed", json.dumps(env)[:500]])

    return emit(True, {
        "url": url,
        "source_path": rel,
        "title": fields["title"],
        "fetch_method": fields["fetch_method"],
        "event_id": env.get("artifacts", {}).get("event_id", event_id_for(rel)),
        "content_hash": content_hash_of(path),
        "bytes": path.stat().st_size,
        "recorded": bool(env.get("artifacts", {}).get("recorded")),
        "agent": meta,
    }, warnings, [])


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="obsidian-content ingest-url",
        description="Black-box verb: headless claude captures a URL into raw/ + ingest event.",
    )
    p.add_argument("--url", required=True, help="Article URL to capture")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                   help=f"Agent wall-clock budget in seconds (default {DEFAULT_TIMEOUT})")
    p.add_argument("--max-turns", type=int, default=DEFAULT_MAX_TURNS,
                   help=f"Agent turn budget (default {DEFAULT_MAX_TURNS})")
    p.add_argument("--dry-run", action="store_true",
                   help="Idempotency precheck only; never spawns the agent")
    return p


def main(argv: list[str] | None = None) -> int:
    # 内层 headless claude 会继承本进程 env；若带着会话的 TELEGRAM_STATE_DIR，
    # 其 telegram 插件会抢走 bot poller、瘫痪回话通道（07-05/07-13 事故根因）。
    os.environ.pop("TELEGRAM_STATE_DIR", None)
    args = build_parser().parse_args(argv)
    return cmd_ingest_url(args)


if __name__ == "__main__":
    sys.exit(main())
