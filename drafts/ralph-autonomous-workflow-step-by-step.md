---
status: draft
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
  - raw/2026-04-15-ghuntley-ralph-wiggum-original.md
  - raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md
  - raw/2026-04-15-anthropic-ralph-wiggum-plugin.md
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
  - raw/2026-04-15-aihero-getting-started-with-ralph.md
  - raw/2026-04-15-repo-ralph-orchestrator.md
  - raw/2026-04-15-ralph-workflow-design-qa.md
platform: blog
created: 2026-04-15
last-updated: 2026-04-15
tags: [draft]
---

<!-- HOOK: 你可以和 AI 一起设计方案，然后让它自己去建。不是一次一个 prompt，是一个循环跑到底。这篇是从规划到自主执行的完整 step-by-step。 -->

# 从规划到自动执行：用 Ralph Wiggum 实现 Plan → Build 自主开发流

大多数人用 AI 编程工具是这样的：给它一个任务，看它做，做错了纠正，做完了再给下一个。全程盯着。

但有一种方式可以让你：和 AI 一起把方案敲定，然后让它自己去执行整个实现计划 — 你去做别的事，回来看 commit。

这就是 Ralph Wiggum 工作流的核心：**Plan 阶段人机协作，Build 阶段 AI 自主循环。**

本文不是 Ralph 入门 — 如果你还不了解 Ralph 是什么，先看 [Ralph Wiggum 完全指南]。本文专注于一个具体问题：**怎样设计从交互式规划到自主执行的完整流程。**

---

## 整体流程

```
┌─────────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│  Phase 0: 规划      │    │  Phase 0.5: 导出  │    │  Phase 1~N: 执行    │
│  你 + Claude Code   │ →  │  /ralph-plan      │ →  │  ralph.sh (AFK)     │
│  交互式，plan mode  │    │  生成 specs/ +    │    │  Docker sandbox     │
│  直到方案满意       │    │  plan.json        │    │  每次 fresh context │
└─────────────────────┘    └──────────────────┘    └─────────────────────┘
        HITL                    自动化                     AFK
```

关键原则：**规划的质量决定执行的质量。** Geoffrey Huntley（Ralph 发明者）的经验："specification quality = output quality"。不要急着跳到执行 — 把 specs 写扎实。

---

## Step 0: 前置条件

### 安装

```bash
# Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Docker Desktop 4.50+（AFK 执行必须）
# 从 docker.com 下载安装

# 验证 sandbox 可用
docker sandbox run claude --version
```

### 项目文件结构

在你的项目里准备这些：

```
your-project/
├── specs/              ← 技术规格（人 + AI 协作产出，不变）
├── plan.json           ← 实现计划（AI 生成，可丢弃可重建）
├── progress.txt        ← 执行日志（每次 iteration 追加）
├── ralph.sh            ← AFK 循环脚本
├── ralph-once.sh       ← HITL 单次执行脚本
└── .claude/
    └── commands/
        └── ralph-plan.md  ← 导出命令
```

---

## Step 1: 交互式规划（HITL）

启动 Claude Code，进入 plan mode（`shift-tab`），和 AI 一起设计方案。

这个阶段的目标不是写代码 — 是**对齐意图**：

- 你要建什么？为什么？
- 分哪几个阶段？每个阶段的边界是什么？
- 有什么技术约束？（框架、数据库、已有代码）
- 什么是"完成"？怎么验证？

**不要急。** 这是整个流程中人类价值最高的环节。Huntley 的原则："Steer with signals, not scripts" — 你在这里定义信号，Ralph 在后面执行。

### Specs vs Implementation Plan — 它们不是一回事

很多人把 PRD 和实现计划混在一起。Huntley 的方法论明确分层：

| 文档 | 是什么 | 生命周期 | 谁写 |
|------|--------|----------|------|
| `specs/*.md` | 技术规格 — **要建什么** | 不变（除非需求变） | 人 + AI 协作 |
| `plan.json` | 任务清单 — **怎么建** | 可丢弃，随时重建 | AI 生成，人审核 |

Specs 是需求文档：功能描述、API 设计、数据模型、边界条件。Implementation plan 是执行路径：分几个 phase，每个 phase 有哪些 task。

