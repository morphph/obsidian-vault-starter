# LLM Wiki — Schema

## Owner
vfan — builder based in Singapore. Growth marketer + independent AI content builder.
Bilingual (EN/ZH). Concise, action-oriented.

## Architecture

Three layers:
- `raw/` — Immutable source documents. Human curates what goes in. LLM reads but never modifies.
- `wiki/` — LLM-maintained knowledge base. LLM owns entirely. Creates, updates, cross-references pages.
- This file (CLAUDE.md) — Schema. Conventions, workflows, structure. Co-evolved by human and LLM.

Two special files in wiki/:
- `wiki/index.md` — Content catalog. Every wiki page listed with link + one-line summary. Organized by category (entities, concepts, synthesis, sources). Updated on every ingest.
- `wiki/log.md` — Chronological record. Append-only. Every operation (ingest, query, lint) logged with timestamp.

## Domain Focus
AI Builder's Knowledge Base:
- AI/LLM industry (companies, models, products, capabilities, pricing)
- Content distribution (AEO, SEO, bilingual arbitrage, newsletter, social platforms)
- Builder tools and workflows (Claude Code, Remotion, MCP, pipelines)
- People and their ideas
- My projects: LoreAI (loreai.dev), blog2video (AI精读)

## Wiki Page Format

Every wiki page uses this structure:

```
---
type: entity | concept | synthesis | source-summary
created: YYYY-MM-DD
last-updated: YYYY-MM-DD
sources:
  - raw/filename.md
tags: []
---

# Title

## Summary
[2-3 sentences]

## Details
[Bullet points preferred over prose]

## Connections
- Related: [[other wiki pages]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
```

## Conventions
- Flat file structure in wiki/ — no subdirectories. Use index.md categories for organization.
- Wiki page filenames: kebab-case, descriptive (e.g., `anthropic.md`, `aeo-strategy.md`)
- Link wiki pages to each other with [[wikilinks]]
- Link concepts worth tracking: [[AEO as distribution strategy]], [[bilingual content arbitrage]]
- Don't link generic terms: AI, marketing, Python
- Chinese-English mixing is normal. Don't standardize.
- When sources contradict: use `> [!warning]` callout, keep both claims with sources
- Every claim must trace to a source file in raw/

## Log Format

```
## [YYYY-MM-DD] ingest | Source Title
source: raw/filename.md
pages-created: page1.md, page2.md
pages-updated: page3.md

## [YYYY-MM-DD] query | Question text
pages-consulted: page1.md, page2.md
answer-filed: synthesis-page.md (or "chat only")

## [YYYY-MM-DD] lint
pages-scanned: N
issues: orphans(N), stale(N), contradictions(N)
auto-fixed: description
```

## Repo Locations (for reference)
- LoreAI: ~/Desktop/Project/loreai-v2
- blog2video: ~/Desktop/Project/blog2video
