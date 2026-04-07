"""
SessionStart hook - injects wiki knowledge into every conversation.

When Claude Code starts a session, this hook reads the wiki index and
recent session captures, then injects them as additional context so
Claude always "remembers" what the knowledge base contains.

Pure local I/O, no API calls, runs in under 1 second.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
RAW_DIR = ROOT / "raw"
INDEX_FILE = WIKI_DIR / "index.md"

MAX_CONTEXT_CHARS = 20_000
MAX_LOG_LINES = 30


def get_recent_session_log() -> str:
    """Read the most recent session capture from raw/ (today or yesterday)."""
    today = datetime.now(timezone.utc).astimezone()

    for offset in range(2):
        date = today - timedelta(days=offset)
        date_prefix = date.strftime("%Y-%m-%d")
        # Find session files for this date
        session_files = sorted(
            f for f in RAW_DIR.glob(f"{date_prefix}-session-*.md") if f.is_file()
        )
        if session_files:
            # Read the most recent one
            latest = session_files[-1]
            lines = latest.read_text(encoding="utf-8").splitlines()
            recent = lines[-MAX_LOG_LINES:] if len(lines) > MAX_LOG_LINES else lines
            return f"(from {latest.name})\n" + "\n".join(recent)

    return "(no recent session captures)"


def build_context() -> str:
    """Assemble the context to inject into the conversation."""
    parts = []

    today = datetime.now(timezone.utc).astimezone()
    parts.append(f"## Today\n{today.strftime('%A, %B %d, %Y')}")

    # Wiki index (the core retrieval mechanism)
    if INDEX_FILE.exists():
        index_content = INDEX_FILE.read_text(encoding="utf-8")
        parts.append(f"## Knowledge Base Index\n\n{index_content}")
    else:
        parts.append("## Knowledge Base Index\n\n(empty - no articles compiled yet)")

    # Recent session capture
    recent_log = get_recent_session_log()
    parts.append(f"## Recent Session Capture\n\n{recent_log}")

    context = "\n\n---\n\n".join(parts)

    if len(context) > MAX_CONTEXT_CHARS:
        context = context[:MAX_CONTEXT_CHARS] + "\n\n...(truncated)"

    return context


def main():
    context = build_context()

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }

    print(json.dumps(output))


if __name__ == "__main__":
    main()
