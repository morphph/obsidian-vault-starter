---
name: ingest
description: "Use this skill whenever the user wants to add a new source to the wiki. This includes pasting a URL, sharing a file path in raw/, asking to 'save this article', 'add this to wiki', 'ingest this', 'process this link', '把这个加入 wiki', or scanning raw/ for un-logged files. Also triggers when user shares a substantive article, tweet thread, or doc and context suggests they want it captured (not just discussed). **Don't use when** the user is asking what the wiki already contains — use `/query` instead."
---

# Ingest — Add Source to Wiki

Read AGENTS.md first for wiki conventions.

## Bundled references — read on demand

step 3 **按源类型分流**（见下方 step 3）。先按类型挑对应 reference，走到 step 3 前必读那一个：

- `references/github-deep-scan.md` — **GitHub repo URL** 的深扫流程 + 源文档模板。遇到 GitHub repo URL 必读。
- `references/structured-close-reading.md` — **博文 / 文章 / 长推文**：全文自然翻译（原文口吻直译、不压缩；2026-07-15 作者拍板）。
- `references/essence-extraction.md` — **PDF / YouTube 视频**：精要提炼（核心论点 + 框架 + 数据 + 金句 + 可执行要点）。
- `references/study-guide-12.md` — 备选：12-section 重组式 study guide。仅当用户**明确要求** study guide / 深度解读框架时使用。

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

**Step 1 — Classify the source** (决定获取方式 + 下游 step 3 走哪条):
- **GitHub repos** (github.com/{owner}/{repo}, no file path): Read `references/github-deep-scan.md` and follow it, then continue with steps 2-8 below. → step 3 走 deep-scan 模板。
- **YouTube videos** (youtube.com/watch, youtu.be): 真正的内容是**字幕/转录**,不是页面 HTML。用 yt-dlp 抓（见下）。→ step 3 走**精要**（essence-extraction）。
- **PDF** (URL 以 `.pdf` 结尾，或本地 `.pdf` 路径): 用 `Read` 工具直接读（原生 PDF，含图/扫描件，长 PDF 分页读），不必装任何库。→ step 3 走**精要**（essence-extraction）。
- **JS-heavy sites** (need browser rendering): twitter.com, x.com, reddit.com, linkedin.com, facebook.com, instagram.com, medium.com (paywalled), substack.com (paywalled)。→ step 3 走**全文翻译**（structured-close-reading）。
- **Static sites** (WebFetch works fine): most blogs, news sites, docs sites。→ step 3 走**全文翻译**。

> 类型只是默认。用户一句话可覆盖（"这个 PDF 其实是篇散文，给我全文翻译" → 改走 structured-close-reading）。

**Step 2 — Fetch using the right method:**

For **YouTube videos** — 抓字幕（字幕就是内容。以下命令 2026-07-15 在本机 yt-dlp 2026.02.21 实测通过）:
```bash
# 1) 抓字幕：手动优先 + 自动兜底；en 优先，中文次之。--js-runtimes node 消除新版 JS-runtime 报错
yt-dlp --js-runtimes node --skip-download --write-subs --write-auto-subs \
  --sub-langs "en.*,zh-Hans,zh-Hant,zh" --sub-format vtt \
  -o "raw/{YYYY-MM-DD}-{slug}.%(ext)s" "{URL}"
# 若一条字幕都没抓到，先看有哪些轨道，再挑一个可用语言重跑：
yt-dlp --list-subs "{URL}"
# 2) 抓元数据（标题/频道/时长/发布日，填进精要元信息头）
yt-dlp --js-runtimes node --skip-download \
  --print "%(title)s || %(uploader)s || %(duration_string)s || %(upload_date)s" "{URL}"
```
- 抓到多个 `.vtt`（en / en-orig / …）时，**优先手动/原文轨道**（最干净），自动字幕次之。
- **vtt → 纯文本**（去时间轴/头部/cue 标签，去连续重复行——自动字幕常有滚动重复）:
  ```bash
  sed -E '/^WEBVTT/d; /^Kind:/d; /^Language:/d; /-->/d; /^[[:space:]]*$/d; s/<[^>]*>//g' \
    "raw/{...}.en.vtt" | awk '$0!=prev {print} {prev=$0}'
  ```
- ⚠️ YouTube 常改，flag 可能失效。报错就 `--list-subs` 探测 + 按提示调整；真抓不到字幕，回退到 `--print "%(description)s"` 的简介 + 章节，并在 Report 标注"仅简介、无转录"。

