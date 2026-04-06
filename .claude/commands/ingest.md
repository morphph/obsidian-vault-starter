---
name: ingest
description: "Ingest a source into the wiki. Usage: /ingest <file-path|URL|scan>"
---

# Ingest — Add Source to Wiki

Read CLAUDE.md first for wiki conventions.

## Arguments
Parse `$ARGUMENTS` for one of:
- **File path** in raw/ (e.g., `/ingest raw/2026-04-06-article.md`)
- **URL** (e.g., `/ingest https://example.com/article`)
- **"scan"** — find all files in raw/ not yet logged in wiki/log.md, ingest each

## Workflow

### 1. Acquire the source

- **If URL:** Fetch content via WebFetch. Save to `raw/{YYYY-MM-DD}-{slug}.md` with the article content in markdown. The file is now immutable.
- **If file path:** Verify the file exists in raw/. Read it.
- **If "scan":** Read wiki/log.md, list all raw/ files. Find files not yet ingested (not mentioned in any log entry). Ingest each in order.

### 2. Read and extract

Read the source document. Extract:
- **Entities:** People, companies, products, models mentioned
- **Concepts:** Strategies, frameworks, technical ideas, patterns
- **Key claims:** Factual assertions worth tracking
- **Connections:** Links to existing wiki pages

### 3. Discuss with user

Briefly share 3-5 key takeaways from the source. Ask if there's anything specific to emphasize or skip.

### 4. Create/update wiki pages

For each entity and concept worth a page:

**If wiki page already exists:**
- Read the existing page
- Add new information from this source
- Add the source to frontmatter `sources:` list
- Update `last-updated` date
- Add row to Source Log table
- If new info contradicts existing content, use `> [!warning]` callout and keep both claims

**If no wiki page exists:**
- Create new page following the Wiki Page Format in CLAUDE.md
- Use kebab-case filename
- Include frontmatter with type, dates, sources, tags
- Write Summary, Details, Connections, Source Log sections
- Link to other wiki pages with [[wikilinks]]

Also create a source summary page: `wiki/source-{slug}.md` with type: source-summary

### 5. Update index

Read wiki/index.md. Add or update entries for every page touched. Each entry: `- [[page-name]] — one-line summary`

Organize under the correct category (Entities, Concepts, Synthesis, Sources).

### 6. Update log

Append to wiki/log.md:
```
## [YYYY-MM-DD] ingest | {Source Title}
source: raw/{filename}
pages-created: {list}
pages-updated: {list}
```

### 7. Report

Show in terminal:
- Source title
- Pages created (with links)
- Pages updated (with links)
- Total pages touched