**为什么要分开？** 当 Ralph 在执行过程中遇到模糊的任务，它可以回去查 specs 获取上下文 — 而不是猜。Plan 可以丢掉重建（"The plan is disposable — regeneration costs one planning loop"），但 specs 不能丢。

---

## Step 2: 导出 Ralph 计划

规划满意后，运行 `/ralph-plan` 命令。这个命令会把你的规划转化为 Ralph 可执行的结构化文件。

### 安装命令

创建 `.claude/commands/ralph-plan.md`：

```markdown
Convert our plan into structured Ralph execution files.

## Step 1: Create Specs

For each major feature or component in our plan, create a spec file in specs/:

- specs/{feature-name}.md
- Include: what it does, API design, data model, edge cases, constraints
- These are the REQUIREMENTS — they should be specific enough that
  someone (or an agent) can implement without asking questions
- Do NOT include implementation steps in specs — only WHAT, not HOW

## Step 2: Create Implementation Plan

Analyze specs/ against the current codebase and create plan.json:

{
  "name": "feature-name",
  "created": "YYYY-MM-DD",
  "phases": [
    {
      "name": "Phase 0: Test Infrastructure",
      "description": "Set up testing foundation before feature work",
      "tasks": [...]
    },
    {
      "name": "Phase 1: ...",
      "description": "...",
      "tasks": [
        {
          "id": "1.1",
          "description": "Clear description of what to implement",
          "spec_ref": "specs/relevant-spec.md",
          "acceptance": [
            "specific testable criterion 1",
            "specific testable criterion 2",
            "command that must pass: npm run test -- feature.test.ts"
          ],
          "passes": false,
          "notes": ""
        }
      ]
    }
  ],
  "feedback": {
    "test": "detected test command or null",
    "typecheck": "detected typecheck command or null",
    "lint": "detected lint command or null",
    "build": "detected build command or null"
  }
}

### Rules for creating the plan:

Phase design:
- Each phase should have 3-8 tasks (not more)
- Phases are SEQUENTIAL — Phase 2 starts only after Phase 1 is 100% done
- Put dependent work in later phases
- Tasks WITHIN a phase should have NO hard dependencies on each other

Task design:
- Each task must be completable in ONE iteration (one context window)
- If a task feels too large, split it
- acceptance criteria must be TESTABLE — not "works well" but "returns 200 on GET /users"

Test infrastructure:
- If this project has NO test suite, Phase 0 MUST be "Set up test infrastructure"
- Detect existing: package.json scripts, pytest.ini, Cargo.toml [test], etc.
- If none found, Phase 0 creates the testing foundation

## Step 3: Create progress.txt

Create an empty progress.txt with header:
```
# Progress Log
# Auto-appended by Ralph loop. Do not edit manually.
```

## Step 4: Report

Show:
- Total phases and tasks
- Detected feedback loops
- Whether Phase 0 (test infra) was added
- Estimated iterations needed (tasks × 1.5 for buffer)
- Next step: ./ralph-once.sh (test first) then ./ralph.sh <N>
```

---

## Step 3: 三层测试标准

这是整个流程的命脉。没有测试，Ralph 就是在黑暗中写代码 — 它无法知道自己写的东西是否正确。

Geoffrey Huntley 的原则：**"Backpressure over prescription" — 不要告诉 agent 怎么做，创造门槛拦住坏代码。**

### 第一层：项目级自动化检查（硬门槛）

这是 `plan.json` 的 `feedback` 字段。每次 commit 前 Ralph 必须跑这些：

```json
"feedback": {
  "typecheck": "npm run typecheck",
  "test": "npm run test",
  "lint": "npm run lint",
  "build": "npm run build"
}
```

**任何一个失败 = 不能 commit。** Ralph 必须修好再继续。

如果你的项目还没有这些命令 — 这就是为什么 Phase 0 存在。

### 第二层：任务级验收标准（精准门槛）

每个 task 的 `acceptance` 字段是该任务特有的验收条件。它们必须是**可程序化验证的** — 不是主观感受，是具体断言：

```json
// ❌ 不可验证
{
  "description": "添加用户认证",
  "acceptance": ["认证功能正常工作", "安全性足够好"]
}

// ✅ 可验证
{
  "description": "添加 JWT 认证中间件",
  "acceptance": [
    "POST /auth/login 用正确密码返回 200 + JWT token",
    "POST /auth/login 用错误密码返回 401",
    "GET /protected 无 token 返回 401",
    "GET /protected 有效 token 返回 200",
    "npm run test -- src/auth/__tests__/ 全部通过",
    "JWT secret 从环境变量读取，不硬编码"
  ]
}
```

