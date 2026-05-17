---
type: source-summary
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-aihero-5-agent-skills.md
tags: [wiki, source, claude-code, skills]
---

# Source: AI Hero — 5 Agent Skills I Use Every Day

## Summary
Matt's marketing-tier writeup of the 5-skill workflow. Same content as the mattpocock/skills README but framed for broader audience (less code-focused). Useful as the "elevator pitch" reference.

## 要点解读

### 1. Skills 解决 agent "没有记忆"的根本问题
Agent 每个 session 都是从零开始——你的 coding 偏好、项目结构、过去决策都不记得。Matt 把这些经验编码到 reusable prompts 里——每次启动 skill，agent 就"想起"了所有规则。**这是把 skill 当 institutional memory 的最简实现。**

### 2. /grill-me 的设计来源：Brooks 的 Design Tree
《The Design of Design》by Frederick P. Brooks：每个设计决策都是一棵树，branches 互相依赖。/grill-me 就是 walk through 这棵树，每个 branch 都要回答。一次会话产生 16–50 个澄清问题——这个数量级证明 implementation 之前其实有这么多隐含决策没说清楚。

**对你的启示：**任何非 trivial 的工作（包括写文章），开始前花时间回答 16-50 个问题，比直接动手再返工高效。

### 3. /to-prd 的策略：跳过已完成步骤
PRD 不是模板填空——如果对话里某些部分已经讨论过，skill 会跳过对应的 PRD section，避免重复。**实操：**写自己的 prompt skill 时也要加这种"already-done detection"，否则 agent 会问你已经回答过的问题，用户体验很差。

### 4. /tdd —— Matt 称为"the most consistent way to improve agent outputs"
注意这句话的强度——他用 5 个 skill 但单独点名 /tdd 是改进 agent output 最一致的方法。**为什么：**因为它强制 agent 写下"什么是正确"的可执行定义（test），然后让 agent 自己验证。**对内容工作的类比：**写文章前先写"成功标准"（这篇文章是否回答了 X？是否包含 Y？），写完用 checklist 自检。

### 5. Vertical slice 测试：honest vs deceptive tests
- **Honest test**：通过 public interface 测试 observable behavior —— refactor 不破，行为变才破
- **Deceptive test**：mock 内部、query 数据库 —— behavior 不变也会破

Matt 主张 honest test。**实操：**你的测试如果在 refactor 后大量需要修，就是 deceptive；只在功能变更后需要修的才是 honest。

### 6. "Garbage codebase input yields poor AI output" —— 重申第 5 步的重要性
他在两处文章都强调架构清理。这是 Ralph 时代的核心戒律——**agent 速度越快，codebase 质量对最终质量影响越大**，因为 agent 会快速放大现有 pattern（包括坏的）。

## Connections
- [[mattpocock-skills-library]]
- [[matt-pocock]]
- [[idea-to-afk-agent-flow]]
- Related: [[verification-loops]], [[software-entropy]]

## Source Log
| Date | Action |
|------|--------|
| 2026-05-17 | Initial ingest |
