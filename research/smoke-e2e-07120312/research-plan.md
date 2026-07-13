# Research Plan: AI 结对编程时代的 code review 该长什么样
> depth: quick · ⚠️ 互动数据：X/YouTube 本机无 scanner，将标「推断·未实测」
> ⚠️ headless: plan checkpoint skipped（WF3 driver 调起，无人应答，按 Headless rule 不暂停）

## 焦点 / 消歧
话题为概念性命题（「AI 结对/agent 写代码后，人类 review 该变成什么」），**不含未知实体**，无需消歧块。
消歧自决记录：无歧义实体，直接进扫外。

## 渠道① Web / 官方站   ← quick 深度下最硬的实测源
- 查询：
  - "AI code review" 2026 best practices
  - "reviewing AI-generated code" engineering blog
  - Anthropic / OpenAI code review agent-generated code guidance
  - "code review" agent coding site:anthropic.com OR site:openai.com
  - Simon Willison / Thoughtworks / Google engineering "AI code review"
  - "PR review" LLM agent workflow 2026
  - "trust but verify" AI generated code review
  - GitHub Copilot / Cursor / Claude Code code review feature docs
- 点名直查：anthropic.com（Claude Code review、`/code-review`）· openai.com（Codex review）·
  github.blog（Copilot code review）· martinfowler.com / thoughtworks · latent.space · pragmaticengineer.com
- 搜法：官方文档 / 原始出处优先；实操流程 > 空泛评论。

## 渠道② X / Twitter
- 查询：
  - "AI code review" min_faves:50 site:x.com
  - "reviewing AI code" site:x.com
  - "code review is the bottleneck" agent site:x.com
  - Boris Cherny / @thariq / Garry Tan code review site:x.com
- 搜法：按收藏(bookmark)加权（收藏=想存来重读，信号比赞硬）；抓 long-article 格式；
  记 作者@handle + 互动 + 是否长文。
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」。

## 渠道③ YouTube
- 查询：
  - "reviewing AI generated code" 2026
  - "code review AI agents" workflow
  - Claude Code / Cursor code review demo 2026
- 搜法：近 90 天优先；实操 demo > 理论；标发布日期。
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」。

## 内部锚点（查内已确认，供综合时免重复核验）
- [[verification-loops]] · [[cross-modal-review]] · [[self-evaluation-bias]] · [[iterative-repair-loop]]
  · [[quality-gate-loop]] · [[software-entropy]] · [[hitl-vs-afk-classification]] · [[agent-improvement-flywheel]]
- drafts/ 无 code-review 成稿；raw/ 无直接 code-review 源 → 本话题对 vault 是**新地** → 外部为主。

## 综合契约（提醒 step 5）
- report.md 按双轴综合：事实轴（锚官方源）+ 增长轴（按渠道排 Top-N + 形式拆解 + 角度）。
- 报告末【建议角度】节 = 强制契约（角度闸，2–4 个 × 六件套）。**调研阶段不写 outline.md**。
- 候选源对 raw/ 去重；拿不到的互动数据标「推断·未实测」，绝不瞎编。
