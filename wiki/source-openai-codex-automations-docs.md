---
type: source-summary
created: 2026-05-20
last-updated: 2026-05-20
sources:
  - raw/2026-05-14-openai-codex-automations-docs.md
tags: [wiki, source, openai, codex, automations, official-docs, scheduling, triggers, afk]
---

# Source: OpenAI Codex Automations (Official Docs)

## Summary
Codex Automations let you schedule recurring background tasks across three modalities: **thread automations** (heartbeat attached to current conversation), **standalone automations** (fresh runs reported to Triage), **project-scoped automations** (local app + worktree isolation). Custom cron syntax + skill invocation via `$skill-name` + `approval_policy = "never"` unattended mode. **Functional parity with Claude Code routines + scheduled tasks combined**, with a slight philosophical difference (Codex unifies under "Automations" with sub-types; Anthropic splits `/loop` vs cloud routines).

## Source Metadata
- **URL:** https://developers.openai.com/codex/app/automations
- **Publisher:** OpenAI Developers (official docs)
- **Fetch date:** 2026-05-20

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
- **作者**：OpenAI Developers Docs
- **来源**：codex/app/automations — 与 mobile / hooks / cloud 并列的 "app feature" 一等页面
- **在 OpenAI 输出中的位置**：是 Codex 从 "CLI tool" 升级为 "always-on app platform" 的关键 surface

### 2. 核心论点（Thesis）
OpenAI 主张：AFK 不是"按一下 `/goal` 就走"——**是"建一套定期 fire 的 automation"**。**因为** 一次性触发只解决一次任务，长期 ROI 在重复调度；**所以** Codex 提供三层自动化（heartbeat / standalone / project-scoped）覆盖所有"recurring background task"用例。

简化压缩包：**"Automation 把 AFK 从『单次』升级到『 cron 化的 routine』。"**

### 3. 论证结构
```
1. 三种自动化类型对应三种 use case
   - thread (持续监控同一对话) - heartbeat
   - standalone (独立扫描多项目) - fresh
   - project-scoped (本地 worktree 隔离)
2. cron syntax 支持任意调度
3. approval_policy = "never" 让 unattended 真正自动
4. skill 集成让 automation 不只是 prompt
```

### 4. 关键概念字典

> **Thread Automation（线程心跳）**
> - **是什么**：把 wake-up call attach 到当前对话；按分钟/天/周节奏唤醒，**保留对话上下文**
> - **为什么重要**：让"等一个长跑命令完成"、"轮询 Slack/GitHub"、"复用同一 thread 的 review loop" 变成 trivial
> - **直觉类比**：像 cron 唤醒一个 background 进程让它检查状态
> - **适用场景**：长跑构建监控、Slack/GitHub 轮询、ongoing research、需要积累上下文的 triage

> **Standalone Automation（独立调度）**
> - **是什么**：每次 fire 都是 fresh run，没有对话历史；结果进入 **Triage inbox**
> - **为什么重要**：跨项目扫描、findings 作为独立 run 入库、合规审计场景
> - **适用场景**：每日依赖安全扫描、跨多个 repo 的代码质量巡检
> - **反面**：误用于需要上下文积累的任务 → 每次冷启动，效率差

> **Project-scoped Automation（项目隔离）**
> - **是什么**：必须 app 运行 + 项目 on disk；可选 local 跑或 worktree 隔离跑
> - **为什么重要**：让自动化"改你的工作仓库"安全 —— worktree 隔离防止动 active work
> - **适用场景**：本地仓库的定期 refactor / lint / test 自动修复
> - **反面**：app 没开 / 笔记本关了就不跑（vs cloud-based standalone 持续跑）

> **`approval_policy = "never"` Mode**
> - **是什么**：跑 automation 时不弹审批，全自动决策
> - **为什么重要**：**让 hooks 成为唯一 safety net** —— 没有 hook 守门，automation 可以做任何沙盒允许的事
> - **关键警示**：unattended + never approval = 必须用 hooks 锁住边界

### 5. 框架与心智模型

**何时选哪种 automation**：

