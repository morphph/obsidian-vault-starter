---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-repo-mattpocock-sandcastle.md
tags: [wiki, source, claude-code, afk, sandbox, orchestration]
---

# Source: mattpocock/sandcastle (GitHub Deep Scan)

## Summary
Matt's TypeScript orchestration framework for AFK coding agents — 4,465 stars, published as `@ai-hero/sandcastle`. Provider-agnostic (Docker / Podman / Vercel Firecracker). `sandcastle.run()` as the AFK primitive.

## 要点解读

### 1. `sandcastle.run()` 把 AFK agent 收敛成一个函数调用
最核心的 API 就是 `await run({ agent, sandbox, promptFile })`。所有复杂的 sandboxing、分支管理、commit 合并都在这一行后面。**为什么重要：**之前 Ralph 是一堆 bash 脚本 + Docker 命令拼起来的；Sandcastle 把这套流程做成了可编程的 TS API，你可以在 CI、cron、其他脚本里调用。**实操建议：**如果你想做"夜间跑 AFK"——用 Sandcastle 比手写 bash loop 可靠。

### 2. Provider 抽象 —— 同样代码本地 / 云端 / 自建
内置三个 provider：
- **Docker** —— 本地最常见，bind-mount 你的本地代码
- **Podman** —— rootless 替代 Docker，CI 友好
- **Vercel** —— 云端 Firecracker microVMs（适合并行很多 agent）

`docker()` `podman()` `vercel()` 可以互换。**实操：**开发时用 docker()，生产并行跑多个 agent 时切到 vercel() 完全不改代码。

### 3. `createWorktree()` —— interactive→AFK 升级路径的 API 化
单独的 worktree API（独立于 sandbox）。典型用法：
1. 先用 worktree 跑 **interactive** 会话（不进 sandbox），人工探索代码
2. 把同一个 worktree 交给 **AFK agent**（进 sandbox 跑）

这正是 Matt 在 tweet 里描述的 "iterate interactively → AFK one-shot" 的代码实现。**实操建议：**这是 idea-to-AFK 流程的关键基础设施，记下来。

### 4. Completion Signal —— agent 自己说"我完成了"
默认 `<promise>COMPLETE</promise>`。当 agent 输出这个字符串，loop 立即结束。比基于时间的轮询好用：agent 知道自己什么时候完成。**实操：**在你给 agent 的 system prompt 里要求"完成所有任务后输出 `<promise>COMPLETE</promise>`"。

### 5. `.factory/` 是"software-factory"的真身
仓库内 `.factory/` 文件夹包含 `implement-prompt.md` + `review-prompt.md` + `run-daemon.sh` + `implement-task.ts`。**这就是 Matt 说的 software-factory** —— 不是单独的仓库，而是 Sandcastle 仓库内的一个引用实现。模式：plan → implement → review → merge 4 个 prompt + 一个 bash daemon 持续跑。**实操建议：**复制这个 `.factory/` 结构到你自己的项目，是建立 overnight AFK pipeline 最快的路径。

### 6. 设计成熟度证据：14+ ADR
仓库内 `docs/adr/` 有 14+ 个决策记录，比如 `0003-reuse-worktree-by-default`、`0010-structured-output`、`0014-docker-uid-alignment-via-build-arg`。Matt 自己用 grill-with-docs 流程开发 Sandcastle，是吃自己的狗粮——这是质量信号。

## Connections
- [[sandcastle]] (concept page), [[matt-pocock]]
- [[ralph-wiggum]] (the pattern Sandcastle productizes)
- [[claude-code-sandboxing]] (security foundation)
- Related: [[idea-to-afk-agent-flow]] (Phase 5 primitive)

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial deep scan + ingest |
