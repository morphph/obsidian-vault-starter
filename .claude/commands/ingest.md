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

### 3. Discuss with user — 详细学习型解读（Chinese Study Guide）

**目的**：让用户最大程度地从这篇英文源中学到东西。用户正在学习 AI coding / agent development / content automation 等课题，英文阅读有限，希望通过中文深度解读快速且彻底地内化原文。

**核心原则**：
- **长度不限**——宁可详细到啰嗦也不要简短。用户明确接受长输出换学习深度的 trade-off
- **不是 summary，是 study guide**——目标不是"概括"而是"教会"
- **每个概念都要解释为什么重要，不只是描述它是什么**
- **主动思考交叉链接**——这篇文章如何与现有 wiki 知识互动
- **语言**：中文为主体。英文只在两处出现：(a) 概念原名（中文译名后加括号注），(b) 关键原文引语保留英文 + 附中文意译。**不要把整段中文再翻译成英文重复一遍**

**完整结构**（不是每篇都需要全部 section，但每次必须主动思考每个维度是否适用；不适用的明确说明"无"而不是直接省略，让用户知道你想过了）：

---

#### 1. 元信息
- **作者**：姓名 + 在该领域的位置/身份/stake（是 insider 还是 outsider？为什么他的观点值得听？）
- **来源**：发表平台 + 时间
- **影响力指标**（如果可见）：views / likes / bookmarks / stars
- **在作者整体输出中的位置**：是系列文？独立观点？回应了谁？

#### 2. 核心论点（Thesis）
用 2-3 句中文清晰复述作者的核心论点。建议格式："作者主张 X，因为 Y，所以 Z。" 这是整篇文章的"压缩包"。

#### 3. 论证结构
作者怎么论证这个核心论点的？分了几步？逻辑链是什么？画出思路骨架——这通常比记住单个观点更有迁移价值，因为骨架可以套用到自己的思考。

#### 4. 关键概念字典
**每个新概念用一个完整段落（2-3 段）**，不是 bullet 一行带过：

> **概念中文名 (English Original)**
> - **是什么**：精确定义，避免循环定义
> - **为什么重要**：在作者整个 thesis 里扮演什么角色？基础概念还是推论？
> - **直觉/类比**：用一个生活化例子帮助理解
> - **适用场景**：什么时候用得上？
> - **反面/失败模式**：误用、过度使用、错配场景会怎样？

#### 5. 框架与心智模型
如果原文有理论框架、决策规则、判断流程——用中文重新表述 + 至少一个具体例子展示如何套用。框架是这类文章迁移价值最高的部分。

#### 6. 关键数据与例证
所有量化数据、case study、demo 结果——按重要性排序，每条说明它支撑作者的哪个观点。**要保留具体数字**（"102 features in 7 days" 比 "many features" 强 10 倍）。这些是文章可信度的核心，也是你日后引用时的弹药。

#### 7. 关键引语
摘录 3-7 句最有冲击力的原文（保留英文 + 附中文意译）。这些是写自己文章引用时的弹药；同时它们浓缩了文章最锐利的观点。

#### 8. 实操指南
作者明确说"how to do"的内容——给步骤、checklist、清单。如果作者只给方法论没给步骤，你帮他翻译成可执行步骤。如果文章是案例描述而不是 how-to，从案例中反推出可重复的 pattern。

#### 9. 对比与反对意见
- **与哪些主流做法对比**？（如 "vs vibe coding"、"vs traditional planning"、"vs RAG"）
- **作者明确反对什么**？为什么？这通常揭示作者的核心信念。
- **作者隐含承认的限制是什么**？边界条件、不适用场景。

#### 10. 与 wiki 知识的连接
- **强连接**：与哪些现有 wiki 页面直接相关 — `[[page-name]]` — 一句话说明怎么相关
- **强化**：这篇文章如何深化我们对某个已有概念 `[[X]]` 的理解
- **挑战/补充**：是否对某个已有观点 `[[Y]]` 提出了反例、新角度、或互补观点
- **扩展方向**：这篇文章引出了哪些可以继续探索的问题？是否值得 ingest 它 reference 的某个源？

> **重要**：调用 wikilink 前先快速扫一下 `wiki/index.md` 确认页面存在，避免引用不存在的页面。

#### 11. 对用户（vfan）的启示
基于用户的具体情况（参考 memory 里的 [[user_profile]]），这篇文章意味着什么？给 3 类建议：
- **短期**（本周可做）
- **中期**（接下来 2-4 周）
- **长期**（如果方向被验证后）

如果文章与用户工作完全无关，这一节明确写"暂无直接应用"——让用户知道你思考过这件事。

#### 12. 一句话总结
压缩到一句话——可以发推/朋友圈/作为博客标题的版本。这是 stress test：如果你不能压缩到一句话，可能你自己还没真正理解。

---

#### 收尾互动
完成上述解读后，问用户 3 件事：
1. 有什么要 emphasize 或 deep dive 的概念吗？
2. 是否需要 ingest 文章里 reference 的某个源？
3. 这次解读的哪部分对你最有用？（用来校准未来 ingest 的侧重点）

**源纯度提醒**：如果用户偏好只用官方来源（参考 memory 里相关 feedback），在 ingest 前先确认该 URL 是 author 本人的官方源（repo / 个人网站 / 本人社交账号）还是第三方解读。第三方解读 ingest 前要明确提醒，让用户决定是否继续。

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
