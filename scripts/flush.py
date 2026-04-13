"""
Memory flush agent - extracts knowledge from conversation context.

Spawned by session-end.py or pre-compact.py as a background process.
Reads pre-extracted conversation context, uses the Claude Agent SDK
to decide what's worth saving, and writes the result to raw/ in the
wiki vault.

Usage:
    uv run python scripts/flush.py <context_file.md> <session_id>
"""

from __future__ import annotations

# Recursion prevention: set BEFORE any imports that might trigger Claude
import os
os.environ["CLAUDE_INVOKED_BY"] = "memory_flush"

import asyncio
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw"
SCRIPTS_DIR = ROOT / "scripts"
STATE_FILE = SCRIPTS_DIR / "last-flush.json"
LOG_FILE = SCRIPTS_DIR / "flush.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def load_flush_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_flush_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state), encoding="utf-8")


def detect_project_name(project_dir: str = "") -> str:
    """Detect project name from CLI arg, env var, or default to 'unknown'."""
    # Priority: CLI arg (from hook) > env var > fallback
    path = project_dir or os.environ.get("CLAUDE_PROJECT_DIR", "") or os.environ.get("CLAUDE_CWD", "")
    if not path:
        return "unknown"
    name = path.lower()
    if "loreai" in name:
        return "loreai"
    elif "blog2video" in name:
        return "blog2video"
    return Path(path).name.lower() or "unknown"


def save_to_raw(content: str, project: str) -> Path:
    """Save extracted knowledge to raw/ directory."""
    today = datetime.now(timezone.utc).astimezone()
    date_str = today.strftime("%Y-%m-%d")
    time_str = today.strftime("%H%M")

    filename = f"{date_str}-session-{project}-{time_str}.md"
    filepath = RAW_DIR / filename

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    header = (
        f"# Session Capture: {project}\n\n"
        f"**Date:** {date_str}\n"
        f"**Project:** {project}\n"
        f"**Source:** Claude Code session (auto-captured via hooks)\n"
        f"**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK\n\n"
        f"---\n\n"
    )

    filepath.write_text(header + content, encoding="utf-8")
    return filepath


async def run_flush(context: str) -> str:
    """Use Claude Agent SDK to extract important knowledge from conversation context."""
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )

    prompt = f"""Review the conversation context below and respond with a concise summary
of important items that should be preserved in the knowledge base.
Do NOT use any tools — just return plain text.

Format your response as a structured session summary with these sections:

**Context:** [One line about what the user was working on]

**Key Exchanges:**
- [Important Q&A or discussions]

**Decisions Made:**
- [Any decisions with rationale]

**Lessons Learned:**
- [Gotchas, patterns, or insights discovered]

**Action Items:**
- [Follow-ups or TODOs mentioned]

Skip anything that is:
- Routine tool calls or file reads
- Trivial back-and-forth or clarification exchanges
- Content that's obvious or not worth remembering

Only include sections that have actual content. If nothing is worth saving,
respond with exactly: FLUSH_OK

## Conversation Context

{context}"""

    response = ""

    try:
        async for message in query(
            prompt=prompt,
            options=ClaudeAgentOptions(
                cwd=str(ROOT),
                allowed_tools=[],
                max_turns=2,
            ),
        ):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        response += block.text
            elif isinstance(message, ResultMessage):
                pass
    except Exception as e:
        import traceback
        logging.error("Agent SDK error: %s\n%s", e, traceback.format_exc())
        response = f"FLUSH_ERROR: {type(e).__name__}: {e}"

    return response


COMPILE_AFTER_HOUR = 18  # 6 PM local time


def maybe_trigger_compilation() -> None:
    """If past compile hour and new raw files exist, run compile.py."""
    import subprocess as _sp
    from hashlib import sha256

    now = datetime.now(timezone.utc).astimezone()
    if now.hour < COMPILE_AFTER_HOUR:
        return

    # Check if there are uncompiled raw files
    compile_state_file = SCRIPTS_DIR / "state.json"
    ingested = {}
    if compile_state_file.exists():
        try:
            compile_state = json.loads(compile_state_file.read_text(encoding="utf-8"))
            ingested = compile_state.get("ingested", {})
        except (json.JSONDecodeError, OSError):
            pass

    # Check if any raw files are new or changed
    has_new = False
    for f in sorted(RAW_DIR.glob("*.md")):
        if f.name == "README.md":
            continue
        current_hash = sha256(f.read_bytes()).hexdigest()[:16]
        prev = ingested.get(f.name, {})
        if not prev or prev.get("hash") != current_hash:
            has_new = True
            break

    if not has_new:
        return

    compile_script = SCRIPTS_DIR / "compile.py"
    if not compile_script.exists():
        return

    logging.info("End-of-day compilation triggered (after %d:00)", COMPILE_AFTER_HOUR)

    cmd = ["uv", "run", "--directory", str(ROOT), "python", str(compile_script)]

    kwargs: dict = {}
    if sys.platform == "win32":
        kwargs["creationflags"] = _sp.CREATE_NEW_PROCESS_GROUP | _sp.DETACHED_PROCESS
    else:
        kwargs["start_new_session"] = True

    try:
        log_handle = open(str(SCRIPTS_DIR / "compile.log"), "a")
        _sp.Popen(cmd, stdout=log_handle, stderr=_sp.STDOUT, cwd=str(ROOT), **kwargs)
    except Exception as e:
        logging.error("Failed to spawn compile.py: %s", e)


def main():
    if len(sys.argv) < 3:
        logging.error("Usage: %s <context_file.md> <session_id>", sys.argv[0])
        sys.exit(1)

    context_file = Path(sys.argv[1])
    session_id = sys.argv[2]
    project_dir = sys.argv[3] if len(sys.argv) > 3 else ""

    logging.info("flush.py started for session %s, context: %s", session_id, context_file)

    if not context_file.exists():
        logging.error("Context file not found: %s", context_file)
        return

    # Deduplication: skip if same session was flushed within 60 seconds
    state = load_flush_state()
    if (
        state.get("session_id") == session_id
        and time.time() - state.get("timestamp", 0) < 60
    ):
        logging.info("Skipping duplicate flush for session %s", session_id)
        context_file.unlink(missing_ok=True)
        return

    # Read pre-extracted context
    context = context_file.read_text(encoding="utf-8").strip()
    if not context:
        logging.info("Context file is empty, skipping")
        context_file.unlink(missing_ok=True)
        return

    project = detect_project_name(project_dir)
    logging.info("Flushing session %s (project: %s): %d chars", session_id, project, len(context))

    # Run the LLM extraction
    response = asyncio.run(run_flush(context))

    # Save to raw/
    if "FLUSH_OK" in response:
        logging.info("Result: FLUSH_OK — nothing worth saving")
    elif "FLUSH_ERROR" in response:
        logging.error("Result: %s", response)
    else:
        filepath = save_to_raw(response, project)
        logging.info("Result: saved to %s (%d chars)", filepath.name, len(response))

    # Update dedup state
    save_flush_state({"session_id": session_id, "timestamp": time.time()})

    # Clean up context file
    context_file.unlink(missing_ok=True)

    # End-of-day auto-compilation
    maybe_trigger_compilation()

    logging.info("Flush complete for session %s", session_id)


if __name__ == "__main__":
    main()