**写验收标准的诀窍：** 想象你把这个 task 交给一个完全不了解项目的新人。他需要什么信息才能自信地说"我做完了"？那就是你的 acceptance criteria。

Huntley 还有一个额外建议：**"Capture test intent — document WHY tests matter."** 不只写测试什么，还写为什么测。这样未来的 iteration 即使上下文被清空，也知道不能删这个测试。

### 第三层：LLM-as-Judge（主观标准）

对于无法用测试覆盖的标准 — UI 质量、文案语气、代码可读性 — 用 LLM 自身做评判，但必须是**二元 pass/fail**：

```
在 acceptance 里加一条：
"LLM-judge: 检查 src/components/Header.tsx 的布局是否匹配 specs/ui-design.md 的描述。PASS 或 FAIL。"
```

这是 Huntley playbook 里的高级技巧：non-deterministic testing。不是所有标准都需要单元测试，但所有标准都需要门槛。

### Phase 0: 没有测试基础设施？先建

**这是最重要的建议：如果你的项目还没有 test suite，Ralph 的第一个 phase 必须是搭建测试基础设施。**

为什么？因为 Ralph 的质量完全依赖反馈循环。没有测试 = 没有 backpressure = Ralph 可以提交任何东西而不会被拦住。后果：

- Phase 1 提交了有 bug 的代码
- Phase 2 在有 bug 的基础上继续建
- Phase 3 累积更多问题
- 你回来发现一堆 commit，全是表面上"完成"但实际上不工作的代码

Phase 0 的典型任务：

```json
{
  "name": "Phase 0: Test Infrastructure",
  "description": "搭建测试基础设施，确保后续 phase 有反馈循环",
  "tasks": [
    {
      "id": "0.1",
      "description": "安装测试框架并配置",
      "acceptance": [
        "npm run test 命令可用且返回 exit code 0",
        "至少一个示例测试存在并通过",
        "测试配置文件存在（jest.config / vitest.config 等）"
      ],
      "passes": false
    },
    {
      "id": "0.2",
      "description": "配置 TypeScript 类型检查（如适用）",
      "acceptance": [
        "npm run typecheck 命令可用",
        "当前代码库无类型错误"
      ],
      "passes": false
    },
    {
      "id": "0.3",
      "description": "配置 linter",
      "acceptance": [
        "npm run lint 命令可用",
        "当前代码库无 lint 错误",
        ".eslintrc 或等效配置存在"
      ],
      "passes": false
    },
    {
      "id": "0.4",
      "description": "为现有核心模块添加基础测试",
      "acceptance": [
        "核心业务逻辑有至少 1 个测试",
        "npm run test 通过"
      ],
      "passes": false
    }
  ]
}
```

**Phase 0 应该用 HITL 跑** — 你在旁边看着，确保测试基础是正确的。之后的 phase 才适合 AFK。

---

## Step 4: 准备执行脚本

### ralph-once.sh（HITL — 先用这个）

```bash
#!/bin/bash
# ralph-once.sh — 单次迭代，你在旁边看着

claude --permission-mode acceptEdits \
"@specs/ @plan.json @progress.txt

You are in Ralph mode — autonomous building from a phased plan.

## Context
- specs/ contains the technical specifications (WHAT to build)
- plan.json contains the implementation plan (tasks to execute)
- progress.txt contains what previous iterations have done

## Task Selection
1. Read plan.json. Find the current phase (first phase with any passes: false).
2. Within that phase, pick the task YOU judge as highest priority.
3. Read the relevant spec file (spec_ref field) for context.
4. ONLY WORK ON THIS SINGLE TASK.

## Implementation
5. Study the codebase before changing anything. Search, don't assume.
6. Implement fully. No placeholders. No TODOs. Full implementation.
7. If the task is too large, break it into a subtask and do only that.

## Verification — Three Layers
8. Run EVERY feedback loop in plan.json (test, typecheck, lint, build).
   If ANY fails, fix it. Do NOT commit broken code. Do NOT skip tests.
9. Verify each acceptance criterion for this task.
   If a criterion requires a new test, write the test first.
10. For LLM-judge criteria: evaluate honestly. PASS or FAIL. If FAIL, fix it.

## Commit & Progress
11. Commit with message: 'ralph: [task-id] description'
12. Update plan.json: set this task's passes to true. Commit plan.json.
13. APPEND to progress.txt (do NOT overwrite):
    - Task id and description
    - What you implemented
    - Key decisions and WHY
    - Files changed
    - Any issues encountered

## Completion
If ALL tasks in ALL phases have passes: true, output <promise>COMPLETE</promise>.
Only output this when EVERY task passes. Not before."
```

