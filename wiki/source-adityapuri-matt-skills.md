---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
tags: [wiki, source, claude-code, skills, third-party-walkthrough]
---

# Source: Aditya Puri — Matt Pocock's 5 Claude Code Skills Made Me Rewrite How I Work With AI Agents

## Summary
Third-party walkthrough of Matt's 5 skills in practice. Most valuable additions: the **HITL/AFK label per issue** pattern from `/to-issues`, and the **vertical slicing** unit-of-work definition.

## 要点解读

### 1. 心态转变：把 agent 当成"被约束的初级工程师"
作者最初摇摆于两个极端：全权委托（出来一坨没法 review 的复杂代码）vs 不委托（自己累死）。Matt 的 skills 给出了第三条路——**把 agent 当成有约束的 junior engineer**：你给它清晰的 spec（PRD）、明确的 task 切片（vertical slice）、强制的反馈循环（TDD）、定期的代码 review（architecture skill），然后才放手让它工作。

**给你的启示：**不要用"用 vs 不用 AI"的二元思维，用"什么约束下用 AI"的工程思维。

### 2. /to-issues 的 HITL/AFK 标签 —— Ralph 流程的入口分类器
每个 issue 被打上：
- **HITL（Human-in-the-loop）**：需要人决策（架构、UX、有 risk 的变更）
- **AFK（Away from keyboard）**：agent 可以自主执行（well-scoped 的实现、refactor、tests）

**这是缺失的拼图：**Ralph 文章都讲怎么跑 loop，但什么任务能进 loop？答案就是被打上 AFK 标签的那批。**实操建议：**你的 backlog 应该一开始就分类，未分类的 issue 不进 Ralph loop。

### 3. Vertical slicing —— 任务切片单位
不要按层切（先写所有 schema，再写所有 API，再写所有 UI），按 **vertical slice** 切：每个 issue 是一个"穿透所有层的薄片"（schema + API + UI + tests）。

**为什么：**
- vertical slice 是独立可 ship 的，每个完成都有用
- 暴露未知问题更快（端到端 demo 比纯后端先验证假设）
- 多 agent 可以并行做不同 slice，互不阻塞

**对内容创作者也适用：**写文章别按"先写所有大纲、再写所有正文、再校对所有"——按"完成一个完整章节（含 hook + 论证 + 结尾）"切片。

### 4. Deep modules（来自 John Ousterhout）—— /to-prd 的隐含原则
PRD 里要识别 **deep modules**：简单接口隐藏复杂实现。**反面：**shallow modules（接口和实现一样复杂，等于没封装）。

**实操判断：**写完一个模块问自己——这个接口的复杂度比实现的复杂度低很多吗？是 → deep；差不多 → shallow，需要重构。

### 5. Deletion test —— /improve-codebase-architecture 的判定方法
对每个模块问："如果删掉它，多少复杂度消失？" 复杂度消失多 = 模块有价值；消失少 = shallow module 应该被合并或重构。

**为什么有用：**比 "代码质量"这种模糊概念更操作化。**实操：**每周对你的 codebase 跑一遍这个测试。

### 6. 闭环的关键：第 5 步不能跳
5 个 skill 是个 closed loop：plan → spec → slice → implement → architecture → (back to plan)。**跳过第 5 步**（architecture cleanup），整条流水线就退化成"快速产出垃圾"——agent 输出质量会单调下降。

**给你的提醒：**用 AI 做内容也一样——快速产出文章后，每周必须有一次"反思 + 整理 + 文档化经验"，否则会陷入"产出多但成长慢"。

## Connections
- [[mattpocock-skills-library]]
- [[hitl-vs-afk-classification]] (new)
- [[vertical-slicing]] (new)
- [[idea-to-afk-agent-flow]]

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial ingest |
