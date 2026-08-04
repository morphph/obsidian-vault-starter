---
name: research
description: "Use this skill whenever the user wants to research a topic before writing — gather what's known internally + externally, and produce a single research report (facts + per-channel popularity + content angles) + a list of sources worth ingesting. Triggers: 'research X', '调研一下 X', 'help me research before I write about Y', 'what's out there on Z', 'gather sources on W', 'I want to write about X, research it first'. Produces research-plan.md + report.md (Gate-1 闸面：末尾强制 2-4 个建议角度供作者选择) + ingest-candidates.md in a non-vault workspace (research/<slug>/); outline.md 在作者选定角度后经 outline 细化模式单角度产出 (`/research outline <slug> angle:<N>`). **Two output modes** via `mode:`：`report`（默认，选题决策文档，走 Gate-1 角度闸）或 `guide`（常青读者指南——话题含 指南/教程/上手/进阶/guide/handbook/tutorial 时自动建议，产出 facts.md 核验台账 + `<slug>-guide.md` 或成对 overview+advanced 指南，指南本身即交付物、不走角度闸）。 **Don't use when** the user wants to add a known source to the wiki — use `/ingest`. **Don't use when** the user just wants an answer from the existing wiki — use `/query`. **Don't use when** they're ready to write from existing material — use `/draft`."
---

# Research — Investigate a Topic → Report + Ingest Candidates

Read CLAUDE.md first for wiki conventions. This skill produces research artifacts in a
**non-vault** workspace; it never writes to `raw/` or `wiki/`, never auto-ingests,
never pushes or publishes. It only produces candidates for a human to select.

## Bundled references — read on demand

- `references/report-template.md` — step 5 `mode:report` 的 report.md 完整模板（双轴综合 §1-7 + appendix）。**写 report 前必读**。
- `references/guide-template.md` — step 5 `mode:guide` 的常青读者指南骨架 + 写法纪律（头部契约 → 心智模型 → 映射/边界 → 主题节处方 → 端到端工作流 → 分阶段计划 → 可复制模板 → 检查清单 → 官方索引 + 硬性配额）。**写 guide 前必读**。
- `references/outline-template.md` — step 5 的 outline.md 模板（Gate-1 artifact，含 prior_coverage 强制字段）。**写 outline 前必读**。

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
- **Optional `mode:`** — `report | guide` (default `report`). Decides the **step-5 deliverable
  shape**, not the collection method (steps 1-4 are identical either way):
  - `report` (默认) — 现行为：选题决策文档（事实轴 + 渠道 Top-N + 末尾 Gate-1 建议角度），喂选题闸。
  - `guide` — 常青**读者指南**（headings-as-journey：头部契约 → 心智模型 → 能力映射/职责边界 →
    主题节处方 → 端到端工作流 → 分阶段上手计划 → 可复制模板 → 检查清单 → 官方索引）。指南本身即
    交付物，**不产渠道 Top-N、不产【建议角度】节**（Gate-1 角度闸不适用）。
  - **自动建议规则**：话题含 `指南/教程/上手/进阶/guide/handbook/tutorial`（大小写不敏感）时建议
    `guide` 模式。**交互式**跑：问一句确认（"这看起来像要写读者指南，用 `mode:guide` 产出常青指南、
    而不是选题决策报告？"）。**Headless**（被 driver / 非交互调起）：自选 `guide`，并把
    `"mode auto-selected: guide (topic matched guide keyword)"` 记入 `warnings[]`，不暂停。
    显式传 `mode:` 时以显式值为准，跳过建议。
- **Optional `pair:`**（仅 `mode:guide`）— `true | false`（默认按题量自判）。`true` 或题材大到
  「概览 + 进阶」两层时，成对产出 `<slug>-overview.md` + `<slug>-advanced.md`（互相引用）；否则单篇
  `<slug>-guide.md`。

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

Output of this step — **exactly three lists, hard cap ONE page total**（plan §11.6：内部存量只
塑造 outline、不填充正文；用内部存量撑厚度恰恰是自我重复的开始）:
1. **已表达角度清单**（≤3 条）— drafts/ 或已发布内容里已经写过的角度，各附链接/路径。
2. **内部锚点清单**（top 5–8 个 Tier-1 页）— 作者亲手圈过、可直接引用免重复核验。
3. **旧判断回收** — 作者过去对这个话题下过的判断/立场（wiki 页或旧稿里的），供 Gate 1
   写新 take 时参照或推翻。
