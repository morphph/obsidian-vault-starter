---
type: source-summary
created: 2026-05-20
last-updated: 2026-05-20
sources:
  - raw/2025-10-07-openai-cookbook-plans-md-multi-hour.md
tags: [wiki, source, openai, codex, cookbook, plans-md, agents-md, long-horizon, durable-memory]
---

# Source: OpenAI Cookbook — Using PLANS.md for Multi-Hour Problem Solving

## Summary
OpenAI Cookbook article from **2025-10-07** — predates the May 2026 long-horizon cookbook trilogy by 7 months. Introduces **AGENTS.md + PLANS.md (ExecPlan)** as a two-file durable-memory pattern that has powered "more than seven hours from a single prompt" runs. **Significance for long-horizon writing: this is the chronologically 2nd independent reinvention of the durable-files pattern (after Ralph Wiggum, before Matt Pocock's CONTEXT.md, before OpenAI's own May 2026 Prompt+Plan+Implement triad).** Demonstrates that single-file ExecPlan is a viable alternative to triad split — same pattern, different decomposition.

## Source Metadata
- **URL:** https://developers.openai.com/cookbook/articles/codex_exec_plans (redirected from cookbook.openai.com)
- **Publisher:** OpenAI Developers Cookbook
- **Publish date:** 2025-10-07
- **Fetch date:** 2026-05-20

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息
- **作者**：OpenAI Developers Cookbook（未具名工程师，官方）
- **来源**：cookbook.openai.com（现重定向到 developers.openai.com/cookbook）
- **时间**：**2025-10-07** —— 比 May 2026 trilogy 早 7 个月
- **战略意义**：这是 OpenAI 最早把"长跑能力 + durable file"提到官方文档级别的内容。**Codex 长跑叙事的起点**

### 2. 核心论点（Thesis）
OpenAI 主张：让 agent 跑数小时不漂移的关键，**不是更聪明的模型，是 fully self-contained 的 living document**。**因为** agent 跨多 turn 后会丢失对话上下文，**所以** 把所有"我在建什么 + 我做到哪 + 我为什么选这条路"全部 inline 到一个 plan 文件里，每个 turn reload。

简化压缩包：**"PLAN.md 是 agent 的 SOP + 进度册 + 决策日志合一。"**

### 3. 论证结构
```
1. AGENTS.md 注入 trigger 词（"ExecPlan"）
   → 这是 vocabulary-as-trigger pattern
2. PLANS.md 的 5 个 non-negotiable 标准
   → self-containment / living / novice-enable / demonstrable / plain
3. 7 个 required section
   → Purpose / Progress / Surprises / Decisions / Outcomes / Steps / Validation
4. 行为驱动验收 ("localhost:8080/health returns 200")
   → 而非 spec-matching ("function returns 200")
5. 7 小时单 prompt 完成的 case
   → 证明 pattern 有效
```

### 4. 关键概念字典

> **ExecPlan（执行计划，作为 vocabulary trigger）**
> - **是什么**：一个由 AGENTS.md 定义的 shorthand 词，触发"用 PLANS.md 模板做完整设计"协议
> - **为什么重要**：揭示一种 *trigger-by-vocabulary* 模式 —— 不直接在 prompt 里 hardcode 整套流程，而是让 AGENTS.md 把流程绑到一个词上，需要时只 say "ExecPlan" 即可
> - **直觉类比**：像编程语言里的宏 —— 写 `LOG_ERROR(x)` 比每次手写 try/except 短得多
> - **适用场景**：复杂 feature / 重大重构
> - **反面/失败模式**：trigger 词被滥用在简单任务上 → setup cost 浪费

> **Self-containment（完全自包含）**
> - **是什么**：PLAN 里必须包含所有完成任务需要的知识 —— "一个完全的新手"能照着做完
> - **为什么重要**：解决 "agent 在 hour 5 想 reference 一个 hour 1 提到但没记的事实" 的问题
> - **直觉类比**：像 IKEA 说明书 —— 不假设你看过家具学院的课
> - **适用场景**：所有长跑任务
> - **反面**：plan 里写 "see X meeting notes" / "ask Y for details" → agent 卡死

> **Living document（活文档）**
> - **是什么**：plan 不是写完冻结，而是边跑边更新 Progress / Surprises / Decisions
> - **为什么重要**：是 vs Anthropic Prompt.md (FROZEN) 的核心差异 —— **single-file 模式必须 living，否则就放不下决策日志**
> - **直觉类比**：像项目经理的 working draft —— 一直在改但永远是 source of truth
> - **反面**：完全冻结 → 决策无处记录 → agent 重复犯错

> **Behavior-focused validation（行为驱动验收）**
> - **是什么**：每个 milestone 的验收条件是 *user-visible 可观察行为*，而非"代码 match spec"
> - **为什么重要**：让 agent 没法"满足 spec 但产品错"（silent fallback antipattern）
> - **关键例子**：`"after starting the server, navigating to localhost:8080/health returns HTTP 200"` 而不是 `"function health_check() returns 200"`
> - **适用场景**：所有有 user-visible 结果的任务

### 5. 框架与心智模型

**ExecPlan 7 section 模板**：

```
1. Purpose / Big Picture     - user-visible outcomes + verification
2. Progress                  - timestamped checkpoint list (Markdown checklist OK here)
3. Surprises & Discoveries   - unexpected findings + evidence
4. Decision Log              - rationale for choices
5. Outcomes & Retrospective  - achievements + lessons
6. Concrete Steps            - exact commands + expected output
7. Validation & Acceptance   - observable behavior verification
```

**Single-file vs Triad 决策**：

