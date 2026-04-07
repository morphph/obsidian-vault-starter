# Claude Memory Compiler

**Source:** https://github.com/coleam00/claude-memory-compiler
**Author:** coleam00
**Stars:** 70 | **Language:** Python | **Last updated:** 2026-04-07
**Fetch method:** GitHub Deep Scan (gh CLI)

## What It Does

Gives Claude Code a memory that evolves with your codebase. Hooks automatically capture conversation transcripts at session end and pre-compaction. A background process (flush.py) uses the Claude Agent SDK to extract key decisions, lessons learned, and patterns into daily logs. A compiler (compile.py) then organizes daily logs into structured, cross-referenced knowledge articles — concepts, connections, and Q&A pages.

Directly adapted from Karpathy's LLM Knowledge Base architecture, but the raw source is your own AI conversations instead of external articles.

**Key claim:** At personal scale (50-500 articles), the LLM reading a structured index.md outperforms vector similarity for retrieval. No RAG needed.

## Architecture

The "compiler analogy" is the central metaphor:
```
daily/          = source code    (conversations — the raw material)
LLM             = compiler       (extracts and organizes knowledge)
knowledge/      = executable     (structured, queryable knowledge base)
lint            = test suite     (health checks for consistency)
queries         = runtime        (using the knowledge)
```

