---
type: synthesis
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-09-bcherny-claude-code-best-practices.md
  - raw/2026-04-09-tw93-claude-code-architecture-governance.md
tags: [wiki, connection, practice, context]
---

# 为什么Boris的Best Practices有效——用Tw93的框架理解

## Summary
[[boris-cherny|Boris Cherny]]发了三条viral thread教大家怎么用好[[claude-code|Claude Code]]。[[tw93]]写了一篇2.8M views的深度文章拆解Claude Code的底层逻辑。我把两篇放在一起读，发现Boris的每条建议都能用Tw93的框架解释清楚：不只是"这样做更好"，而是"因为系统是这样运作的，所以必须这样做"。

## 先理解一件事：Claude为什么会变笨

用Claude Code久了都会发现：对话刚开始时它很聪明，越往后越不靠谱。大多数人以为是"context太满了，装不下了"。

Tw93纠正了这个认知：

> **Context问题不是容量问题，是噪音问题。**

200K token的窗口其实很大。问题是：Claude每一轮对话都要"看"窗口里所有的内容——系统指令、工具定义、MCP server描述、CLAUDE.md、历史对话、工具输出……当有用的信息被大量无关内容淹没时，Claude就开始找不到重点，表现下降。

Tw93给了一个具体的数字让我非常震撼：

| 内容 | 大概占多少token |
|------|----------------|
| 系统指令 | ~2K |
| Skill描述 | ~1-5K |
| MCP工具定义 | ~10-20K |
| CLAUDE.md | ~2-5K |
| Memory | ~1-2K |
| **真正留给对话的** | **~160-180K** |

一个典型的MCP Server就要吃掉4,000-6,000 token。连5个server = 25,000 token，光固定开销就占了12.5%。这些token**每一轮API调用都在**，无论你用不用它们。

理解了这个成本结构，Boris的建议就不再是"经验之谈"，而是对系统约束的精确回应。

## Tw93的五层Context分层

Tw93的核心框架是：不同类型的信息应该放在不同的"层"里，按需加载，避免所有东西都挤在context窗口里。

| 层 | 机制 | 什么时候在context里 |
|---|------|-------------------|
| **Always resident** | CLAUDE.md | 永远在，每轮都加载 |
| **Path-loaded** | `.claude/rules/` | 进入对应目录/文件类型时自动加载 |
| **On-demand** | Skills / Commands | 用户触发时才加载 |
| **Isolated** | Subagents | 完全独立的context窗口，只返回结果 |
| **Not in context** | Hooks | 不进context，在外部执行 |

从上到下，**对context的占用递减，对context的保护递增**。这个分层的指导原则是Tw93的一句话：

> 偶尔用的东西就不要每次都加载进来。

有了这个框架，我们一条一条看Boris的建议。

## Boris的建议 × Tw93的解释

### 1. "投资CLAUDE.md，每次纠正后都更新"

**Tw93的解释：** CLAUDE.md在"Always resident"层——它是唯一一个每轮API调用都会被Claude看到的用户自定义内容。2-5K token的固定开销，无法避免。

这意味着CLAUDE.md的质量有**乘法效应**：
- 写得精准 → 每轮对话都在给Claude正确的方向
- 写得模糊 → 每轮对话都在注入噪音
- 写得太长 → 真正重要的规则被淹没

Boris说"ruthlessly edit over time until error rates measurably drop"。Tw93给了同样的建议："Start with nothing. When you find yourself repeating the same thing, add it."

Tw93进一步指出CLAUDE.md**不该放什么**：长篇背景介绍、完整API文档、"write high quality code"这种模糊原则、Claude自己能从代码推断的信息。只放**每个session都必须为true的东西**：构建命令、关键目录结构、编码规范、环境陷阱、NEVER list。

**怎么做得更好：** 在CLAUDE.md里加一个"Compact Instructions"section，告诉Claude压缩context时保留什么、可以丢什么。Tw93说默认压缩算法会丢掉架构决策——如果你不主动管理，两小时后Claude就忘了之前的关键决定。

### 2. "用slash commands做重复操作"

**Tw93的解释：** Commands和Skills在"On-demand"层——只有你主动触发时才加载进context。

Boris每天用几十次`/commit-push-pr`。如果把这些指令写进CLAUDE.md，就是把偶尔用的东西放进了"Always resident"层——每轮都在占空间，但大部分时间没用。

Tw93还给了一个Skill descriptor优化的具体建议：每个启用的Skill的描述**都会常驻context**。一个啰嗦的描述~45 token，一个精简的描述~9 token。如果你有10个Skill，差距就是360 token的固定开销差异。数字不大，但原则重要：**每一个常驻item都应该被优化**。

更细的策略：
- 每天用>1次的Skill → 保持auto-invoke，但把描述写精简
- 每天用<1次 → 关掉auto-invoke，需要时手动触发
- 每月<1次 → 直接删掉，放进docs

### 3. "用Subagents保持main context focus"

**Tw93的解释：** Subagents在"Isolated"层——完全独立的context窗口，干完活只把结论带回来。

Boris说"append 'use subagents' to any request where you want Claude to throw more compute at the problem"。但Tw93纠正了一个常见误解：**Subagent的核心价值不是并行，是隔离。**

场景：你让Claude扫描整个codebase找一个pattern。搜索结果可能有几千行。如果在主session里做，这些结果全部进入context，把有用的对话历史挤出去。如果交给subagent做，主session只收到一段总结。

Tw93的反面教材也值得注意：
- 不要给subagent和主线程一样宽的权限（这让隔离失去意义）
- 要规定输出格式（否则主线程无法有效消费结果）
- 不要让子任务之间有强依赖（需要共享中间状态的任务不适合拆分）

