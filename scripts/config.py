"""Path constants and configuration for the LLM Wiki pipeline."""

from pathlib import Path
from datetime import datetime, timezone

# ── Paths ──────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT_DIR / "raw"
WIKI_DIR = ROOT_DIR / "wiki"
SCRIPTS_DIR = ROOT_DIR / "scripts"
HOOKS_DIR = ROOT_DIR / "hooks"
SCHEMA_FILE = ROOT_DIR / "CLAUDE.md"

INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"
STATE_FILE = SCRIPTS_DIR / "state.json"

# ── Compilation settings ───────────────────────────────────────────────
COMPILE_AFTER_HOUR = 18  # 6 PM local time


# ── Helpers ────────────────────────────────────────────────────────────
def now_iso() -> str:
    """Current time in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today_iso() -> str:
    """Current date in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
