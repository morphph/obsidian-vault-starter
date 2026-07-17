# LLM Wiki — Schema

## Owner
vfan — builder based in Singapore. Growth marketer + independent AI content builder.
Bilingual (EN/ZH). Concise, action-oriented.

## Architecture

Five layers:
- `raw/` — Immutable source documents. Human curates what goes in. LLM reads but never modifies.
- `wiki/` — LLM-maintained knowledge base. LLM owns entirely. Creates, updates, cross-references pages.
- `drafts/` — Articles for publication. Human owns. LLM creates initial draft via `/draft` (from wiki page, raw source, or topic), human polishes to publish.
- `learn/` — Learning notes from `/learn` sessions. One file per session (mastery checklist + takeaways) for a blog, a Claude output, or pasted material. Human owns; prune or graduate into wiki/ as useful.
- `references/` — Content reference library. Curated source material (videos, articles, talks) I deliberately draw on **when creating content** — not for ingest. One folder per source (`references/<slug>/`) with a note card (source, why it's a reference, takeaways, content angles) + transcript/captions. Human curates, LLM helps capture. Distinct from `raw/` by purpose: create-from vs ingest-into-wiki. See `references/README.md`.
- This file (CLAUDE.md) — Schema. Conventions, workflows, structure. Co-evolved by human and LLM.

Plus one **non-vault workspace** (not a vault layer — see `research/README.md`):
- `research/` — `/research` output (research-plan + single report + ingest-candidates per topic). Report mirrors a proven shape: §1-2 facts · §3-5 per-channel Top-N · §6 insights · §7 ranked content angles · timeline. **Tier-4 derivative**: archival, excluded from vault / selection input / gbrain Tier-1 sync. Feeds `/ingest` (selected candidates) and `/draft research/<slug>/` (writing, from §7 angle). Never auto-enters `raw/` or `wiki/`.

Plus one **taste anchor** at repo root:
- `audience-profile.md` — reader persona + voice + GEO writing rules. Read by `/research` (report §7 angles) and `/draft` (writing). vault snapshot; content-ops version is canonical.

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
- Never auto-ingest `/research` candidates — only human-selected candidates go through `/ingest`
- Never auto-ingest `references/` material into `wiki/` — it's a create-from library; ingest only if the human explicitly asks
- Never treat `research/` outputs as Tier-1 or as selection/topic input — they are Tier-4 derivatives

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

Eight slash commands. Lightweight ones live in `.claude/commands/{name}.md`; heavyweight ones (`/ingest`, `/research`) are skill folders in `.claude/skills/{name}/` — SKILL.md holds the workflow, `references/` holds templates loaded on demand (progressive disclosure).

| Command | What it does |
|---------|-------------|
| `/ingest <url\|file\|scan>` | Drop a source into the wiki. One source fans out across multiple pages. |
| `/ingest-anthropic-daily [window]` | Sweep all Anthropic + Claude sources, dedupe, write category-grouped digest. |
| `/research <topic>` | Research a topic → research-plan + ingest-candidates in `research/<slug>/` (non-vault). `mode:report` (default): single report (facts + per-channel Top-N + ranked angles). `mode:guide`: evergreen reader guide(s) + facts.md ledger. Doesn't auto-ingest. |
| `/query <question>` | Ask a question against the wiki. Synthesize with [[wikilink]] citations. |
| `/lint` | Health check: orphans, stale pages, contradictions, index drift. |
| `/visualize <topic\|path\|blank>` | Generate Excalidraw diagram from wiki knowledge. |
| `/draft <research-dir\|wiki-page\|raw-file\|topic>` | Create a draft article in `drafts/` from a research workspace, wiki page, raw source, or topic. |
| `/learn <url\|"last output"\|paste>` | Teach me a target incrementally until mastery — quizzes, running notes in `learn/`. |

## Skills

| Skill | Purpose |
|-------|---------|
| excalidraw-diagram | Generate `.excalidraw` JSON diagrams that make visual arguments. Used by `/visualize`. Local: `.claude/skills/excalidraw-diagram/`. |
| obsidian:obsidian-markdown | Write valid Obsidian flavored markdown (wikilinks, callouts, embeds, properties). Auto-invoked when editing wiki/. From the installed kepano `obsidian` plugin (marketplace), not a local copy. |
| obsidian:defuddle | Extract clean markdown from URLs (less noise than WebFetch). Prefer for `/ingest <url>`. Requires `npm install -g defuddle`. From the installed kepano `obsidian` plugin. |

## Documentation Layers

When adding or changing features, put information in the right layer:

| What changed | Update where |
|-------------|-------------|
| New convention (applies every session) | This file (CLAUDE.md) |
| Rule for specific file types/directories | `.claude/rules/{name}.md` with `paths:` glob |
| New slash command (lightweight, no templates) | `.claude/commands/{name}.md` + add row to Commands table above |
| New slash command (heavyweight, bundles templates) | `.claude/skills/{name}/SKILL.md` + `references/` + add row to Commands table above |
| New skill | `.claude/skills/{name}/SKILL.md` + add row to Skills table above |
| Skill/command behavior details | Inside the skill/command file, NOT here |

Principle: **CLAUDE.md declares WHAT exists. Skills and commands define HOW they work.**

## Compact Instructions

When compressing context, preserve in priority order:
1. Architecture decisions and the four-layer model (raw → wiki → drafts → CLAUDE.md)
2. NEVER list — always re-check before acting
3. Which files have been modified and key changes made
4. Current task state and open TODOs
5. Tool outputs can be discarded — keep only pass/fail status
