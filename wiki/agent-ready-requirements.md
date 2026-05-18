---
type: concept
created: 2026-05-18
last-updated: 2026-05-18
sources:
  - raw/2026-05-17-nurijanian-goal-for-product-managers.md
tags: [wiki, concept, product-management, requirements, agent-design]
---

# Agent-Ready Requirements

## Summary
[[george-nurijanian|George]] 在 [[source-nurijanian-goal-for-pms|/goal for PMs]] 提出的 PM 写需求的新标准：从"够 engineer 理解意图"升级到"够 agent 反复执行 + harness 验证 + 人判定产品正确"。包含 7 个组件 —— observable behavior / negative cases / scope boundaries / validation evidence / stop conditions / status-report expectations / customer-facing success criteria。**核心 framing**：a prompt asks for effort, a contract defines the condition where effort stops.

## Details

### 7 个必备组件

1. **Observable behavior**：用户实际看到/做到的行为（不是抽象状态）
   - ❌ "users should be able to manage notifications more easily"
   - ✅ "users can turn product updates / billing alerts / research reminders on or off independently"

2. **Negative cases**：什么不能发生（往往比 positive case 更重要）
   - 例："users who turn off billing alerts see a warning explaining which emails cannot be disabled for legal or account-security reasons"

3. **Scope boundaries**：哪些文件/系统/逻辑不能动
   - 例："no billing email logic is modified outside the documented preference gate"

4. **Validation evidence**：用什么命令/检查证明完成
   - 例："the notification preferences tests pass / browser smoke test shows persistence after refresh"

5. **Stop conditions**：N turns 或时间上限
   - 例："stop after 20 turns with a status report if any criterion remains blocked"

6. **Status-report expectations**：失败 / 成功时记什么
   - 例："update docs/status-{feature}.md with cause / files changed / validation output"

7. **Customer-facing success criteria**：对最终用户有什么意义
   - 例："default state matches the existing notification behavior for current users"

### 为什么这是范式转变

传统 ticket 写给 engineer 看，依赖**对话补全**模糊处："你看不懂可以问我"。
Agent ticket 写给 unattended loop 看，**没有对话**："agent 看不懂只会按它猜的样子做 40 turns"。

> "A one-shot mistake is annoying. A loop can spend 40 turns making the wrong thing more internally consistent." — George

### Weak vs Strong 对照

| Weak Goal | Strong Goal |
|---|---|
| "improve onboarding" | "implement the new onboarding checklist from docs/onboarding-spec.md. All acceptance criteria pass. npm test -- onboarding exits 0. No files outside paths X are changed. Stop after 20 turns." |
| "make it cleaner" | "Split settings so billing / profile / notification can be tested independently. Each module owns its form state. Existing behavior must not change. Done when each module has its own test file." |
| "polish the onboarding flow" | "After signup, users land on setup checklist. First incomplete step expanded. Completing workspace-profile marks complete without full-page refresh. If API fails, step returns to incomplete with existing toast pattern." |

### 反模式（要主动 grep 自己 spec 找）

| 反模式 | 为什么坏 | 替换 |
|---|---|---|
| 形容词（better / cleaner / easier / smarter） | agent 无从证明 | observable behavior |
| Vibes（"polish the flow"） | 任何 PR 都可以声称"polished" | named product behavior |
| Implementation preference 包装成 product goal（"refactor into cleaner architecture"） | 实际是工程审美而非产品需求 | name the pain the refactor must relieve |

### 适用边界

- ✅ **AFK / unattended agent loops** —— 这是必需，否则烧 token
- ✅ **Long-running specs**（feature 级别） —— ROI 高
- ⚠️ **Interactive sessions** —— 不需要这么严，对话能补全
- ⚠️ **One-off prototyping** —— overhead 太高，weak goal 反而灵活

### 写 agent-ready spec 的 ROI

成本：PM 工作量从写 ticket 增加 2-5×。
收益：
- AFK loop 不在错方向跑 40 turns
- Spec 本身可复用（同类任务下次直接 copy）
- 团队对齐成本下降（spec 自洽不需口头解释）
- agent 输出质量可预测

## Connections
- 出处：[[source-nurijanian-goal-for-pms]]
- 作者：[[george-nurijanian]]
- 对应模板：[[goal-template]]（实操形态）
- 相关命令：[[claude-code-goal]]
- 相关方法论：[[ralph-wiggum]], [[sprint-contracts]], [[grill-with-docs]]
- 工程同源：[[idea-to-afk-agent-flow]] Phase 1（discovery 输出的就是 agent-ready spec）
- 反面案例：[[silent-fallback-antipattern]]（agent 把模糊 spec 填成自己以为的样子）

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-18 | raw/2026-05-17-nurijanian-goal-for-product-managers.md | Initial creation — formalize George's 7-component agent-ready requirements framework |