### ralph.sh（AFK — 跑通 HITL 后再用）

```bash
#!/bin/bash
# ralph.sh — AFK 循环，Docker sandbox 隔离
set -e

ITERATIONS=${1:-20}

echo "Starting Ralph loop (max $ITERATIONS iterations)"
echo "Plan: $(jq '.name' plan.json 2>/dev/null || echo 'plan.json')"
echo "Tasks remaining: $(jq '[.phases[].tasks[] | select(.passes == false)] | length' plan.json 2>/dev/null || echo '?')"
echo ""

for ((i=1; i<=$ITERATIONS; i++)); do
  echo "=== Iteration $i/$ITERATIONS ==="
  remaining=$(jq '[.phases[].tasks[] | select(.passes == false)] | length' plan.json 2>/dev/null || echo '?')
  echo "Tasks remaining: $remaining"

  result=$(docker sandbox run claude --permission-mode acceptEdits -p \
"@specs/ @plan.json @progress.txt

You are in Ralph mode — autonomous building from a phased plan.

## Context
- specs/ contains the technical specifications (WHAT to build)
- plan.json contains the implementation plan (tasks to execute)
- progress.txt contains what previous iterations have done

## Task Selection
1. Read plan.json. Find the current phase (first phase with any passes: false).
2. Within that phase, pick the task YOU judge as highest priority.
3. Read the relevant spec file (spec_ref field) for context.
4. ONLY WORK ON THIS SINGLE TASK.

## Implementation
5. Study the codebase before changing anything. Search, don't assume.
6. Implement fully. No placeholders. No TODOs. Full implementation.
7. If the task is too large, break it into a subtask and do only that.

## Verification — Three Layers
8. Run EVERY feedback loop in plan.json (test, typecheck, lint, build).
   If ANY fails, fix it. Do NOT commit broken code. Do NOT skip tests.
9. Verify each acceptance criterion for this task.
   If a criterion requires a new test, write the test first.
10. For LLM-judge criteria: evaluate honestly. PASS or FAIL. If FAIL, fix it.

## Commit & Progress
11. Commit with message: 'ralph: [task-id] description'
12. Update plan.json: set this task's passes to true. Commit plan.json.
13. APPEND to progress.txt (do NOT overwrite):
    - Task id and description
    - What you implemented
    - Key decisions and WHY
    - Files changed
    - Any issues encountered

## Completion
If ALL tasks in ALL phases have passes: true, output <promise>COMPLETE</promise>.
Only output this when EVERY task passes. Not before.")

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo ""
    echo "All phases complete after $i iterations."
    # macOS notification
    osascript -e 'display notification "All phases complete!" with title "Ralph Done"' 2>/dev/null || true
    exit 0
  fi
done

echo ""
echo "Reached $ITERATIONS iterations. Review progress.txt and plan.json."
echo "Remaining tasks:"
jq '.phases[].tasks[] | select(.passes == false) | .id + ": " + .description' plan.json 2>/dev/null
```

设置权限：

```bash
chmod +x ralph-once.sh ralph.sh
```

---

## Step 5: 执行

### 5a. HITL 验证（必须先做）

```bash
# 跑一次，在旁边看着
./ralph-once.sh
```

检查：
- Ralph 选对了任务吗？（应该是当前 phase 中最高优先级的）
- 它在写代码之前先搜索了代码库吗？
- 测试跑了吗？通过了吗？
- Commit message 清晰吗？
- progress.txt 更新了吗？
- plan.json 的 passes 字段更新了吗？

**Phase 0（测试基础设施）建议全程 HITL。** 测试基础是后面一切的根基，不能出错。

### 5b. AFK 执行

Phase 0 HITL 验证通过后，后续 phase 可以 AFK：