```
需要保留上下文 + 间隔 ≤ daily   →  Thread
需要独立 fresh run + 跨项目     →  Standalone
需要修改本地 repo + 周期固定     →  Project-scoped
间隔 ≥ daily + 完全无人值守     →  Standalone (cloud-based)
```

**4-axis 决策**：
1. **上下文积累 vs 重置**：积累 → Thread；重置 → Standalone
2. **本地 vs 云**：必须改 local repo → Project-scoped；其他 → Standalone (cloud)
3. **触发频率**：minute/hour → Thread；day/week → 任意
4. **结果 sink**：保留在对话 → Thread；进 Triage inbox → Standalone

### 6. 关键数据与例证

- **三种类型** automation
- **三种** sandbox 模式（read-only / workspace-write / danger-full-access）
- **cron syntax** 支持任意 cadence
- **`approval_policy = "never"`** 是 unattended 默认

### 7. 关键引语

> **"For project-scoped automations, the app needs to be running, and the selected project needs to be available on disk."**
> 项目级自动化需要 app 在跑且项目在磁盘上 —— 这是本地 vs 云的关键 trade-off。

> **"Schedule recurring Codex tasks."**
> 一句话定义。

> **"Automations use `approval_policy = "never"` when organizational policy permits."**
> 无人审批模式 —— hooks 是唯一守门。

### 8. 实操指南

**典型 standalone automation setup**：
1. Codex app → Automations → Create
2. 选 standalone
3. 写 prompt（或引用 `$skill-name`）
4. 选 schedule（daily/weekly 或 cron）
5. 选 sandbox（workspace-write 默认 OK；danger-full-access 慎用）
6. 确认 `.codex/hooks.json` 已 commit 到 repo（unattended 模式 hooks 是唯一安全网）

**典型 thread automation use case**：
- 长跑 build 监控："每 5 分钟 check `npm run build` 是否完成，完成后跑 lint 并报告"
- Slack 轮询："每 30 分钟 read 我 Slack 里 starred 消息，summarize 后存进 triage"

### 9. 对比与反对意见

**vs Claude Code routines + `/loop`**：

| Dimension | Codex Automations | Claude Code |
|---|---|---|
| Heartbeat in-session | Thread automation | `/loop` skill |
| Cloud unattended | Standalone (cloud-based) | Cloud routines |
| Local + worktree | Project-scoped | `claude --bg` |
| Cron | Custom cron syntax | Cron via web UI / `/schedule` skill |
| Skill invocation | `$skill-name` | Plugin skills |
| Output | Triage inbox + threads | Run history at claude.ai/code + PRs |

**结论**：完全 functional parity；Codex 把三层统一为 "Automations" 概念家族，Anthropic 分开命名。

### 10. 与 wiki 知识的连接

**强连接**：
- [[source-claude-code-routines-docs]] —— 跨厂商对应
- [[source-claude-code-scheduled-tasks-docs]] —— in-session 调度对应
- [[source-openai-codex-hooks-docs]] —— **hook + automation 是配套：automation 跑，hook 守门**
- [[source-openai-codex-cloud-environments-docs]] —— standalone (cloud) 跑在 cloud env 里

**挑战旧观点**：
- 之前文章里"OpenAI Codex 的等价物大多是 `claude -p` 自己拼"——错。**Codex Automations 是一等公民产品，5/14 之后已 GA**

### 11. 对用户（vfan）的启示

#### 短期
- 写 methodology 文章 Part 3 Layer 2 时，**必须把 Codex Automations 加进对照表**

#### 中期
- 自己 vault 里的 `/lint` `/ingest` 等命令未来可考虑 standalone automation 化（每天早上自动 lint wiki）

#### 长期
- "跨厂商 automation 对照"是中文 SEO 真空，可写

### 12. 一句话总结

**"Codex Automations = thread heartbeat + cloud standalone + local project-scoped 三合一；2026-05 与 Anthropic routines 等价。"**

---

## Connections
- Related: [[source-claude-code-routines-docs]], [[source-claude-code-scheduled-tasks-docs]], [[source-openai-codex-hooks-docs]], [[source-openai-codex-cloud-environments-docs]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-20 | raw/2026-05-14-openai-codex-automations-docs.md | Initial creation — Codex Automations as cross-vendor parity for Anthropic routines |
