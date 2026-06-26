---
name: research
description: "Use this skill whenever the user wants to research a topic before writing — gather what's known internally + externally, and produce a research report + article outline + a list of sources worth ingesting. Triggers: 'research X', '调研一下 X', 'help me research before I write about Y', 'what's out there on Z', 'gather sources on W', 'I want to write about X, research it first'. Produces report.md + outline.md + ingest-candidates.md in a non-vault workspace (research/<slug>/). **Don't use when** the user wants to add a known source to the wiki — use `/ingest`. **Don't use when** the user just wants an answer from the existing wiki — use `/query`. **Don't use when** they're ready to write from existing material — use `/draft`."
---

# Research — Investigate a Topic → Report + Outline + Ingest Candidates

Read CLAUDE.md first for wiki conventions. This skill produces research artifacts in a
**non-vault** workspace; it never writes to `raw/` or `wiki/`, never auto-ingests,
never pushes or publishes. It only produces candidates for a human to select.

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

Find what the vault already has, so the outline builds on existing Tier-1 anchors instead of
repeating them.

1. Read `wiki/index.md` — **the vault's retrieval mechanism** — to find related pages, then
   read those pages. Pull out the Tier-1 anchors (concepts/claims we already track) worth
   carrying into the outline.
2. **Check `drafts/`** for an existing article on this topic. If one exists, **report it
   prominently** ("⚠️ 你已经写过 `drafts/<file>` on this topic") so the user doesn't re-draft a
   published piece. Decide with them whether this is a new angle or a duplicate.
3. Optionally query gbrain as an **accelerator**: `mcp__gbrain__query` / `mcp__gbrain__search`
   for the topic. Treat results as a hint, not authority — **`wiki/index.md` + `drafts/` on disk
   are the source of truth** (gbrain may be stale). If gbrain disagrees with on-disk state,
   trust on-disk and note the discrepancy in `warnings`.

Output of this step: a short list of vault Tier-1 anchors + any duplication warning.

### 3. 扫外 — scan external sources (best-effort, isolate the noise)

