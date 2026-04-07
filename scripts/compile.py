"""
Compile new raw sources into wiki pages + discover connections.

This is the "LLM compiler" — it reads raw sources and produces organized
wiki pages (the executable). It also scans for non-obvious connections
between existing concepts.

Usage:
    uv run python scripts/compile.py                     # compile new/changed only
    uv run python scripts/compile.py --all               # force recompile everything
    uv run python scripts/compile.py --file raw/file.md  # compile a specific file
    uv run python scripts/compile.py --dry-run           # show what would be compiled
"""

from __future__ import annotations

# Recursion prevention
import os
os.environ["CLAUDE_INVOKED_BY"] = "wiki_compiler"

import argparse
import asyncio
import sys
from pathlib import Path

# Add scripts/ to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import INDEX_FILE, LOG_FILE, RAW_DIR, ROOT_DIR, SCHEMA_FILE, WIKI_DIR, now_iso
from utils import file_hash, list_raw_files, list_wiki_articles, load_state, read_all_wiki_content, read_wiki_index, save_state


async def compile_sources(raw_files: list[Path], state: dict) -> float:
    """Compile raw source files into wiki pages and discover connections.

    Returns the API cost.
    """
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        query,
    )

    schema = SCHEMA_FILE.read_text(encoding="utf-8")
    wiki_index = read_wiki_index()
    all_wiki = read_all_wiki_content()

    # Read all new raw files
    new_content_parts = []
    for f in raw_files:
        content = f.read_text(encoding="utf-8")
        new_content_parts.append(f"### {f.name}\n\n{content}")
    new_content = "\n\n---\n\n".join(new_content_parts)

    timestamp = now_iso()
    file_list = ", ".join(f.name for f in raw_files)

    prompt = f"""You are the wiki compiler. Your job is to read new source files and
compile them into structured wiki pages, then discover connections between concepts.

## Schema (CLAUDE.md)

{schema}

## Current Wiki Index

{wiki_index}

## All Existing Wiki Pages

{all_wiki}

## New Source Files to Compile

{new_content}

## Your Task

### Part 1: Compile Sources into Wiki Pages

For each new source file, follow the /ingest workflow from CLAUDE.md:

1. **Extract entities and concepts** — people, companies, products, strategies, frameworks, patterns
2. **Create new wiki pages** for entities/concepts that don't have pages yet
   - Use the exact Wiki Page Format from CLAUDE.md (YAML frontmatter + sections)
   - Use kebab-case filenames
   - Include `sources:` in frontmatter pointing to the raw file
   - Use [[wikilinks]] to link to other wiki pages
3. **Update existing wiki pages** if new source adds information
   - Add the new source to frontmatter sources list
   - Update last-updated date
   - Add row to Source Log table
   - If new info contradicts existing content, use `> [!warning]` callout
4. **Create a source summary page** for each raw file: `wiki/source-{{slug}}.md`
5. **Update wiki/index.md** — add new entries under correct categories
6. **Append to wiki/log.md**:
   ```
   ## [{timestamp}] compile | {{source title}}
   source: raw/{{filename}}
   pages-created: {{list}}
   pages-updated: {{list}}
   ```

### Part 2: Discover Connections

After compiling, scan ALL wiki concepts (existing + newly created).
Look for non-obvious relationships between 2+ concepts that:
- Are NOT already linked in either page's Connections section
- Have a genuine insight worth recording (not just "both relate to AI")
- Would be valuable for future /query retrieval
- Reveal a pattern, contradiction, or surprising bridge

For each connection discovered, create a connection article:
- Filename: `wiki/connection-{{concept1}}-and-{{concept2}}.md`
- Frontmatter: type: concept, tags: [wiki, connection, insight]
- Sections: The Connection, Key Insight, Where Else This Applies, Related Concepts, Source Log
- Add to wiki/index.md under the **Connections** category
- Add to wiki/log.md

**Be selective** — 0-2 connections per compilation is normal. Only create ones with genuine, non-obvious insights. Quality over quantity.

### File paths
- Write wiki pages to: {WIKI_DIR}
- Update index at: {INDEX_FILE}
- Append log at: {LOG_FILE}

### Important
- Follow CLAUDE.md conventions exactly (flat structure, kebab-case, wikilinks)
- Every claim must trace to a source file
- Chinese-English mixing is normal
"""

    cost = 0.0

    try:
        async for message in query(
            prompt=prompt,
            options=ClaudeAgentOptions(
                cwd=str(ROOT_DIR),
                system_prompt={"type": "preset", "preset": "claude_code"},
                allowed_tools=["Read", "Write", "Edit", "Glob", "Grep"],
                permission_mode="acceptEdits",
                max_turns=50,
            ),
        ):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        pass  # LLM writes files directly via tools
            elif isinstance(message, ResultMessage):
                cost = message.total_cost_usd or 0.0
                print(f"  Cost: ${cost:.4f}")
    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return 0.0

    # Update state for all compiled files
    for f in raw_files:
        state.setdefault("ingested", {})[f.name] = {
            "hash": file_hash(f),
            "compiled_at": now_iso(),
            "cost_usd": cost / len(raw_files),
        }
    state["total_cost"] = state.get("total_cost", 0.0) + cost
    save_state(state)

    return cost


def main():
    parser = argparse.ArgumentParser(description="Compile raw sources into wiki pages")
    parser.add_argument("--all", action="store_true", help="Force recompile all sources")
    parser.add_argument("--file", type=str, help="Compile a specific raw file")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be compiled")
    args = parser.parse_args()

    state = load_state()

    # Determine which files to compile
    if args.file:
        target = Path(args.file)
        if not target.is_absolute():
            target = RAW_DIR / target.name
        if not target.exists():
            target = ROOT_DIR / args.file
        if not target.exists():
            print(f"Error: {args.file} not found")
            sys.exit(1)
        to_compile = [target]
    else:
        all_raws = list_raw_files()
        if args.all:
            to_compile = all_raws
        else:
            to_compile = []
            for raw_path in all_raws:
                prev = state.get("ingested", {}).get(raw_path.name, {})
                if not prev or prev.get("hash") != file_hash(raw_path):
                    to_compile.append(raw_path)

    if not to_compile:
        print("Nothing to compile — all raw sources are up to date.")
        return

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Files to compile ({len(to_compile)}):")
    for f in to_compile:
        print(f"  - {f.name}")

    if args.dry_run:
        return

    # Compile all files in one pass (so LLM can see cross-file patterns)
    print(f"\nCompiling {len(to_compile)} source(s)...")
    cost = asyncio.run(compile_sources(to_compile, state))

    articles = list_wiki_articles()
    print(f"\nCompilation complete. Cost: ${cost:.2f}")
    print(f"Wiki: {len(articles)} pages")


if __name__ == "__main__":
    main()
