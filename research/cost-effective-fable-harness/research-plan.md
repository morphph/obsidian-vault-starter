# Research Plan: 低成本多模型 agent harness — Fable 5 当规划/评审 + 便宜 coder 居中

> depth: standard · ⚠️ 互动数据：X/YouTube 本机无 scanner，将标「推断·未实测」
> ⚠️ 知识截止：本机训练截止 2026-01；Fable 5（2026-06）、GPT-5.5、Lance Martin 本条帖均**超截止** → 事实轴全部依赖外部一手源，逐条挂 URL + 核验状态。
> **headless 调起**：按 Headless rule 执行——不暂停、消歧自决并记录（见文末「消歧自决记录」）。

## 话题拆解（给 scan 用的意图锚）
一个「贵脑 + 便宜手 + 贵评审」的三段式 harness：
- **规划/架构（planner/architect）= Claude Fable 5 @ xhigh effort**：吸收模糊、拆解任务、写实施计划。
- **执行/编码（coder）= 更便宜的订阅制模型（如 GPT-5.5）**：按计划批量写代码，占绝大多数 token。
- **评审（judge）= Fable 5 再上场**：fresh-context 校验产出、给通过/打回。
- **经济命题**：典型「全程贵模型」的单次往返 $50+ → 降到几美元。种子源 = Lance Martin @rlancemartin。
- **本质**：这是 [[cross-modal-review]]（跨厂商多模型评审）+ [[thin-harness-fat-skills]]（规划/执行分层）+ [[llm-judgment-vs-scripts]] 的成本工程化。

## 渠道① Web / 官方站   ← 现在最硬的实测源
- 查询：
  - `Lance Martin multi-model agent harness cost` · `rlancemartin planner coder judge`
  - `Claude Fable 5 planner GPT-5.5 coder cost` · `frontier model planner cheap model executor pattern`
  - `architect editor model aider cost` · `plan mode act mode cheap model coding agent`
  - `Claude Fable 5 pricing $10 $50 official` site:platform.claude.com / anthropic.com
  - `GPT-5.5 pricing coding subscription` site:openai.com · `GPT-5.5 API price per token`
  - `LLM as judge cross-model cost` · `multi-model orchestration cost reduction agent`
- 点名直查：**rlancemartin.com / hwchase17 orbit（LangChain）· platform.claude.com（Fable 定价/prompting guide）· openai.com（GPT-5.5 定价）· simonwillison.net（Fable/GPT 成本实测）· aider.chat docs（architect/editor 分离模型的先例）· cline / RA.Aid / roo-code（plan-act 双模型）**
- 搜法：官方文档 / 原始出处优先；定价一律锚官方页；harness 模式找有实测成本数字的一手实践帖。

## 渠道② X / Twitter
- 查询：
  - `from:rlancemartin Fable planner judge` · `"Fable 5" planner coder judge cost site:x.com`
  - `"cheap coder" expensive planner agent site:x.com` · `Fable xhigh judge GPT-5.5 site:x.com`
  - `multi-model harness cost dollars site:x.com min_faves:50`
- 搜法：按收藏(bookmark)加权；抓 long-article；记 作者@handle + 互动 + 是否长文。
- **必抓种子源**：https://x.com/rlancemartin/status/2075641284635799865 —— 取其原话/数字/harness 结构图（若为 thread 取全串）。
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」。

## 渠道③ YouTube
- 查询：`Lance Martin agent harness` · `multi-model coding agent cost` · `Claude Fable 5 GPT-5.5 workflow` · `planner executor judge coding agent tutorial 2026`
- 搜法：近 60 天优先；实操 > 理论。
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」。

## 消歧块 —— headless 自决（不暂停）
- **「Fable 5」** → `claude-fable-5`（Anthropic，2026-06-09 GA，$10/$50）。无歧义，vault 内部已核（best-practices-for-claude-fable-5 报告）。
- **「GPT-5.5」** → OpenAI 的编码向订阅模型（wiki [[cross-modal-review]] 已引它作「recall」评审档）。作者原话是 `e.g. GPT-5.5` = **举例的便宜 coder**，非硬约束 → scan 时把「便宜订阅 coder」当类别，GPT-5.5 只作代表实例，也留意 Codex / Sonnet 5 / DeepSeek 等同位替代。
- **「$50+ → 几美元」** → 是**单次复杂任务往返**的量级对比（非月费）；核验时找 Lance 原帖的具体数字，拿不到就标「推断·未实测」。

## 综合契约（提醒 step 5）
- report.md 按双轴综合：事实轴（锚官方源：Fable/GPT 定价、refusal 兜底、effort 拨盘）+ 增长轴（按渠道排 Top-N + 形式拆解 + 角度）。
- **重点 dedup**：本 vault 已有 `research/best-practices-for-claude-fable-5/`（§6#16 路由经济学=「80–90% 留便宜 Claude」）——本话题的新增量是**跨厂商三段式（Fable 脑 + 非-Anthropic 便宜手 + Fable 评审）+ 可量化省钱**，报告须显式声明与它的边界。
- 候选源对 raw/ 去重；拿不到的互动/成本数据标「推断·未实测」，绝不瞎编。
- 报告末【建议角度】节 = 强制契约（2–4 角度 × 六件），Gate-1 闸面。
