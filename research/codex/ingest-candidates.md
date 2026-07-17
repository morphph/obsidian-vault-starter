# Ingest Candidates — Codex 常青报告（概览 + 进阶）

> 圈选后才 `/ingest`（本 skill 不自动入库）。已对 `raw/` 去重。
> 源纯度（memory `feedback_source_purity`）：本话题几乎全官方源（learn.chatgpt.com / developers.openai.com），优先级高；唯一第三方已标注。
> ⚠️ **域名迁移注意**：raw/ 里已有的 Codex 源多是 2026-05 从旧域名 `developers.openai.com/codex/*` 抓的，现内容已变（Scheduled tasks 改名、hooks 10 事件、默认模型 gpt-5.6-sol）——**已在库者标「旧状态，可刷新」**。

## A. 新官方页（进阶面缺口，优先）—— raw/ 未收
- [ ] https://learn.chatgpt.com/docs/extend/mcp?surface=cli — **MCP 精确 `[mcp_servers]` TOML**（上手篇留的 TODO 的正解，进阶指南金块）
- [ ] https://learn.chatgpt.com/docs/config-file/config-reference — config 键/默认值权威表（进阶配置锚定）
- [ ] https://learn.chatgpt.com/docs/environments/git-worktrees — Local/Worktree/Hand off（worktree 并行事实源）
- [ ] https://learn.chatgpt.com/docs/remote-connections — Codex Remote 手机控主机 + QR（2026-06-25 GA）
- [ ] https://learn.chatgpt.com/docs/third-party/github — `@codex review/fix` 触发串 + 自动评审
- [ ] https://learn.chatgpt.com/docs/developer-commands?surface=cli — `/goal` `/plan` 等 slash 命令速查
- [ ] https://learn.chatgpt.com/docs/models — 默认 `gpt-5.6-sol` + 弃用清单（**当前状态锚，纠偏用**）
- [ ] https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6 — GPT-5.6 prompting（省 41–66% token 硬数字）
- [ ] https://developers.openai.com/cookbook/articles/codex_exec_plans — PLANS.md/ExecPlan 四小节（Aaron Friel）※注：内容可能已由 [[source-openai-cookbook-plans-md]] 覆盖，ingest 前比对
- [ ] https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex — Review/Repair/Validate（若 [[source-openai-codex-cookbook-trilogy]] 未含独立页则收）
- [ ] https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop — 改进 Loop + codex_handoff.md（真名 "Loop" 非 "Flywheel"，纠偏）
- [ ] https://agentskills.io/specification — Agent Skills 开放标准（frontmatter 约束 + 渐进披露预算）

## B. 活文档（持续更新，按需刷新而非一次性 ingest）
- [ ] https://learn.chatgpt.com/docs/changelog — 追新唯一权威（截 2026-07-16）※living page，建议 `/ingest` 时取快照并注日期

## C. 已在库（勿重复 ingest；但内容已随域名迁移/改名变化，可择机刷新）
- [ ] https://learn.chatgpt.com/docs/automations — (已在库 raw/2026-05-14-openai-codex-automations-docs.md，**旧状态**：已改名 Scheduled tasks + RRULE，值得刷新)
- [ ] https://learn.chatgpt.com/docs/hooks — (已在库 raw/2026-05-14-openai-codex-hooks-docs.md，**旧状态**：实为 10 事件，值得刷新)
- [ ] https://learn.chatgpt.com/docs/agent-configuration/subagents — (已在库 raw/2026-05-20-openai-codex-subagents-docs.md，07-17 仍在更新，可刷新)
- [ ] https://learn.chatgpt.com/docs/environments/cloud-environment — (已在库 raw/2026-05-20-openai-codex-cloud-environments-docs.md)
- [ ] https://learn.chatgpt.com/docs/build-skills — (已在库 raw/2026-05-20-openai-codex-skills-docs.md)
- [ ] https://developers.openai.com/blog/run-long-horizon-tasks-with-codex — (已在库 raw/2026-05-05-openai-blog-long-horizon-tasks-codex.md；注：本轮考据作者=Derrick Choi 2026-02-23、**四文件**非三文件，比对是否需刷新)
- [ ] https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex — (已在库 raw/2026-05-09-openai-cookbook-using-goals-in-codex.md)

## D. 第三方（结构参照，ingest 前确认；本话题优先官方，默认不收）
- [ ] https://codex.danielvaughan.com/2026/06/11/loop-engineering-codex-cli-autonomous-agent-loops-automations-subagents-goal-mode/ — (第三方,ingest 前确认) 无人值守循环最完整第三方叙事；⚠️ 其 `[goals]` TOML 官方无法证实，勿作事实源