### 4. "用Hooks做自动格式化"

**Tw93的解释：** Hooks在"Not in context"层——完全不进入Claude的context窗口，在外部执行。

Boris的PostToolUse hook在每次代码修改后自动格式化。如果让Claude自己来做格式化，它需要在context里加载格式化规则、执行检查、修复问题——这些全都占context空间，而且结果是确定性的（不需要LLM判断）。

Tw93给了一个更完整的框架来判断什么该用Hook：

| 适合Hook | 不适合Hook |
|----------|-----------|
| 阻止编辑受保护文件 | 需要大量context的语义判断 |
| 自动格式化 | 长时间运行的业务流程 |
| SessionStart注入动态context | 多步推理决策 |
| 完成时推送通知 | |

原则：**Hook做确定性的事，Skill做需要判断的事，CLAUDE.md声明规则。** 三层协作才是完整的治理体系。Tw93说"少一层就有gap"。

还有一个实操细节：Hook的输出也要控制长度，用`| head -30`限制，否则Hook输出本身也会污染context。

### 5. "给Claude一种验证自己工作的方式"

**Tw93的解释：** Claude Code的核心循环是 **收集上下文 → 采取行动 → 验证结果 → 完成或回到收集**。瓶颈几乎从来不是模型智能——而是context错误或者无法验证。

Boris说Chrome extension是他最重要的建议。Tw93从架构层面解释了为什么：**如果Claude无法验证自己的输出，核心循环里"验证结果"这一步就是空的**——它只能凭记忆猜测自己做得对不对，然后告诉你"done"。但"Claude saying it's done" is useless。

Tw93给了验证的层次：
- 最基础：exit codes、lint、typecheck、unit test
- 中间层：integration tests、截图对比、contract tests
- 更高层：生产日志验证、monitoring metrics、人工review

以及一个很好的判断标准：**如果你说不清"做完长什么样"，这个任务可能不适合让Claude自主完成。**

Boris的Chrome extension就是中间层的截图验证——让Claude能看到自己写的前端实际渲染出来是什么样，然后迭代。

### 6. "跑5个并行session + Git worktrees"

**Tw93的context框架解释：** 每个session有独立的context窗口。一个session做一件事 = 每个context窗口保持干净和聚焦。把多个任务塞进同一个session = context里混入了不相关的工具输出、文件内容、讨论历史，信噪比快速下降。

Boris的团队还有一个做法值得注意：有人维护专门的analysis worktree跑日志查询和BigQuery分析——这些数据密集型操作会产生大量输出，和常规开发session共用一个context是灾难。

### 7. "Plan mode先规划，然后一次执行"

**Tw93的解释：** Plan mode把探索和执行分开。"For complex refactors, migrations, cross-module changes, this is much better than rushing to code."

从context角度理解：对话越长，context里堆积的内容越多，噪音越多，Claude的判断力越差。Plan mode的价值是**在context最干净的时候做最重要的决策**——方向确认后，执行阶段即使context变杂，Claude也只是在执行已确认的计划，不需要再做高难度判断。

还有一个Tw93提到的prompt cache考量：Plan mode的实现方式是让Claude调用EnterPlanMode工具——而不是切换到只读工具集。因为如果切换工具集，会打破prompt cache，代价很高。Boris可能不知道这个技术细节，但他的用法刚好是cache-friendly的。

### 8. "不要中途切换模型"

这条Boris没有直接说，但Tw93的Prompt Cache分析解释了一个很多人会犯的错误：在同一个session里从Opus切到Sonnet（或反过来），想着省钱。

**实际情况：** Prompt cache是按模型隔离的。你用Opus跑了100K token的对话，切到Sonnet——Sonnet需要从零建立自己的cache，之前Opus的cache全废了。不但没省钱，反而更贵。

正确做法：需要用不同模型时，用Subagent。Subagent有自己的cache，不影响主session的cache。

## 用Tw93的三个阶段检验自己

Tw93把Claude Code的使用分成三个阶段：

1. **"这个功能怎么用"** — 学feature
2. **"学会了功能和pattern"** — 用feature  
3. **"怎么让agent在约束下自主运行"** — 这才是真正的质变

Boris的best practices几乎全部属于第三阶段。如果你看完Boris的tips觉得"有道理但不知道怎么落地"，可能是因为还在第一或第二阶段——先把Tw93文章里的成本结构和分层逻辑理解了，Boris的建议自然就知道怎么做了。

一个自检清单：
1. **我的CLAUDE.md有没有Compact Instructions？** → 如果没有，压缩时架构决策会丢失
2. **我有几个MCP server常开？** → 每多一个 = 4-6K token固定开销，不用的关掉
3. **我是不是在同一个session里做太多事？** → /clear或开新session
4. **Claude犯的错，是因为能力不够还是看到了错误的信息？** → Tw93说"大多数时候是后者"
5. **我有没有在CLAUDE.md里塞了不需要每次都看的东西？** → 移到Skills或Rules里

## Connections
- Related: [[boris-cherny]], [[tw93]], [[claude-code]], [[context-noise-governance]], [[context-management]], [[prompt-cache-optimization]]
- Boris给的是"怎么做"；Tw93解释的是"系统为什么是这样的"。结合起来才能从"照着做"升级到"理解了所以这样做"
- Tw93的三层协作栈（CLAUDE.md + Skills + Hooks）是理解Boris tips分层的最好框架

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-09-bcherny-claude-code-best-practices.md, raw/2026-04-09-tw93-claude-code-architecture-governance.md | Initial creation |
| 2026-04-09 | (same) | Rewrite: removed metaphor, used Tw93's framework directly, added first-person voice |
