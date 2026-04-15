# Ralph Autonomous Workflow — Design Q&A Notes

**Source:** Internal conversation (2026-04-15)
**Context:** Designing a plan-to-build autonomous workflow using Ralph Wiggum pattern

---

## Q1: PRD vs Implementation Specs

PRD 和 implementation specs 是不同的东西。Huntley 的原始方法论有明确分层：

| 层级 | 文件 | 是什么 | 谁创建 |
|------|------|--------|--------|
| **Specs** | `specs/*.md` | 详细技术规格 — 描述**要建什么** | 人 + LLM 协作 |
| **Implementation Plan** | `IMPLEMENTATION_PLAN.md` | 任务清单 — LLM 对比 specs 和现有代码后生成的**怎么建** | LLM 生成，人审核 |
| **PRD** (Pocock 用法) | `prd.json` | 把 specs + plan 合并成一个带 `passes` 字段的 TODO 列表 | 混合体 |

Huntley 的方法更严谨：specs 是**不变的需求文档**，implementation plan 是**可丢弃的任务列表**（"The plan is disposable — regeneration costs one planning loop"）。

**更好的做法：**
```
交互式确定需求 → 输出 specs/（详细规格）
                → 输出 implementation-plan.json（任务清单，可丢弃）
Ralph 同时读 specs/ 和 plan，按 plan 执行，参考 specs 理解意图
```

好处：当 Ralph 遇到模糊的任务时，可以回去查 specs 获取上下文，而不是猜。

## Q2: 三层测试标准

这是决定 Ralph 成败的关键。Huntley: "Backpressure over prescription — don't prescribe how, create gates that reject bad work."

### 第一层：项目已有的自动化检查（必须）
```json
"feedback": {
  "typecheck": "npm run typecheck",
  "test": "npm run test",
  "lint": "npm run lint",
  "build": "npm run build"
}
```
硬门槛 — 不过就不能 commit。

### 第二层：任务级别的验收标准（关键）
每个 task 的 `acceptance` 字段必须**可程序化验证**：

```json
// ❌ 差的
"acceptance": ["用户认证功能正常工作"]

// ✅ 好的
"acceptance": [
  "POST /auth/login 返回 JWT token",
  "无效密码返回 401",
  "npm run test -- auth.test.ts 全部通过",
  "migration 文件存在于 db/migrations/"
]
```

Huntley 原则：**"Capture test intent — document WHY tests matter"** — 不只写测试命令，还写为什么重要。未来 iteration 即使没有上下文也知道不能删这个测试。

### 第三层：LLM-as-judge（主观标准）
UI 质量、文案语气等无法用测试覆盖的，用**二元 pass/fail 的 LLM 判断**。

**关键建议：** 如果项目还没有测试基础设施，Ralph 的第一个 phase 应该是**搭建测试基础设施本身** — 否则后续 phase 没有 backpressure，质量无法保证。

## Q3: 任务依赖处理

**两层机制：**

**层级一：Phase 间 — 严格顺序**
Phase 2 不会开始直到 Phase 1 的所有 task 都 `passes: true`。规划时把有依赖关系的工作放在不同 phase：
```
Phase 1: 数据库 schema + ORM models  ← 必须先完成
Phase 2: API endpoints              ← 依赖 Phase 1
Phase 3: 前端 UI                    ← 依赖 Phase 2
```

**层级二：Phase 内 — Agent 自行判断**
同一 Phase 内的 task 理论上不应有强依赖。Agent 通过以下信息判断：
- progress.txt — 前面的 iteration 做了什么
- git log — 代码历史
- 直接读代码 — 理解当前状态

如果 task 之间有依赖：
1. 拆到不同 phase（推荐）
2. 在 task 的 notes 字段里写明依赖关系

## Q4: 执行日志

每个 iteration 结束后 Ralph append 到 `progress.txt`。这是跨 context window 的记忆机制。

关键 prompt 技巧：用 **"append"** 不要用 "update" — 否则 agent 可能覆盖之前的记录。

Ralph Orchestrator 有更高级的日志：
- `.ralph/agent/memories.md` — 持久化学习
- `.ralph/agent/tasks.jsonl` — 结构化任务追踪
- `.ralph/diagnostics/` — JSONL 日志

## Q5: Skill vs Custom Command

| 类型 | 位置 | 区别 |
|------|------|------|
| Custom Command | `.claude/commands/name.md` | 单个 markdown，简单 prompt |
| Skill | `.claude/skills/name/SKILL.md` | 多文件，可有 assets |

调用方式一样（`/name`）。对于 ralph-plan，custom command 就够了。

## Q6: Ralph Orchestrator Worktree 方案

用 `git worktree` 实现同一 repo 上跑多个并行 Ralph 循环：

- **Primary loop** 在主 workspace，持有 `.ralph/loop.lock`
- **Worktree loops** 通过 `git worktree add` 创建隔离副本
- Memories、specs、tasks 通过 symlink 共享
- Worktree loop 完成后排队到 merge-queue
- Primary loop 按顺序处理 merge queue

对 solo builder 来说暂时不需要并行 loop。先用单循环，等熟悉了再考虑。

## Design Decision: Specs + Plan 分离

最终设计采用 Huntley 的分层方式：
1. 交互式规划 → 输出 `specs/` + `implementation-plan.json`
2. Ralph 读两者执行
3. Plan 可丢弃，specs 不变
