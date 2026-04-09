---
status: draft
sources:
  - raw/2026-04-09-bcherny-claude-code-best-practices.md
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
platform: blog
created: 2026-04-09
last-updated: 2026-04-09
tags: [draft]
---

<!-- HOOK: 大多数人用Claude Code的best practices是在"照着做"。Boris Cherny（Claude Code创始人）发的tips很好用，但你知道每条建议背后对应的是哪个系统约束吗？理解了这些，你自己就能推导出正确做法。 -->

# 为什么Boris的Best Practices有效——用Tw93的框架理解

Boris Cherny发了三条viral thread教大家怎么用好Claude Code。Tw93写了一篇2.8M views的深度文章拆解Claude Code的底层逻辑。我把两篇放在一起读，发现：**先理解Tw93的框架，再看Boris的建议，每一条都变成了"显而易见"的事。**

这篇文章先完整介绍Tw93的context分层框架，再用它来解释Boris的全部best practices。

---

## Context是噪音问题，不是容量问题

用Claude Code久了都会发现：对话刚开始时很聪明，越往后越不靠谱。大多数人以为是"context太满了"。

Tw93纠正了这个认知：**Context问题不是容量问题，是噪音问题。**

200K token的窗口很大。真正的问题是：Claude每一轮对话都要"看"窗口里所有的内容。当有用的信息被无关内容淹没时，它找不到重点，表现就下降了。

Tw93算过一笔账：

| 内容 | Token开销 | 特点 |
|------|----------|------|
| 系统指令 | ~2K | 固定，每轮都在 |
| Skill描述 | ~1-5K | 固定，每轮都在 |
| MCP工具定义 | ~10-20K | 固定，每轮都在 |
| CLAUDE.md | ~2-5K | 固定，每轮都在 |
| Memory | ~1-2K | 固定，每轮都在 |
| **真正留给对话的** | **~160-180K** | 动态 |

一个MCP Server就吃掉4,000-6,000 token。连5个 = 25,000 token，光固定开销就占12.5%。

理解了这个成本结构，下面的框架就有了动机。

---

## Tw93的五层Context分层

这是整篇文章的核心。理解了这五层，后面Boris的所有建议都不需要死记——你自己就能推导出来。

Tw93的指导原则只有一句话：**偶尔用的东西就不要每次都加载进来。**

五层从"永远在"到"完全不在"，每一层对context的占用递减，对context的保护递增。

### Layer 1: Always Resident — CLAUDE.md

CLAUDE.md在Claude Code里有特殊地位：**每一轮API调用，Claude都会读它。** 无论你在对话里聊什么、做什么，CLAUDE.md都在那里。

这意味着：
- 2-5K token固定开销——无法避免
- 它是唯一一个你能完全控制、并且每轮都在的用户自定义信息
- 它的质量有**乘法效应**——写得精准，每轮都在给Claude正确方向；写得差，每轮都在注入噪音

什么该放：构建命令、关键目录结构、编码规范、环境陷阱、NEVER list
什么不该放：长篇背景介绍、完整API文档、"write high quality code"之类模糊原则、Claude自己能从代码推断的信息

Tw93的建议很实际："Start with nothing. When you find yourself repeating the same thing, add it."

还有一个关键机制叫**Compact Instructions**。Claude Code在context满时会压缩对话历史。默认的压缩算法会丢掉"可以重新读取"的内容（比如文件内容、工具输出），但也可能丢掉架构决策。你可以在CLAUDE.md里写一段Compact Instructions，明确告诉Claude压缩时什么必须保留、什么可以丢。不写的话，两小时后Claude可能忘了之前做的关键决定。

### Layer 2: Path-loaded — .claude/rules/

这一层的东西**不是一直在的**。它们在你进入特定目录或编辑特定文件类型时自动加载，离开时释放。

例如：TypeScript编码规范只在编辑.ts文件时才需要。如果放在CLAUDE.md里，它每轮都占空间，但90%的时间没用。放在`.claude/rules/ts.md`里，只在需要时才出现。

原则：如果某个规则只适用于特定语言、特定目录或特定文件类型，不要让它常驻CLAUDE.md——放到rules里，让系统按需加载。

### Layer 3: On-demand — Skills / Commands

Skills和Commands的完整内容只在你主动触发时才加载（比如输入`/commit-push-pr`）。用完之后，内容就释放了，不占常驻空间。

但这里有一个容易忽略的细节：**每个启用的Skill的描述文字是常驻的。** Claude需要看到描述才知道什么时候该调用某个Skill。Tw93测量过：

- 一个啰嗦的描述 ~45 token
- 一个精简的描述 ~9 token

单个差异不大，但如果你有10个Skill，差距就是360 token常驻开销。更重要的原则是频率管理：

- 每天用>1次 → 保持auto-invoke，但精简描述
- 每天用<1次 → 关掉auto-invoke，需要时手动触发
- 每月用<1次 → 直接删掉Skill，把内容移进文档

### Layer 4: Isolated — Subagents

Subagent有自己完全独立的context窗口。它做完任务后，只把结论带回主session——过程中产生的所有中间结果（搜索输出、文件内容、分析细节）都留在它自己的context里，不会污染你的主对话。

Tw93特别强调一个关键认知：**Subagent的核心价值是隔离，不是并行。**

