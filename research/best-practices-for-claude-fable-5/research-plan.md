# Research Plan: Best Practices for Claude Fable 5
> depth: standard · generated: 2026-07-08
> ⚠️ 互动数据：X/YouTube 本机无 scanner（`bird`/`summarize`/`last30days` = VPS-only，本机缺失），将标「推断·未实测」
> ⚠️ headless: plan checkpoint skipped（被 WF3 driver 以 headless 方式调起，无人应答暂停 → 不暂停，消歧自决并记录）

## 消歧块（已自决 — headless，记录如下）
- **"Claude Fable 5" = Anthropic Claude 5 家族的一个模型，model ID `claude-fable-5`**。
  - 证据①（环境锚点）：本机 environment context 明列 —— "The most recent Claude models are the
    Claude 5 family, Opus 4.8, and Haiku 4.5. Model IDs — Fable 5: 'claude-fable-5' …"。
  - 证据②（内部存量）：`raw/2026-07-08-fable-finding-your-unknowns.md` —— Thariq（@trq212，
    Claude Code @ Anthropic）以 Fable 5 为日常 driver 写的实操长文（Jul 4, 2026 发布，3.35M views）。
  - 排除项：非 Microsoft 游戏《Fable》、非其他同名产品 —— 本 vault 是 AI builder KB，且 prompt
    明确写 "Claude Fable 5"。
- 消歧结论：按「Anthropic 新一代模型 Fable 5」执行扫描；关注其相对前代（Opus 4.7/4.8、Sonnet/
  Haiku）的行为差异与**用它做 agentic coding 的最佳实践**。

## 渠道① Web / 官方站   ← 现在最硬的实测源
- 查询：
  - `Claude Fable 5 best practices` · `claude-fable-5 prompting guide`
  - `Claude Fable 5 site:anthropic.com` · `Fable 5 model card docs.anthropic.com`
  - `Claude 5 family Fable release` · `Fable 5 vs Opus 4.8 when to use`
  - `Claude Fable 5 agentic coding` · `Fable 5 effort level task budget`
  - `Claude Fable 5 pricing context window` · `Fable 5 what's new API`
- 点名直查：anthropic.com（announcement + engineering blog）· docs.anthropic.com（model card /
  API "what's new" / prompting guide）· latent.space · simonwillison.net · every.to
- 搜法：官方文档 / 原始出处优先（这一渠道喂事实核验最准）；先钉死「Fable 5 是什么、何时该用、
  相对前代变了什么」的官方事实，再收社区最佳实践。

## 渠道② X / Twitter
- 查询：
  - `"Fable 5" min_faves:50 site:x.com` · `"Claude Fable" best practices site:x.com`
  - `"claude-fable-5" site:x.com` · `Fable 5 prompting tips site:x.com`
  - 点名 @trq212（Thariq，已有长文）· @anthropicai · Anthropic 研究员/Claude Code team handles
- 搜法：按收藏(bookmark)加权（收藏=想存来重读，信号比赞硬）；抓 long-article 格式；记
  作者@handle + 互动 + 是否长文
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」；Thariq 那篇的实测数已在 raw/ 里（3.35M views·
  20,168 bookmarks），可直接引用

## 渠道③ YouTube
- 查询：`Claude Fable 5 tutorial` · `Fable 5 Claude Code walkthrough 2026` · `Claude 5 Fable review`
- 搜法：近 60 天优先；实操 > 理论
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」；Fable 极新，YouTube 覆盖可能稀薄

## 综合契约（提醒 step 5）
- report.md 按双轴综合：事实轴（锚 anthropic.com/docs 官方源）+ 增长轴（按渠道排 Top-N + 形式
  拆解 + 排序角度）
- 候选源对 `raw/` 去重：`raw/2026-07-08-fable-finding-your-unknowns.md`（Thariq 那篇）**已在库**，
  命中即标「已在库，勿重复 ingest」
- 拿不到的互动/观看数据标「推断·未实测」，绝不瞎编
- 源纯度：方法论/模型行为类话题**强烈优先官方源**（anthropic.com/docs.anthropic.com/官方博客）+
  Anthropic 员工一手帖；第三方解读标 `(第三方,ingest 前确认)`
