---
type: source-summary
created: 2026-05-18
last-updated: 2026-05-18
sources:
  - raw/2026-05-05-openai-blog-long-horizon-tasks-codex.md
tags: [wiki, source, openai, codex, long-horizon, durable-memory]
---

# Source: OpenAI Blog — Run long-horizon tasks with Codex

## Summary
OpenAI 官方博客（约 2026-05-05 发布）。**不讲 /goal 命令，讲 long-horizon coherence 这个底层能力**。给出 **Prompt.md / Plan.md / Implement.md** 三文件 durable memory 模式 —— 跟 [[source-chrishayduk-codex-goals-effectively|Chris Hayduk]] 的 PLAN/EXPERIMENTS/SCRATCHPAD 模式是 convergent 的不同表达。核心信号：OpenAI 把"长跑能力"从"/goal 命令"分离讲，暗示 /goal 只是这个能力的一个 UX。

## Source Metadata
- **URL:** https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- **Author:** OpenAI Developers (official blog)
- **Estimated publish:** ~2026-05-05
- **Fetch date:** 2026-05-18
- **Fetch method:** WebFetch

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
- **作者**：OpenAI Developers（官方博客 channel，非具名工程师）
- **来源**：OpenAI Developers Blog
- **影响力指标**：无显示数据（官方 blog 不公开 view count）
- **在 OpenAI 输出中的位置**：是 2026 年 Codex 长跑能力推广的 **awareness-tier** 内容 —— 跟 cookbook（教学）和 use-case docs（操作）形成 3-tier 产品 marketing 矩阵

### 2. 核心论点（Thesis）
**OpenAI 主张**：Codex 2026 真正的改变不是新命令、不是更聪明的模型，**是 time horizon —— agent 能在长时间里保持 coherence**，端到端完成更大块工作、出错能恢复不丢线索。**因为**长跑能力是底层能力（不是 /goal 命令本身），**所以**真正的实操关键是"怎么让 agent 在小时-到-天的尺度上不漂移" —— 答案是 durable memory 模式（三 markdown 文件）。

简化压缩包：**"长跑能力是真正的进步；/goal 只是这个能力的一个 UX；durable memory 模式（freeze the target + plan + runbook）才是核心。"**

### 3. 论证结构
```
1. Reframe（颠覆"新命令"叙事）
   → 真正的变化是 time horizon，不是命令名字
2. 描述 agent loop（标准 TAO）
   → plan / edit / run / observe / repair / document
3. 关键创新（durable memory pattern）
   → 三个 markdown 文件，每个有明确角色
4. 验证纪律（per-milestone gates）
   → lint / typecheck / tests / build 必须 pass 才能推进
```

骨架很短但很有力 —— 4 步建立了"为什么这个 capability 重要 + 怎么真正用上"的完整闭环。

### 4. 关键概念字典

> **Time Horizon as the Real Capability（time horizon 作为真正的能力）**
> - **是什么**：agent 能在长时间（hours-to-days）里保持 task coherence，不掉线索、不漂移、不退化
> - **为什么重要**：是文章的核心 reframe。把读者从"哪个命令更新"的注意力，拉到"什么 capability 让这一切成为可能"
> - **直觉类比**：跟"内存大小"vs"具体软件"的关系一样 —— 内存大才能跑大软件；time horizon 长才能跑长任务。命令是软件，capability 是内存
> - **适用场景**：评估任何"AI 长跑"功能时
> - **反面/失败模式**：只看命令名字 → 错过底层能力的进步含义

> **Prompt.md（规格 + 交付物）**
> - **是什么**：冻结目标 spec 的文件。agent 每轮 reload 它，作为"我在建什么"的 source of truth
> - **为什么重要**：解决 "agent 在 hour 50 时偏离原始目标"的核心问题。**冻结的 target 比对话里漂浮的意图稳定 100×**
> - **直觉类比**：像建筑师的 blueprint —— 工人每天回来看 blueprint，不是问业主"你今天想加什么"
> - **适用场景**：任何 > 30 分钟的 agent 跑
> - **反面/失败模式**：让 agent 自己修改 Prompt.md → goal drift 几乎必然发生

