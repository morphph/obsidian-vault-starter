---
name: visualize
description: "Generate Excalidraw diagram from wiki knowledge. Usage: /visualize <topic|source-path|blank for full map>"
---

# Visualize — Generate Wiki Diagrams

Read CLAUDE.md for wiki conventions. Use the excalidraw-diagram skill for diagram generation.

## Arguments

Parse `$ARGUMENTS` to determine scope:

- **Topic name** (e.g., `/visualize harness-design`) → synthesize from all wiki pages connected to that topic
- **Source path** (e.g., `/visualize raw/2026-04-07-article.md`) → diagram just that one source
- **Blank** (`/visualize`) → generate a full wiki map showing all entities, concepts, and their connections

## Workflow

### 1. Gather content

**If topic:**
- Read `wiki/index.md` to find the topic page and related pages
- Read the topic's wiki page — follow its `## Connections` links
- Read all connected pages (1 hop out)
- Collect: entities, concepts, relationships, key claims, data points

**If source path:**
- Read the source file
- Extract: entities, concepts, relationships, key claims, data points
- Check if any wiki pages already exist for these — read them for additional context

**If blank (full map):**
- Read `wiki/index.md`
- Read all wiki pages
- Map: every entity, concept, and the links between them

### 2. Design the visual argument

Before generating JSON, plan the diagram:

- **What story does this tell?** Not just boxes and labels — what's the argument?
- **What layout embodies the meaning?** Flow (left→right for processes), hierarchy (top→down for dependencies), radial (center→out for ecosystems), timeline (for sequences)
- **What level of detail?** Simple/conceptual for overviews, comprehensive/technical for deep dives
- **Color semantics:** Use the palette from the excalidraw-diagram skill — red for problems, purple for AI/LLM concepts, blue for architecture, green for success/output, yellow for decisions/principles

### 3. Generate the diagram

Use the excalidraw-diagram skill to generate valid `.excalidraw` JSON.

Follow the skill's methodology:
- Shapes should BE the meaning (isomorphism test)
- Include evidence artifacts for technical diagrams (real data, actual names)
- Multi-zoom: summary flow + section boundaries + detail

### 4. Render and validate

Render to PNG using the skill's renderer:
```
cd .claude/skills/excalidraw-diagram/references
uv run python render_excalidraw.py <excalidraw-file> --output <png-file>
```

View the PNG to check for:
- Text overlap or misalignment
- Arrow connections making sense
- Visual balance and readability
- The story being clear without reading labels

Fix issues and re-render if needed. Delete the PNG after validation.

### 5. Save and register

**Filename convention:**
- Topic diagram: `wiki/visual-{topic}.excalidraw`
- Source diagram: `wiki/visual-source-{slug}.excalidraw`
- Full map: `wiki/visual-wiki-map.excalidraw`

**Update wiki/index.md** — add entry under `## Visuals` category:
`- [[visual-{name}]] — one-line description of what the diagram argues`

**Update wiki/log.md:**
```
## [YYYY-MM-DD] visualize | {Description}
scope: {topic / source / full-map}
source-pages: {list of wiki pages consulted}
output: visual-{name}.excalidraw
```

### 6. Report

Show in terminal:
- What the diagram argues (1 sentence)
- Pages consulted
- File created
- Suggest embedding in relevant wiki page: `![[visual-{name}.excalidraw]]`
