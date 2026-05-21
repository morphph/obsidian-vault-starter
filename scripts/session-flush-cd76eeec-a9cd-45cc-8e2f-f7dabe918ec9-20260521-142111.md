**Assistant:** ```markdown
---
title: "Claude Memory vs CLAUDE.md：两套记忆系统到底怎么选？"
slug: claude-memory-vs-claude-md
description: "Claude Memory 和 CLAUDE.md 是 Claude Code 的两套持久化系统，一个自动记录偏好，一个手动定义规则。详解差异与最佳搭配。"
item_a: Claude Memory
item_b: CLAUDE.md
category: tools
related_glossary: [claude-code, claude-md]
related_blog: [claude-code-memory, claude-code-seven-programmable-layers]
related_compare: []
related_topics: [claude-code]
lang: zh
---

# Claude Memory vs CLAUDE.md：两套记忆系统到底怎么选？

**TL;DR：** **CLAUDE.md** 是团队共享的项目规则手册，签入 Git，所有人看到同一份指令。**Claude Memory** 是个人自动笔记本，跨会话记住你的偏好和反馈。两者不是竞争关系——**CLAUDE.md 管"项目怎么做"，Memory 管"你习惯怎么做"**。最佳实践是同时使用。

## 概述：Claude Memory

**Claude Memory**（也叫 Auto Memory）是 Claude Code 的自动持久化记忆系统，存储在 `~/.claude/projects/` 目录下。它在对话过程中自动捕捉你的偏好、工作习惯和项目上下文，写入独立的 Markdown 文件，下次对话时自动加载。

Memory 解决的核心问题是**会话间的上下文丢失**。没有它，你每次启动 Claude Code 都要重新解释"我喜欢简洁的 commit message""测试用真实数据库别用 mock""这个项目的部署走 Vercel"。Memory 让 Claude 记住这些，不需要你重复。

Memory 分四种类型：`user`（用户画像）、`feedback`（行为纠正）、`project`（项目动态）、`reference`（外部资源指引）。每条记忆是一个带 frontmatter 的 Markdown 文件，通过 `MEMORY.md` 索引。关于 Memory 系统的完整架构，可以参考[Claude Code 记忆系统详解](/zh/blog/claude-code-memory)。

## 概述：CLAUDE.md

**CLAUDE.md** 是 Claude Code 的项目级指令文件，放在仓库根目录，签入版本控制。它定义了项目的构建命令、代码规范、工作流约束和架构决策——本质上是一份**写给 AI 的项目手册**。

CLAUDE.md 解决的核心问题是**项目规范的一致性传递**。无论是新加入的团队成员还是换了一台机器，只要拉取仓库，Claude Code 就会读取同一份 CLAUDE.md，按照同样的规则工作。不会因为换人而丢失"提交前必须跑测试""中文内容用 CJK 字数统计"这些项目约定。

CLAUDE.md 支持多级加载：全局 `~/.claude/CLAUDE.md` 定义个人通用规则，项目根目录定义项目规则，子目录可以有局部覆盖。Claude Code 启动时自动合并这些层级。想深入理解这套分层架构，推荐阅读[Claude Code 七层架构深度解析](/zh/blog/claude-code-seven-programmable-layers)。

## 功能对比

| 维度 | Claude Memory | CLAUDE.md |
|------|--------------|-----------|
| **存储位置** | `~/.claude/projects/` 本地目录 | 仓库根目录，签入 Git |
| **作用范围** | 个人——只对你生效 | 团队——所有克隆仓库的人共享 |
| **创建方式** | 自动捕捉 + 手动触发 | 纯手动编写和维护 |
| **内容类型** | 用户偏好、行为反馈、项目动态 | 构建命令、代码规范、架构约束 |
| **持久性** | 跨会话，但不跨机器 | 跨会话、跨机器、跨团队成员 |
| **版本控制** | 不纳入 Git | 纳入 Git，可追溯变更历史 |
| **加载时机** | 会话启动时自动加载 | 会话启动时自动加载 |
| **适用场景** | 个人工作风格适配 | 项目工程规范统一 |

## 核心差异详解：确定性 vs 自适应

这两套系统的本质区别在于**确定性程度**。

CLAUDE.md 是确定性的。你写什么，Claude 就执行什么。"提交前必须通过 `npm run build` 和 `npm test`"——这条规则不会因为你的心情、习惯或对话历史而改变。它像一份合同，白纸黑字，所有人遵守同一套标准。

Memory 是自适应的。它根据你的行为模式自动调整。你连续三次纠正"不要在回复末尾写总结"，Memory 就会记住这个偏好。下次新对话，Claude 直接按你的习惯来，不需要你再说一遍。但这个偏好只属于你——你的同事不会受影响。

这个区别直接决定了什么该放哪里：

- **放 CLAUDE.md 的**：构建命令、测试要求、代码风格规范、Git 工作流、部署流程、已知陷阱（gotchas）。这些是项目级共识，必须所有人一致执行。
- **放 Memory 的**：你偏好简洁回复还是详细解释、你习惯的 commit message 风格、你正在追踪的项目进展、你常用的外部工具链接。这些是个人偏好，不该强加给团队。

## 协作场景详解：团队共享 vs 个人定制

CLAUDE.md 的一个关键优势是**团队协作中的规范传递**。

假设你在一个 5 人团队工作，CLAUDE.md 里写了："API 路由变更必须同步更新 `docs/context/SYSTEM-OVERVIEW.md`"。无论哪个开发者用 Claude Code 改了 API，这条规则都会被执行。新人入职第一天，不需要任何口头交接，Claude Code 就知道该怎么做。

Memory 解决的是另一个维度的问题。同一个团队里，资深工程师可能希望 Claude 直接上手改代码不要啰嗦，而新人可能需要 Claude 先解释再动手。Memory 让每个人都能得到适合自己的交互方式，而不影响项目规范的统一执行。这就是[Claude Code 扩展栈](/zh/blog/claude-code-extension-stack-skills-hooks-agents-mcp)中多层配置的设计哲学——团队标准和个人偏好在不同层级共存。

## 什么时候选 Claude Memory

以下场景 Memory 是更好的选择：

- **个人工作风格**：你喜欢 Claude 用中文回复、不要加 emoji、commit message 用英文——这些属于个人偏好，不应该签入团队仓库
- **行为纠正记录**：你纠正过 Claude 的某个错误行为（比如"不要在这类测试里 mock 数据库"），希望后续会话自动避免
- **跨项目的个人习惯**：你在所有项目里都用同一套 Git 工作流，写在全局 Memory 比每个项目的 CLAUDE.md 都复制一遍更合理
- **临时项目进展**：当前冲刺的目标、某个 bug 的调查进展、即将到来的 deadline——这些信息有时效性，不适合签入仓库

## 什么时候选 CLAUDE.md

以下场景 CLAUDE.md 是唯一正确选择：

- **构建和测试命令**：`npm run build`、`npm test`、`npm run lint` 等，整个团队必须执行同一套质量门禁
- **代码规范和架构约束**：禁止在 pipeline 脚本里 import Next.js 模块、中文内容必须用 CJK 字数统计——这些规则一旦有人不遵守就会出 bug
- **工作流约定**：新功能先讨论设计再写代码、Pipeline 变更必须跑验证脚本、commit 后必须 push
- **已知陷阱**：`upsertKeyword()` 必须传三个参数、Gemini Deep Research 需要 Python SDK——这些踩坑经验必须团队共享，每个人都受益于了解[如何高效使用 Claude Code](/zh/blog/how-to-effectively-prompt-a-claude-code)

## 最佳实践：两者搭配使用

**最有效的 Claude Code 配置是 CLAUDE.md + Memory 双系统并行。** 它们不是二选一的关系。

一个推荐的搭配方式：

1. **CLAUDE.md 定义底线**：把所有"必须执行"的规则放进 CLAUDE.md。构建命令、测试要求、文档同步规则——这些是不可协商的项目标准
2. **Memory 处理个性化**：让 Memory 自动记录你的交互偏好。如果你总是纠正某个行为，Memory 会帮你记住
3. **全局 CLAUDE.md 管个人通用规则**：把跨项目通用的个人规则（比如 Git 工作流）放在 `~/.claude/CLAUDE.md`，而不是每个项目重复写
4. **定期清理 Memory**：Memory 会随时间积累，过期的项目动态和已解决的 bug 记录应该及时清理，避免给 Claude 注入过时信息

这种分层策略也体现在整个[Claude Code Skills 体系](/zh/blog/9-principles-writing-claude-code-skills)的设计理念中——不同类型的知识放在不同的载体里，各司其职。

## 常见问题

### Claude Memory 和 CLAUDE.md 会冲突吗？
不会直接冲突，但如果两者对同一个行为给出了矛盾指令，CLAUDE.md 的优先级更高。CLAUDE.md 是项目级强制规则，Memory 是个人建议——规则优先于建议。

### Memory 的内容会被其他团队成员看到吗？
不会。Memory 存储在你本地的 `~/.claude/` 目录下，不纳入 Git 版本控制。每个开发者有自己独立的 Memory 空间，互不影响。

### 我应该把所有规则都写进 CLAUDE.md 吗？
不应该。CLAUDE.md 应该只包含团队必须共同遵守的规则。个人偏好（回复风格、交互方式）放 Memory，项目规范（构建流程、代码约束）放 CLAUDE.md。过度臃肿的 CLAUDE.md 会降低 Claude 的执行效率。

### 没有 CLAUDE.md 的项目，Memory 够用吗？
对于个人项目，Memory 可以覆盖大部分需求。但一旦涉及团队协作或者项目有明确的工程规范，强烈建议创建 CLAUDE.md。Memory 是个人的、隐式的；CLAUDE.md 是共享的、显式的——团队协作需要后者。

---

*觉得有用？[订阅 LoreAI](/subscribe)，每天 5 分钟掌握 AI 动态。*
```
