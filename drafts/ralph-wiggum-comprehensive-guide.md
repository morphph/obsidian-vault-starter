---
status: draft
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
  - raw/2026-04-15-ghuntley-ralph-wiggum-original.md
  - raw/2026-04-15-anthropic-ralph-wiggum-plugin.md
  - raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
  - raw/2026-04-15-humanlayer-brief-history-of-ralph.md
  - raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md
  - raw/2026-04-15-aihero-getting-started-with-ralph.md
  - raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md
  - raw/2026-04-15-repo-ralph-orchestrator.md
  - raw/2026-04-15-ralph-workflow-design-qa.md
platform: blog
created: 2026-04-15
last-updated: 2026-04-15
tags: [draft]
---

<!-- HOOK: 5 万美元合同，297 美元 API 成本交付。一个编程语言，在创造者睡觉的时候被 AI 自主构建。这就是 Ralph Wiggum —— 把 AI 编程工具放进一个 while 循环，然后走开。 -->

# Ralph Wiggum 完全指南：从理解到落地的自主 AI 编程

5 万美元的合同，297 美元的 API 成本交付。一个完整的编程语言 —— 编译器、标准库、LLVM 集成 —— 在创造者睡觉的三个月里被自主构建。Y Combinator hackathon 中一夜之间交付六个完整的代码仓库。测试覆盖率从 16% 拉到 100%，开发者全程没看屏幕。

这就是 Ralph Wiggum 技术。以辛普森家族里那个永不放弃的角色命名，它是自主 AI 编程中最简单也最强大的模式：把你的 AI agent 放进一个循环，定义"完成"是什么样子，然后走开。

这篇指南覆盖全部 —— 从理解它是什么，到你可以直接 copy-paste 的脚本和命令，再到生产级的进阶用法。

---

## 目录

