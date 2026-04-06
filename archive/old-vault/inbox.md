# Inbox

## 2026-03-23
- [build] Claude Code /insights review → 归纳出防 buggy code 的三层决策框架：(1) **预防** CLAUDE.md 行为指导（Known Gotchas, "read before edit"）(2) **拦截** Hooks pre-commit gate（`lint && test && build`，project level）(3) **进阶** Parallel agents 并行测试（等 test suite 大了再用）。选择标准：bug >20% 频率 → hook/skill validation；偶尔 → CLAUDE.md gotchas；一次性 → 不管。案例：blog2video Stage 3 曾用错 prompt file（slide-data-generator vs slide-html-generator）导致 stale slides，这种偶发 bug 适合 CLAUDE.md gotchas 而不是 skill validation。另外 plan mode (`shift+tab`) 解决了 Claude 讨论没完就跳去实现的问题。Next: [[LoreAI]] v2 加 pre-commit hook，[[blog2video]] CLAUDE.md 加 Known Gotchas section

## 2026-03-21
- 研究 agency-agents：61个 AI agent 定义文件，覆盖工程/产品/设计等9个部门，支持 Claude Code/Cursor 等多工具。看看能不能用到自己的工作流里。来源：https://github.com/msitarzewski/agency-agents