| 因素 | Single ExecPlan | Triad (Prompt+Plan+Implement) |
|---|---|---|
| Setup 成本 | 低（一个文件）| 中（3 个文件 + 互相 reference）|
| 角色分离强制度 | 弱（Decisions / Surprises 混在一起）| 强（FROZEN spec / 可变 plan / 行为手册）|
| Spec 保护 | 必须靠纪律或 hook | FROZEN flag + hook 双层 |
| 适合 | 单人独立项目 / 探索 | 团队 / 高 stake / 长生命周期 |

### 6. 关键数据与例证
- **5** 个 non-negotiable PLAN.md 标准
- **7** 个 required section
- **7+ 小时** 单 prompt 工作 record
- **2 个文件**（AGENTS.md + PLANS.md）

### 7. 关键引语

> **"The particular PLANS.md included below is very similar to one that has enabled Codex to work for more than seven hours from a single prompt."**
> ⭐ 7 小时单 prompt 是 OpenAI 给的长跑 ROI 实证 —— 比 May 2026 trilogy 的"stays coherent longer"更具体。

> **"When writing complex features or significant refactors, use an ExecPlan (as described in .agent/PLANS.md) from design to implementation."**
> ⭐ AGENTS.md 触发条款的模板。

> **"Milestones function as narrative units, not bureaucratic checkpoints."**
> ⭐ Milestone 设计哲学一句话 —— 反对"打卡式"分解。

### 8. 实操指南

**Minimal setup**：

`AGENTS.md`（仓库根）：
```markdown
## Working Agreement

When writing complex features or significant refactors,
use an ExecPlan (as described in .agent/PLANS.md) from
design to implementation.

The plan must be self-contained — a novice should be able
to follow it end-to-end without prior knowledge.
```

`.agent/PLANS.md`（仓库子目录）：
```markdown
# ExecPlan: <Feature Name>

## Purpose / Big Picture
[User-visible outcome + how to verify]

## Progress
- [ ] Milestone 1: <name>
- [ ] Milestone 2: <name>

## Concrete Steps
### Milestone 1
1. Run `<command>`
2. Expected output: `<text>`

## Validation & Acceptance
After milestone 1, verify:
- `<observable behavior 1>`
- `<observable behavior 2>`

## Surprises & Discoveries
(filled by agent during run)

## Decision Log
(filled by agent during run)

## Outcomes & Retrospective
(filled at end)
```

### 9. 对比与反对意见

**vs OpenAI 自家 May 2026 Prompt+Plan+Implement triad**：
- PLANS.md = 单文件 living document
- Triad = 三文件 + FROZEN spec
- **两者都是 OpenAI 官方** —— **不矛盾，是同一 pattern 的不同 decomposition**
- 选择依据：复杂度 / 团队规模 / FROZEN 需求

**vs Ralph Wiggum（2025-07）**：
- Ralph 用 `PRD.md` + `progress.txt` + `AGENTS.md` —— 三文件
- PLANS.md 把 PRD + progress 合并成单 ExecPlan，AGENTS.md 仅做 trigger
- **概念家族同源**

**vs Matt Pocock CONTEXT.md（2026-04）**：
- Matt 的 CONTEXT.md 是 *glossary*（领域词汇 + ADR），不是 plan
- PLAN.md 是 *executable spec*
- **职责不同**，可以同时存在（CONTEXT.md 在仓库根，PLAN.md 在 feature 目录）

### 10. 与 wiki 知识的连接

**强连接**：
- [[source-openai-codex-cookbook-trilogy]] —— 2026-05 的 successor，更 formal
- [[source-openai-long-horizon-tasks-codex]] —— 2026-05 blog 推 Prompt+Plan+Implement triad
- [[ralph-wiggum]] —— 时间上 PLANS.md (2025-10) 在 Ralph 后 3 个月
- [[idea-to-afk-agent-flow]] —— Matt 的 CONTEXT.md 是 glossary，PLAN.md 是 plan，两者 complementary
- [[grill-with-docs]] —— grill 输出可以作为 PLAN.md 的 Purpose section

**强化已有概念**：
- 强化 [[agentic-loop-tracking-files]] —— durable-files 模式的第 2 个独立来源（chronologically）

**新发现**：
- 修订 wiki 里关于"三独立来源"的说法 —— **应该是四独立来源**：Ralph (2025-07) → PLANS.md (2025-10) → CONTEXT.md (2026-04) → triad (2026-05)

### 11. 对用户（vfan）的启示

#### 短期
- **更新 pm-long-horizon-methodology.md** Part 1 转换 2 的"三独立来源"表格，**加入 PLANS.md 作为第 2 行**
- 时间线变得更有说服力（4 个独立发明，跨越 10 个月）

#### 中期
- 写 blog2video chapter splitter 时，**single-file ExecPlan** 可能比 triad 更轻 —— 试一次再对比

#### 长期
- "PM 长跑：single-file 还是 triad？" 是一个独立的中文短文角度，**可以基于这个 source 写**

### 12. 一句话总结

**"PLANS.md（2025-10）是 OpenAI 长跑叙事起点；单文件 ExecPlan 是三文件 triad 的轻量替代。Durable-files pattern 至少有 4 个独立来源。"**

---

## Connections
- Related: [[source-openai-codex-cookbook-trilogy]], [[source-openai-long-horizon-tasks-codex]], [[ralph-wiggum]], [[idea-to-afk-agent-flow]], [[grill-with-docs]], [[agentic-loop-tracking-files]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-20 | raw/2025-10-07-openai-cookbook-plans-md-multi-hour.md | Initial creation — PLANS.md as 2nd independent reinvention of durable-files |