Three layers (same as Karpathy):
1. **daily/** — Immutable conversation logs. Append-only, never edited.
2. **knowledge/** — LLM-owned compiled knowledge. Concepts, connections, Q&A, index.md, log.md.
3. **AGENTS.md** — Schema file (equivalent to our CLAUDE.md). Tells the LLM how to compile and maintain.

File structure:
```
.claude/settings.json          # Hook configuration
hooks/
  session-start.py             # Injects knowledge index into every session
  session-end.py               # Captures transcript → spawns flush.py
  pre-compact.py               # Safety net before context compaction
scripts/
  flush.py                     # Background: extract knowledge from conversations
  compile.py                   # Daily logs → knowledge articles (Claude Agent SDK)
  query.py                     # Index-guided retrieval
  lint.py                      # 7 health checks
  config.py                    # Path constants
  utils.py                     # Shared helpers
knowledge/
  index.md                     # Master catalog — THE retrieval mechanism
  log.md                       # Append-only build log
  concepts/                    # Atomic knowledge articles
  connections/                 # Cross-cutting insights linking 2+ concepts
  qa/                          # Filed query answers
daily/
  YYYY-MM-DD.md                # One file per day
```

## Tech Stack

- Python 3.12+, managed by uv
- claude-agent-sdk >= 0.1.29 (for compile.py and flush.py)
- python-dotenv, tzdata
- No API key needed — uses Claude Code's built-in credentials
- Anthropic has clarified personal use of Agent SDK is covered under Claude subscription (Max, Team, Enterprise)

## Patterns & Best Practices

### Harness Engineering

**Hook-based automatic capture (zero-friction memory)**
SessionEnd and PreCompact hooks fire automatically. The hook itself does NO API calls (fast, <10s) — it reads the JSONL transcript, extracts recent turns, writes to a temp file, then spawns a background process. The background process (flush.py) uses the Claude Agent SDK to decide what's worth saving. This separation (fast hook → detached background process) is critical: hooks must be fast, but LLM extraction is slow.

Why both PreCompact AND SessionEnd? Long sessions trigger multiple auto-compactions before you close. Without PreCompact, intermediate context is lost to summarization before SessionEnd fires. This is a non-obvious edge case.

**Recursion prevention via environment variable**
flush.py sets `CLAUDE_INVOKED_BY=memory_flush` before any imports. The hooks check this env var and exit immediately if set. This prevents infinite recursion: hook → flush.py → Agent SDK → Claude Code → hook → flush.py → ... Simple, elegant, critical.

**SessionStart knowledge injection**
session-start.py injects the knowledge index into every new session via hook output JSON: `{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "..."}}`. Max 20,000 chars. This means every Claude Code session starts aware of your accumulated knowledge — no manual context loading.

**Time-gated auto-compilation**
flush.py triggers compile.py automatically after 6 PM local time if today's daily log has changed (SHA-256 hash comparison). Separates capture (all day) from synthesis (end of day). No cron job needed — the compilation piggybacks on the last session flush of the day.

**Detached background process spawning (cross-platform)**
Windows: `CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS` flags. Mac/Linux: `start_new_session=True`. flush.py must survive after the hook process exits. Also: on Windows, do NOT use `DETACHED_PROCESS` for Agent SDK subprocesses — it breaks I/O. Use `CREATE_NO_WINDOW` instead.

**Flush deduplication**
Tracks session_id + timestamp in last-flush.json. Skips if same session was flushed within 60 seconds. Prevents duplicate flushes when both PreCompact and SessionEnd fire for the same session.

**Connection articles as first-class objects**
`knowledge/connections/` is a separate directory for cross-cutting insights linking 2+ concepts. Not just a "related" section within pages, but standalone articles with their own evidence, source citations, and bidirectional links. This promotes non-obvious relationships from metadata to content.

**Index-over-RAG for personal scale**
"The LLM understands what you're really asking; cosine similarity just finds similar words." At 50-500 articles, loading the full index.md into context and letting the LLM select relevant pages outperforms embedding-based retrieval. RAG threshold: ~2,000+ articles / ~2M+ tokens.

### System Design

**Compiler analogy as architecture framework**
Naming layers by their role in compilation (source code, compiler, executable, test suite, runtime) makes the architecture immediately understandable. This analogy could be applied to any knowledge pipeline.

**Incremental compilation with hash tracking**
state.json tracks SHA-256 hashes of daily logs. compile.py skips unchanged files. Supports --all for full recompile and --file for targeted recompile. Cost-efficient: only reprocesses what changed.

**7-check lint system**
Structural checks (free): broken links, orphan pages, orphan sources, stale articles, missing backlinks, sparse articles. LLM check (costs ~$0.15-0.25): contradictions across articles. The --structural-only flag lets you lint frequently without cost.

**File-back pattern for compounding queries**
`query.py "question" --file-back` creates a Q&A article in knowledge/qa/ and updates index + log. Every question makes the knowledge base smarter. The answer becomes retrievable for future queries — knowledge compounds from usage, not just from capture.

### Developer Experience

**Self-setup via AI agent**
README quick start: tell your coding agent to clone, set up hooks, and install deps. The AGENTS.md file is designed to give an AI agent everything it needs to understand, modify, or rebuild the system. This is "repo as prompt" — the documentation IS the interface.

**Cost transparency**
Every operation's cost is documented: compile ($0.45-0.65/log), query ($0.15-0.25), flush ($0.02-0.05/session). Users can make informed decisions about frequency.

**Pure markdown + wikilinks = Obsidian-native**
No custom database, no special viewer. Point Obsidian at knowledge/ and get graph view, backlinks, search for free. Flat files, git-backable, human-readable.

## Ecosystem Connections

- **Same Karpathy lineage** as this wiki — adapted for conversations instead of external articles
- Implements [[harness-design]] concretely: hooks = harness perception, LLM = reasoning, knowledge base = memory
- The hook architecture relates to [[claude-code]] internals: SessionStart, SessionEnd, PreCompact are 3 of the 20 hook event types documented in [[permission-system]]
- The compile step is analogous to our `/ingest` — source → LLM extraction → wiki pages
- The query step is analogous to our `/query` — index-guided retrieval → answer → optionally file back
- The lint step is analogous to our `/lint` — 7 checks vs our similar set
- Uses Claude Agent SDK (not Claude Code CLI) — different execution model, same subscription

## Repo Vitals

- Stars: 70 | Language: Python
- Last commit: "URL change for repo in README" (2026-04-07)
- Only 2 commits — very new repo, just launched
- 5 top-level files + 3 hooks + 6 scripts = minimal, focused
- Active: updated today