一个典型场景：让Claude搜索整个codebase找一个pattern。搜索结果可能有几千行。如果在主session里做，这些结果全部进入context，把之前有用的对话历史挤出去。交给subagent做，主session只收到一段总结。

### Layer 5: Not in Context — Hooks

Hooks完全在context外部执行。**Claude甚至不知道它们在运行。** 当Claude修改了代码，PostToolUse hook可以自动跑格式化——Claude不需要"想"要不要格式化，不需要在context里加载格式化规则，格式化结果也不进入context。

什么适合Hook：阻止编辑受保护文件、自动格式化、SessionStart注入动态context、完成推送通知
什么不适合：需要大量context的语义判断、多步推理决策、长时间运行的业务逻辑

Tw93总结了一个三层协作模型，把Layer 1、3、5串起来：
- **CLAUDE.md** 声明规则："提交前必须通过测试和lint"
- **Skills** 提供方法：告诉Claude测试顺序、如何读failure、如何修复
- **Hooks** 硬执行：在关键路径上做验证，该阻止时阻止

"三层都在才是稳定的setup。缺一层就有gap。"

---

## 超越分层的三个原则

五层分层解决的是"什么信息放在哪"。但还有三个原则不属于某一层，而是影响整体context效率。

### 在context最干净时做最重要的决策

对话越长，context里堆积的内容越多，噪音越多。Plan mode把探索和执行分开——先在read-only状态下反复讨论方案，确认方向后再执行。这样最关键的决策是在context最干净的时候做的。

### 给Claude验证自己工作的方式

Claude Code的核心循环是：收集上下文 → 采取行动 → 验证结果 → 完成或回到收集。瓶颈几乎从来不是模型智能——**而是context错误或无法验证**。

Tw93的判断标准：**如果你说不清"做完长什么样"，这个任务可能不适合让Claude自主完成。**

### 不要打破Prompt Cache

Prompt Cache是Claude Code架构的核心优化，cache hit vs miss的成本差距可达200倍。两个实操影响：
- **不要中途切模型**——cache按模型隔离。用Opus跑了100K token的对话，切到Sonnet，之前的cache全废了。需要换模型时，用Subagent（Layer 4的隔离就是为此设计的）
- **Plan Mode不破坏cache**——它通过Claude调用EnterPlanMode工具实现，工具集不变，所以cache不受影响

---

## Boris的Best Practices——现在它们显而易见了

理解了上面的框架，再来看Boris Cherny的建议。每一条都是对某个层或原则的直接应用：

| Boris的Best Practice | 对应的层/原则 | 为什么有效 |
|---------------------|-------------|-----------|
| 每次纠正后都更新CLAUDE.md | Layer 1 Always Resident | 2-5K token每轮都在，质量有乘法效应 |
| 用slash commands做重复操作 | Layer 3 On-demand | 写进CLAUDE.md=每轮占空间；做成command=用时才加载 |
| 用subagents保持main context focus | Layer 4 Isolated | 大任务输出不污染主session |
| PostToolUse hook自动格式化 | Layer 5 Not in Context | 确定性的事不需要占Claude的注意力 |
| Chrome extension验证前端 | 验证闭环 | 让核心循环的"验证"步骤不再是空的 |
| Plan mode先规划再执行 | context最干净时做决策 | 关键判断在噪音最少时完成 |
| 跑5个并行session | 所有层 | 一个session一件事=每个context保持单一focus |
| 不中途切模型 | Prompt Cache | cache按模型隔离，切模型=cache全废 |

### 几条值得展开的

**CLAUDE.md的乘法效应**：Boris说团队"after every correction, end with: update your CLAUDE.md so you don't make that mistake again"。不是因为怕忘——是因为CLAUDE.md是Layer 1，每轮都在。纠正一次进入CLAUDE.md，等于纠正了之后所有的对话。不进入CLAUDE.md，你可能在下一个session还要纠正同样的事。

**Subagent不是"更多算力"**：Boris说"append 'use subagents' to any request where you want Claude to throw more compute at the problem"。表面看是"更多计算"，但Tw93的框架告诉我们真正的价值是Layer 4的隔离——大量搜索输出和中间结果不进入你的主context。

**Slash command vs CLAUDE.md的界限**：Boris每天用几十次`/commit-push-pr`。为什么不写进CLAUDE.md？因为CLAUDE.md是Layer 1（每轮都在），command是Layer 3（触发才加载）。一个每天用几十次的操作，99%的时间还是不在用的——不应该常驻。

---

## 自检清单

1. **我的CLAUDE.md有没有Compact Instructions？** → 没有的话，压缩时架构决策会丢失
2. **CLAUDE.md里有没有只在特定场景用的规则？** → 移到.claude/rules/（Layer 2）
3. **有几个MCP server常开？** → 每多一个 = 4-6K token常驻开销，不用的关掉
4. **有没有在同一个session里做太多事？** → /clear或开新session
5. **Claude犯的错，是因为能力不够还是看到了错误的信息？** → 大多数时候是后者

---

Tw93把Claude Code使用分成三个阶段：学feature → 用feature → **让agent在约束下自主运行**。Boris的best practices全部属于第三阶段。理解了Tw93的框架，你就有了到达第三阶段的认知基础。

<!-- CTA: [placeholder for closing call-to-action] -->
