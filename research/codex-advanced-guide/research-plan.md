# Research Plan: Codex 完全使用指南（进阶续集 / advanced）

> depth: standard · generated: 2026-07-17
> 角度已定：**进阶续集**——承接已发的 `drafts/openai-codex-getting-started`（装/surface/AGENTS.md/config/模型/CC 对照），
> 本轮只扫**上手稿只是「一瞥」的进阶面**：skills · subagents · automations · cloud environments ·
> MCP 深配 · worktree 并行 · hooks 实战 · prompting · `/goal` loop 方法论落地。**假设读者已装好、会跑第一个任务。**
> ⚠️ 互动数据：X/YouTube 本机无 scanner（bird/last30days/summarize VPS-only），将标「推断·未实测」。Web/官方为实测主力。
> ⚠️ 现有 `research/openai-codex`（2026-07-06，11 天前）的模型/定价/changelog 事实需重核当前（2026-07-17）状态。

## 渠道① Web / 官方站   ← 最硬的实测源，进阶面事实全在这里
- 点名直查（官方，权威锚定）：
  - `developers.openai.com/codex/skills`（agentskills.io 标准 · $skill 调用 · progressive disclosure 8K cap）
  - `developers.openai.com/codex/subagents`（max_threads=6 · max_depth=1 · default/worker/explorer · spawn_agents_on_csv）
  - `developers.openai.com/codex/automations`（thread heartbeat · standalone/Triage · project-scoped worktree · cron · approval_policy="never"）
  - `developers.openai.com/codex/cloud` + `/cloud-environments`（chatgpt.com/codex · 12h 容器缓存 · @codex GitHub mention · setup/agent 网络分离）
  - `developers.openai.com/codex/mcp`（**精确 `[mcp]` TOML 语法**——上手稿留了 TODO，本轮必须引出一手）
  - `developers.openai.com/codex/hooks`（6 lifecycle events · exit 2 block · requirements.toml；hooks GA 2026-05-14）
  - `developers.openai.com/codex/config-reference` + `/config-advanced`（进阶旋钮穷举）
  - `developers.openai.com/codex/changelog`（2026-05~07 进阶功能投放，重核当前）
- OpenAI Cookbook（官方，方法论一手）：
  - Using Goals in Codex · Iterative Repair Loops · Agent Improvement Flywheel（cookbook 三层 loop）
  - AGENTS.md + PLANS.md 多小时长任务
- 查询：`Codex skills site:developers.openai.com` · `Codex subagents max_threads` · `Codex automations cron` ·
  `Codex MCP config.toml example` · `Codex hooks requirements.toml exit 2` · `Codex cloud environment setup script` ·
  `Codex worktree parallel` · `Codex prompting best practices GPT-5.5`（8-12 条）
- 搜法：官方文档 / 原始出处优先；第三方（freeCodeCamp handbook 进阶章节、Simon Willison、cookbook 二创）作结构范本 + 外部视角。

## 渠道② X / Twitter
- 查询：`"Codex" "AGENTS.md" min_faves:50 site:x.com` · `"Codex" subagents site:x.com` ·
  `"Codex" worktree parallel site:x.com` · `"Codex" skills site:x.com` · `@OpenAIDevs Codex` ·
  `@simonw Codex` ·（6-10 条）
- 搜法：按收藏(bookmark)加权（收藏=想存来重读，信号比赞硬）；抓 workflow long-thread；记 作者@handle + 互动 + 是否长文。
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」；handle/URL 未核前不在正文归因具体人。

## 渠道③ YouTube
- 查询：`Codex subagents tutorial 2026` · `Codex automations cron youtube` · `Codex MCP setup youtube` ·
  `OpenAI Codex advanced workflow 2026` · `Codex parallel worktree youtube`（5-8 条）
- 搜法：近 60 天优先；实操（屏幕共享 build-along）> 理论；记 频道 + 观看 + 长度。
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」，仅作 leads。

## 消歧块
- 无需消歧：Codex = OpenAI 2026 四-surface agentic 编码平台（CLI-first），已在现有 vault 锚定。
  唯一需重核的是**进阶功能的当前状态**（哪些 GA、哪些还 preview、旋钮名/默认值是否变），不是实体身份。

## 综合契约（提醒 step 5）
- report.md 按双轴综合：事实轴（锚官方源，每条标 ✅/⚠️/❌）+ 增长轴（按渠道排 Top-N + 形式拆解 + 排序角度）。
- §0 只放**进阶面**的 vault 锚点（skills/subagents/automations/cloud/hooks/goal 各源页），且声明与已发上手稿的零重复关系。
- 候选源对 `raw/` 去重（Codex 进阶源页多已在库，命中标「已在库」）。
- 拿不到的互动数据标「推断·未实测」，绝不编造。
- 报告末【建议角度】2-4 个，每个六件套（标题/thesis/为何我们为何现在/prior_coverage 关系/骨架/渠道）。