```bash
# 预估迭代次数 = 剩余任务数 × 1.5
./ralph.sh 30
```

然后做别的事。Ralph 会：
1. 每次迭代读取 plan.json + progress.txt + specs/
2. 选择任务，实现，测试，提交
3. 更新 plan.json 和 progress.txt
4. 所有任务完成后输出 COMPLETE

### 5c. 回来后检查

```bash
# 看看做了什么
git log --oneline

# 看执行日志
cat progress.txt

# 看还有什么没完成
jq '.phases[].tasks[] | select(.passes == false) | .id + ": " + .description' plan.json

# 如果有没完成的，继续跑
./ralph.sh 10
```

---

## Step 6: 处理意外情况

### Ralph 跑偏了

```bash
# 看 progress.txt 找到哪里跑偏的
cat progress.txt

# 回退到跑偏前的 commit
git log --oneline
git revert <bad-commit>  # 或 git reset --soft

# 调整 plan.json：把跑偏的 task 设回 false，加 notes 说明
# 重新跑
./ralph.sh 10
```

### 某个 task 反复失败

如果同一个 task 连续几次失败，说明：
1. Task 太大 — 拆成更小的 subtask
2. Acceptance criteria 不明确 — 改写得更具体
3. 依赖没满足 — 检查是否有 task 应该在更早的 phase

修改 plan.json 后重新跑。记住：**"The plan is disposable."** 重建比修补便宜。

### 需要改需求

```bash
# 修改 specs/ 中的相关规格文件
# 调整 plan.json 中受影响的 task（设回 passes: false，更新 acceptance）
# 重新跑
./ralph.sh 15
```

---

## 任务依赖：Phase 是答案

Ralph 不理解复杂的依赖图。它的依赖机制很简单：

**Phase 间：严格顺序。** Phase N+1 不会开始直到 Phase N 的所有 task 都完成。

```json
{
  "phases": [
    {"name": "Phase 0: 测试基础设施"},     // ← 必须先完成
    {"name": "Phase 1: 数据库 + Models"},  // ← 必须先完成
    {"name": "Phase 2: API Endpoints"},     // ← 依赖 Phase 1 的 models
    {"name": "Phase 3: 前端 UI"}            // ← 依赖 Phase 2 的 API
  ]
}
```

**Phase 内：Agent 自行判断。** 同一 phase 内的 task 不应有强依赖。如果有 — 拆到不同 phase。

这个约束反过来也是一个规划原则：**如果你无法把 task 分成无依赖的组，说明你的 phase 粒度不对。** 重新规划。

---

## 执行日志（progress.txt）

每次 iteration 后 Ralph 追加日志。格式：

```
## Iteration 3 — Task 1.2: 添加 JWT 认证中间件
- Implemented: auth middleware using jose library
- Decision: chose jose over jsonwebtoken (better ESM support, smaller bundle)
- Files: src/middleware/auth.ts, src/auth/__tests__/auth.test.ts, package.json
- Feedback: test ✅ | typecheck ✅ | lint ✅
- Notes: none
```

**关键 prompt 词汇：用 "APPEND" 不要用 "update"。** 否则 agent 可能覆盖之前的记录。Progress.txt 是 append-only。

这个文件有两个作用：
1. **Ralph 的跨迭代记忆** — 新的 iteration 读它来了解已经做了什么
2. **你的审计日志** — 回来后快速了解发生了什么

用完删掉。它是 session-specific 的，不是永久文档。

---

## 清单：开始前确认

- [ ] 项目有测试框架吗？没有 → Phase 0 必须搭建
- [ ] plan.json 的每个 task 都有可验证的 acceptance criteria？
- [ ] Phase 间的依赖关系是线性的？（Phase N+1 不依赖 Phase N+2）
- [ ] Phase 内的 task 没有相互依赖？
- [ ] Docker Desktop 4.50+ 已安装？
- [ ] `ralph-once.sh` 跑过一次且行为正确？
- [ ] specs/ 文件足够详细，不需要追问就能实现？

全部 checked → `./ralph.sh <iterations>` → 走开。

<!-- CTA: 从你的下一个 feature 试起。Plan mode 对齐意图，/ralph-plan 导出计划，ralph-once.sh 验证一轮，然后 AFK。代码会在你喝咖啡的时候写好。 -->
