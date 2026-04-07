"""Shared utilities for the LLM Wiki pipeline."""

import hashlib
import json
import re
from pathlib import Path

from config import INDEX_FILE, RAW_DIR, STATE_FILE, WIKI_DIR


# ── State management ──────────────────────────────────────────────────

def load_state() -> dict:
    """Load persistent state from state.json."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"ingested": {}, "total_cost": 0.0}


def save_state(state: dict) -> None:
    """Save state to state.json."""
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


# ── File hashing ──────────────────────────────────────────────────────

def file_hash(path: Path) -> str:
    """SHA-256 hash of a file (first 16 hex chars)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


# ── Slug / naming ─────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


# ── Wiki content helpers ──────────────────────────────────────────────

def read_wiki_index() -> str:
    """Read the wiki index file."""
    if INDEX_FILE.exists():
        return INDEX_FILE.read_text(encoding="utf-8")
    return "# Index\n\n(empty)"


def read_all_wiki_content() -> str:
    """Read index + all wiki pages into a single string for context."""
    parts = [f"## INDEX\n\n{read_wiki_index()}"]

    for md_file in sorted(WIKI_DIR.glob("*.md")):
        if md_file.name in ("index.md", "log.md"):
            continue
        rel = md_file.name
        content = md_file.read_text(encoding="utf-8")
        parts.append(f"## {rel}\n\n{content}")

    return "\n\n---\n\n".join(parts)


def list_wiki_articles() -> list[Path]:
    """List all wiki article files (excluding index.md, log.md)."""
    articles = []
    for md_file in sorted(WIKI_DIR.glob("*.md")):
        if md_file.name in ("index.md", "log.md"):
            continue
        articles.append(md_file)
    return articles


def list_raw_files() -> list[Path]:
    """List all raw source files (excluding README.md)."""
    if not RAW_DIR.exists():
        return []
    return sorted(
        f for f in RAW_DIR.glob("*.md") if f.name != "README.md"
    )


# ── Wikilink helpers ──────────────────────────────────────────────────

def extract_wikilinks(content: str) -> list[str]:
    """Extract all [[wikilinks]] from markdown content."""
    return re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", content)
