# LLM Wiki — Schema

## Owner
vfan — builder based in Singapore. Growth marketer + independent AI content builder.
Bilingual (EN/ZH). Concise, action-oriented.

## Architecture

Four layers:
- `raw/` — Immutable source documents. Human curates what goes in. LLM reads but never modifies.
- `wiki/` — LLM-maintained knowledge base. LLM owns entirely. Creates, updates, cross-references pages.
- `drafts/` — Articles for publication. Human owns. LLM creates initial draft via `/draft` (from wiki page, raw source, or topic), human polishes to publish.
- This file (CLAUDE.md) — Schema. Conventions, workflows, structure. Co-evolved by human and LLM.

Two special files in wiki/:
- `wiki/index.md` — Content catalog. Every wiki page listed with link + one-line summary. Updated on every ingest.
- `wiki/log.md` — Chronological record. Append-only. Every operation logged with timestamp.

## Domain Focus
AI Builder's Knowledge Base:
- AI/LLM industry (companies, models, products, capabilities, pricing)
- Content distribution (AEO, SEO, bilingual arbitrage, newsletter, social platforms)
- Builder tools and workflows (Claude Code, Remotion, MCP, pipelines)
- People and their ideas
- My projects: LoreAI (loreai.dev), blog2video (AI精读)

## NEVER
- Never modify files in `raw/` — they are immutable source documents
- Never create subdirectories in `wiki/` — flat structure only, use index.md categories
- Never create wiki pages without updating `wiki/index.md`
- Never make claims in wiki pages without tracing to a source file in `raw/`
- Never link generic terms (AI, marketing, Python) — only link concepts worth tracking

## Conventions
- Wiki page filenames: kebab-case, descriptive (e.g., `anthropic.md`, `aeo-strategy.md`)
- Link wiki pages to each other with [[wikilinks]]
- Link concepts worth tracking: [[AEO as distribution strategy]], [[bilingual content arbitrage]]
- Chinese-English mixing is normal. Don't standardize.
- When sources contradict: use `> [!warning]` callout, keep both claims with sources
- Every claim must trace to a source file in raw/
- Wiki page format template: `.claude/rules/wiki-page-format.md` (auto-loaded when editing wiki/)
- Log entry format: `.claude/rules/log-format.md` (auto-loaded when editing wiki/log.md)

## Commands

Five slash commands. Each has full instructions in `.claude/commands/`.

| Command | What it does |
|---------|-------------|
| `/ingest <url\|file\|scan>` | Drop a source into the wiki. One source fans out across multiple pages. |
| `/ingest-anthropic-daily [window]` | Sweep all Anthropic + Claude sources, dedupe, write category-grouped digest. |
| `/query <question>` | Ask a question against the wiki. Synthesize with [[wikilink]] citations. |
| `/lint` | Health check: orphans, stale pages, contradictions, index drift. |
| `/visualize <topic\|path\|blank>` | Generate Excalidraw diagram from wiki knowledge. |
| `/draft <wiki-page\|raw-file\|topic>` | Create a draft article in `drafts/` from wiki page, raw source, or topic. |

## Skills

| Skill | Purpose |
|-------|---------|
| excalidraw-diagram | Generate `.excalidraw` JSON diagrams that make visual arguments. Used by `/visualize`. |

## Pipeline B: Internal Knowledge Capture

SessionEnd/PreCompact hooks in LoreAI and blog2video capture session knowledge → `scripts/flush.py` → `raw/`.
After 6 PM: `scripts/compile.py` auto-compiles new raw files into wiki pages.
Safety: `CLAUDE_INVOKED_BY` env var prevents recursion. No hooks configured in THIS repo.

## Documentation Layers

When adding or changing features, put information in the right layer:

| What changed | Update where |
|-------------|-------------|
| New convention (applies every session) | This file (CLAUDE.md) |
| Rule for specific file types/directories | `.claude/rules/{name}.md` with `paths:` glob |
| New slash command | `.claude/commands/{name}.md` + add row to Commands table above |
| New skill | `.claude/skills/{name}/SKILL.md` + add row to Skills table above |
| Skill/command behavior details | Inside the skill/command file, NOT here |

Principle: **CLAUDE.md declares WHAT exists. Skills and commands define HOW they work.**

## Compact Instructions

When compressing context, preserve in priority order:
1. Architecture decisions and the three-layer model (raw → wiki → CLAUDE.md)
2. NEVER list — always re-check before acting
3. Which files have been modified and key changes made
4. Current task state and open TODOs
5. Tool outputs can be discarded — keep only pass/fail status
