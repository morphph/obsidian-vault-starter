---
type: source-summary
created: 2026-04-17
last-updated: 2026-04-17
sources:
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
tags: [wiki, source, anthropic, model-release]
---

# Source — Introducing Claude Opus 4.7

## Summary
Anthropic's official announcement of [[claude-opus-4-7]] (published 2026-04-16). Positions 4.7 as the "delegate-without-watching" Opus: better agentic reliability, literal instruction following, self-verification, and the first high-resolution vision in the Claude family. Same price as 4.6.

**URL:** https://www.anthropic.com/news/claude-opus-4-7

## 要点解读

### 1. 核心定位：不是"更聪明的 4.6"，而是"可放心委派的 4.6"
Opus 4.7 的关键卖点不是单纯能力提升，而是**可信度提升**——用户反馈"可以放心把长时间、复杂的编码任务丢给它不用盯着"。背后有两个能力变化：
- **指令遵循更严格**（literal）：字面理解你说的话，而不是"猜你想要什么"。对 prompt engineer 来说，**4.6 时代写得含糊还能跑通的 prompt，在 4.7 上可能偏离预期**，需要重新调参。
- **自验证能力**（self-verification）：模型报告之前会自己检查输出。这呼应了 [[verification-loops]] 的理念——原本需要外部 verification loop 的能力，现在被"内化"到模型本身。

**实操建议**：把 loreai glossary 生成器、blog2video 脚本生成器等关键 prompt 放到 4.7 上重跑一遍对比，看哪些因为"字面化"产生新问题。

### 2. 视觉能力的跃升：2576px / 3.75MP，是过去的 3 倍多
这是**第一个 Claude 高分辨率视觉模型**：
- 长边从 1568px → 2576px
- 总像素从 1.15MP → 3.75MP
- XBOW CEO 报告 visual-acuity benchmark **98.5% vs 4.6 的 54.5%**（数量级跃升，不是百分点）

**为什么重要**：以前让 Claude 读截图、PPT、设计稿经常"看不清细节文字"——那不是理解问题，是分辨率瓶颈。这个瓶颈破了意味着 **computer-use agents、screenshot understanding、document analysis** 三类工作流终于可以进入生产。

**实操建议**：blog2video 如果有"从截图/设计稿生成脚本"环节可以重新评估；小红书内容若要做"读懂竞品截图 → 生成自己内容"工作流，4.7 是拐点。

### 3. 新控制原语 `xhigh` + Task Budgets：成本/效果的细粒度旋钮
4.7 引入两个新旋钮：
- **[[xhigh-effort-level]]**：在 `high` 和 `max` 之间新增一档。官方推荐 agentic coding 用 `xhigh`，日常对话用 `high`。
- **[[task-budgets]]**：给模型一个"整个 agentic loop 大约应该花多少 token"的提示，包括思考、工具调用、结果、最终输出。

**心智模型**：Anthropic 把 [[context-anxiety]] 的解法从 harness 层**下沉到模型层**——模型自己知道"我应该花多深的力气"。过去我们在 Claude Code 里靠外部逻辑管理预算，现在模型原生支持。

**实操建议**：价格不变（$5/$25 per M），但 `xhigh` 会产生更多 thinking tokens，实际账单可能涨。**先小样本测 ROI，再切全量。**

### 4. Claude Code 新增 `/ultrareview`：专用代码审查模式
Claude Code 新增 `/ultrareview`：**专用代码审查会话**，Pro/Max 用户每月赠送 3 次免费 ultrareview。Anthropic 官方把"AI code review"做成一等公民。

**为什么重要**：和 [[verification-loops]]、[[ralph-wiggum]] 形成闭环——Ralph 生成代码 → ultrareview 审查 → 回修。这是官方版的 review 层。

### 5. 安全护栏：Cyber 能力"故意被阉割"（相对 Mythos）
- Anthropic 在 Opus 4.7 **刻意降低了网络安全攻击能力**（相对未发布的 Mythos Preview）
- 自动拦截高风险 cyber 请求
- 合法安全研究者可以申请 **Cyber Verification Program** 解锁

**背后逻辑**：这是 Project Glasswing 的具体落地——前沿模型发布前先做"能力削减"，等安全验证机制跟上再放出完整版。信号：**以后 Anthropic 可能常态化地先发"削减版"再发"完整版"**。

## Key Entities & Concepts Extracted
- Entities: [[claude-opus-4-7]], [[anthropic]], [[claude-code]], [[claude-model-family]]
- Concepts: [[xhigh-effort-level]], [[task-budgets]], [[verification-loops]], [[context-anxiety]], [[assumptions-expire]]

## Connections
- Related: [[claude-opus-4-7]], [[anthropic]], [[claude-model-family]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Initial creation with 要点解读 |
