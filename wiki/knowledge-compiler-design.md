---
type: synthesis
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, synthesis, roadmap, harness-engineering, architecture]
---

# 从两个灵感源到一套知识编译系统

## Summary

这篇文章记录了我们如何从 Karpathy 的 LLM Knowledge Base 和 coleam00 的 claude-memory-compiler 两个灵感源中各取所长，设计出一套同时捕获外部知识和内部知识的编译系统。不只是技术方案，更是决策过程——为什么选了这些能力，为什么放弃了那些，以及这套系统最终如何让知识自动流动、自动连接、自动复利。

![[visual-wiki-architecture]]

![[visual-agent-sdk-roadmap]]

---

## 两个灵感源，各取所长

### 灵感源 A：Karpathy 的 LLM Wiki

Andrej Karpathy 在 2026 年 4 月发布了一个 gist，描述了一种用 LLM 构建个人知识库的模式。核心思想：

> 不要每次查询都从原始文档重新推导（RAG 模式），而是让 LLM **增量构建并维护一个持久化的 wiki**。知识编译一次，持续更新，而不是每次重新推导。

**我们从 Karpathy 拿了什么：**
- [[compiler-analogy|三层架构]]：`raw/`（不可变源文件）→ `wiki/`（LLM 维护的知识页面）→ `CLAUDE.md`（schema）
- 两个结构文件：`index.md`（内容目录，LLM 的检索入口）和 `log.md`（操作日志）
- 三个核心操作：Ingest（编译）、Query（查询）、Lint（健康检查）
- [[index-over-rag]]：在个人规模（50-500 篇文章），LLM 读结构化 index 比向量相似度检索更准

**我们没有用 Karpathy 的什么：**
- 他的设计只处理外部文章（web clipper → 源文件 → wiki）。没有内部知识捕获的概念。
- 没有自动化——所有操作都是手动触发的。
- 没有跨概念连接发现的机制。

### 灵感源 B：claude-memory-compiler

coleam00 构建了一个开源工具，让 Claude Code 拥有持久化记忆。他也是基于 Karpathy 的架构，但做了一个关键转向：**源数据不是外部文章，而是你自己的 AI 对话。**

**我们从 claude-memory-compiler 拿了什么：**
- [[zero-friction-capture]]：Hook-based 零摩擦捕获。SessionEnd + PreCompact hooks 自动触发，hook 只做本地 I/O（<10秒），spawn 后台进程用 Agent SDK 做 LLM 提取。你什么都不用做。
- [[time-gated-compilation]]：白天只积累，晚上 6 PM 统一编译。省钱（一次 vs 多次）、省心（不需要 cron）、质量更好（LLM 看到全天上下文）。
- [[connection-articles]]：跨概念连接不只是页面底部的 "Related:" 链接，而是独立的一等公民文章，记录洞察、证据、和双向链接。
- [[agent-sdk-vs-claude-code|Agent SDK vs CLI 的分工]]：交互任务用 CLI，无人值守任务用 Agent SDK。
- 递归防护（`CLAUDE_INVOKED_BY` env var）：防止 hook → Agent SDK → Claude Code → hook 的无限循环。

**我们没有用 claude-memory-compiler 的什么：**
- 他的 `daily/` 目录结构——我们不需要单独的日志目录，所有东西直接进 `raw/`
- 他的 `concepts/` `connections/` `qa/` 子目录——我们的 wiki 保持扁平结构，用 `index.md` 分类组织
- 他用 Agent SDK 跑 compile.py 做编译——我们继续用 Claude Code 的 `/ingest` 命令做编译（更灵活，支持交互讨论），Agent SDK 只用在后台无人值守任务

---

## 我们的设计：两条管道，一个知识库

### 核心架构

```
Pipeline A (外部知识)          Pipeline B (内部知识)
  Desktop 手动 /ingest           Claude Code Hooks
  Telegram bot (Channels)        SessionEnd + PreCompact
  RSS feeds                      → flush.py → Agent SDK
         ↘                              ↙
              raw/ (Layer 1)
                    ↓
           LLM Compiler (/ingest scan)
           ⏰ Time-gated 6 PM or manual
                    ↓
              wiki/ (Layer 2)
         index.md + log.md + pages
                    ↓
      /query  /lint  /visualize (Operations)
```

