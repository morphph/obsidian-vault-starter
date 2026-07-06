# Research Plan: OpenAI Codex 指南

> depth: standard · generated: 2026-07-06 · ⚠️ 互动数据：X/YouTube 本机无 scanner，将标「推断·未实测」
> ⚠️ headless: 被 WF3 driver 以 headless 方式调起 —— plan checkpoint skipped（无人可应答暂停）；消歧自行按证据定并记录在下方。

## 消歧块（已按证据解决 —— headless 不暂停）

「Codex」有两个可能所指：
1. **OpenAI Codex（2021）** — 初代代码补全模型（code-davinci），驱动过早期 GitHub Copilot，2023 弃用。
2. **OpenAI Codex（2025 relaunch → 2026）** — 全新的 **agentic 编码 agent 产品**：CLI + Cloud/Web + IDE 扩展 + App 四大 surface，`/goal` 循环、hooks、skills、subagents、cloud environments 一整套；是 Claude Code 的直接对位竞品。

**判定 = 义项 2（现代 agentic Codex）。证据：**
- 话题带「指南/guide」→ 指向可上手的活跃工具，而非弃用的旧模型。
- vault 已有 13 个 raw/ 源 + 10 个 wiki 页**全部**是 2026 年 agentic Codex（cookbook trilogy、hooks GA 5/14、skills、subagents、cloud、`/goal`），无一涉及 2021 旧模型。
- audience = 全背景 AI builder，关心「怎么把能力用进工作流」→ 只有活跃产品才有「指南」价值。
- **本报告全程指义项 2。** 若出现旧模型内容，仅作历史脉络一句带过。

## 渠道① Web / 官方站 ← 现在最硬的实测源（standard 主力）
- 查询：
  - `OpenAI Codex getting started` site:developers.openai.com
  - `Codex CLI` site:developers.openai.com · `codex config.toml AGENTS.md`
  - `"Codex" quickstart guide 2026` · `OpenAI Codex CLI install npm`
  - `Codex cloud environments` · `Codex IDE extension VS Code`
  - `OpenAI Codex vs Claude Code 2026` · `Codex GPT-5.5 codex model`
  - `Codex /goal command tutorial` · `AGENTS.md spec codex`
- 点名直查：developers.openai.com/codex · openai.com/index (Codex 发布/loop 帖) · developers.openai.com/cookbook (Codex 系列) · chatgpt.com/codex · Latent Space / swyx · Simon Willison (simonwillison.net，常评 Codex CLI) · agentskills.io
- 搜法：官方文档 / 原始出处优先（喂事实核验最准）；分辨 official docs vs cookbook vs 第三方教程。

## 渠道② X / Twitter
- 查询：
  - `"Codex" CLI min_faves:50 site:x.com` · `"codex /goal" site:x.com`
  - `OpenAI Codex tips site:x.com` · `Codex vs Claude Code site:x.com`
  - `AGENTS.md site:x.com` · `@ChrisHayduk codex site:x.com`
- 搜法：按收藏(bookmark)加权（收藏=想存来重读，信号比赞硬）；抓 long-article 格式；记 作者@handle + 互动 + 是否长文。
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」。

## 渠道③ YouTube
- 查询：
  - `OpenAI Codex CLI tutorial 2026` · `Codex agent walkthrough`
  - `Codex vs Claude Code youtube` · `Codex /goal demo`
- 搜法：近 90 天优先；按观看/互动；实操 > 理论。
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」。

## 综合契约（提醒 step 5）
- report.md 按双轴综合：事实轴（锚官方 developers.openai.com / openai.com）+ 增长轴（按渠道排 Top-N + 形式拆解 + 排序角度）。
- 内部存量（10 个 wiki 页）只塑造 outline + §0 锚点，**不填充正文**（plan §11.6：内部撑厚度=自我重复）。
- 溯源标注：每论断标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游 writer 只穿透引用原始出处，不引本报告。
- 候选源对 raw/ 去重；拿不到的互动数据标「推断·未实测」，绝不瞎编。