Raw scraped material is heavy context pollution. **Spawn ONE sub-agent (Agent tool, type
`general-purpose`)** to run the external fan-out and return ONLY synthesized findings — do not
let raw fetches flood the main session. Give the sub-agent the topic, the vault anchors from
step 2 (so it doesn't re-surface what we already have), and the depth budget.

The sub-agent uses, in order of reliability:

- **`deep-research` skill — baseline engine, always available.** Run it on the topic; it
  fans out web searches, fetches sources, adversarially verifies claims, and returns a cited
  synthesis. This is the floor: even if every other tool below is missing, research still works.
- **`last30days`** — web / Reddit / HN / YouTube trends (engagement-weighted).
- **`bird`** — X targeted search / threads / engagement counts.
- **`summarize`** — YouTube transcripts.
- Use the **`defuddle`** skill to clean any fetched URLs.

**Graceful degradation (required).** `last30days`, `bird`, and `summarize` are **VPS-only and
absent on this machine today** — calling them locally will fail, and that is expected. Treat
each external scanner as **best-effort**: if a tool is missing or errors, **record it in
`warnings[]` and continue** — never fail the run for a missing scanner. The baseline
(`deep-research` + 查内) must always produce all three artifacts.

The sub-agent returns: synthesized external findings + a list of candidate source URLs (with
canonical URL + a one-line reason each) + which tools ran vs. were skipped.

### 4. 综合 — synthesize (anchored on audience-profile.md)

Read `audience-profile.md` (repo root) for the reader persona, voice, and GEO writing rules.
Produce the three artifacts below into `research/<slug>/`.

#### `report.md` — two-track research synthesis

```markdown
# Research: <topic>

> depth: <quick|standard|deep> · generated: <YYYY-MM-DD> · tools: <ran> | skipped: <skipped>

## TL;DR
<3-5 句:这个话题最关键的发现 + 我们该怎么切>

## Track A — 事实锚定（fact anchoring）
关键事实**逐条对官方文档/原始出处核验**。每条:claim + 出处链接 + 核验状态。
矛盾的用 `> [!warning]`,两个 claim 都留 + 各自出处。
- **<claim>** — source: <official URL> — ✅ verified / ⚠️ unconfirmed / ❌ contradicted

## Track B — 竞品缺口 + 制胜写法（gap & winning angle）
- **现有内容覆盖了什么**:已有文章/视频怎么讲这个话题(列代表作 + 角度)
- **缺口 / 没人讲清楚的**:读者还没被满足的问题
- **我们的制胜角度**:结合 vault 已有 Tier-1 锚点 + audience-profile,我们能给出的独特切法
- **GEO 弹药**:可引用的官方出处 + 可用的统计数字(供 outline/draft 落地)

## Vault 已有锚点（from 查内）
- [[<wiki-page>]] — 一句话:我们已经怎么讲过这个
- (若 drafts/ 已有成稿,这里显著标注)
```

#### `outline.md` — article outline

- 以 `audience-profile.md` 为品味锚:分层深度 + 角色化入口。
- **带入 step 2 的 vault Tier-1 锚点**,避免重复表达已写过的东西。
- 按 GEO 规则**显式标注**该在哪加引用、哪加统计数据(例:`<!-- GEO: 此处加官方文档引用 -->`、
  `<!-- GEO: 此处加 +37% 统计 -->`),这样 `/draft` 写稿时知道去填。
- 标出每个 section 依赖哪条 report claim / 哪个候选源(为 draft 的取源做准备)。

#### `ingest-candidates.md` — sources worth ingesting

每条一行:`- [ ] <canonical-URL> — 一句理由(为什么值得进 vault)`

- **对 `raw/` 已有源去重**:扫一遍 `raw/` 的源 URL/标题;命中的候选标 `(已在库,勿重复 ingest)`
  并默认不勾。这是 §硬约束「双重入库」的操作化。
- 源纯度提醒(per memory `feedback_source_purity`):方法论/观点类话题,**强烈优先官方源**
  (作者本人 repo / 网站 / 社交账号);第三方解读标注 `(第三方,ingest 前确认)`。

#### `meta.json` — machine record (for re-run + future CLI-ification)

```json
{"slug":"<slug>","topic":"<topic>","depth":"<depth>","generated":"<YYYY-MM-DD>",
 "tools_ran":[],"tools_skipped":[],"artifacts":["report.md","outline.md","ingest-candidates.md"]}
```

### 5. 停 — stop here

Do **NOT**: auto-ingest candidates · write `wiki/log.md` (this is not a vault op) · push ·
publish · write any ledger. The candidate list goes back to the human; only selected items
later go through `/ingest`.

### 6. Emit machine-readable envelope

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
    "report":     { "path": "research/<slug>/report.md",            "sha256": "..." },
    "outline":    { "path": "research/<slug>/outline.md",           "sha256": "..." },
    "candidates": { "path": "research/<slug>/ingest-candidates.md", "sha256": "..." }
  },
  "warnings": ["last30days unavailable (VPS-only)", "..."],
  "errors": []
}
```

On fatal failure: `ok:false`, reasons in `errors[]`, still print valid JSON.

### 7. Report (human-facing)

After the envelope, show in terminal:
- Topic + slug + depth + workspace path
- Which tools ran vs. skipped
- Duplication warning if `drafts/` already covers this topic
- Candidate count (and how many flagged "already in vault")
- Next steps: "圈选 `ingest-candidates.md` → `/ingest` 选中的源 → `/draft research/<slug>/` 写博客"

## Hard constraints (handoff §3 — safety invariants, preserve all)

- **不批量把调研结果塞进 vault**。只产候选清单,人圈选后才 `/ingest`。
- **输出落非 vault `research/`**,不混进 `raw/`/`wiki/`,不被 gbrain Tier-1 sync 收。
- 调研报告**本身 = Tier-4**:归档可检索,排除出 vault / 选题输入。
- 报告**引用的外部原文 = Tier-3**:圈选后才作来源。
- `/research` 自身**不写 ledger、不 push、不发布**。