### 为什么是两条管道？

**Pipeline A（外部知识）** 捕获别人构建的东西——文章、开源 repo、推文、newsletter。这是 Karpathy 设计的核心场景。

**Pipeline B（内部知识）** 捕获你自己构建时学到的东西——编码决策、踩过的坑、发现的 patterns、架构选择。这是 claude-memory-compiler 的核心场景。

**为什么必须合二为一？** 因为最有价值的洞察往往出现在**交叉地带**。

举例：你读了一篇关于 [[harness-design]] 的文章（Pipeline A），然后在 LoreAI 项目里实践了这个模式（Pipeline B）。如果两条管道分开，你永远不会发现："我在 LoreAI 里遇到的 bug 其实就是文章里说的 [[context-anxiety]]"。但在同一个 wiki 里，`/query` 可以同时搜索两个来源，connection articles 可以桥接外部理论和内部实践。

### 为什么汇入同一个 raw/？

这是一个关键的架构决策。两条管道的输出格式不同（文章 vs 对话摘要），但都是 markdown 文件。让它们共享 `raw/` 意味着：
- 同一个 LLM Compiler（`/ingest scan`）处理所有输入
- 同一个 `wiki/index.md` 检索所有知识
- 同一个 `/query` 搜索所有来源
- 同一个 Obsidian graph view 显示所有连接

没有两套系统，没有知识孤岛。

---

## 时间节奏：白天积累，晚上编译

| 时间 | 发生什么 | 管道 |
|------|---------|------|
| 全天 | 你手动 `/ingest` 感兴趣的文章/repo | Pipeline A |
| 全天 | Telegram bot 收到你转发的内容，自动存到 `raw/` | Pipeline A |
| 全天 | 你在 LoreAI / blog2video 里编码，hooks 自动提取对话知识到 `raw/` | Pipeline B |
| 18:00 | [[time-gated-compilation]]：`/ingest scan` 自动编译当天所有新 raw 文件 | 统一编译 |
| 随时 | `/query` 问问题、`/lint` 健康检查、`/visualize` 生成图表 | Wiki 操作 |

这个节奏的好处：
- **零摩擦**：你的日常工作流不受影响。编码就编码，阅读就阅读，知识在后台自动流动。
- **成本可控**：编译一天只跑一次（~$0.45-0.65），而不是每个 session 都跑。
- **质量更高**：LLM 在一次编译中看到全天的碎片，能做更好的综合和连接发现。

---

## Connection Articles：知识复利的引擎

这是从 [[claude-memory-compiler]] 学到的最有价值的模式。

**问题**：传统 wiki 里，连接只是页面底部的 "Related:" 链接列表。它告诉你"A 和 B 有关系"，但不告诉你**为什么有关系、关系的洞察是什么**。

**解决方案**：把非显然的跨概念连接提升为独立的一等公民文章。

我们的第一篇 connection article（[[connection-context-anxiety-and-zero-friction-capture]]）就是一个例子：

> [[context-anxiety]]（LLM 在上下文快满时草率完成）和 [[zero-friction-capture]]（自动知识捕获）看起来完全不相关。但它们之间的桥梁是：**人类也有 context anxiety——在长编码 session 里认知负荷高时，你会跳过记录和反思。Zero-friction capture 是人类 context anxiety 的解药，就像 4-layer compression 是 LLM context anxiety 的解药。**

这个洞察不属于任何一个页面。没有 connection article，它永远不会被 `/query` 检索到。

**更重要的是**：将来 Agent SDK 在编译时会自动发现这类连接。每次 ingest 新内容，编译器不只是创建/更新页面，还会扫描所有已有概念，寻找新内容是否揭示了它们之间的非显然关系。这是知识的**自动复利**——不依赖人类去问对的问题。

### 白天手动 vs 晚上自动：Connection 发现在哪一步？

一个重要的澄清：**白天手动 `/ingest` 不会自动发现 connections。** 它只做基本编译——创建/更新 entity 和 concept 页面。

