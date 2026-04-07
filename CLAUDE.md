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

## Commands

Four slash commands operate on the wiki:

### `/ingest <url|file|scan>`
Drop a source into the wiki. The core operation — one source fans out updates across multiple wiki pages.
- **URL**: Fetches content (see Source Fetching Tools below), saves to `raw/`, then ingests
- **GitHub repo URL**: Deep scan — fetches README, file tree, deps, key source files, synthesizes architecture summary (see Source Types below)
- **File path**: Ingests an existing file in `raw/`
- **scan**: Finds all files in `raw/` not yet in `wiki/log.md`, ingests each in order
- Creates source summary + entity/concept pages, updates index + log
- Discuss key takeaways with user before creating pages

### `/query <question>`
Ask a question against the wiki. Reads `wiki/index.md` to find relevant pages, synthesizes an answer with [[wikilink]] citations.
- Optionally file good answers back as synthesis pages
- Flags data gaps when the wiki can't fully answer
- Logs every query to `wiki/log.md`

### `/lint`
Periodic health check of the wiki.
- Checks: orphan pages, stale pages, missing cross-references, contradictions, index drift, unresolved links, thin coverage
- Optionally auto-fixes index drift and missing links
- Logs results to `wiki/log.md`

### `/visualize <topic|source-path|blank>`
Generate Excalidraw diagrams from wiki knowledge. Uses the excalidraw-diagram skill.
- **Topic** (e.g., `/visualize harness-design`): Synthesizes from all connected wiki pages on that topic
- **Source path** (e.g., `/visualize raw/article.md`): Diagrams just that one source
- **Blank**: Full wiki map of all entities, concepts, and connections
- Saves as `wiki/visual-{name}.excalidraw`, registered in index under Visuals category
- Renders to PNG for validation, then deletes PNG (`.excalidraw` is the artifact)
- Embed in wiki pages with `![[visual-{name}]]`

## Skills

### excalidraw-diagram
Generates `.excalidraw` JSON files that make visual arguments. Installed at `.claude/skills/excalidraw-diagram/`.
- Diagrams should argue, not just display — shapes embody meaning
- Color palette in `references/color-palette.md` (customizable)
- Playwright-powered render pipeline for visual validation
- Used by `/visualize` command

## Source Types

### Articles & Posts
Standard web content — blogs, documentation, X/Twitter articles. Saved as-is to `raw/`.

### GitHub Repos (Deep Scan)
For repo URLs, `/ingest` runs a deep architecture scan via `gh` CLI: README, file tree, dependencies, CLAUDE.md/AGENTS.md, key source files, recent commits. Synthesized into a structured summary in `raw/` covering: what it does, architecture, tech stack, patterns & best practices, ecosystem connections.

## Pattern Categories

When extracting patterns from repos (or any source), classify under these three categories:

- **Harness Engineering** — Everything about building around LLMs: agents, tools, memory, evaluation loops, hooks, prompts, cost management, Claude Code patterns, MCP configurations
- **System Design** — Architecture, pipelines, data flow, modularity, error recovery — the non-LLM craft
- **Developer Experience** — Onboarding, repo structure, documentation design, self-setup patterns

Only include categories that have actual content. These categories may expand over time.

## Source Fetching Tools

For `/ingest` URL handling, use this priority chain:

1. **WebFetch** — Built-in. Fast, works for static sites (blogs, docs, GitHub pages).
2. **Claude for Chrome MCP** — Uses real browser with user's login sessions. Best for JS-heavy and authenticated sites (Twitter/X, YouTube, Reddit, LinkedIn). Requires Chrome extension installed.
3. **Playwright MCP** — Headless browser automation. Fallback for JS-heavy sites when Chrome isn't available. Configured as `playwright` MCP server.

JS-heavy sites (need browser): twitter.com, x.com, youtube.com, reddit.com, linkedin.com, facebook.com, instagram.com, medium.com, substack.com

## Repo Locations (for reference)
- LoreAI: ~/Desktop/Project/loreai-v2
- blog2video: ~/Desktop/Project/blog2video