> **Plan.md（milestone checkpoints）**
> - **是什么**：把工作分解成 milestone，每个 milestone 有自己的 validation criteria
> - **为什么重要**：milestone-level validation 是 sweet spot —— 比 per-turn 太频繁，比 per-session 太迟
> - **直觉类比**：像建筑工程进度表 —— "地基完了验收一次，再做主体；主体完了再验收，再做装修"，不是每砌一块砖验收一次
> - **适用场景**：任何复杂多步骤任务
> - **反面/失败模式**：milestone 太大（一周一个）→ 偏离后回不来；太小（每个函数一个）→ 每次都在验证

> **Implement.md（execution runbook）**
> - **是什么**：agent 操作行为手册 —— 用什么工具、怎么记录进度、什么时候 stop
> - **为什么重要**：把"agent 怎么工作"从"agent 在建什么"分离 —— 这两件事独立 evolve
> - **直觉类比**：像 SOP 文件 vs 项目规格 —— 一个是"工作流程"，一个是"工作产品"，两者不该混
> - **适用场景**：定义 agent 在你 codebase 里的"行为标准"
> - **反面/失败模式**：把 implementation 细节塞进 Prompt.md → 修 runbook 时改到了 spec

### 5. 框架与心智模型

**核心框架：Durable Memory Triad（持久记忆三角）**

```
Prompt.md（what you're building）— 冻结
    +
Plan.md（when / order / checkpoints）— 可演进但有 milestone gate
    +
Implement.md（how the agent operates）— 行为手册
```

**怎么套用（举例：blog2video chapter generator）**：

- **Prompt.md**：定义 chapter generator 的输出规格（每个 chapter 30-60s / 三段结构 / CTA 结尾）+ 接受标准。冻结。
- **Plan.md**：milestone = "生成 5 个 chapter 通过 lint + 人工抽查 3 个论点完整 + 总时长 ≤ 文章 1/3"
- **Implement.md**：用什么工具（read article from raw/，write to docs/output/）、怎么记录（更新 status-chapters.md）、什么时候 stop（5 个 chapter 全过后 emit COMPLETE）

### 6. 关键数据与例证
**无量化数据**。文章是 narrative-style 宣告（"agents can stay coherent for longer"），不给 benchmark / view count / case study。这是 OpenAI 官方博客的标准风格 —— 战略叙事 > 数据点。

**这是文章的弱点**：没有"long-horizon ROI 是多少"的具体数。你要做案例研究的话，正好是空白。

### 7. 关键引语

> **"The practical change is that agents can stay coherent for longer, complete larger chunks of work end-to-end, and recover from errors without losing the thread."**
> 实践层的真正改变是：agent 能在长时间里保持 coherence，端到端完成更大块工作，出错能恢复而不丢线索。
> ⭐ 文章 thesis 一句话版。

> **"Freeze the target so the agent doesn't build something impressive but wrong."**
> 冻结目标，让 agent 不至于建出一个"impressive 但 wrong"的东西。
> ⭐ Prompt.md 设计哲学的最强一句。可作为博客标题或推文金句。

### 8. 实操指南

**Triad 建设 checklist**：
- [ ] 写 **Prompt.md**（spec + 交付物 + 接受标准）—— 写完 commit + 标记 "FROZEN"
- [ ] 写 **Plan.md**（按 milestone 分解 + 每个 milestone 的验证标准）
- [ ] 写 **Implement.md**（工具 + 记录格式 + stop 条件）
- [ ] 每个 milestone 都设 validation gate（lint / typecheck / tests / build）
- [ ] 跑长任务前先**人工 review**这三个文件 —— 任何模糊处 agent 都会按它自己的理解填

**Milestone validation gate 模板**：
```
Milestone X complete when:
- npm run lint exits 0
- npm run typecheck exits 0
- npm test -- <relevant scope> exits 0
- npm run build exits 0
ONLY THEN proceed to Milestone X+1
```

### 9. 对比与反对意见