Connection 发现发生在**晚上 6 PM 的 Agent SDK 自动编译**。原因：
1. **慢**：扫描所有已有 wiki 页面（现在 27 个，将来可能几百个）+ LLM 判断每个关系是否非显然且有价值——这很耗时，不应该让你在 CLI 里等
2. **全天上下文更好**：如果你一天 ingest 了 3 个源，6 PM 统一编译时 LLM 同时看到三个新源和所有已有概念，发现的连接质量比逐个 ingest 时高
3. **批量更高效**：一次扫描发现所有连接，比每次 ingest 都扫描一遍省钱省时间

```
白天：/ingest <url>
  → 快速编译：创建/更新 entity + concept 页面
  → 不找 connection（快，交互，省时间）

晚上 6 PM：Agent SDK 自动编译
  → 编译当天所有新 raw 文件
  → 额外步骤：扫描所有已有 wiki 概念
  → 发现非显然关系 → 自动创建 connection articles
  → 慢，深度，无人值守
```

当然，如果你在白天讨论中发现了一个 connection（像我们发现 context-anxiety × zero-friction-capture），你随时可以**手动创建** connection article。自动发现是补充，不是替代。

---

## Agent SDK：无人值守的 LLM 操作

从 claude-memory-compiler 学到的一个关键分工：

> **Claude Code CLI 是给人用的交互工具。Agent SDK 是给代码用的编程接口。**

所有需要人参与的操作（`/ingest`、`/query`、`/lint`、`/visualize`）用 CLI。所有在后台自动运行的操作用 Agent SDK。

### Phase 1 — 基础（现在要建的）

| 能力 | 做什么 | 为什么用 Agent SDK |
|------|--------|-------------------|
| Knowledge Flush | Hooks 提取对话知识 → `raw/` | Claude Code 已关闭，headless |
| Time-Gated Compile | 6 PM 自动 `/ingest scan` | 无人值守定时任务 |
| Auto Connections | 编译时发现跨概念桥梁 | 需要 LLM 判断但不需要人 |
| GitHub Deep Scan | 后台 repo 分析 + pattern 提取 | 分析耗时 ~60s，不阻塞 CLI |

### Phase 2 — 自动化（Pipeline B 跑通后）

| 能力 | 做什么 | 为什么用 Agent SDK |
|------|--------|-------------------|
| Telegram Bot | Claude Code Channels 接收 → `raw/` | 异步消息，无人在场 |
| Auto Weekly /lint | 每周日健康检查 → 报告 | 定时任务 |

### Phase 3 — 智能化（wiki 规模变大后）

| 能力 | 做什么 | 为什么用 Agent SDK |
|------|--------|-------------------|
| Weekly Digest | 生成周报 → Telegram/email | 定时生成 |
| RSS Intelligent Filter | LLM 判断文章是否相关 | 比关键词过滤强得多 |
| Auto /visualize | ingest 3+ 页后自动更新图表 | 图表生成慢，不需要人 |

---

## 最终效果：知识自动流动、自动连接、自动复利

建成后的系统是这样的：

1. **你只需要做两件事**：编码（内部知识自动流出）和阅读/分享（外部知识手动或自动流入）
2. **编译器处理剩下的一切**：提取实体和概念、创建/更新 wiki 页面、发现跨概念连接、维护 index 和 log
3. **知识在三个层面复利**：
   - **页面层面**：每个新源让已有页面更丰富（多源交叉验证）
   - **连接层面**：每次编译可能发现新的非显然关系
   - **查询层面**：每个好答案可以 file back 成新页面，让未来的查询更智能
4. **你随时可以问**：`/query "我见过哪些 pipeline 设计模式？"` 会同时搜索你读过的文章和你自己编码时积累的经验

这就是 [[compiler-analogy|知识编译器]]的最终形态：你不手动整理知识，你有对话，你编码，你阅读——编译器处理综合、交叉引用和维护。

---

## 执行状态：已完成 vs 待建

### ✅ 已完成

