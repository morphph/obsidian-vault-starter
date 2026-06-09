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

# Draft an article
/draft <wiki-page|raw-file|topic>
```

## Architecture

```
  /ingest <url|file|scan>
            ↓
   raw/ (immutable sources)
            ↓
   wiki/ (knowledge pages, LLM-owned)
            ↓
   /query  /lint  /visualize  /draft
            ↓
   drafts/ (articles for publication)
```

**Four layers:**
- `raw/` — Immutable source documents. You curate what goes in. LLM never modifies.
- `wiki/` — LLM-maintained knowledge pages. Entities, concepts, connections, visuals.
- `drafts/` — Articles for publication. LLM seeds via `/draft`, human polishes.
- `CLAUDE.md` — Schema. Conventions, commands, workflows.

## Commands

| Command                             | What it does                                                                                          |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `/ingest <url\|file\|scan>`         | Drop a source → wiki pages fan out. Supports articles, GitHub repos (deep scan), tweets (Playwright). |
| `/query <question>`                 | Ask the wiki. Optionally file answer back as synthesis page.                                          |
| `/lint`                             | Health check: orphans, contradictions, stale pages, missing links.                                    |
| `/visualize <topic\|source\|blank>` | Generate Excalidraw diagram from wiki knowledge.                                                      |
| `/draft <wiki-page\|raw-file\|topic>` | Create a draft article in `drafts/` from wiki page, raw source, or topic.                           |

## Agent integration — `obsidian-content` CLI

This repo is the human-curated **Tier-1 source layer** of an autonomous content
system. The **Hermes** orchestration agent does not read this repo's internals —
it calls a stable CLI that emits machine-readable JSON.

```bash
bin/obsidian-content list-ingests --status new      # discover new Tier-1 ingests
bin/obsidian-content export-source --id <event_id>  # pull clean source markdown
bin/obsidian-content mark-routed   --id <event_id>  # ack once routed (idempotent)
```

`/ingest` appends a stable event to `events/ingest-events.jsonl` after each
successful ingest; Hermes folds that append-only log into state. The CLI never
writes Hermes's ledger, never pushes, and never calls external services.

**Full contract** (verbs, JSON shape, exit codes, idempotency, Hermes usage):
[`docs/obsidian-content-cli.md`](docs/obsidian-content-cli.md).

## Vault Structure

```
raw/                    Sources (articles, repos, manually curated)
wiki/                   Knowledge pages (LLM-owned)
  index.md              Content catalog — THE retrieval mechanism
  log.md                Operation history
  *.md                  Entity, concept, synthesis, connection, source pages
  visual-*.excalidraw   Diagrams
drafts/                 Articles for publication (human-owned, LLM-seeded)
events/                 Machine-readable event log (Hermes contract surface)
  ingest-events.jsonl   Append-only ingest/routed events
bin/obsidian-content    Agent-native CLI (thin shim → scripts/obsidian_content.py)
scripts/                Helper scripts (obsidian_content.py, content_agent.py, ...)
.claude/commands/       Slash commands (ingest, query, lint, visualize, draft)
.claude/skills/         Skills (excalidraw-diagram + kepano/obsidian-skills)
docs/                   Contracts & ops docs (obsidian-content-cli.md, ...)
CLAUDE.md               Schema — the operating manual
AGENTS.md               Mirror of CLAUDE.md for Codex CLI / agents.md tooling
archive/                Everything from the pre-wiki vault
```

## Changelog

### v0.4 — Agent-native CLI for Hermes (2026-06-09)

- Added `bin/obsidian-content` + `scripts/obsidian_content.py` — stdlib-only CLI
  exposing a stable JSON contract (`contract_version`, `ok`, `verb`, `artifacts`,
  `warnings`, `errors`) to the Hermes orchestration agent
- Verbs: `list-ingests`, `export-source`, `mark-routed`, `record-ingest`,
  `backfill-from-log` — all idempotent where possible
- Added `events/ingest-events.jsonl` append-only event log (folded to state)
- `/ingest` now emits a stable ingest event (step 7) after each successful ingest
- Backfilled 50 historical Tier-1 ingests from `wiki/log.md`
- Contract docs: `docs/obsidian-content-cli.md`. Does not write Hermes's ledger,
  push, or call external services.

### v0.3 — Pipeline B removed (2026-05-21)

- Removed dormant auto-capture pipeline (last ran 2026-04-09)
- Deleted `scripts/{flush,compile,config,utils}.py`, `hooks/`, related state files
- Manual `/ingest` is now the only path into `raw/`
- Registered `obsidian-markdown` + `defuddle` skills from kepano/obsidian-skills
- Added `drafts/` as the fourth layer (was already present, now documented)

### v0.2 — Pipeline B + Auto Connections (2026-04-07) [removed in v0.3]

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