For **PDF** — 用 `Read` 工具读全文：长 PDF 用 `pages` 参数**分页读完**（别只读前几页——中段最容易漏），扫描件/图重的靠 Read 的视觉能力直接读。无需 PyMuPDF4LLM 等外部库。

For **JS-heavy / authenticated sites**:
1. **Try Codex for Chrome** (if available): Use the `Codex-in-chrome` MCP tools to navigate to the URL, wait for rendering, and extract the page content as text. This works best because it uses your real browser session with existing logins.
2. **Fallback to Playwright MCP**: `browser_navigate` → wait for load → `browser_snapshot` → extract main content → close the browser.
3. **Last resort — WebFetch**: Try anyway. May return partial content, which is better than nothing. Flag if content looks incomplete.

For **static sites**:
1. **WebFetch** (fast, simple) — try this first (prefer the `defuddle` skill for cleaner extraction)
2. **Fallback to Playwright MCP** if WebFetch returns empty or error

**Step 3 — Save the content:**
Save to `raw/{YYYY-MM-DD}-{slug}.md` with the content in markdown (YouTube: cleaned transcript + metadata header; PDF: extracted text or a note pointing at the local `.pdf`). Include a header with the source URL and fetch method used. The file is now immutable.

### 2. Read and extract

Read the source document. Extract:
- **Entities:** People, companies, products, models mentioned
- **Concepts:** Strategies, frameworks, technical ideas, patterns
- **Key claims:** Factual assertions worth tracking
- **Connections:** Links to existing wiki pages

### 3. Chinese 学习产物 — 按源类型分流

按 step 1 判定的类型，读对应 reference 并**完整遵循**：

| 源类型 | 模式 | Reference | 产出要点 |
|---|---|---|---|
| **博文 / 文章 / 长推文**（含 JS-heavy/static 抓来的正文） | **全文自然翻译** | `references/structured-close-reading.md` | 原文口吻直译、不压缩、去转述腔——读中文 ≈ 读原文全部 |
| **PDF / YouTube 视频** | **精要提炼** | `references/essence-extraction.md` | 核心论点 + 框架 + 关键数据 + 金句 + 可执行要点；覆盖度优先、盯中段、单遍不分块 |

两条共同硬性要求：
- 术语留英文原名括号注；关键引语/金句 EN + 中译；数据逐字保留
- 元信息头含 `**一句话主旨**：`（**逐字用这个字段名**——下游 gate packet / learn_note.py 提 Hook 用）；收尾含视频适配自评
- 结束后走 reference 里的收尾互动 + 源纯度提醒

**覆盖：**
- 类型判断有歧义时（如一个 PDF 其实是短散文、一个视频其实是密集讲座），按内容实质选，或直接问作者一句。
- 用户**明确要求** study guide / 深度解读框架时，改读 `references/study-guide-12.md` 并完整遵循（12-section 重组式解读，产出包成 `## 要点解读`）。

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
- Create new page following the Wiki Page Format in AGENTS.md
- Use kebab-case filename
- Include frontmatter with type, dates, sources, tags
- Write Summary, Details, Connections, Source Log sections
- Link to other wiki pages with [[wikilinks]]

Also create a source summary page: `wiki/source-{slug}.md` with type: source-summary. Include the full output of step 3, wrapped by the section heading matching the mode used: `## 精读`（博文全文翻译）· `## 精要`（PDF/视频精要）· `## 要点解读`（study guide 备选）. This preserves the step-3 学习产物 for future reference and downstream export.

### 4b. 白板图（默认自动 — 作者 2026-07-11 拍板「ingest 完自动跟精读」）

step 3 学习产物（精读/精要）已经产出；这一步补上配套的白板图，让每次 ingest 直接得到「文＋图」完整学习包。图嵌入 step 3 产物里最相关章节之后（不论该 section 是 `## 精读` 还是 `## 精要`）。

- **单一真源**：读 `.Codex/commands/learn-note.md` 的 **Step 2（白板图）与 Step 3（嵌入）**并完整照做——
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
1. `**一句话主旨**`（逐字取自 step 3 产物元信息头）
2. 5-10 句中文摘要（从精读/精要提炼：核心论证链 + 最硬的 1-2 个数据/引语）
3. 白板图：用 Read 展示 `visuals/<slug>/<slug>-diagram.png`（或注明 LEARN_NO_VISUAL 原因）
4. step 3 产物全文路径 `wiki/source-<slug>.md`

然后才是账目：
- Pages created / updated (with links) · total touched
- Ingest event id(s) recorded (from step 7)