These feed the search plan (so it doesn't re-surface what we already have), `report.md`
§"Vault 已有锚点", and `outline.md` 的 `prior_coverage` 字段（见 step 5）.

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
  eyeball the queries / fix a misread intent — a wrong plan wastes the whole scan.
- `quick`: proceed without pausing.
- If the plan contains a **消歧块** (unknown entity): **always pause to confirm** which entity
  is meant, regardless of depth — a wrong disambiguation wastes the whole scan.
- **Headless rule（被 headless claude / driver 调起时）**: there is no one to answer a pause —
  do NOT pause at any depth; write the plan, note `"headless: plan checkpoint skipped"` in
  `warnings[]`, resolve 消歧 by best evidence and RECORD the choice in the plan, then proceed.
  (Headless invocation is detectable: non-interactive run, or the caller says so in the prompt.)

### 4. 扫外 — execute the plan per-channel (best-effort, isolate the noise)

Raw scraped material is heavy context pollution. **Spawn ONE sub-agent (Agent tool, type
`general-purpose`)** to run the external fan-out and return ONLY synthesized findings — do not
let raw fetches flood the main session. Give the sub-agent `research-plan.md`, the vault anchors
from step 2, and the depth budget. It runs the two phases below **in strict order — 4a
deep-research first, then 4b per-channel scanners** — and never fires a channel scanner before
deep-research has returned.

#### 4a. 先跑 deep-research（强制地板，永远第一步）

**The sub-agent MUST invoke the `deep-research` skill FIRST, before any channel scanner, at
every depth — including `quick`.** It is the baseline engine: fans out web searches, fetches
sources, adversarially verifies claims, returns a cited synthesis. Give it the topic plus the
plan's 渠道① Web/官方 queries as the research question. This guarantees a floor of verified,
cited findings even if every scanner in 4b is missing.

- deep-research is a built-in skill and is **always available** — it MUST appear in `tools_ran`,
  never in `tools_skipped`. There is no depth or condition under which it is skipped.
- If it genuinely errors out (not merely returns thin results), that is a **hard failure**, not a
  degradable scanner: record it in `warnings[]` prominently, and if it produced nothing usable set
  `ok:false` with the reason in `errors[]` (step 7). Never silently proceed without it.
- Use the **`defuddle`** skill to clean any URLs (from 4a or 4b) you open for closer reading.

#### 4b. 再按渠道补扫（best-effort，增量叠加在 deep-research 之上）

Only after 4a returns, augment each channel with its native scanner — these sharpen the
engagement/recency signal deep-research alone can't measure. Each channel keeps its native search
method from the plan:

- **`last30days`** — web / Reddit / HN / YouTube trends (engagement-weighted).
- **`bird`** — X targeted search / threads / engagement counts (bookmarks).
- **`summarize`** — YouTube transcripts.

**Graceful degradation (required, 4b only).** `last30days`, `bird`, and `summarize` are **VPS-only
and absent on this machine today** — calling them locally will fail, and that is expected. Treat
each **4b** scanner as **best-effort**: if a tool is missing or errors, **record it in `warnings[]`
and continue** — never fail the run for a missing 4b scanner (this leniency does NOT extend to 4a
deep-research). When a scanner is absent, that channel still stands on the 4a deep-research harvest
(content is findable; only precise engagement numbers are not) — mark those numbers
**「推断·未实测」**, never fabricate them.

The sub-agent returns, **grouped by channel**: per-channel candidate pieces (link · author ·
date · engagement-or-「推断」· core content · **writing-style note**), plus a flat list of
candidate source URLs (canonical URL + one-line reason each), plus which tools ran vs. skipped.

### 5. 综合 — synthesize into the deliverable (anchored on audience-profile.md)

Read `audience-profile.md` (repo root) for reader persona, voice, and GEO writing rules. Now read
the channel-organized harvest through **both axes**. **What you write depends on `mode:`** — the
harvest is the same, the deliverable shape differs. Take the branch below.

#### 5A. `mode:report`（默认）— synthesize into ONE report

Write a single `research/<slug>/report.md`.

**Read `references/report-template.md` and follow its structure exactly** (§TL;DR · §0 Vault
已有锚点 · §1 事实轴 · §2 焦点实体 · §3-5 per-channel Top-N · §6 洞察+溯源纪律 · §7 排序角度 ·
附录时间线). Key disciplines baked into the template — do not drop them:
- §1 每条 claim 对官方源核验并标 ✅/⚠️/❌；矛盾用 `> [!warning]` 双留。
- §6 溯源标注纪律：每个论断标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游只许穿透引用原始出处。
- §3-5 互动数据拿不到就标「推断·未实测」，绝不编造。

**报告末【建议角度】节 = 强制契约（角度闸，2026-07-10 作者批准的机制）**：2–4 个角度，每个必含
六件：① 标题候选 ② 一句 thesis ③ 为什么是我们/为什么现在 ④ 与 step 2「已表达角度清单」的
prior_coverage 关系 ⑤ 3–5 行骨架 ⑥ 渠道建议。可标一个「推荐」。这一节就是 Gate-1 的闸面——
作者读完报告直接做选择题。

**调研阶段不再写 outline.md**（省去为没选中角度白做的功）。outline 由作者在角度闸选定后经
下方「Outline 细化模式」单角度产出。

#### 5B. `mode:guide` — synthesize into 核验台账 + 常青读者指南

指南**本身就是交付物**，所以这个分支**不写 report.md、不产渠道 Top-N、不产【建议角度】节**
（Gate-1 角度闸不适用——没有"选哪个角度写"的问题，指南就是要写的东西）。改写两类文件：

1. **`facts.md` — 核验事实台账**。把 §1 的核验纪律全部搬到这里：逐条 ✅/⚠️/❌、确切配置值/
   默认值、GA/弃用状态、第三方谣言辨伪、`推断·未实测` 标注、矛盾双留。**所有研究元话术只住这里**
   （核验状态、GA 标注纪律、存疑辨伪、"推断未实测"），**绝不进指南正文**。指南正文只从这份台账里
   取"已核验的结论"，并把最要命的 gotcha 以 `> [!tip]` / `> [!warning]` callout 精华形式带进对应节。

2. **指南正文**：单篇 `research/<slug>/<slug>-guide.md`，或 `pair:true`／题量大时成对
   `<slug>-overview.md` + `<slug>-advanced.md`（概览篇 + 进阶篇，互相引用、不重复）。
   **写指南前必读 `references/guide-template.md`** 并按其骨架 + 硬性配额落地——它是这个分支的核心资产：
   头部契约 → 心智模型（+需求→入口决策表）→ 从已知工具的能力映射 + 职责边界清单 → 主题节（每节
   处方收尾 + "不要混淆"辨析块）→ 端到端工作流 → 分阶段上手计划 → 可复制模板 → 检查清单 → 官方索引，
   文末 `## 更新记录` 表。写完按模板的**硬性配额自查**（≥3 决策表 / ≥2 可复制模板 / 1 分阶段计划 /
   1 检查清单 / 官方索引；进阶题材加架构图），不达标就补到达标。

#### 5C. 两模式都写：`ingest-candidates.md` — sources worth ingesting

每条一行:`- [ ] <canonical-URL> — 一句理由(为什么值得进 vault)`

- **对 `raw/` 已有源去重**:扫一遍 `raw/` 的源 URL/标题;命中的候选标 `(已在库,勿重复 ingest)`
  并默认不勾。这是 §硬约束「双重入库」的操作化。
- 源纯度提醒(per memory `feedback_source_purity`):方法论/观点类话题,**强烈优先官方源**
  (作者本人 repo / 网站 / 社交账号);第三方解读标注 `(第三方,ingest 前确认)`。

#### `meta.json` — machine record (for re-run + future CLI-ification)

`artifacts` 随模式变：`mode:report` 列 `report.md`；`mode:guide` 列 `facts.md` + 指南文件
（单篇 `<slug>-guide.md`，或成对 `<slug>-overview.md` + `<slug>-advanced.md`）。

```json
// mode:report
{"slug":"<slug>","topic":"<topic>","mode":"report","depth":"<depth>","generated":"<YYYY-MM-DD>",
 "tools_ran":[],"tools_skipped":[],"artifacts":["research-plan.md","report.md","ingest-candidates.md"]}
// mode:guide（单篇）
{"slug":"<slug>","topic":"<topic>","mode":"guide","depth":"<depth>","generated":"<YYYY-MM-DD>",
 "tools_ran":[],"tools_skipped":[],"artifacts":["research-plan.md","facts.md","<slug>-guide.md","ingest-candidates.md"]}
```

### 6. 停 — stop here

Do **NOT**: auto-ingest candidates · write `wiki/log.md` (this is not a vault op) · push ·
publish · write any ledger. The candidate list goes back to the human; only selected items
later go through `/ingest`. In `mode:report` the report's §7 angles go to the human; the chosen
one feeds `/draft`. In `mode:guide` the guide itself is the deliverable — it goes to the human
to read/publish (发布走 `/draft <slug>-guide.md`)，没有角度闸这一步。

### 7. Emit machine-readable envelope

Print exactly one JSON object to the terminal, **aligned to obsidian-content contract 1.0**
(`docs/obsidian-content-cli.md`). This is printed by the skill — it is NOT a verb in
`scripts/obsidian_content.py` (that CLI is LLM-free by design). Compute each `sha256` with
`shasum -a 256 <path>`.

`mode:report` — `artifacts` 有 `plan` / `report` / `candidates`：

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

`mode:guide` — `report` 键换成 `facts` + `guide`（单篇）或 `guides`（成对数组）：

```json
{
  "contract_version": "1.0",
  "ok": true,
  "verb": "research",
  "artifacts": {
    "plan":       { "path": "research/<slug>/research-plan.md",     "sha256": "..." },
    "facts":      { "path": "research/<slug>/facts.md",             "sha256": "..." },
    "guide":      { "path": "research/<slug>/<slug>-guide.md",      "sha256": "..." },
    "candidates": { "path": "research/<slug>/ingest-candidates.md", "sha256": "..." }
  },
  "warnings": ["mode auto-selected: guide (topic matched guide keyword)", "..."],
  "errors": []
}
```
（成对时把 `"guide"` 换成 `"guides": [ {…overview…}, {…advanced…} ]`。）

On fatal failure: `ok:false`, reasons in `errors[]`, still print valid JSON.

### 8. Report (human-facing)

After the envelope, show in terminal:
- Topic + slug + **mode** + depth + workspace path
- Which tools ran vs. skipped (and which engagement data is 「推断·未实测」)
- Duplication warning if `drafts/` already covers this topic
- Candidate count (and how many flagged "already in vault")
- **`mode:report`**：The §7 top recommended angle (one line)。Next steps: "圈选
  `ingest-candidates.md` → `/ingest` 选中的源 · 读 report 末【建议角度】选一个（WF3 任务：
  `wf3.py choose-angle --task <id> --angle N [--note …]` → resume）→ outline 细化 → `/draft`"
- **`mode:guide`**：指南文件名 + 硬性配额自查结果（几张决策表 / 几个可复制模板 / 有无分阶段计划 +
  检查清单 + 官方索引；进阶篇有无架构图）+ 篇幅 KB。Next steps: "读指南 · 要发布走
  `/draft research/<slug>/<slug>-guide.md` · 核验细节见 `facts.md`"

## Outline 细化模式 — `/research outline <slug> angle:<N>`（角度闸选定后）

由 WF3 driver 在作者 `choose-angle` 之后 headless 调起（也可作者手动调）。**不重新调研**：

1. 读 `research/<slug>/report.md`（含建议角度节）与 `research-plan.md`；prompt 里会带作者的
   修正意见（若有）。
2. **Read `references/outline-template.md` and follow it**，只为选中角度写
   `research/<slug>/outline.md`：`prior_coverage` 仍是机器可检的强制字段；
   **take 段直接由选中角度的 thesis + 作者修正合成**——作者的选择即 take，绝不留
   `⏳ 待作者 take` 占位。
3. 只写 outline.md 这一个文件；结尾打 envelope（verb: "research-outline"，artifacts 只含 outline）。
4. Headless 铁律同上：不暂停、不问、消歧自决记录在 outline 文末注记。

## Hard constraints (handoff §3 — safety invariants, preserve all)

- **不批量把调研结果塞进 vault**。只产候选清单,人圈选后才 `/ingest`。
- **输出落非 vault `research/`**,不混进 `raw/`/`wiki/`,不被 gbrain Tier-1 sync 收。
- 调研报告**本身 = Tier-4**:归档可检索,排除出 vault / 选题输入。
- 报告**引用的外部原文 = Tier-3**:圈选后才作来源。
- `/research` 自身**不写 ledger、不 push、不发布**。
- 拿不到的互动/观看数据一律标 **「推断·未实测」**,绝不像第三方调研那样编造数字。
- **外扫必须以 deep-research 打底**：step 4 的子 agent 每次、每个 depth 都先跑 `deep-research`(4a),
  再叠加渠道 scanner(4b)。deep-research 只许出现在 `tools_ran`,绝不 skip;它硬失败按 `ok:false` 处理。
- **`mode:guide` 元话术隔离**：研究元话术（核验状态 ✅/⚠️/❌、GA 标注纪律、存疑辨伪、
  「推断·未实测」）**只住 `facts.md`,绝不进指南正文**。指南正文只写已核验的结论;拿不准的事实要么
  略去、要么降级成有实质内容的 `> [!warning]` callout,绝不当已核验事实写。确切默认值/版本弃用状态/
  精确 gotcha 以 `> [!tip]`/`> [!warning]` 形式织入对应节(这是我们相对第三方指南的差异化武器)。