| 组件 | 说明 | 完成时间 |
|------|------|---------|
| 三层架构 | `raw/` + `wiki/` + `CLAUDE.md` | 2026-04-06 |
| `/ingest` 命令 | 手动 ingest，支持 URL、文件、scan | 2026-04-06 |
| `/query` 命令 | 问 wiki 问题，可 file back | 2026-04-06 |
| `/lint` 命令 | 7 项健康检查 | 2026-04-06 |
| `/visualize` 命令 | Excalidraw 图表生成 | 2026-04-07 |
| Smart URL fetch | WebFetch → Chrome → Playwright 分级 | 2026-04-06 |
| Playwright MCP | 配置完成，JS-heavy 站点可抓取 | 2026-04-06 |
| GitHub Deep Scan | `/ingest` 自动检测 GitHub URL，gh CLI 深度扫描 | 2026-04-07 |
| 三个 Pattern 分类 | Harness Engineering / System Design / DX | 2026-04-07 |
| Excalidraw skill | 安装并可用，Playwright 渲染验证 | 2026-04-07 |
| Connection articles（手动） | 概念定义 + 第一篇 connection + index 分类 | 2026-04-07 |
| CLAUDE.md 文档化 | 所有命令和 skills 有使用指南 | 2026-04-07 |
| 3 次外部 ingest | Anthropic 文章 + Claude Reviews Claude + claude-memory-compiler repo | 2026-04-06~07 |
| 2 次内部 capture | 架构讨论 + Agent SDK roadmap（手动） | 2026-04-07 |

### 🔨 待建：Phase 1 — 基础

| 组件 | 做什么 | 依赖 | 预估工作量 |
|------|--------|------|-----------|
| hooks (SessionEnd + PreCompact) | 在 LoreAI / blog2video 项目里安装 hooks，捕获对话 transcript | 需要修改项目 `.claude/settings.json` | 中等 |
| flush.py | 后台进程，用 Agent SDK 从 transcript 提取知识，写到 wiki 的 `raw/` | hooks + Claude Agent SDK 安装 | 中等 |
| 递归防护 | `CLAUDE_INVOKED_BY` env var 防止无限循环 | flush.py | 小 |
| Time-Gated Compile | 6 PM 自动触发 `/ingest scan` 编译当天新 raw 文件 | flush.py（搭便车在最后一次 flush 上） | 小 |
| Auto Connection Discovery | 编译时自动扫描已有概念，发现非显然关系 | Time-Gated Compile | 中等 |

### 🔜 待建：Phase 2 — 自动化

| 组件 | 做什么 | 依赖 | 预估工作量 |
|------|--------|------|-----------|
| Telegram Bot (Channels) | Claude Code Channels 配置，接收转发文章 → `raw/` | Phase 1 完成 + Claude Code Channels 功能 | 中等 |
| Auto Weekly /lint | 每周日 Agent SDK 跑健康检查 → 报告写入 wiki | Phase 1 完成 | 小 |

### 🔮 待建：Phase 3 — 智能化

| 组件 | 做什么 | 依赖 | 预估工作量 |
|------|--------|------|-----------|
| Weekly Digest | 每周一生成知识周报 → Telegram/email | Phase 2 完成 | 中等 |
| RSS Intelligent Filter | LLM 判断 RSS 文章相关性 → 只存相关的到 `raw/` | Phase 1 完成 | 中等 |
| Auto /visualize | ingest 3+ 页后自动生成图表 | Phase 1 完成 + excalidraw skill | 小 |

### 还有一个待完成的 ingest

Ryan Sarver 的 X Article（AI Chief of Staff on OpenClaw）已经存到 `raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md`，key takeaways 已讨论，但 wiki 页面尚未创建。

---

## Connections
- Related: [[agent-sdk-vs-claude-code]], [[two-pipeline-architecture]], [[zero-friction-capture]], [[time-gated-compilation]], [[connection-articles]], [[compiler-analogy]], [[claude-memory-compiler]], [[harness-design]], [[context-anxiety]], [[index-over-rag]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | Internal discussion: multi-round architecture design | Initial creation — synthesized from Karpathy + claude-memory-compiler + discussion insights |
| 2026-04-07 | Rewrite: expanded from Agent SDK roadmap to full system design narrative | Added inspiration sources analysis, decision rationale, connection articles as compounding engine |
| 2026-04-07 | Added connection timing clarification + execution status tracking | CLI ingest 不找 connection，6 PM Agent SDK 编译时找；全面扫描已完成 vs 待建 |
