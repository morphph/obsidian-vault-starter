---
name: ingest
description: "Use this skill whenever the user wants to add a new source to the wiki. This includes pasting a URL, sharing a file path in raw/, asking to 'save this article', 'add this to wiki', 'ingest this', 'process this link', '把这个加入 wiki', or scanning raw/ for un-logged files. Also triggers when user shares a substantive article, tweet thread, or doc and context suggests they want it captured (not just discussed). **Don't use when** the user is asking what the wiki already contains — use `/query` instead."
---

# Ingest — Add Source to Wiki

Read CLAUDE.md first for wiki conventions.

## Bundled references — read on demand

- `references/github-deep-scan.md` — GitHub repo URL 的深扫流程 + 源文档模板。**遇到 GitHub repo URL 必读**。
- `references/structured-close-reading.md` — step 3 的**默认**结构：原文结构精读（贴原文章节序的中文精读，2026-07-07 作者拍板）。**每次走到 step 3 前必读**。
- `references/study-guide-12.md` — step 3 的备选结构：12-section 学习型解读（重组式 study guide）。仅当用户明确要求 study guide / 深度解读框架时使用。

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
- **GitHub repos** (github.com/{owner}/{repo} with no file path after): Read `references/github-deep-scan.md` and follow it, then continue with steps 2-8 below
- **JS-heavy sites** (need browser rendering): twitter.com, x.com, youtube.com, reddit.com, linkedin.com, facebook.com, instagram.com, medium.com (paywalled), substack.com (paywalled)
- **Static sites** (WebFetch works fine): most blogs, news sites, GitHub pages, documentation sites

**Step 2 — Fetch using the right method:**

For **JS-heavy / authenticated sites**:
1. **Try Claude for Chrome** (if available): Use the `claude-in-chrome` MCP tools to navigate to the URL, wait for rendering, and extract the page content as text. This works best because it uses your real browser session with existing logins.
2. **Fallback to Playwright MCP**: `browser_navigate` → wait for load → `browser_snapshot` → extract main content → close the browser.
3. **Last resort — WebFetch**: Try anyway. May return partial content, which is better than nothing. Flag if content looks incomplete.

For **static sites**:
1. **WebFetch** (fast, simple) — try this first
2. **Fallback to Playwright MCP** if WebFetch returns empty or error

**Step 3 — Save the content:**
Save to `raw/{YYYY-MM-DD}-{slug}.md` with the article content in markdown. Include a header with the source URL and fetch method used. The file is now immutable.

### 2. Read and extract

Read the source document. Extract:
- **Entities:** People, companies, products, models mentioned
- **Concepts:** Strategies, frameworks, technical ideas, patterns
- **Key claims:** Factual assertions worth tracking
- **Connections:** Links to existing wiki pages

### 3. Chinese close reading — 原文结构精读（默认）

**Read `references/structured-close-reading.md` and follow it completely.** 硬性要求（详见 reference）：
- 贴原文章节顺序，压缩翻译密度——读完精读 ≈ 读完原文，不重组、不夹私货
- 术语留英文原名括号注；关键引语 EN+中译；数据逐字保留
- 元信息头含「一句话主旨」（下游 gate packet 提 Hook 用）；收尾含视频适配自评
- 结束后走 reference 里的收尾互动 + 源纯度提醒

**备选**：用户明确要求 study guide / 深度解读框架时，改读 `references/study-guide-12.md` 并完整遵循（12-section 重组式解读）。

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

Also create a source summary page: `wiki/source-{slug}.md` with type: source-summary. Include the full output of step 3 as a `## 精读` section (or `## 要点解读` if the study-guide structure was used) — this preserves the close reading for future reference and downstream export.

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

### 7. Emit machine-readable ingest event

After the log is updated, record a stable event so the autonomous content system
(Hermes) can detect this Tier-1 ingest and route it downstream. This does **not**
publish, push, or call any external service — it only appends one line to a local
append-only log (`events/ingest-events.jsonl`).

Run the repo CLI once per source ingested:

```bash
bin/obsidian-content record-ingest \
  --source "raw/{filename}.md" \
  --title "{Source Title}" \
  --fetch-method "{fetch method used}" \
  --pages-created "{comma-separated pages}" \
  --pages-updated "{comma-separated pages}"
```

Notes:
- Idempotent: re-running for the same `--source` is a no-op (the event id is a
  hash of the source path), so a re-ingest won't create duplicates.
- For a multi-source ingest (the `sources:` form), call it once per source file.
- If the command is unavailable for any reason, don't block the ingest — just
  note it in the Report; the event can be backfilled later with
  `bin/obsidian-content backfill-from-log`.

### 8. Report

Show in terminal:
- Source title
- Pages created (with links)
- Pages updated (with links)
- Total pages touched
- Ingest event id(s) recorded (from step 7)
