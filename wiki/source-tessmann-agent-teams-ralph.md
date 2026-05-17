---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-tessmann-agent-teams-ralph-hybrid.md
tags: [wiki, source, ralph, multi-agent, hybrid]
---

# Source: Meag Tessmann — When Agent Teams Meet the Ralph Wiggum Loop

## Summary
Production case for hybrid architecture: Agent Teams handle creative work (docs, design) in single-shot mode; Ralph loops handle mechanical work (code + tests) in parallel git worktrees. The decision rule: **"machine-verifiable → loop, not verifiable → human."** 10 tasks completed for $15–25 in under an hour with 100% success rate.

## 要点解读

### 1. 两种模式各自的失败模式
- **纯 Agent Teams**：擅长创意决策但 first-attempt 有 error 就需要人介入修，慢且贵
- **纯 Ralph Loop**：擅长机械重复但缺判断力，会自信地把需要人 taste 的任务（UX 文案、API 设计）标记为完成

合并使用：creative track 走人工 review，mechanical track 跑 Ralph loop，互补。**判断标准就一条**：output 能不能机器验证？能 → loop；不能 → 人。

### 2. Shared Contracts 模式 —— 解决并行 agent 命名不一致
最重要的工程创新。问题：parallel agents 给同一个组件起了不同的 test ID（`inline-quick-add` vs `quick-add-inline`），下游 test 找不到。解决：**planner 在工作开始前先生成 Shared Contracts 表格**，列出每个组件的 test ID 和使用它的 agent。所有下游 agent 必须严格使用这些 ID。

三条强制规则：
1. 只有 planner 能定义 contracts
2. 每个 test 引用的 ID 必须出现在 contracts 里
3. 只为真实存在的元素定义 ID

**实操建议：**任何 multi-agent 协作（包括你和你自己的不同会话）都需要这种 contract。写下来，强制遵守。

### 3. 不可靠任务用 bash 兜底
经验：agents 能可靠地写代码、读 error，但不可靠地做"机械维护"（如 git commit）。Tessmann 试了 3 次 prompt engineering 让 agent 自己 commit 都失败，最后用 4 行 bash 包住搞定。

**原则：**"Know what the model is reliable at and what it isn't. Use bash for the latter."

**实操：**写 AFK loop 时，agent 完成 implementation 后立即用 bash 脚本 stage + commit，不要依赖 agent 自己 commit。

### 4. Prompt 格式：显式否定 > 叙述性
- 失败：`if everything passes, mark complete` —— agent 有太多解释空间
- 成功：`Do NOT mark [x] unless BOTH commands exit with code 0` —— 难以忽略

**为什么：**叙述性 prompt 给 agent 解读余地，agent 会找 loophole；显式否定是布尔条件，无歧义。**实操：**任何关键判断都写成"Do NOT X unless Y AND Z"格式。

### 5. 实测成本数据（少见且珍贵）
- Model: Claude Sonnet（便宜的选择）
- 10 tasks / 3 worktrees / 3-4 iterations each
- 每 iteration: $1-2
- 总 run cost: $15-25
- Wall clock: <1 小时
- 成功率: 10/10

**给个人开发者的参考：**一个完整 feature（10 个 sub-task）大约 $25、1 小时。这是 AFK pipeline 的 unit economics 锚点。

### 6. 两个未解决的问题
- **Agents 互相不感知**——纯结构化协调对清晰可分解的 feature 有效，需要实时协商的场景失效
- **判断边界目前是二元的**（autonomous vs human review）——有些工作中途需要偶尔的 taste 决策，没有干净的"agent 请求人帮忙"模式

这两个问题是当前 multi-agent + Ralph 混合架构的边界。

## Connections
- [[ralph-wiggum]], [[multi-agent-architecture]]
- [[shared-contracts-pattern]] (new concept)
- [[sprint-contracts]] (close cousin)
- [[llm-judgment-vs-scripts]] (machine-verifiable cut)
- [[idea-to-afk-agent-flow]] (advanced pattern for Phase 5)

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial ingest |
