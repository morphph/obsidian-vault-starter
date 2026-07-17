# LLM Wiki — Personal Knowledge Compiler

A personal knowledge base that compiles itself. Drop sources in, knowledge compounds out.

Built on [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern + [claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) patterns.

## Quick Start

```bash
# Ask the wiki a question
/query what harness engineering patterns have I collected?

# Ingest an article (blog/tweet → full natural Chinese translation)
/ingest https://example.com/interesting-article

# Ingest a PDF or YouTube video (→ Chinese 精要 / essence extraction)
/ingest paper.pdf
/ingest https://www.youtube.com/watch?v=...

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
  /research <topic>
        ↓
  research/<slug>/  (report + outline + ingest-candidates — non-vault, Tier-4)
        │
        ├─(human picks candidates)─→ /ingest <url|file|scan> ─→ raw/ (immutable sources)
        │                                                              ↓
        │                                                wiki/ (knowledge pages, LLM-owned)
        │                                                              ↓
        │                                                   /query  /lint  /visualize
        │
        └─(outline + report)───────→ /draft ─→ drafts/ (articles for publication)
                                       ↑
                    raw/ + wiki/ + references/ also feed /draft
```

**Five layers:**
- `raw/` — Immutable source documents. You curate what goes in. LLM never modifies.
- `wiki/` — LLM-maintained knowledge pages. Entities, concepts, connections, visuals.
- `drafts/` — Articles for publication. LLM seeds via `/draft`, human polishes.
- `references/` — Content reference library. Curated source material (videos, articles, talks) you create *from* — folder per source with a note card + transcript. Not for ingest; feeds `/draft`.
- `CLAUDE.md` — Schema. Conventions, commands, workflows.

## Commands

| Command                             | What it does                                                                                          |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `/ingest <url\|file\|scan>`         | Drop a source → wiki pages fan out. Step 3 routes by type: **blog/article/tweet → full natural translation**; **PDF/YouTube → 精要 extraction** (yt-dlp captions / `Read` for PDF); GitHub repo → deep scan. |
| `/research <topic>`                 | Research a topic → report + outline + ingest-candidates in `research/<slug>/` (non-vault). Doesn't auto-ingest. |
| `/query <question>`                 | Ask the wiki. Optionally file answer back as synthesis page.                                          |
| `/lint`                             | Health check: orphans, contradictions, stale pages, missing links.                                    |
| `/visualize <topic\|source\|blank>` | Generate Excalidraw diagram from wiki knowledge.                                                      |
| `/draft <research-dir\|wiki-page\|raw-file\|topic>` | Create a draft article in `drafts/` from a research workspace, wiki page, raw source, or topic. |
| `/learn <url\|"last output"\|paste>` | Teach a target incrementally until mastery — quizzes, running notes in `learn/`.                      |
| `/ingest-anthropic-daily [window]`  | Sweep all Anthropic + Claude sources, dedupe, write category-grouped digest.                          |

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
learn/                  /learn session notes (human-owned; graduate into wiki/ as useful)
references/             Content reference library — create-from material, not for ingest
  <slug>/               README.md (note card) + transcript.txt + captions.srt
research/               /research workspace (non-vault, Tier-4) — report + outline + candidates per topic
  <topic-slug>/         report.md, outline.md, ingest-candidates.md, meta.json
events/                 Machine-readable event log (Hermes contract surface)
  ingest-events.jsonl   Append-only ingest/routed events
audience-profile.md     Reader persona + voice + GEO rules (read by /research + /draft)
bin/obsidian-content    Agent-native CLI (thin shim → scripts/obsidian_content.py)
scripts/                Helper scripts (obsidian_content.py, ingest_url.py, ...)
.claude/commands/       Lightweight slash commands (query, lint, visualize, draft, learn, ingest-anthropic-daily)
.claude/skills/         Heavyweight commands as skill folders (ingest/, research/ — SKILL.md + references/) + excalidraw-diagram
prompts/                Reusable prompts (skill-audit, research dispatch, ...)
docs/                   Contracts & ops docs (obsidian-content-cli.md, ...)
CLAUDE.md               Schema — the operating manual
archive/                Everything from the pre-wiki vault + retired handoffs
```

## Changelog

### v0.8 — 风格模板参照迁出至 blog2video (2026-07-17)

- **风格模板类参照不再放 `references/`**:用来定义视频格式/风格的参照(旁白口吻 +
  视觉系统 + 渲染方式)统一落在 blog2video 仓库的 `templates/`(视频风格模板库,
  模板 = transcript + visual-style-prompt 两半 + 模板卡)。`references/` 继续用于
  「做内容的素材来源」。
- 移除 `references/sean-agent-harness-loop-engineering/`(其风格模板角色已由
  blog2video `templates/sean-whiteboard-explainer/` 承接,git 历史留底)。
- `handoff/whiteboard-video-skill/` 使命完成,归档为
  `archive/whiteboard-video-skill-handoff/`(随附的参照对已迁 blog2video,归档内
  不留副本);`handoff/` 目录随之移除。

### v0.7 — `references/` layer (2026-07-17)

- Added **`references/`** as a fifth vault layer: a curated content-reference library
  of source material (videos, articles, talks) to create *from* — distinct from `raw/`
  (create-from vs ingest-into-wiki). One folder per source (`references/<slug>/`) with a
  note card (`README.md`: source, why it's a reference, takeaways, content angles) +
  `transcript.txt` + `captions.srt`. Human-curated; never auto-ingested (new NEVER rule).
- First entry: Sean's AI Stories — *Agent Harness & Loop Engineering (19 min)*, captured
  via `yt-dlp` (auto-caption pull + rolling-caption de-dupe → clean transcript).
- Layer conventions + `yt-dlp` capture recipe documented in `references/README.md`.

### v0.6 — Claude Code only + skill folders (2026-07-06)

- **Removed the Codex mirror layer**: deleted `AGENTS.md` (find-replace-damaged mirror
  pointing at nonexistent `.Codex/` paths), `.codex/`, and `.agents/` (stale copies of
  lint/excalidraw skills + broken obsidian-skills gitlink). Claude Code is the only dev
  harness for this vault; `.claude/` is the single source of agent config.
- **`/ingest` + `/research` → skill folders** (`.claude/skills/{ingest,research}/`):
  SKILL.md keeps the workflow; big templates moved to `references/` loaded on demand —
  ingest's per-type step-3 modes (full-translation / 精要 / study-guide) + GitHub deep-scan,
  research's report + outline (Gate-1) templates. Invocation unchanged.
- **`/lint` now checks docs drift**: CLAUDE.md/README command+skill tables, count words,
  and structure listings vs actual files; auto-fixable with permission.
- **Cleanup**: root stray prompts moved to `prompts/` (`research-dispatch.md`,
  `research-prompt.md`, `fable5-pipeline-audit-prompt.md`) and `docs/`
  (`research-to-obsidian-handoff.md`); deleted empty `visual-best-practices-guide.md`,
  `Untitled/`, stray session-flush file; removed the broken `obsidian-skills` gitlink
  (the installed kepano `obsidian` plugin provides those skills).

### v0.5 — `/research` skill + draft seam (2026-06-26)

- Added `/research <topic>` skill (`.claude/commands/research.md`): 查内 (index.md/drafts/gbrain)
  → 扫外 (sub-agent: `deep-research` baseline + best-effort `last30days`/`bird`/`summarize`,
  missing tools → `warnings[]`) → 综合 (report + outline + ingest-candidates) in a **non-vault**
  `research/<slug>/` workspace. Stops at candidates — never auto-ingests. Prints a contract-1.0
  envelope. Completes the content loop: `/research` → `/ingest` → `/draft`.
- Wired the **research → draft seam**: `/draft research/<slug>/` is a 4th input mode. Pragmatic
  sourcing — `sources:` = ingested `raw/` only, un-ingested URLs go in new `external-refs:`;
  `research:` frontmatter points back. Load-bearing claims must trace to `raw/`.
- Added `audience-profile.md` (taste anchor: reader persona + voice + GEO writing rules), read by
  both `/research` and `/draft`. vault snapshot of the content-ops canonical version.
- `research/` is Tier-4 (excluded from vault / selection input / gbrain Tier-1 sync — see
  `research/README.md`). `obsidian_content.py` untouched (it stays LLM-free by design).

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
