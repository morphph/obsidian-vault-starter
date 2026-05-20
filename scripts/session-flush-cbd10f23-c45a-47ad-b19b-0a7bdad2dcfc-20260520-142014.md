**Assistant:** ```markdown
---
title: "Claude Memory vs CLAUDE.md：两套持久化机制怎么选？"
slug: claude-memory-vs-claude-md
description: "Claude Memory 和 CLAUDE.md 是 Claude Code 的两套持久化系统。一文讲清区别、适用场景和最佳搭配方案。"
item_a: Claude Memory
item_b: CLAUDE.md
category: tools
related_glossary: [claude-code, claude-md]
related_blog: [claude-code-memory, claude-code-seven-programmable-layers]
related_compare: []
related_topics: [claude-code]
lang: zh
---

# Claude Memory vs CLAUDE.md：两套持久化机制怎么选？

**TL;DR：** **CLAUDE.md** 是写给项目的规则手册——团队共享、版本控制、每次会话自动加载；**Claude Memory** 是写给个人的自动笔记——跨会话积累上下文、记住你的偏好和反馈。两者不是竞争关系，而是互补关系。规则放 CLAUDE.md，经验放 Memory。

## Overview：Claude Memory

Claude Memory 是 Claude Code 的文件级持久记忆系统。它把跨会话需要保留的信息——用户偏好、项目背景、工作反馈、外部资源指引——以独立 Markdown 文件的形式存储在 `~/.claude/projects/<project>/memory/` 目录下。每个记忆文件带有 frontmatter 元数据（类型、描述），并通过一个 `MEMORY.md` 索引文件在会话开始时自动加载。

Claude Memory 的核心设计理念是**让 AI 像同事一样积累对你和项目的了解**。它不存代码结构或 git 历史这些可以实时查询的信息，而是存那些"只有合作过才知道"的隐性知识：你是高级工程师还是初学者、你讨厌冗长的总结、上次那个 PR 拆分策略被验证有效。

Memory 分四种类型：`user`（用户画像）、`feedback`（行为指导）、`project`（项目动态）、`reference`（外部资源）。这套分类确保信息不是杂乱堆积，而是结构化存储、按需检索。更多技术细节可参考 [Claude Code 记忆系统详解](/zh/blog/claude-code-memory)。

## Overview：CLAUDE.md

CLAUDE.md 是 Claude Code 的项目级指令文件——本质上是一份写给 AI 的工程手册。它以 Markdown 格式存放在项目根目录，随代码一起 `git commit`、`git push`，团队每个成员的 Claude Code 会话都会自动读取同一份 CLAUDE.md。

CLAUDE.md 的内容通常包括：构建命令（`npm run build`、`npm test`）、代码风格约定、提交前的质量门禁、技术栈说明、已知陷阱和禁忌操作。它是**确定性的、显式的、版本化的**——和 `.eslintrc` 或 `tsconfig.json` 属于同一层面的项目基础设施。

除了项目根目录的 CLAUDE.md，Claude Code 还支持用户级 `~/.claude/CLAUDE.md`（个人全局指令）和子目录级的 CLAUDE.md（模块专属规则）。三层配置按优先级合并，形成完整的指令上下文。这套分层架构在 [Claude Code 七层架构深度解析](/zh/blog/claude-code-seven-programmable-layers) 中有详细剖析。

## 功能对比

| 维度 | Claude Memory | CLAUDE.md |
|------|--------------|-----------|
| **存储位置** | `~/.claude/projects/…/memory/` | 项目根目录（或 `~/.claude/`） |
| **版本控制** | 不进 git，个人本地 | 随项目 git 管理 |
| **团队共享** | 仅限当前用户 | 整个团队共享 |
| **写入方式** | AI 自动写入 + 用户指令 | 人工编写和维护 |
| **加载机制** | MEMORY.md 索引自动加载 | 会话启动时自动注入 |
| **内容类型** | 用户偏好、反馈、项目动态、资源指引 | 构建命令、代码规范、质量门禁、已知陷阱 |
| **生命周期** | 渐进积累，需定期清理 | 随代码演进，PR 级更新 |
| **适用范围** | 跨项目（用户级）+ 项目专属 | 严格绑定单个项目 |

## 持久化机制：核心差异详解

CLAUDE.md 和 Claude Memory 解决的是同一个问题的两个面：**如何让 AI 在新会话中不从零开始**。但它们的设计哲学截然不同。

CLAUDE.md 是**声明式配置**。你告诉 AI "提交前必须跑 `npm test`"、"中文内容用 CJK 字数统计"、"不要在 pipeline 脚本里 import Next.js 模块"——这些是不随会话变化的硬性规则。它的价值在于**一致性**：不管是你、你的同事、还是 CI 环境里的 Claude Code，读到的都是同一份指令。

Claude Memory 是**经验式积累**。AI 在和你合作的过程中，自动（或按你的指示）记录下 "这个用户是数据科学家、偏好简洁回复、上次确认过单 PR 策略有效" 这类信息。它的价值在于**个性化**：同一个项目，不同角色的开发者会积累出不同的 Memory，AI 的协作风格也随之调整。

一个实际的例子：你在 CLAUDE.md 里写 "commit message 用英文、祈使语气"——这是团队规范，所有人遵守。而 Memory 里记录 "这个用户喜欢我在 commit message 里加上改动原因，不只是描述改了什么"——这是个人偏好，只影响你的会话。

两者的交互也值得注意：CLAUDE.md 的优先级高于 Memory。如果 Memory 记录了"用户偏好 tab 缩进"，但 CLAUDE.md 明确要求 "使用 2 空格缩进"，Claude Code 会遵循 CLAUDE.md。这是合理的——团队规范覆盖个人偏好。

## 写入与维护：谁来管、怎么管

CLAUDE.md 的维护是**人工主导**的工程活动。它通常在项目初始化时创建（Claude Code 提供 `/init` 命令生成初始版本），随后像其他配置文件一样，通过 PR 流程更新。好的 CLAUDE.md 会随项目演进而迭代——新增构建步骤、记录新发现的陷阱、更新依赖约束。这个过程需要工程判断，不能完全自动化。

Claude Memory 的写入是**半自动**的。AI 会在对话中检测到值得记忆的信息时主动保存——比如你纠正了它的做法、你透露了自己的技术背景、你提到了一个项目截止日期。你也可以显式地说 "记住这个"。每条 Memory 是一个独立的 Markdown 文件，带有类型标签和描述，通过 `MEMORY.md` 索引管理。

维护负担也不同。CLAUDE.md 的维护成本低——它变化不频繁，变化时有 git diff 可审查。Memory 的维护需要更多注意：记忆会过时（项目动态变化）、会冲突（记忆说文件存在但已被删除）、会膨胀（积累太多低价值信息）。Claude Code 内置了一些防护——比如写入前检查是否重复、优先更新而非新建——但定期审查 Memory 目录仍然是好习惯。

如果你想更系统地理解 Claude Code 的可编程层级（CLAUDE.md、Skills、Hooks、Memory 各自的定位），推荐阅读 [Claude Code 扩展栈拆解](/zh/blog/claude-code-extension-stack-skills-hooks-agents-mcp)。

## 什么时候用 Claude Memory

Memory 的最佳场景是**个人工作流优化**：

- **角色适配**：你是 PM 而不是工程师，AI 应该调整解释的技术深度
- **行为校正**：你告诉 AI "别在每次回复末尾总结"，这个偏好应该跨会话生效
- **项目动态**：代码冻结时间、正在进行的重构方向、某个 bug 的背景
- **外部资源**：bug 追踪在 Linear 的哪个项目、oncall dashboard 的 URL

Memory 不适合存代码结构、文件路径、函数签名这些可以通过读代码获取的信息。它也不适合存"任务清单"或"当前进度"——这些用 Claude Code 的 Task 系统更合适。关于 Skills 系统如何与 Memory 配合使用，可以参考 [我每天都在用的 5 个 Claude Code 技巧](/zh/blog/5-claude-code-skills-i-use-every-single-day)。

## 什么时候用 CLAUDE.md

CLAUDE.md 的最佳场景是**团队级工程标准**：

- **构建流程**：`npm run build`、`npm test`、lint 命令——确保 AI 知道怎么验证改动
- **质量门禁**：提交前必须通过哪些检查、禁止哪些操作
- **代码规范**：命名约定、缩进风格、import 排序规则
- **已知陷阱**：特定模块的坑、不能碰的配置、容易出错的操作
- **工作流约定**：commit message 格式、分支策略、PR 流程

如果一条规则需要团队所有成员（包括新加入的人）都遵守，它属于 CLAUDE.md。如果一条信息只对你个人有价值，它属于 Memory。判断标准很简单：**这条信息应该进 git 吗？** 是，放 CLAUDE.md；不是，放 Memory。

了解如何编写高质量的 Skills 文件来补充 CLAUDE.md，可以参考 [Claude Code Skills 最佳实践](/zh/blog/9-principles-writing-claude-code-skills)。

## 结论

**CLAUDE.md 和 Claude Memory 不是二选一的关系，而是分工明确的互补系统。** CLAUDE.md 负责项目的"法律"——确定性规则、团队标准、工程约束；Memory 负责个人的"经验"——用户画像、行为偏好、项目洞察。最佳实践是两者同时使用：用 CLAUDE.md 确保 AI 遵守团队规范，用 Memory 让 AI 越用越懂你。

对于刚开始使用 Claude Code 的团队，建议先写好 CLAUDE.md（从 `/init` 生成的模板开始迭代），Memory 则让它在日常协作中自然积累。不要试图一次性把所有信息都塞进 CLAUDE.md——那些属于个人偏好和项目动态的信息，交给 Memory 系统处理更合适。

## 常见问题

### Claude Memory 的内容会被其他团队成员看到吗？

不会。Claude Memory 存储在你本地的 `~/.claude/` 目录下，不进版本控制，不会推送到远程仓库。每个开发者的 Memory 是独立的，AI 只在你的会话中读取你的 Memory。团队共享信息应放在 CLAUDE.md 中。

### CLAUDE.md 和 Memory 冲突时以哪个为准？

CLAUDE.md 优先。Claude Code 的设计原则是显式规则覆盖隐式记忆。如果 CLAUDE.md 要求 "使用 TypeScript strict 模式"，即使 Memory 中记录了你曾偏好宽松类型检查，AI 也会遵循 CLAUDE.md 的要求。

### Memory 文件可以手动编辑吗？

可以。Memory 文件是标准 Markdown，存储在 `~/.claude/projects/<project>/memory/` 目录下。你可以直接用编辑器修改、删除过时的记忆、或手动创建新的记忆文件。只要保持 frontmatter 格式正确并更新 `MEMORY.md` 索引即可。

---

*觉得有用？[订阅 LoreAI](/subscribe)，每天 5 分钟掌握 AI 动态。*
```
