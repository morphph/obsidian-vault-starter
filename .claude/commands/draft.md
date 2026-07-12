---
name: draft
description: "Use this skill whenever the user wants to graduate wiki/raw content into a publication-ready article. Triggers: 'draft an article about X', 'turn this wiki page into a post', 'write a draft from this raw source', 'I want to publish about Y', 'graduate this to drafts', '把这个写成一篇文章'. Use even if the user hasn't explicitly said 'draft' — when they ask for a 'post', 'article', 'blog', or want something 'publish-ready'. **Don't use when** the user wants to add a raw source to the wiki — use `/ingest`."
---

# Draft — Create Article Draft

Read CLAUDE.md first for wiki conventions.

## Arguments
Parse `$ARGUMENTS` for one of:
- **Research workspace** (e.g., `/draft research/openai-codex/`) — build article from a `/research` run (report + candidates). Optionally name an angle: `/draft research/<slug>/ angle:2` (default: §7 角度1，the recommended one)
- **Wiki page path** (e.g., `/draft wiki/context-noise-governance.md`) — graduate a wiki page
- **Raw file path** (e.g., `/draft raw/2026-04-09-bcherny-claude-code-best-practices.md`) — build article from source
- **Topic** (e.g., `/draft Claude Code best practices`) — find relevant raw/ sources and build article

If no argument given, ask the user what to draft.

## Workflow

### 1. Gather source material

**If research workspace:** Read `report.md` + `outline.md` + `ingest-candidates.md` from the
`research/<slug>/` dir. `outline.md` is the Gate-1-approved skeleton — follow its structure;
`report.md` supplies the facts (§1-2, with verification status) and per-channel form references
(§3-5). Also read `audience-profile.md` (repo root) for voice + GEO rules.
**Sourcing follows the 务实 rule** — see step 4.

**Take gate（WF3 铁律，plan §11.1/§11.2 拍板 A）：** if `outline.md` exists, its take section is
load-bearing —
- take 已填（3-5 句作者亲笔）→ **全文围绕 take 展开**：take 的观点必须出现在成稿**前 30%**
  （GEO 位置偏置），每个主张段能挂回 take。
- take 仍是占位（`⏳ 待作者 take`）→ **拒绝开工**：interactive 下告诉用户「Gate 1 take 未填，
  writer 无 take 不开工」；headless 下打印 `ok:false, errors:["take_missing"]` envelope 退出。
- take 占位 **且调用 prompt 含 `TAKE_OPTIONAL`**（作者显式豁免——只能来自 wf3 driver 的
  `resume --take-optional` 旗标，2026-07-09 作者拍板）→ **开工**：用 outline 的候选 thesis 方向当
  **编辑立场**工作论点（行文不得伪称作者亲笔 take），thesis 仍出现在成稿前 30%，
  frontmatter 加 `take: waived`；署名与否由 Gate 2 作者看稿定夺。
- 无 `outline.md`（非 WF3 的旧式 /draft 用法）→ 本 gate 不适用，照常。

**穿透引用（plan §11.7）：** 成稿只许引用 report 里标注的**原始出处**（`[外部: URL]` 的 URL、
`[内部/Tier-1: 页名]` 对应的 raw/ 源），**绝不引用 report.md/outline.md 本身**——防「报告引报告」。
**If wiki page:** Read the wiki page + all files in its `sources:` frontmatter.
**If raw file:** Read the raw file. Check wiki/ for related pages that add context.
**If topic:** Search raw/ and wiki/ for relevant files. Show what you found, ask user to confirm.

### 2. Detect page type and choose article structure

Analyze the content and classify it:

**Narrative / Analytical** (has a thesis, argues a point, connects ideas):
→ Article structure: Hook → Thesis → Evidence/Argument → Implications → Takeaway

**Guide / Reference** (how-to, list of practices, configurations):
→ Article structure: Hook → Why this matters → The practices (reorganized for reading flow) → Quick-start summary

**Entity / Profile** (about a person, company, product):
→ Article structure: Hook → What they did → Why it matters → What to watch

### 3. Show the user a brief plan

Before creating the draft, show:
- Detected type and chosen structure
- Proposed article angle/hook (1 sentence)
- Source files being used
- What will be cut vs kept (if from wiki page)

Ask for confirmation or adjustments.