| 对比对象 | 作者立场 | 隐含信念 |
|---|---|---|
| **vs "agents got smarter"** | 反对（at least implicitly）| 是 capability，不是 intelligence；不是 model magic |
| **vs Chris Hayduk 三文件（PLAN/EXPERIMENTS/SCRATCHPAD）** | 不冲突，是 alternative decomposition | 三文件结构是 universal，命名是 personal |
| **vs 让 agent 修改 Prompt.md** | 强烈反对（"Freeze the target"）| Spec drift 是长跑致命问题 |
| **vs per-turn validation** | 反对（implicit）| Per-milestone validation 是 sweet spot |

**作者隐含承认的限制**：
- 没量化 ROI —— "stays coherent longer" 没有数字支撑
- 没说哪些任务**不适合**长跑 —— 文章只讲适合的
- 没说 milestone 怎么定大小 —— "milestone" 太大太小都坏，没指导
- 没讨论 verification 失败时怎么 recover（"recover from errors without losing the thread" 怎么实现没说）

### 10. 与 wiki 知识的连接

**强连接**：
- [[claude-code-goal]] — Claude Code 同款长跑能力的产品 UX
- [[source-openai-codex-cookbook-trilogy]] — OpenAI 自家的 /goal cookbook，本文是 cookbook 的前置 awareness 内容
- [[source-chrishayduk-codex-goals-effectively]] — Chris Hayduk 的 PLAN/EXPERIMENTS/SCRATCHPAD 模式，跟本文 Prompt/Plan/Implement 是 convergent
- [[source-nurijanian-goal-for-pms]] — George 的 "spec as product surface" 跟本文 "freeze the target" 同源
- [[agentic-loop-tracking-files]] — wiki 已有的 durable memory 概念页

**强化已有概念**：
- 强化 [[agentic-loop-tracking-files]]：又一种三文件命名方案，证明 pattern 是 universal
- 强化 [[ralph-wiggum]]："fresh context + durable files" 是 Ralph 核心，本文官方背书

**与新 wiki 的关系**：
- [[idea-to-afk-agent-flow]] —— Matt Pocock 的 Phase 1（grill-with-docs + CONTEXT.md）就是 Prompt.md 的兄弟实现
- [[sandcastle]] —— Sandcastle 的 `promptFile` 参数 + completion signal 完全适配 Prompt.md/Plan.md 模式
- [[context-md-pattern]] —— Matt 的 CONTEXT.md "glossary only" 比 Prompt.md 更窄；Prompt.md 是 spec，不是 glossary

**扩展方向**：
- 没 reference 其他源；自包含官方内容
- 如果想深挖 milestone 设计，可以 ingest 关于 "Definition of Done" / "Acceptance criteria patterns" 的产品管理经典内容

### 11. 对用户（vfan）的启示

#### 短期（本周）
- 如果你要跑 blog2video chapter generator，**先建 Triad 文件**（Prompt / Plan / Implement），别直接 /goal
- 写完后人工 review **每一句**，找 ambiguity —— agent 会把模糊处填成自己的猜测

#### 中期（接下来 2-4 周）
- 建立 Triad templates，每类 AFK 任务都用同样三文件结构
- 把 Triad 和 George 的 6-section /goal template 配套使用：Triad 是"项目级 spec"，/goal template 是"这次 run 的具体目标"

#### 长期
- "Long-horizon 跨 vendor convergence" 是写作角度：Claude / OpenAI / community 都在 4 周内独立收敛到同样的 pattern，可以作为博客文章的有力论据

### 12. 一句话总结

**"真正的进步不是更聪明的模型，是更长的 coherence；冻结目标 + plan + runbook 是让长跑不漂移的三文件铁律。"**

---

## Connections
- Related: [[claude-code-goal]], [[source-openai-codex-cookbook-trilogy]], [[source-chrishayduk-codex-goals-effectively]], [[agentic-loop-tracking-files]], [[ralph-wiggum]], [[idea-to-afk-agent-flow]], [[context-md-pattern]], [[sprint-contracts]], [[source-nurijanian-goal-for-pms]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-18 | raw/2026-05-05-openai-blog-long-horizon-tasks-codex.md | Initial creation — OpenAI's long-horizon thesis + Prompt/Plan/Implement triad |
