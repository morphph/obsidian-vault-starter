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

- **If file path:** Verify the file exists in raw/. Read it.
- **If "scan":** Read wiki/log.md, list all raw/ files. Find files not yet ingested (not mentioned in any log entry). Ingest each in order.
- **If URL:** Use the smart fetch chain below.

#### Smart URL Fetch Chain

Detect the URL type and use the best fetching method. Try methods in order — if one fails or returns empty/unusable content, fall through to the next.

**Step 1 — Classify the URL:**
- **GitHub repos** (github.com/{owner}/{repo} with no file path after): Use the GitHub Deep Scan (see below)
- **JS-heavy sites** (need browser rendering): twitter.com, x.com, youtube.com, reddit.com, linkedin.com, facebook.com, instagram.com, medium.com (paywalled), substack.com (paywalled)
- **Static sites** (WebFetch works fine): most blogs, news sites, GitHub pages, documentation sites

**Step 2 — Fetch using the right method:**

For **JS-heavy / authenticated sites**:
1. **Try Claude for Chrome** (if available): Use the `claude-in-chrome` MCP tools to navigate to the URL, wait for rendering, and extract the page content as text. This works best because it uses your real browser session with existing logins.
2. **Fallback to Playwright MCP**: Use the `playwright` MCP server tools:
   - `browser_navigate` to the URL
   - Wait for page to load (use `browser_wait_for_load_state` or similar)
   - `browser_snapshot` to get the accessibility tree as structured text
   - Extract the main content from the snapshot
   - Close the browser when done
3. **Last resort — WebFetch**: Try anyway. May return partial content, which is better than nothing. Flag if content looks incomplete.

For **static sites**:
1. **WebFetch** (fast, simple) — try this first
2. **Fallback to Playwright MCP** if WebFetch returns empty or error

**Step 3 — Save the content:**
Save to `raw/{YYYY-MM-DD}-{slug}.md` with the article content in markdown. Include a header with the source URL and fetch method used. The file is now immutable.

#### GitHub Deep Scan

For GitHub repo URLs (e.g., `https://github.com/owner/repo`), run a deep architecture scan using `gh` CLI:

**Step 1 — Fetch repo data:**
```bash
# Metadata
gh repo view {owner}/{repo} --json name,description,stargazerCount,primaryLanguage,updatedAt

# File tree
gh api "repos/{owner}/{repo}/git/trees/main" --paginate --jq '.tree[] | select(.type=="blob") | .path'

# README
gh api repos/{owner}/{repo}/contents/README.md --jq '.content' | base64 -d

# Dependencies (try each, take what exists)
gh api repos/{owner}/{repo}/contents/package.json --jq '.content' | base64 -d
gh api repos/{owner}/{repo}/contents/pyproject.toml --jq '.content' | base64 -d

# Agentic config (if exists)
gh api repos/{owner}/{repo}/contents/CLAUDE.md --jq '.content' | base64 -d
gh api repos/{owner}/{repo}/contents/AGENTS.md --jq '.content' | base64 -d

# Recent activity
gh api "repos/{owner}/{repo}/commits?per_page=15" --jq '.[].commit.message' 
```

**Step 2 — Read key source files:**
From the file tree, identify and fetch 2-3 key files:
- Entry point (e.g., `src/index.ts`, `main.py`, `scripts/` directory)
- Main config or schema file
- Any file that reveals the core architecture pattern

Use `gh api repos/{owner}/{repo}/contents/{path} --jq '.content' | base64 -d` to fetch each.

**Step 3 — Synthesize into structured source document:**

Save to `raw/{YYYY-MM-DD}-repo-{repo-name}.md` with this structure:

```markdown
# {Repo Name}

**Source:** {github URL}
**Author/Org:** {owner}
**Stars:** {count} | **Language:** {lang} | **Last updated:** {date}
**Fetch method:** GitHub Deep Scan (gh CLI)

## What It Does
[Problem it solves, who it's for, why it exists — from README]

## Architecture
[File structure analysis + key design decisions from reading source files]

## Tech Stack
[Language, dependencies, frameworks — from package.json/pyproject.toml]

## Key Patterns & Takeaways
[Reusable patterns, design decisions, best practices worth remembering]

## Ecosystem Connections
[How this relates to existing wiki concepts — link with [[wikilinks]]]

## Repo Vitals
- Stars: {N} | Forks: {N}
- Language: {lang}
- Last commit: {date} — {message}
- Active/stale assessment
```

**Important:** The Patterns section is the primary value — each pattern should state: what it is, why it works, where else it could apply.

Then proceed with normal ingest steps 2-7 (extract, discuss, create/update pages, update index + log).

### 2. Read and extract

Read the source document. Extract:
- **Entities:** People, companies, products, models mentioned
- **Concepts:** Strategies, frameworks, technical ideas, patterns
- **Key claims:** Factual assertions worth tracking
- **Connections:** Links to existing wiki pages

### 3. Discuss with user

用中文提供 3-5 个**详细深入的要点解读**（不是简短 bullet point）。每个要点需要：
- 解释概念是什么、为什么重要
- 如果原文有理论框架或心智模型，用中文重新阐述
- 如果有实操建议（how to practice），明确列出
- 中文为主，英文要点可附在后面保持简短

目的：用户英文阅读有限，通过中文要点尽可能快速、深入地理解原文内容。

Ask if there's anything specific to emphasize or skip.

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

Also create a source summary page: `wiki/source-{slug}.md` with type: source-summary. Include a `## 要点解读` section with the detailed Chinese takeaways from step 3 — this preserves the analysis for future reference.

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
