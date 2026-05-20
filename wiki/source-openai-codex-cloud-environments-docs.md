---
type: source-summary
created: 2026-05-20
last-updated: 2026-05-20
sources:
  - raw/2026-05-20-openai-codex-cloud-environments-docs.md
tags: [wiki, source, openai, codex, cloud, cloud-environments, afk, unattended, official-docs]
---

# Source: OpenAI Codex Cloud / Web + Cloud Environments

## Summary
Codex Web (chatgpt.com/codex) is OpenAI's cloud execution surface for unattended agent runs. **Cloud Environments** provide customizable container configs with **12-hour state caching**, auto-install for common package managers, secret encryption restricted to setup phase, and toggleable network access for agent execution. Triggered via @codex GitHub mention / IDE delegation / direct web / automation cron. **Functional parity with Anthropic Cloud Routines**, with explicit container caching as differentiator.

## Source Metadata
- **URLs:** https://developers.openai.com/codex/cloud + /codex/cloud/environments
- **Publisher:** OpenAI Developers (official docs)
- **Fetch date:** 2026-05-20
- **Access requirement:** Plus / Pro / Business / Edu / Enterprise plan

---

## 要点解读（12-Section Compressed Study Guide）

### 1. 元信息
官方 docs，Codex 的 cloud surface 主入口。**与 Codex CLI、Codex App、Codex IDE 并列的 4 大产品 surface 之一**。

### 2. 核心论点
让 agent 在 OpenAI cloud container 里 unattended 跑、修改代码、开 PR；laptop 关了照样工作。

### 3. 论证结构
```
1. GitHub 集成 → @codex 触发
2. 容器化 + 12h 缓存 → 快速 follow-up
3. 网络访问分阶段（setup ON / agent 默认 OFF）
4. PR 输出 → 异步审计
```

### 4. 关键概念字典

> **Container caching（12 小时缓存）**
> - **是什么**：跑过一次的容器状态保留 12 小时；follow-up 任务复用，无需重 setup
> - **为什么重要**：让 "改完后再追问一下" 不用等 setup 3 分钟
> - **直觉类比**：Docker layer cache
> - **企业 perk**：Business/Enterprise tier 可跨团队成员共享

> **分阶段网络（network gating）**
> - **是什么**：setup 脚本可以装包（network ON）；agent 跑时默认 network OFF（防 exfil）
> - **为什么重要**：解决 "want to install but don't want agent to call out" 的张力
> - **适用场景**：所有 cloud unattended 任务的默认

> **@codex GitHub trigger**
> - **是什么**：在 issue/PR 里 @codex 自动派 cloud task
> - **直觉类比**：像 @claude 的 GitHub bot

### 5. 框架与心智模型

**Codex Cloud vs Anthropic Cloud Routines 决策矩阵**：

| 你的需求 | 选哪个 |
|---|---|
| 团队已 ChatGPT Enterprise | Codex Cloud |
| 团队已 Claude Enterprise | Anthropic Cloud Routines |
| 需要 GitHub @mention 自动触发 | Codex Cloud (`@codex`) |
| 需要 HTTP POST trigger | Anthropic Routines |
| 需要 12h state caching 明确语义 | Codex Cloud |
| 需要 Telegram/Discord push 通知 | Anthropic（channels） |

### 6. 关键数据
- **12 小时** container state cache
- **3** sandbox modes（read-only / workspace-write / danger-full-access）
- **5** 种 package manager 自动支持（npm / yarn / pnpm / pip / pipenv / poetry）

### 7. 关键引语
> "Codex caches container state for up to 12 hours to speed up new tasks and follow-ups."

> "Codex can work on tasks in the background (including in parallel)."

### 8. 实操指南

**Setup minimal**：
1. Plus+ plan → chatgpt.com/codex
2. Connect GitHub
3. 配置 repo 的 `setup.sh`（可 persist `~/.bashrc`）
4. 决定 agent 是否需要 internet
5. `@codex` an issue 或在 web 提交 task
6. 等 PR

### 9. 对比与反对意见

**vs Anthropic Cloud Routines**：
- 触发模型：Codex `@codex` mention 更轻；Routines 需要 label / HTTP / schedule 配置
- 缓存：Codex 明确 12h；Anthropic 没明确缓存语义
- 通知：Codex 进 Triage + PR；Anthropic 进 run history + PR
- 网络：两家都默认 agent OFF

### 10. wiki 连接

- [[source-claude-code-routines-docs]] —— 跨厂商对应
- [[source-openai-codex-automations-docs]] —— Cloud env 是 standalone automation 的 runtime
- [[source-openai-codex-hooks-docs]] —— Cloud 无人审批模式下 hook 是唯一守门

### 11. 对用户启示
- 文章 Part 3 Layer 2 表格需加 Codex Cloud 一行
- 中期：测试一次 blog2video 用 Codex Cloud + PLANS.md 跑一晚（vs Claude Code cloud routine 的对比 case）

### 12. 一句话总结
**"Codex Cloud = OpenAI 的 always-on agent platform；2026-05 与 Anthropic Cloud Routines 功能等价，12h 容器缓存是其差异化点。"**

---

## Connections
- Related: [[source-claude-code-routines-docs]], [[source-openai-codex-automations-docs]], [[source-openai-codex-hooks-docs]], [[source-openai-codex-cookbook-trilogy]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-20 | raw/2026-05-20-openai-codex-cloud-environments-docs.md | Initial creation |
