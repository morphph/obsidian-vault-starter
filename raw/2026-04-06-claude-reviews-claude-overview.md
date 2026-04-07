# Claude Reviews Claude — 架构总览

**Source:** https://openedclaude.github.io/claude-reviews-claude/zh-CN/overview
**Language:** Chinese (zh-CN)
**Type:** Technical architecture analysis — overview/landing page for a 17-chapter deep-dive series

## Overview

"Claude Reviews Claude" 是一份全面的 Claude Code 架构分析文档，共17章，总计8,600+行技术分析。将 Claude Code（Anthropic 官方 CLI 工具）作为分析对象，深入剖析其内部架构和设计模式。

## Core Architecture: Six Foundational Pillars

1. **System Prompt** — 身份定义、规则、42+ tool descriptions
2. **Tool System** — 42个集成模块，每个30+方法
3. **Query Loop** — 12步状态机驱动 agentic 迭代
4. **Context Management** — 四层压缩系统
5. **Multi-Agent Coordination** — 分布式任务执行
6. **Security & Permissions** — 七层纵深防御架构

## Core Design Principle

"LLM functions as the reasoning center; the Harness provides perception, action, memory, and constraints."

LLM 作为推理中心；Harness 提供感知、行动、记忆和约束。

## Learning Paths (6 tracks)

- Core loop track (4 chapters)
- Security track
- Multi-agent track
- Infrastructure track
- UI track
- Operations track

## Notable Engineering Patterns

- **"35-line Store"** — 用 React 19 的 `useSyncExternalStore` 替代 Redux 做状态管理
- **"Fork Ink"** — 重新实现终端渲染引擎，支持正确的事件处理
- **"Leaf Module Pattern"** — 隔离 bootstrap 代码，通过 ESLint 规则防止循环依赖

## Security Design

- **Fail-closed defaults** — 未知操作默认拒绝（safety-critical operations）
- **Fail-open degradation** — 配置和外部服务允许优雅降级
- 7 permission rule sources
- 20 hook event types

## Quantified Scope

- 17 chapters, 711-980 lines each
- 42+ integrated tools
- 4 compression layers for context management
- 12-step query loop state machine
- 7 permission rule sources
- 20 hook event types
- Context window treated as "scarcest resource"