1. [什么是 Ralph](#什么是-ralph)
2. [两种实现：Bash Loop vs 官方插件](#两种实现)
3. [核心原则](#核心原则)
4. [落地：从规划到自主执行](#落地从规划到自主执行)
5. [三层测试标准](#三层测试标准)
6. [安全：Sandbox 是底线](#安全sandbox-是底线)
7. [进阶：Ralph Orchestrator 与并行执行](#进阶ralph-orchestrator-与并行执行)
8. [局限性](#局限性)
9. [时间线与生态](#时间线与生态)

---

## 什么是 Ralph

AI 编程在过去一年经历了四个阶段：

1. **Vibe coding** —— 让 AI 写代码，不检查。快，但质量差。
2. **Planning** —— 让 AI 先规划再写。质量提升，但受限于单个 context window。
3. **Multi-phase plans** —— 把大功能拆成阶段，每个阶段写不同的 prompt。可以 scale，但需要持续的人工参与。
4. **Ralph** —— 同一个 prompt 跑在循环里。Agent 自己选任务。你定义终态。

Ralph 最简单的形式就是一行 bash：

```bash
while :; do cat PROMPT.md | claude-code ; done
```

每次迭代：读计划 → 选任务 → 实现 → 跑测试 → 提交 → 记录进度。全部完成后停止。

**关键转变：agent 选任务，不是你选。** 你定义终态，Ralph 到达那里。

Geoffrey Huntley（2025 年中发明了 Ralph）这样总结：**"The loop is the hero, not the model."** 不要等更聪明的模型。构建持续运行的系统，迭代到成功为止。

---

## 两种实现

Ralph 有两种实现方式，社区对此有根本性的分歧。

### Bash Loop（原始方式）

```bash
while :; do cat PROMPT.md | claude-code ; done
```

每次迭代启动**全新的 context**。Agent 重新读取 specs、plan、代码。Huntley 认为这是核心设计 —— 新鲜的 context 意味着没有累积的混乱，没有 context rot。

### Anthropic 官方插件（Stop Hook）

Anthropic 在 2025 年 12 月发布了官方插件，由 Boris Cherny（Claude Code 负责人）主导：

```bash
/ralph-loop "Build a REST API for todos. Output <promise>COMPLETE</promise> when done." \
  --completion-promise "COMPLETE" \
  --max-iterations 50
```

插件用 **Stop hook** 拦截 Claude 的退出尝试。Agent 工作 → 尝试退出 → hook 拦截 → 同一个 prompt 重新喂入 → 重复。循环发生在**同一个 session 内**，不需要外部 bash 脚本。

### 选哪个？

| | Bash Loop | 官方插件 |
|---|-----------|---------|
| Context | 每次迭代全新 | 同一 session 累积 |
| Context rot 风险 | 无 | 随迭代增长 |
| 设置 | 需要脚本文件 | 内置命令 |
| 调试 | 容易（每次独立） | 复杂（session 内状态） |
| 推荐者 | Huntley, Dex Horthy | Anthropic |

Dex Horthy（HumanLayer，从早期就在用 Ralph）至今仍然偏好 "5-line bash loops"。官方插件 "dies in cryptic ways unless you have `--dangerously-skip-permissions`"。

Huntley 的核心论点：fresh context is reliability。"Smart zone" 是 ~176K 可用 token 的 40-60%。超过这个范围，质量下降。

**建议：从 bash loop 开始。** 更容易理解、更容易调试、遵循原始设计意图。

---

## 核心原则

这些原则来自 Huntley 的 playbook、Matt Pocock 的 11 tips、以及 Ralph Orchestrator 的 Six Tenets。

### 1. 每次循环只做一件事

每次迭代只实现一个功能。保持 ~170K token 的 context window 不被耗尽。任务太大 → 拆分成子任务。

### 2. Backpressure Over Prescription

不要告诉 agent **怎么做**。创造**门槛**拦住坏代码。

```
❌ "先写测试，然后实现函数，然后跑 linter..."
✅ "提交前跑 test、typecheck、lint。任何一个失败就不能提交。"
```

Agent 自己想办法。你定义什么必须通过。

### 3. Plan 可丢弃，Specs 不能丢

这是很多人搞混的地方 —— PRD、implementation specs、implementation plan 不是一回事：

| 文档 | 是什么 | 生命周期 |
|------|--------|----------|
| **Specs** (`specs/*.md`) | 技术规格 — **要建什么** | 不变（除非需求变） |
| **Implementation Plan** (`plan.json`) | 任务清单 — **怎么建** | 可丢弃，随时重建 |

Specs 是需求文档。Plan 是执行路径。**当 Ralph 遇到模糊任务时，它回去查 specs 获取上下文，而不是猜。**

Huntley："The plan is disposable — regeneration costs one planning loop." 重建 plan 很便宜。修补烂 plan 很贵。

### 4. 代码库会赢

你的指令和代码库在竞争。Prompt 是几行。代码库是几千行。冲突时，agent 跟着代码库走。

你可以在 prompt 里写 "不要用 `any` 类型"。但如果代码库到处都是 `any`，Ralph 会继续用 `any`。

**Agents 放大它看到的东西。** 烂代码 → 更烂的代码。人一天提交 1-2 次。Ralph 几小时堆几十个 commit。如果这些 commit 质量差，software entropy 加速恶化。

所以：在放 Ralph 之前，**先把代码库清理干净。** 明确告知 repo 类型："Production code. Must be maintainable." 或 "Prototype. Speed over perfection."

### 5. Prompt 措辞有讲究

Huntley 发现特定的措辞 Claude 响应更好：

- **"study"**（不是 "read"）—— 暗示更深的分析
- **"don't assume not implemented"** —— 强制搜索代码库再动手
- **"using parallel subagents"** —— 触发并行化
- **"capture the why"** —— 记录决策理由
- **"DO NOT IMPLEMENT PLACEHOLDER"** —— 防止偷懒

还有一个高级技巧：让 agent 在发现更好的 build/test 方式时自动更新 `AGENTS.md`。Self-learning agent。

### 6. 先 HITL，再 AFK

不要一上来就放手。进程：

1. **HITL**（human-in-the-loop）：跑一次，在旁边看，纠正，打磨 prompt
2. **AFK**（away from keyboard）：prompt 验证通过后，放进循环跑，你去做别的事
3. **回来检查**：看 git log，看 progress.txt，处理遗留问题

对于高风险任务（架构决策、基础设施），用 HITL。对于低风险任务（功能实现、测试、打磨），用 AFK。

---

## 落地：从规划到自主执行

理论够了。以下是具体的实操流程。

### 整体流程

```
┌─────────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│  规划阶段           │    │  导出阶段         │    │  执行阶段           │
│  你 + Claude Code   │ →  │  /ralph-plan      │ →  │  ralph.sh (AFK)     │
│  交互式 plan mode   │    │  生成 specs/ +    │    │  Docker sandbox     │
│  直到方案满意       │    │  plan.json        │    │  每次 fresh context │
└─────────────────────┘    └──────────────────┘    └─────────────────────┘
        HITL                    自动化                     AFK
```

### 前置条件

```bash
# Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Docker Desktop 4.50+（AFK 必须）
docker sandbox run claude --version
```

### Step 1: 交互式规划

启动 Claude Code，进入 plan mode（`shift-tab`）。

这个阶段的目标不是写代码 —— 是**对齐意图**。你要建什么？分几个阶段？技术约束？怎么验证完成？

**不要急。** 这是人类价值最高的环节。规划质量 = 输出质量。

规划满意后，运行 `/ralph-plan`（一个 custom command，安装见下方），它会：
1. 把你的规划转化为 `specs/` 目录（技术规格，不变）
2. 生成 `plan.json`（任务清单，可丢弃）
3. 创建空的 `progress.txt`
4. 告诉你接下来怎么跑

### Step 2: `/ralph-plan` 命令

在你的项目里创建 `.claude/commands/ralph-plan.md`：

```markdown
Convert our plan into structured Ralph execution files.

## Step 1: Create Specs

For each major feature or component, create a spec file in specs/:
- specs/{feature-name}.md
- Include: what it does, API design, data model, edge cases, constraints
- Specs are REQUIREMENTS — specific enough to implement without questions
- Do NOT include implementation steps — only WHAT, not HOW

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
      "tasks": [
        {
          "id": "1.1",
          "description": "Clear description of what to implement",
          "spec_ref": "specs/relevant-spec.md",
          "acceptance": [
            "specific testable criterion",
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

### Rules:
- Each phase: 3-8 tasks. More than 8 → split the phase.
- Phases are SEQUENTIAL. Phase N+1 only starts after Phase N is 100% done.
- Tasks WITHIN a phase: NO hard dependencies on each other.
- Each task completable in ONE iteration (one context window).
- If project has NO test suite, Phase 0 MUST set up test infrastructure.
- All acceptance criteria must be programmatically verifiable.

## Step 3: Create progress.txt with header

## Step 4: Report total phases, tasks, detected feedback loops,
whether Phase 0 was added, and the command to start.
```

### Step 3: HITL 验证（必须）

先跑一次，看着它做。创建 `ralph-once.sh`：

```bash
#!/bin/bash
# ralph-once.sh — 单次迭代，你在旁边看

claude --permission-mode acceptEdits \
"@specs/ @plan.json @progress.txt

You are in Ralph mode — autonomous building from a phased plan.

## Task Selection
1. Read plan.json. Find current phase (first with any passes: false).
2. Pick the highest-priority incomplete task in that phase.
3. Read the relevant spec file (spec_ref) for context.
4. ONLY WORK ON THIS SINGLE TASK.

## Implementation
5. Study the codebase before changing anything. Search, don't assume.
6. Implement fully. No placeholders. No TODOs.
7. If too large, break into subtask and do only that.

## Verification — Three Layers
8. Run EVERY feedback loop in plan.json (test, typecheck, lint, build).
   If ANY fails, fix it. Do NOT commit broken code.
9. Verify each acceptance criterion for this task.
   If a criterion requires a new test, write the test first.
10. For LLM-judge criteria: evaluate honestly, PASS or FAIL.

## Commit & Progress
11. Commit with message: 'ralph: [task-id] description'
12. Set this task's passes to true in plan.json. Commit plan.json.
13. APPEND to progress.txt (do NOT overwrite):
    task id, what you did, decisions and WHY, files changed.

## Completion
If ALL tasks in ALL phases pass, output <promise>COMPLETE</promise>."
```

检查清单：
- [ ] Ralph 选对了任务吗？
- [ ] 它在改代码前先搜索了代码库吗？
- [ ] 测试跑了吗？通过了吗？
- [ ] plan.json 的 passes 更新了吗？
- [ ] progress.txt 追加了（不是覆盖）吗？

**Phase 0（测试基础设施）建议全程 HITL。** 测试基础是后面一切的根基。

### Step 4: AFK 执行

HITL 验证通过后，创建 `ralph.sh`：

```bash
#!/bin/bash
set -e

ITERATIONS=${1:-20}

echo "Starting Ralph loop (max $ITERATIONS iterations)"
echo "Tasks remaining: $(jq '[.phases[].tasks[] | select(.passes == false)] | length' plan.json 2>/dev/null || echo '?')"

for ((i=1; i<=$ITERATIONS; i++)); do
  echo "=== Iteration $i/$ITERATIONS ==="

  result=$(docker sandbox run claude --permission-mode acceptEdits -p \
"@specs/ @plan.json @progress.txt

You are in Ralph mode — autonomous building from a phased plan.

## Task Selection
1. Read plan.json. Find current phase (first with any passes: false).
2. Pick the highest-priority incomplete task in that phase.
3. Read the relevant spec file (spec_ref) for context.
4. ONLY WORK ON THIS SINGLE TASK.

## Implementation
5. Study the codebase before changing anything. Search, don't assume.
6. Implement fully. No placeholders. No TODOs.
7. If too large, break into subtask and do only that.

## Verification — Three Layers
8. Run EVERY feedback loop in plan.json (test, typecheck, lint, build).
   If ANY fails, fix it. Do NOT commit broken code.
9. Verify each acceptance criterion for this task.
   If a criterion requires a new test, write the test first.
10. For LLM-judge criteria: evaluate honestly, PASS or FAIL.

## Commit & Progress
11. Commit with message: 'ralph: [task-id] description'
12. Set this task's passes to true in plan.json. Commit plan.json.
13. APPEND to progress.txt (do NOT overwrite):
    task id, what you did, decisions and WHY, files changed.

## Completion
If ALL tasks in ALL phases pass, output <promise>COMPLETE</promise>.")

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "All phases complete after $i iterations."
    osascript -e 'display notification "Ralph done!" with title "Ralph"' 2>/dev/null || true
    exit 0
  fi
done

echo "Reached $ITERATIONS iterations. Check progress.txt."
```

```bash
chmod +x ralph-once.sh ralph.sh
./ralph.sh 30  # 然后走开
```

### Step 5: 回来后

```bash
git log --oneline                          # 看做了什么
cat progress.txt                           # 看执行日志
jq '.phases[].tasks[] | select(.passes == false) | "\(.id): \(.description)"' plan.json  # 看还剩什么
```

没做完？继续跑 `./ralph.sh 10`。跑偏了？`git revert`，修改 plan.json，重跑。

---

## 三层测试标准

这是整个 Ralph 的命脉。**没有测试，Ralph 就是在黑暗中写代码。**

### 第一层：项目级自动化检查

plan.json 的 `feedback` 字段。每次 commit 前 Ralph 必须跑这些命令，全部通过才能提交：

```json
"feedback": {
  "test": "npm run test",
  "typecheck": "npm run typecheck",
  "lint": "npm run lint",
  "build": "npm run build"
}
```

这是硬门槛 —— **不过就不能 commit。** Ralph 无法绕过。

### 第二层：任务级验收标准

每个 task 的 `acceptance` 字段。必须是**可程序化验证的** —— 不是主观感受，是具体断言：

```json
// ❌ 不可验证 — Ralph 会自己判断"正常"然后通过
"acceptance": ["用户认证功能正常工作"]

// ✅ 可验证 — 每条都有明确的 pass/fail
"acceptance": [
  "POST /auth/login 正确密码返回 200 + JWT",
  "POST /auth/login 错误密码返回 401",
  "GET /protected 无 token 返回 401",
  "npm run test -- auth.test.ts 全部通过",
  "JWT secret 从环境变量读取，不硬编码"
]
```

写验收标准的诀窍：想象你把这个 task 交给一个完全不了解项目的新人。他需要什么信息才能自信地说"我做完了"？那就是你的 acceptance criteria。

Huntley 额外建议：**"Capture test intent — document WHY tests matter."** 不只写测试什么，还写为什么测。这样未来的 iteration 即使上下文被清空也知道不能删这个测试。

### 第三层：LLM-as-Judge

对于无法用测试覆盖的标准 —— UI 质量、文案语气、代码可读性 —— 用 LLM 自身做评判，但必须是**二元 pass/fail**：

```json
"acceptance": [
  "LLM-judge: 检查 Header 布局是否匹配 specs/ui-design.md。PASS 或 FAIL。"
]
```

这是 Huntley playbook 里的高级技巧 —— non-deterministic testing。不是所有标准都需要单元测试，但所有标准都需要门槛。

### Phase 0：没有测试？先建

**如果你的项目还没有 test suite，Ralph 的第一个 phase 必须是搭建测试基础设施。**

为什么？因为没有测试 = 没有 backpressure = Ralph 可以提交任何东西。后果是 Phase 1 有 bug → Phase 2 在 bug 上继续建 → Phase 3 雪崩 → 你回来面对一堆表面"完成"实际不工作的 commit。

Phase 0 典型任务：

```json
{
  "name": "Phase 0: Test Infrastructure",
  "tasks": [
    {
      "id": "0.1",
      "description": "安装测试框架并配置",
      "acceptance": ["npm run test 可用且返回 exit 0", "至少一个示例测试通过"]
    },
    {
      "id": "0.2",
      "description": "配置 TypeScript 类型检查",
      "acceptance": ["npm run typecheck 可用", "当前代码库无类型错误"]
    },
    {
      "id": "0.3",
      "description": "配置 linter",
      "acceptance": ["npm run lint 可用", "当前代码库无 lint 错误"]
    }
  ]
}
```

**Phase 0 全程 HITL。** 测试基础是后面一切的根基，不能出错。

---

## 任务依赖：Phase 是答案

Ralph 不理解复杂的依赖图。它用两层机制处理依赖：

**Phase 间：严格顺序。** Phase N+1 不会开始直到 Phase N 的所有 task 都 passes: true。

```json
"phases": [
  {"name": "Phase 0: 测试基础设施"},     // ← 必须先完成
  {"name": "Phase 1: 数据库 + Models"},  // ← 必须先完成
  {"name": "Phase 2: API Endpoints"},     // ← 依赖 Phase 1
  {"name": "Phase 3: 前端 UI"}            // ← 依赖 Phase 2
]
```

**Phase 内：Agent 自行判断。** 同一 Phase 内的 task 不应有强依赖。Agent 通过 progress.txt 和 git history 了解已完成的工作，自行选择优先级。

如果你无法把 task 分成无依赖的组，说明 phase 粒度不对 —— 重新规划。

---

## 安全：Sandbox 是底线

AFK 模式下，sandbox 是**唯一的安全边界**。用了 `--permission-mode acceptEdits`，除了 sandbox 没有任何东西阻止 agent 执行危险操作。

### Docker Sandbox（推荐）

```bash
docker sandbox run claude
```

只挂载当前目录。Agent 可以编辑项目文件、提交代码 —— 但碰不到你的 home 目录、SSH keys、系统文件。

### 原生 Sandbox

Claude Code 内置了 OS 级别的沙箱：
- **macOS**: Seatbelt（开箱即用）
- **Linux/WSL2**: bubblewrap（`sudo apt-get install bubblewrap socat`）

启用：`/sandbox`。内部数据：权限提示减少 84%。

文件系统和网络都被隔离。Anthropic 开源了 sandbox runtime：`npx @anthropic-ai/sandbox-runtime <command>`。

**规则：HITL sandbox 可选。AFK sandbox 必须。过夜跑的 sandbox 不可商量。**

---

## 进阶：Ralph Orchestrator 与并行执行

基础的 bash loop 够用了。但如果你需要更多 —— 多后端、并行循环、远程 HITL —— Ralph Orchestrator 是目前最成熟的实现（2,702 stars，Rust 编写）。

### 安装

```bash
npm install -g @ralph-orchestrator/ralph-cli
```

### 核心功能

**多后端支持** —— 不只是 Claude Code。支持 Gemini CLI、Codex、Kiro、Amp、Copilot CLI、OpenCode、Roo。

```bash
ralph init --backend claude
ralph plan "Add user authentication with JWT"
ralph run -p "Implement from specs/"
```

**Hat 系统** —— 轻量级多 agent 架构。不同的 "hat" 是不同的 agent persona，通过事件总线协调。一个 "reviewer" hat 负责代码审查，一个 "synthesizer" hat 汇总结果。比完整的多 agent 架构简单，但支持角色分工。

**Agent Waves** —— 循环内并行。打破"每次循环只做一件事"的限制。Scatter-gather 模式：agent 发射 wave 事件 → N 个并行 worker → 结果合并回来。适合可并行的工作（比如同时 review 多个文件）。

**Worktree 并行** —— 同一个 repo 上跑多个 Ralph 循环：

```
项目根目录/
├── .ralph/loop.lock          ← Primary loop 持有锁
├── .ralph/merge-queue.jsonl  ← 合并队列
└── .worktrees/
    ├── loop-auth/            ← Worktree loop 1（git worktree）
    └── loop-api/             ← Worktree loop 2（git worktree）
```

Primary loop 在主 workspace 运行。Worktree loops 通过 `git worktree add` 创建隔离副本，memories 和 specs 通过 symlink 共享。完成后排队合并。

**RObot（Telegram HITL）** —— 介于纯 HITL 和纯 AFK 之间的第三种模式。Agent 通过 Telegram 提问并阻塞等待回答。你可以随时从手机发送指导，不需要坐在电脑前。

**Web Dashboard** —— React 前端 + Rust RPC API。可视化监控和管理循环。

### Six Ralph Tenets

Ralph Orchestrator 把哲学编码成了原则：

1. **Fresh Context Is Reliability** —— 每次迭代清空上下文。
2. **Backpressure Over Prescription** —— 创造门槛，不规定步骤。
3. **The Plan Is Disposable** —— 重建 plan 很便宜。
4. **Disk Is State, Git Is Memory** —— 文件是状态，Git 是记忆。
5. **Steer With Signals, Not Scripts** —— 代码库本身就是指令。
6. **Let Ralph Ralph** —— 坐在循环上面，不是坐在循环里面。像调吉他，不是指挥乐团。

---

## 变体循环

Ralph 不只是用来建 feature。任何可以描述为"看 repo，改进一个东西，报告结果"的任务都适合：

**测试覆盖率循环：**
```
找到覆盖率报告中未覆盖的行。
为最关键的未覆盖代码路径写测试。
重新跑覆盖率。目标：80% 最低。
```

**Lint 循环：**
```
跑 npm run lint。
一次只修一个 lint 错误。
修完后重新跑 lint 验证。
重复直到没有错误。
```

**Entropy 循环（逆向 software entropy）：**
```
扫描代码坏味道：未使用的 export、死代码、不一致的模式。
每次迭代修一个。
记录改了什么到 progress.txt。
```

Matt Pocock 用测试覆盖率循环把 AI Hero CLI 从 16% 拉到了 100%。

---

## 局限性

诚实面对 Ralph 不能做的事：

- **只适合 greenfield** —— Huntley 明确说 Ralph 最适合新项目。改造现有代码库有问题。
- **Overbaking 现象** —— 跑太久会产生意料之外的涌现行为。比如没人要的 post-quantum cryptography 支持。
- **需要高级工程师监督** —— Ralph 放大有经验的指导，不能替代它。Operator 的 prompt engineering 和 spec 写作能力是关键成功因素。
- **Context compaction 风险** —— 长 session 中 compaction 可能导致偏移。Huntley 警告："Compaction is the devil."
- **~90% 完成度** —— 最后 10% 需要你自己 review 和 polish。
- **代码会有垃圾** —— 在 production release 之前，预期临时文件和未指定的行为。这是正常的。

---

## 成本

Ralph 可以适配任何预算。

| 方式 | 每个阶段的人工投入 | 适合 |
|------|---------------------|------|
| Multi-phase plans | 每阶段写新 prompt | 一次性大任务 |
| HITL Ralph | 重跑同一个 prompt | 学习、打磨 |
| AFK Ralph | 设好就走 | 批量工作、自动化 |

即使你从不跑 AFK，HITL Ralph 也比 multi-phase planning 好 —— 重跑同一个 prompt 比每次写新 prompt 简单。

本地开源模型目前还不够好。要用 Ralph，你需要付费。但我们正处于黄金时代：AI 做事比人快，但市场仍然按人类工资付费。这个差距不会持续太久。

---

## 时间线与生态

| 时间 | 里程碑 |
|------|--------|
| 2025 年 6 月 | Huntley 在 Twitter agentic coding meetup 首次展示 Ralph |
| 2025 年 7 月 | 官方 blog 发布：`while :; do cat PROMPT.md \| amp ; done` |
| 2025 年 8 月 | 一夜交付 6 个 repo；"specification quality = output quality" 被验证 |
| 2025 年 9 月 | CURSED 编程语言发布（通过 LLVM 编译到 Zig） |
| 2025 年 10 月 | 大会演讲加速社区采用 |
| 2025 年 12 月 | Anthropic 发布官方 Ralph Wiggum 插件（Stop hook 架构） |
| 2026 年 1 月 | Matt Pocock 病毒式 X 帖子（204K views, 4.8K bookmarks） |
| 2026 年+ | 主流采用 —— Workshop、awesome-ralph（849 stars）、Ralph Orchestrator（2,702 stars） |

### 生态系统

- **awesome-ralph** —— 849 star 的资源清单：所有实现、视频、播客、工具
- **Ralph Orchestrator** —— 2,702 star 的 Rust 生产级框架
- **官方插件** —— Anthropic 内置于 Claude Code
- **多种实现** —— ralph-claude-code（智能退出检测）、open-ralph-wiggum（多工具支持）、smart-ralph（spec-driven）
- **社区** —— r/ralphcoding（Reddit）、Discord、Dev Interrupted 播客

---

## 未来方向

**Gas Town**（Steve Yegge 提出）：**"Kubernetes for agents"** —— 不只是一个循环，而是多个循环的分布式编排。协调在成为瓶颈时，这是答案。

**MEOW**（Molecular Expression of Work）：把任务分解到最小可执行单元的方法论。Ephemeral worker 可以 pick up、execute、hand off。"PRD under a microscope."

方向很清楚：从一个 bash loop 到编排的 agent 系统。Ralph 的优雅简洁 —— 一行 bash —— 既是它最大的优势，也是一切进化的起点。

从一个循环开始。定义完成是什么样子。走开。

<!-- CTA: 从你的下一个 feature 试起。Plan mode 对齐意图，/ralph-plan 导出计划，ralph-once.sh 验证一轮，然后 AFK。代码会在你喝咖啡的时候写好。 -->

---

*Sources: Geoffrey Huntley (ghuntley.com/ralph, how-to-ralph-wiggum), Anthropic (Claude Code plugin, sandboxing docs), Matt Pocock (AI Hero — 11 Tips, Getting Started), Dex Horthy (HumanLayer — Brief History of Ralph), Dev Interrupted (Huntley interview), Ralph Orchestrator (mikeyobrien/ralph-orchestrator).*
