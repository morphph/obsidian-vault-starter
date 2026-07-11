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

### 4b. 白板图（默认自动 — 作者 2026-07-11 拍板「ingest 完自动跟精读」）

精读（step 3）已经产出；这一步补上配套的白板图，让每次 ingest 直接得到「精读＋图」完整学习包。

- **单一真源**：读 `.claude/commands/learn-note.md` 的 **Step 2（白板图）与 Step 3（嵌入）**并完整照做——
  同样的可图则图判断、同样的 `visuals/<slug>/` 产物路径、同样的渲染回环与分层导出。
  产物路径与 headless `learn` verb 完全一致，因此 WF1 whiteboard lane 再跑 `learn` 时幂等预检直接跳过，零重复成本。
- 判断「不可图」时照 learn-note 的约定记 `LEARN_NO_VISUAL` 原因（写进 Report），不硬画。
- **scan（批量）模式例外**：白板图逐篇 ≈ 数分钟＋$1-2。先列出待 ingest 清单与预估成本问作者一次，
  作者点头才逐篇带图；否则只做精读、图留给后续 `learn`。

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

### 8. Report — 摘要先行

**开头直接给作者可读的学习包摘要**（不是只报文件清单）：
1. `**一句话主旨**`（逐字取自精读元信息头）
2. 5-10 句中文摘要（从精读提炼：核心论证链 + 最硬的 1-2 个数据/引语）
3. 白板图：用 Read 展示 `visuals/<slug>/<slug>-diagram.png`（或注明 LEARN_NO_VISUAL 原因）
4. 精读全文路径 `wiki/source-<slug>.md`

然后才是账目：
- Pages created / updated (with links) · total touched
- Ingest event id(s) recorded (from step 7)
