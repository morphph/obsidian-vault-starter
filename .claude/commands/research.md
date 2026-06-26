---
name: research
description: "Use this skill whenever the user wants to research a topic before writing — gather what's known internally + externally, and produce a single research report (facts + per-channel popularity + content angles) + a list of sources worth ingesting. Triggers: 'research X', '调研一下 X', 'help me research before I write about Y', 'what's out there on Z', 'gather sources on W', 'I want to write about X, research it first'. Produces research-plan.md + report.md + ingest-candidates.md in a non-vault workspace (research/<slug>/). **Don't use when** the user wants to add a known source to the wiki — use `/ingest`. **Don't use when** the user just wants an answer from the existing wiki — use `/query`. **Don't use when** they're ready to write from existing material — use `/draft`."
---

# Research — Investigate a Topic → Report + Ingest Candidates

Read CLAUDE.md first for wiki conventions. This skill produces research artifacts in a
**non-vault** workspace; it never writes to `raw/` or `wiki/`, never auto-ingests,
never pushes or publishes. It only produces candidates for a human to select.

## Two ideas this skill is built on

- **Collection is organized by CHANNEL; synthesis is organized by AXIS.** You *search* each
  channel (Web/官方站, X, YouTube) with that channel's native method — operators, recency
  window, engagement metric all differ. You *read* the harvest through two lenses: the
  **事实轴** (what's true → anchor to official sources) and the **增长轴** (what's winning,
  where, written how → content angles). One source has **one channel** (where it lives) but
  gets **two readings** (it's both a fact and a growth signal).
- **The final `report.md` mirrors a proven shape** (see `research/_reference/` fixtures):
  §1 what the topic is · §2 focus-entity deep-dive · §3-5 per-channel Top-N · §6 insights ·
  §7 ranked content angles · appendix timeline. Graft our discipline onto that shape — don't
  replace it.

## Arguments

Parse `$ARGUMENTS` for:
- **A topic** (e.g., `/research OpenAI Codex 指南`) — required. If missing, ask the user.
- **Optional `depth:`** — `quick | standard | deep` (default `standard`). Caps the external
  fan-out budget: `quick` ≈ deep-research only; `standard` ≈ deep-research + 1-2 scanners;
  `deep` ≈ all available scanners + more sources. Surface the chosen depth in the report.

## Workflow

### 1. Derive slug + create workspace

- `slug` = ASCII kebab-case of the topic: lowercase, keep `[a-z0-9]` and hyphens, drop CJK
  and punctuation. If the result is empty (e.g., a pure-Chinese topic), fall back to a
  date-based slug `YYYY-MM-DD-research`.
- Create `research/<slug>/`. **Non-destructive**: if it already exists, do NOT overwrite —
  report it and write to `research/<slug>-rerun-N/` (smallest free N). Note this in the report.

### 2. 查内 — search internal knowledge first (zero-cost, authoritative)

Find what the vault already has, so the report builds on existing Tier-1 anchors instead of
repeating them.

1. Read `wiki/index.md` — **the vault's retrieval mechanism** — to find related pages, then
   read those pages. Pull out the Tier-1 anchors (concepts/claims we already track) worth
   carrying into the report.
2. **Check `drafts/`** for an existing article on this topic. If one exists, **report it
   prominently** ("⚠️ 你已经写过 `drafts/<file>` on this topic") so the user doesn't re-draft a
   published piece. Decide with them whether this is a new angle or a duplicate.
3. Optionally query gbrain as an **accelerator**: `mcp__gbrain__query` / `mcp__gbrain__search`
   for the topic. Treat results as a hint, not authority — **`wiki/index.md` + `drafts/` on disk
   are the source of truth** (gbrain may be stale). If gbrain disagrees with on-disk state,
   trust on-disk and note the discrepancy in `warnings`.

Output of this step: a short list of vault Tier-1 anchors + any duplication warning. These feed
the search plan (so it doesn't re-surface what we already have) and `report.md` §"Vault 已有锚点".

### 3. 计划 — write `research-plan.md` (channel-organized search plan + checkpoint)

This is the casual topic → structured search brief expansion. **Organize the plan by CHANNEL,
and give each channel its native search method.** The two axes do NOT appear here — they are a
synthesis-time concern (step 5). Write `research/<slug>/research-plan.md`:

```markdown
# Research Plan: <topic>
> depth: <quick|standard|deep> · ⚠️ 互动数据：X/YouTube 本机无 scanner，将标「推断·未实测」

## 渠道① Web / 官方站   ← 现在最硬的实测源
- 查询：<topic> site:<official-domain> · "<key phrase>" official docs · …(6-12条)
- 点名直查：<列出该领域权威站，如 anthropic.com · openai.com · latent.space …>
- 搜法：官方文档 / 原始出处优先（这一渠道喂事实核验最准）

## 渠道② X / Twitter
- 查询："<topic>" min_faves:50 site:x.com · "<key phrase>" site:x.com · …(6-12条)
- 搜法：按收藏(bookmark)加权（收藏=想存来重读，信号比赞更硬）；抓 long-article 格式；
  记 作者@handle + 互动 + 是否长文
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」

## 渠道③ YouTube
- 查询："<topic>" youtube 2026 · "<key phrase>" tutorial · …(5-10条)
- 搜法：近 60 天优先；按观看/互动；实操 > 理论
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」

## 消歧块（仅当话题含不认识的实体/新名词时）
- "<entity>" 可能是 模型 / 工具 / 系列名 / … → 搜 <消歧查询> 确认后再扫

## 综合契约（提醒后面 step 5）
- report.md 按双轴综合：事实轴（锚官方源）+ 增长轴（按渠道排 Top-N + 形式拆解 + 角度）
- 候选源对 raw/ 去重；拿不到的数据标「推断·未实测」，绝不瞎编
```

**Checkpoint (balance against zero-friction):**
- Always **write `research-plan.md`** (transparent + reproducible).
- `standard`/`deep`: **pause and show the plan** before the expensive scan — let the user
  eyeball the queries / fix a misread intent. This matches the owner's "做完验证再继续" habit.
- `quick`: proceed without pausing.
- If the plan contains a **消歧块** (unknown entity): **always pause to confirm** which entity
  is meant, regardless of depth — a wrong disambiguation wastes the whole scan.

### 4. 扫外 — execute the plan per-channel (best-effort, isolate the noise)

Raw scraped material is heavy context pollution. **Spawn ONE sub-agent (Agent tool, type
`general-purpose`)** to run the external fan-out and return ONLY synthesized findings — do not
let raw fetches flood the main session. Give the sub-agent `research-plan.md`, the vault anchors
from step 2, and the depth budget. It executes **channel by channel, each with that channel's
search method from the plan.**

Tools the sub-agent uses, in order of reliability:

- **`deep-research` skill — baseline engine, always available.** Fans out web searches, fetches
  sources, adversarially verifies claims, returns a cited synthesis. This is the floor: even if
  every scanner below is missing, research still works (and the Web/官方 channel still produces).
- **`last30days`** — web / Reddit / HN / YouTube trends (engagement-weighted).
- **`bird`** — X targeted search / threads / engagement counts (bookmarks).
- **`summarize`** — YouTube transcripts.
- Use the **`defuddle`** skill to clean any fetched URLs.

**Graceful degradation (required).** `last30days`, `bird`, and `summarize` are **VPS-only and
absent on this machine today** — calling them locally will fail, and that is expected. Treat
each external scanner as **best-effort**: if a tool is missing or errors, **record it in
`warnings[]` and continue** — never fail the run for a missing scanner. When a scanner is absent,
the channel still gets searched via `deep-research`/WebSearch (content is findable; only precise
engagement numbers are not) — mark those numbers **「推断·未实测」**, never fabricate them.

The sub-agent returns, **grouped by channel**: per-channel candidate pieces (link · author ·
date · engagement-or-「推断」· core content · **writing-style note**), plus a flat list of
candidate source URLs (canonical URL + one-line reason each), plus which tools ran vs. skipped.

### 5. 综合 — synthesize into ONE report (anchored on audience-profile.md)

Read `audience-profile.md` (repo root) for reader persona, voice, and GEO writing rules. Now read
the channel-organized harvest through **both axes** and write a single `research/<slug>/report.md`.
**Mirror the reference shape (§1-7 + appendix); graft our discipline inline.**

```markdown
# <topic> 深度调研报告
> depth: <quick|standard|deep> · generated: <YYYY-MM-DD> · tools: <ran> | skipped: <skipped>
> ⚠️ 互动数据：X/YouTube 部分为「推断·未实测」（本机无 scanner），已逐条标注

## TL;DR
<3-5 句:最关键的发现 + 我们该怎么切。我们的增值,Dispatch 没有但有用>

## 0. Vault 已有锚点（查内）
- [[<wiki-page>]] — 一句话:我们已经怎么讲过这个
- (若 drafts/ 已有成稿,这里 ⚠️ 显著标注,避免重复 draft)

## 1. 这个话题是什么 — 事实轴
定义 + 演进 + 关键事实。**逐条对官方文档/原始出处核验**:claim + 出处链接 + 状态。
矛盾的用 `> [!warning]`,两个 claim 都留 + 各自出处。
- **<claim>** — source: <official URL> — ✅ verified / ⚠️ unconfirmed / ❌ contradicted

## 2. 焦点实体深挖（仅当话题含焦点/歧义实体时,否则删掉本节）
从 research-plan 消歧块确认的实体,深挖其核心事实 + 与话题的关系(同 §1 的核验纪律)。

## 3. X / Twitter — Top N（增长轴 · 渠道层）
> ⚠️ 互动数据「推断·未实测」(本机无 bird)
### #1 <作者 @handle> — <一句话定位>
- 链接 / 作者 / 日期 / 格式(单帖|thread|长文)
- 互动:<收藏·浏览,实测或「推断·未实测」>
- 核心内容:<摘要>
- **写作风格拆解**:<格言式 / 技术深度+数据 / 实操叙事 … — 这是给写稿用的弹药>
（Top N 后接「#### 补充值得关注」表 + trending,如有）

## 4. Web / 博客 — Top N（增长轴 · 渠道层）
（同上结构;Web 通常有实测发布日期/作者,无互动数属正常)

## 5. YouTube — Top N（增长轴 · 渠道层）
> ⚠️ 观看/互动「推断·未实测」(本机无 summarize/last30days)
（同上结构;标发布日期 + 实操/理论倾向)

## 6. 核心洞察 + 最佳实践
跨渠道综合:N 条洞察(每条挂一两个出处) + 一份可执行的最佳实践清单。

## 7. 对内容创作的启示 — 增长轴 → 排序的内容角度
**这是两轴相乘的地方,也是 /draft 的入口。**
### 时机窗口
<这话题爆发/冷却到哪了 → 现在该不该写,趁哪个窗口>
### 排序的内容角度（3-5 个,每个 = 一个内容赌注）
#### 角度1（推荐）<标题>
- 缺口:为什么有空间(来自竞品扫描)
- 受欢迎度证据:哪些渠道在火 + 数据(实测/「推断」)
- 参考写法:别人怎么写的(引 §3-5 的形式拆解) → 我们怎么改
- 渠道 + 形式:X 长文 / 博客长文 / YouTube 脚本 …
- 依赖:本报告哪几条 claim / 哪些候选源
#### 角度2 … #### 角度3 …
### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
### 内容形式参考库
长文学谁 / 视频学谁 / X 学谁(各引一个范本 + 一句为什么)

## 附录:关键时间线
| 日期 | 事件 | （把话题的演进/引爆点排成时间线,标出爆发节点）
```

Also write:

#### `ingest-candidates.md` — sources worth ingesting

每条一行:`- [ ] <canonical-URL> — 一句理由(为什么值得进 vault)`

- **对 `raw/` 已有源去重**:扫一遍 `raw/` 的源 URL/标题;命中的候选标 `(已在库,勿重复 ingest)`
  并默认不勾。这是 §硬约束「双重入库」的操作化。
- 源纯度提醒(per memory `feedback_source_purity`):方法论/观点类话题,**强烈优先官方源**
  (作者本人 repo / 网站 / 社交账号);第三方解读标注 `(第三方,ingest 前确认)`。

#### `meta.json` — machine record (for re-run + future CLI-ification)

```json
{"slug":"<slug>","topic":"<topic>","depth":"<depth>","generated":"<YYYY-MM-DD>",
 "tools_ran":[],"tools_skipped":[],"artifacts":["research-plan.md","report.md","ingest-candidates.md"]}
```

### 6. 停 — stop here

Do **NOT**: auto-ingest candidates · write `wiki/log.md` (this is not a vault op) · push ·
publish · write any ledger. The candidate list goes back to the human; only selected items
later go through `/ingest`. The report's §7 angles go to the human; the chosen one feeds `/draft`.

### 7. Emit machine-readable envelope

Print exactly one JSON object to the terminal, **aligned to obsidian-content contract 1.0**
(`docs/obsidian-content-cli.md`). This is printed by the skill — it is NOT a verb in
`scripts/obsidian_content.py` (that CLI is LLM-free by design). Compute each `sha256` with
`shasum -a 256 <path>`.

```json
{
  "contract_version": "1.0",
  "ok": true,
  "verb": "research",
  "artifacts": {
    "plan":       { "path": "research/<slug>/research-plan.md",     "sha256": "..." },
    "report":     { "path": "research/<slug>/report.md",           "sha256": "..." },
    "candidates": { "path": "research/<slug>/ingest-candidates.md", "sha256": "..." }
  },
  "warnings": ["last30days unavailable (VPS-only)", "..."],
  "errors": []
}
```

On fatal failure: `ok:false`, reasons in `errors[]`, still print valid JSON.

### 8. Report (human-facing)

After the envelope, show in terminal:
- Topic + slug + depth + workspace path
- Which tools ran vs. skipped (and which engagement data is 「推断·未实测」)
- Duplication warning if `drafts/` already covers this topic
- Candidate count (and how many flagged "already in vault")
- The §7 top recommended angle (one line)
- Next steps: "圈选 `ingest-candidates.md` → `/ingest` 选中的源 · 挑 report §7 一个角度 → `/draft research/<slug>/` 写博客"

## Hard constraints (handoff §3 — safety invariants, preserve all)

- **不批量把调研结果塞进 vault**。只产候选清单,人圈选后才 `/ingest`。
- **输出落非 vault `research/`**,不混进 `raw/`/`wiki/`,不被 gbrain Tier-1 sync 收。
- 调研报告**本身 = Tier-4**:归档可检索,排除出 vault / 选题输入。
- 报告**引用的外部原文 = Tier-3**:圈选后才作来源。
- `/research` 自身**不写 ledger、不 push、不发布**。
- 拿不到的互动/观看数据一律标 **「推断·未实测」**,绝不像第三方调研那样编造数字。
