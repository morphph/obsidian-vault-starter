---
source: agent
created: 2026-03-08
tags: [tooling, workflow, claude-code]
---

# Claude Code 新功能与工作流建议

基于 [[LoreAI]] 和 [[blog2video]] 的实际使用场景。

## 三个核心新功能

### /simplify — 自动代码审查
写完代码后运行，并行启动 3 个 review agent（代码复用、质量、效率），聚合后自动修复。
- **适用场景**：每次 pipeline 改动后的 PR 前质检
- **blog2video 用法**：改 4 阶段 pipeline 后跑一次，自动发现跨阶段重复逻辑

### /batch — 大规模并行迁移
描述变更 → 自动调研 → 拆分 5-30 个独立单元 → 各自在 git worktree 并行执行 → 自动 /simplify → 各自开 PR。
- **适用场景**：[[LoreAI]] ↔ [[blog2video]] 整合接线（[[bilingual content arbitrage]] 的关键一步）
- **具体操作**：用 /batch 批量把 blog2video 外部内容通过 `import-external-blog.ts` 导入 LoreAI

### /loop — 定时轮询监控
设定间隔重复运行命令，默认 10 分钟，3 天自动过期，session-scoped。
- **适用场景**：LoreAI pipeline 状态监控与 debug

## LoreAI Pipeline 监控三层方案

### 第一层：/loop 即时监控（开发时）
```
/loop 5m check Vercel deployment for loreai-v2, show error summary if failed
/loop 10m read last 50 lines of build logs, flag errors and suggest fix
/loop 3m run test suite and report if failing test passes now（debug 陪跑）
```
- prompt 要具体：去哪看 → 看什么 → 发现问题怎么办
- 限制：关终端就没了，Claude 忙时只补一次

### 第二层：Desktop Scheduled Tasks（持久监控）
- 不因关终端消失，重启 app 后仍在
- 每 2 小时扫 error logs → 有问题开 PR 或通知
- 每天早上 pipeline health check → 状态摘要

### 第三层：GitHub Actions（24/7 always-on）
- `claude-code-action@v1` + cron schedule
- 适合不在电脑前时的持续监控

## 落地步骤（优先级排序）

1. **写 `.claude/commands/check-pipeline.md`** — 把 LoreAI 监控逻辑封装成自定义命令
2. **在 CLAUDE.md 记录 Known Pipeline Issues** — 让 Claude 自动识别常见错误模式
3. **用 `/loop 10m /project:check-pipeline`** — 开发时自动巡检
4. **用 `/batch` 做 blog2video → LoreAI 内容接线** — ROI 最高的整合动作（3-4h）
5. **每次代码改动后 `/simplify`** — 养成 PR 前自动质检习惯

## 核心原则

> /loop 本身是简单的定时触发器，真正的价值在于喂给它的 prompt 质量。把监控知识编码成自定义命令 + CLAUDE.md known issues，/loop 就从"帮你看一眼"升级成"帮你值班"。

这些工具最大的价值不是单独用，而是组合成 builder workflow 的一部分。
