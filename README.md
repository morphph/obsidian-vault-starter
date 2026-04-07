# LLM Wiki — Personal Knowledge Compiler

A personal knowledge base that compiles itself. Drop sources in, knowledge compounds out.

Built on [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern + [claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) patterns.

## Quick Start

```bash
# Ask the wiki a question
/query what harness engineering patterns have I collected?

# Ingest an article
/ingest https://example.com/interesting-article

# Ingest a GitHub repo (deep scan)
/ingest https://github.com/owner/repo

# Generate a diagram from wiki knowledge
/visualize harness-design

# Health check
/lint

# Compile new sources (usually auto, but can run manually)
uv run python scripts/compile.py
```

## Architecture

```
Pipeline A (External)              Pipeline B (Internal)
  /ingest <url|file>                 Claude Code Hooks
  Telegram bot (Channels)            SessionEnd + PreCompact
                ↘                          ↙
                    raw/ (immutable sources)
                          ↓
                   LLM Compiler
                   /ingest scan or compile.py
                   ⏰ auto at 6 PM
                          ↓
                    wiki/ (knowledge pages)
                          ↓
              /query  /lint  /visualize
```

**Three layers:**
- `raw/` — Immutable source documents. You curate what goes in. LLM never modifies.
- `wiki/` — LLM-maintained knowledge pages. Entities, concepts, connections, visuals.
- `CLAUDE.md` — Schema. Conventions, commands, workflows.

## Commands

| Command | What it does |
|---------|-------------|
| `/ingest <url\|file\|scan>` | Drop a source → wiki pages fan out. Supports articles, GitHub repos (deep scan), tweets (Playwright). |
| `/query <question>` | Ask the wiki. Optionally file answer back as synthesis page. |
| `/lint` | Health check: orphans, contradictions, stale pages, missing links. |
| `/visualize <topic\|source\|blank>` | Generate Excalidraw diagram from wiki knowledge. |

## Pipeline B (Auto-Capture)

Your LoreAI and blog2video coding sessions are automatically captured.

**How:** Hooks in each project → transcript extraction → Agent SDK knowledge extraction → `raw/` → 6 PM auto-compile + connection discovery.

**No action needed.** Just code. Knowledge flows automatically.

Manual compile: `uv run python scripts/compile.py`

## Vault Structure

```
raw/                    Sources (articles, repos, session captures)
wiki/                   Knowledge pages (LLM-owned)
  index.md              Content catalog — THE retrieval mechanism
  log.md                Operation history
  *.md                  Entity, concept, synthesis, connection, source pages
  visual-*.excalidraw   Diagrams
hooks/                  Claude Code hooks (session-start, session-end, pre-compact)
scripts/                Pipeline scripts (flush.py, compile.py)
.claude/commands/       Slash commands (ingest, query, lint, visualize)
.claude/skills/         Skills (excalidraw-diagram)
CLAUDE.md               Schema — the operating manual
archive/                Everything from the pre-wiki vault
```

## Changelog

### v0.2 — Pipeline B + Auto Connections (2026-04-07)

- **Internal knowledge capture**: hooks + flush.py + compile.py pipeline
- Hooks configured in loreai-v2 and blog2video
- Agent SDK for all unattended operations (flush, compile, connection discovery)
- Time-gated compilation at 6 PM
- Auto connection discovery during compile
- `scripts/compile.py` — manual or auto compilation with `--dry-run` support
- Recursion guard via `CLAUDE_INVOKED_BY` env var

### v0.1.3 — GitHub Deep Scan (2026-04-07)

- `/ingest` detects GitHub URLs → deep architecture scan via `gh` CLI
- First repo ingest: claude-memory-compiler (7 new concept pages)

### v0.1.2 — Excalidraw + /visualize (2026-04-07)

- Installed excalidraw-diagram skill
- `/visualize` command: topic, source, or full wiki map
- First diagrams: harness design ecosystem, wiki architecture, Agent SDK roadmap

### v0.1.1 — Smart URL Fetch (2026-04-06)

- URL classification: static vs JS-heavy sites
- Playwright MCP configured as browser fallback
- Claude for Chrome integration (when available)
- First Playwright fetch: Ryan Sarver X Article

### v0.1 — Full Reset (2026-04-06)

- Rebuilt vault from scratch on Karpathy's LLM Wiki pattern
- Three layers: `raw/` → `wiki/` → `CLAUDE.md`
- Four commands: `/ingest`, `/query`, `/lint`, `/visualize`
- Archived old vault (agent-output, references, building-journal, projects, inbox)
- Seeded with 2 sources: Anthropic harness design article + Claude Reviews Claude
- 14 initial wiki pages

### Pre-v0.1 — Old Vault (archived)

- inbox.md-based capture system
- /build-log, /connect, /sync-project, /context commands
- agent-output/ staging area
- Archived because nothing compounded — many write paths, no synthesis loop