**Headless rule（被 WF3 driver / headless claude 调起时）**: no one can confirm — skip this
pause, follow `outline.md` as the approved plan (that's what Gate 1 approved), and note
`"headless: plan confirmation skipped (outline.md is the approved plan)"` in the envelope warnings.

### 4. Create the draft article

Create `drafts/{descriptive-kebab-case-name}.md` with:

**Frontmatter:**
```yaml
---
status: draft
sources:
  - raw/{source-file-1}.md
  - raw/{source-file-2}.md
external-refs:        # only when drafting from a research workspace; else omit
  - https://example.com/un-ingested-source
research: research/{slug}/   # only when drafting from a research workspace; else omit
platform: blog
created: {today YYYY-MM-DD}
last-updated: {today YYYY-MM-DD}
tags: [draft]
---
```

The `sources:` field **always points to raw/ files** — the immutable source material.

**Sourcing rule when drafting from a research workspace (务实 / pragmatic):**
- `sources:` = only the candidates that have **already been ingested into `raw/`**. Check each
  `ingest-candidates.md` entry: does a `raw/` file exist for that URL/title? If yes → it's a
  source; if no → it goes in `external-refs:`.
- `external-refs:` = the URLs the draft references that are **not yet in `raw/`**.
- `research:` = pointer back to the `research/<slug>/` workspace.
- **Load-bearing claims must be backed by a `raw/` (ingested) source.** `external-refs` are only
  for supporting / color. If a key claim the article leans on has no `raw/` backing, **flag it**
  and tell the user: "claim X 依赖未 ingest 的源 <URL> — 建议先 `/ingest` 它再定稿。" Don't silently
  ship a load-bearing claim that can't trace to raw/.

**Content transformation:**
- Convert `[[wikilinks]]` to plain text (remove brackets) — reader doesn't have your wiki
- Remove `## Source Log` table — not for readers
- Remove `## Connections` section — internal wiki navigation
- Remove wiki-specific frontmatter references
- Add `<!-- HOOK: [placeholder for opening hook] -->` at the top of the body
- Add `<!-- CTA: [placeholder for closing call-to-action] -->` at the bottom
- Restructure sections according to the detected article type
- Keep the substance — don't water down the content, just reshape it for a reader who doesn't have your wiki context
- Preserve the original language (Chinese stays Chinese, English stays English, mixing is fine)

### 5. Offer companion visual (long-form + diagrammable content)

If the draft is long-form (>2000 words) **and** contains diagrammable structure (architecture, layered framework, workflow with stages, comparison matrix), offer to generate a companion visual:

- Run `/visualize <topic>` to produce `drafts/{name}.excalidraw` + `drafts/{name}.png`
- Embed the PNG in the article body with `![[{name}.png]]` near the relevant section — embed the PNG, NOT the `.excalidraw` (per `feedback_visualize_embed` memory)
- Keep both files in `drafts/` so the user can iterate the Excalidraw and re-export

Skip silently if the draft is short or purely narrative with no diagrammable structure. When unsure, ask the user — visuals take real time and don't fit every draft.

Evidence this step pays off: `managed-agents-architecture`, `connection-context-layers-and-best-practices`, and `claude-code-best-practices-guide` all carry companion visuals because the underlying material is structural.

### 6. Update wiki page (only if source was a wiki page)

Add `status: draft` to the wiki page's frontmatter. Do NOT change any other content.

Skip this step if the draft was built directly from raw/, a topic, or a research workspace.

### 6.5 WF3 mode: bilingual output + machine envelope（仅 research-workspace 且「outline 有 take 或 TAKE_OPTIONAL 豁免」时）

WF3 的发布目标是 loreai.dev **EN+ZH 双语**（Gate 2 审的必须是要发的全部东西）：

1. 主稿 `drafts/<slug>.zh.md`（照上面全部规则写）。**正文必须以 `# <标题>` H1 开头**
   （紧跟 frontmatter 之后；loreai 发布链从 H1 提取 title——没有 H1 会拿代码注释当标题）；
   不留 `<!-- HOOK -->` 之类占位注释。
2. 英文版 `drafts/<slug>.en.md` — **同结构同论点的英文成文**（不是逐句直译；面向同一受众
   画像的英文读者重述，保留全部出处链接与数据）。take 同样出现在前 30%。
3. Frontmatter 两份都带（status/sources/external-refs/research/platform/lang）。
3b. **图示（S11 文图一体，强制评估·可图则图）**：读 `.claude/skills/excalidraw-diagram/SKILL.md`，
   判断文章有可空间化的论证结构则画**一张论证型白板图**（Diagrams ARGUE, not DISPLAY）：
   - 写 `drafts/figs/<slug>/<slug>-fig-1.excalidraw` → 渲染回环（render_excalidraw.py，Read 看 PNG 修到合格）
   - 导出整图 SVG `drafts/figs/<slug>/<slug>-fig-1.svg`（博客用）+ `--export-layers` 分层导出
     （steps.json + layers/，留给 make-video 白板视频线零重画）
   - **双语正文**在最相关章节嵌 `![<一句话图说明>](/diagrams/<slug>-fig-1.svg)`（站点根路径；
     发布链会把 SVG 拷进 loreai `public/diagrams/`）
   - 不可图（纯叙事/清单/太短）：envelope warnings 记 `no_figure: <一句原因>`，不硬画不硬嵌。
   - Gate-2 组合 hash 含图（driver 计算）：改图=改稿，同样触发重呈。
4. 打印机器可读 envelope（contract 1.0 同形，skill 打印、非 CLI verb）：

```json
{
  "contract_version": "1.0",
  "ok": true,
  "verb": "draft",
  "artifacts": {
    "draft_zh": { "path": "drafts/<slug>.zh.md", "sha256": "..." },
    "draft_en": { "path": "drafts/<slug>.en.md", "sha256": "..." },
    "figures":  [ { "path": "drafts/figs/<slug>/<slug>-fig-1.svg", "sha256": "..." } ]
  },
  "data": { "slug": "<slug>", "take_present": true, "research": "research/<slug>/" },
  "warnings": [], "errors": []
}
```

（sha256 用 `shasum -a 256`；**若 shasum 不可用（无 Bash 白名单），置 null 并 warning**——
调用方（wf3 driver）无论如何都要对磁盘产物**自行复算权威 hash**（只信外壳原则），skill 给的
hash 只是 courtesy。Gate 2 的 packet content_hash = driver 拿两个权威 sha256 拼合再 hash——
绑「批的就是发的这一对」。）失败也打印合法 envelope（如 `take_missing`）。

### 7. Report

Show in terminal:
- Source(s) → Draft article (paths)
- Detected type
- Article structure chosen
- Companion visual: path if generated, else "none"
- What to do next: "Open `drafts/{filename}` and polish."（WF3 mode: 改为「等 Gate 2——
  content-ops 会出 review packet」）
