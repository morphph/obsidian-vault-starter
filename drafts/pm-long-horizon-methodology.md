---
type: draft
status: ready-for-review
created: 2026-05-19
last-updated: 2026-05-19
target-audience: 想用 AI 自主开发的 PM / 独立 builder / 非全职工程师
framing: 三个心智转换 + 一个 PM 工作流 + 四个反模式
based-on:
  - wiki/source-nurijanian-goal-for-pms.md
  - wiki/agent-ready-requirements.md
  - wiki/goal-template.md
  - wiki/claude-code-goal.md
  - wiki/source-openai-codex-cookbook-trilogy.md
  - wiki/source-openai-long-horizon-tasks-codex.md
  - wiki/source-openai-codex-use-case-follow-goals.md
  - wiki/source-chrishayduk-codex-goals-effectively.md
  - wiki/agentic-loop-tracking-files.md
  - wiki/idea-to-afk-agent-flow.md
  - wiki/grill-with-docs.md
  - wiki/hitl-vs-afk-classification.md
  - wiki/ralph-wiggum.md
  - wiki/sandcastle.md
companion-guide: drafts/pm-long-horizon-blog2video-practice-guide.md
tags: [drafts, methodology, pm, long-horizon, afk, claude-code-goal, chinese]
---

# 长跑任务（long-horizon task）的 PM 方法论：让 AI agent 跑通一件事，不是按一个按钮

> "Agentic coding does not remove product thinking. It punishes vague product thinking faster."
> Agentic coding 不消除产品思考，只是更快地惩罚模糊的产品思考。
>
> —— George (@nurijanian)，[[source-nurijanian-goal-for-pms|/goal for Product Managers]]

## 开场

如果你是 PM 或独立 builder，今年大概率被这套叙事砸过：

> "AFK（away-from-keyboard）coding，一句 prompt + 开个 loop，agent 自己写一晚上代码，醒来 merge。"

听起来像奇迹。社交媒体上的演示视频也确实在展示奇迹 —— 但你自己去试，十次有八次得到的是：loop 跑了 40 turn，写出一坨 "impressive 但 wrong" 的东西。George 给这个失败模式起了个名字：

> "A loop can spend 40 turns making the wrong thing more internally consistent."
> Loop 可以花 40 turn，把一件错的事情做得更加内部一致。

这不是 model 的问题。这是 **PM craft 的瓶颈被搬到了 agent 上**。

这篇文章的主张很简单：**AFK 不是入口，是奖励**。前面有 PM 完整的工作流要走 —— 写 spec、定义验收标准、把状态外置、看头几轮校准。**真正按下 `/goal` 那个按钮之前，PM 的工作已经做了 80%**。

把 AFK 当 "vibe coding 的升级版" 是大多数失败的根源。vibe coding 是 *你陪着 agent，错了立刻拉回来*；AFK 是 *你不在场，agent 错了会把错越做越深*。这两件事不是同一种活动的不同等级，**是两种工作**。

下面用三个心智转换串起整套方法论。每个转换都对应一个"大多数人在用 agent 时没做对"的具体动作 —— 你看完应该能 grep 自己最近 10 个 prompt，认领其中至少一个。

---

## Part 1：三个心智转换

### 转换 1：从 Prompt 到 Contract（从对话到合同）

PM 都熟悉一个东西，叫**验收标准**（acceptance criteria）。给同事看的 ticket，验收标准可以含混 —— *"用户应该能更方便地管理通知"* —— 因为同事会问你。

给 agent 跑的 ticket 没有"问你"这一步。agent 看不懂会按它猜的样子做下去，做 40 turn。

George 把这件事翻译成了一句最 clean 的对照：

> "A prompt asks for effort, while a contract defines the condition where effort stops."
> Prompt 要求努力；contract 定义努力停止的条件。

这是整篇文章 PM 必须记住的第一句话。

Prompt 和 Contract 在执行层是两种完全不同的东西（见 [[claude-code-goal]]）：

| Prompt | Contract |
|---|---|
| Stateless：每次问完就完 | Stateful：跨多 turn 维持目标 |
| "请帮我做 X" | "做到 Y 状态才停止" |
| 委托劳动 | 委托结果 |
| 失败模式：努力但不收敛 | 失败模式：少了 contract 就退化回 prompt |

**Contract 该有什么**（George 的 7 component，见 [[agent-ready-requirements]]）：

1. **Observable behavior** —— 用户实际能看到 / 做到的行为，不是抽象状态
2. **Negative cases** —— 什么不能发生（往往比正面行为更重要）
3. **Scope boundaries** —— 哪些文件 / 系统 / 逻辑不能动
4. **Validation evidence** —— 用什么命令 / 检查证明完成
5. **Stop conditions** —— N turn 或时间上限
6. **Status-report expectations** —— 失败 / 成功时记什么
7. **Customer-facing success criteria** —— 对最终用户有什么意义

OpenAI Cookbook 用了不同命名，但结构同源（见 [[source-openai-codex-cookbook-trilogy]]）—— 他们叫 **6-element strong goal**：Outcome / Verification surface / Constraints / Boundaries / Iteration policy / Blocked stop。这是 **跨厂商收敛的第一个信号** —— 不管你用 Claude `/goal` 还是 Codex `/goal`，contract 的形状已经被两家官方独立验证。

PM 该怎么用？把你最近 5 个 `/goal` 命令拉出来，按这 7 / 6 条 grep 一遍 —— 缺哪条，agent 在那条上就会 hallucinate。

**反共识的点**：很多人以为 "strong goal" 是 "写得很长的 goal"。**Strong goal 的关键不是字数，是是否包含可检验的退出条件**。两行写清楚 "`npm test` exits 0，no files outside `src/auth/` are changed" 远胜于一段抒情。

George 提供的 6-section practical template（见 [[goal-template]]）是把 7 component 落到可 copy-paste 形态：

```
/goal [specific target state]

Source of truth:
- read [spec file]
- follow [implementation plan]
- update [status file]

Acceptance criteria:
- [observable behavior 1]
- [observable behavior 2]
- [negative case]
- [non-regression condition]

Validation:
- [test command]
- [lint/typecheck/build command]
- [browser/visual/manual evidence if needed]

Boundaries:
- only edit [paths]
- do not change [systems]
- preserve [contract/data/API behavior]

Loop behavior:
- after each meaningful change, run the relevant validation
- update the status file with changed files, result, and remaining risk
- stop after [N turns/time] if blocked and report the blocker
```

这一段读起来像合同条款 —— 因为它就是合同条款。PM 这个职业本来就在写合同（产品交付物的合同），只是合同的"对手方"从 engineer 变成了 agent。

---

### 转换 2：从 In-Context 到 On-Disk（从对话内存到磁盘记忆）

第一个转换解决"目标在哪"。第二个解决"agent 跑到一半，目标会不会被它自己忘记"。

会。这是 agent loop 最致命的失败模式之一，叫 **context rot**（上下文腐烂）。

机制简单：每个 turn 之间，上下文会被 compact（压缩），关键信息可能被 summarize 掉。George 一句话讲透这个机制（见 [[source-nurijanian-goal-for-pms]]）：

> "The conversation could rot, but the source of truth stayed outside the conversation."
> 对话可以腐烂，但 source of truth 留在对话之外。

**解药很反直觉**：把 agent 的"工作记忆"从 in-context 搬到磁盘上的 markdown 文件。这些文件每个 turn 都会被重新 load，所以它们是 **跨 compaction 唯一可信的状态载体**。

**这里有一个非常值得 PM 重视的信号**：5 个独立来源、不同上下文、不同时间，**独立发明了同一个 pattern**（见 [[agentic-loop-tracking-files]]）：

| 来源 | 文件命名 | 时间 |
|---|---|---|
| Geoffrey Huntley（[[ralph-wiggum]] 原作者） | `PRD.md` + `progress.txt` + `AGENTS.md` | 2025-07 |
| Matt Pocock（[[grill-with-docs]]） | `CONTEXT.md` + 后续 SKILL 文件 | 2026-04 |
| Chris Hayduk（OpenAI FDE，见 [[source-chrishayduk-codex-goals-effectively]]） | `PLAN.md` + `EXPERIMENTS.md` + `SCRATCHPAD.md` | 2026-05-11 |
| OpenAI 官方博客（见 [[source-openai-long-horizon-tasks-codex]]） | `Prompt.md` + `Plan.md` + `Implement.md` | 2026-05-05 |
| George Nurijanian（PM OS） | spec / plan / status 三文件 | 2026-05-17 |

**当 5 拨完全独立的人在不同问题上独立重新发明同一个 pattern，PM 应该把它当成稳定原型来用**，而不是再问"哪家工具更好"。这是行业级 design pattern，不是某家的 feature。

三文件具体分工（取 Chris Hayduk 的命名，因为最清晰）：

- **PLAN.md**：高层方向。**人 seed 初始想法**；agent 偶尔读，用来自我对齐。变更频率最低。
- **EXPERIMENTS.md**：每次尝试的记录（标题 + 简述 + 结果）。**Chris 明确说"三文件里这个最重要"** —— 防止 agent 重复犯过的错误。
- **SCRATCHPAD.md**：实时按时间顺序的思考流。**给你审计用的** —— 发现跑偏就回去改 PLAN.md。

PM 的角色因此变了一件事：**以前 spec 是 *"给工程师看的内部沟通文档"*，现在 spec 是 *"agent 的执行接口"***。George 给了一个很 sharp 的命名：**spec is now the product surface**（spec 现在是产品界面）。

PM 的 deliverable 没消失，**它升级了**。Spec 写得好不好不再是"团队对齐效率"问题，**它直接决定 agent 这一晚跑出来的东西能不能 ship**。这恰恰是 PM craft 的升级窗口 —— 不是 PM 被 AI 取代，是 PM 的杠杆变大了。

---

### 转换 3：从 Fire-and-forget 到 Calibrate-then-forget（从一键到先校准）

第三个转换是大多数 demo 视频不告诉你的部分 —— **AFK 不是"按一下就走"，是"先看头几轮，再走"**。

George 起了一个诗意但准确的名字：**calibration phase**（校准阶段）。一句话：

> "The loop becomes useful after the spec survives contact with the model."
> Loop 在 spec 经历了与模型的接触并幸存之后，才变得有用。

translate 成实操：**写完 spec 不要立刻关电脑**。启动 loop，**坐着看头 3-5 个 iteration**。这不是"不信任 agent"，是知道 *任何 spec 都需要先经历模型的实际工作场景检验*。新员工 onboarding 第一周你也要坐旁边看 —— 不是因为不信任他，是因为你的工作指令必须经过实际工作检验。

**Calibration 时具体在看什么**（[[source-nurijanian-goal-for-pms]] 给的 checklist）：

| 你看到什么 | 立刻做什么 |
|---|---|
| agent misunderstand 了目标 | Stop → edit spec → restart |
| agent 写错的 test 来 bless 错的行为 | Stop → fix validation 协议 → restart |
| agent 改了不该改的文件 | Stop → 加 scope boundary → restart |
| agent 反复问同一个问题 | Stop → spec 有 ambiguity，明确化 |

OpenAI 用了一个更操作的命名（见 [[source-openai-codex-use-case-follow-goals]]），叫 **"tighten the goal" pattern**：

> "Tighten vague goals rather than adding ad hoc instructions mid-run."
> 跑偏时收紧模糊的 goal，不要在中途追加临时指令。

这是反直觉但极重要的规则。你看到 agent 跑偏，第一反应通常是在 chat 里追加："对了，还要 …"。**不要这么做**。原因：

- chat 里的 ad hoc 指令是 conversation-level state
- 下次 compaction / context reset 时，它会消失
- agent 又会跑偏成同一个样子
- 你以为修了，其实没修

正确做法：**pause loop → 完整 rewrite 你的 /goal 命令 → resume**。把修正写进 durable file，不要让它停留在对话气泡里。

跨厂商收敛 +1 —— **Anthropic 和 OpenAI 都在官方文档里独立写下了 "tighten the goal, don't patch with chat" 这条规则**。这不是某家的偏好，是行业级 best practice。

Matt Pocock 角度的补充（见 [[idea-to-afk-agent-flow]]）：他把 calibration 不当一个 phase，而是当一个**渐进式 escalation**：

```
Interactive（人盯着，错了立刻拉回） → Live-data 调试界面 → 收敛 → AFK
```

Matt 的 [[sandcastle|Sandcastle]] 框架甚至把这件事 API 化 —— `createWorktree()` 同一个 worktree 先 `.interactive()` 跑，然后 `.run()` 转 AFK。**同一个 prompt 经过 interactive 检验才允许进 AFK**。

George 的 calibration loop + Matt 的 interactive-to-AFK escalation = **同一件事的两种讲法**：AFK 之前必须有人在场看 agent 跑。**这一步不能跳**。

---

## Part 2：一个完整的 PM 工作流（5 个动作）

三个心智转换是 *为什么*。下面给 *怎么做* —— 一个完整的 PM workflow，5 个动作。每个动作都对应上面某个转换的具体落地。

### 动作 1：把模糊想法 grill 成 spec

**输入**：脑子里的模糊愿望（"我们要做个 X"）
**输出**：写下来的 acceptance criteria + 必要的 ADR

模糊愿望和 strong contract 之间隔着一座桥，桥的名字叫 **interview**。Matt Pocock 把这件事做成了一个 skill 叫 [[grill-with-docs|/grill-with-docs]]：agent 一次问一个问题（带它的推荐答案），用户接受或修正，**所有决定 inline 写入 CONTEXT.md**。

George 在文章里推荐的也是 Matt 这个 skill + Ryan Singer 的 shaping 方法（见 [[source-nurijanian-goal-for-pms]]）。两人在同一个方法论 trajectory 上。

PM 视角的要点：

- 不要试图一次性想清楚 —— 没人能做到
- 一次回答一个问题，每个问题都带 *"我建议是 X，你接受吗"*
- 模型能从代码 / 现有 wiki 答出来的，**不要问你**
- 关键术语 inline 落地（"materialization cascade" 这种领域词汇）

Matt 报告的真实数据：一次 grill 通常 16-50 个问题，30-90 分钟。**这个时间不是浪费 —— 这是你的 strong goal 的成本**。George 也明说："写 strong goal 的 PM 工作量比写传统 ticket 多 2-5 倍。"

但收益是：**spec 一次写好可以复用，agent 跑出来的东西可预测**。

### 动作 2：写 strong goal

**输入**：动作 1 的 spec
**输出**：一个可以丢给 `/goal` 的完整命令

用 George 的 6-section template（见 [[goal-template]]）—— 转换 1 已经给过。

或者用 OpenAI 的 5-step setup（见 [[source-openai-codex-use-case-follow-goals]]）：

1. 命名 objective + stop condition
2. 指向 source materials
3. 定义 validation artifacts
4. 要求 checkpoint reporting
5. 启动后用 `/goal` 命令监控

两者结构同源 —— **George 适合做 spec library 模板，OpenAI 适合做快速 launch checklist**。我建议组合使用：平时按 George 6-section 写完，launch 时跑 OpenAI 5-step 当 preflight。

**特别提醒：qualitative goal 怎么办？**

不是所有目标都能一句话量化。"chapter 划分要自然"这种 qualitative 目标，怎么写？

Chris Hayduk 的 **200-checklist trick**（见 [[source-chrishayduk-codex-goals-effectively]]）—— 让 model 先把"什么算自然"的规则提取成 markdown checklist（可以是 50 条、200 条），目标变成"勾完 N/N 条"。

> "By providing a checklist, we turn a qualitative goal into a quantitative one. Codex just needs to think 'I have completed the goal when I have checked off all 200 out of 200 rules.'"

每一条 checkbox 单独看可能仍 *有点* 主观，但 **单条的主观远好于整体的模糊**。"chapter 是否自然"无法判定；"chapter 是否以 hook 开头"可以判定。

PM 在这里的工作：**写 checklist**。又是 PM 本来就会的活，挪到了 agent 上。

### 动作 3：建 durable file triad

**输入**：strong goal
**输出**：3 个空 markdown 文件（PLAN / EXPERIMENTS / SCRATCHPAD），seeded 好

具体步骤（见 [[agentic-loop-tracking-files]]）：

1. 创建空文件：

   ```
   docs/PLAN.md         （seed 你的方向）
   docs/EXPERIMENTS.md  （空，模板：title / description / result）
   docs/SCRATCHPAD.md   （空，agent 实时写）
   ```

2. 在 `/goal` 命令里**显式引用这三个文件**：

   ```
   Source of truth:
   - read docs/PLAN.md
   - update docs/EXPERIMENTS.md after each attempt
   - append to docs/SCRATCHPAD.md continuously
   ```

3. 在 goal 里明示：**"Read EXPERIMENTS.md before each new attempt"** —— 这一句决定了 agent 会不会重复犯错

### 动作 4：Calibrate 头 3-5 turn

**输入**：跑起来的 loop
**输出**：能放心 AFK 的 spec

转换 3 的实操。**不要写完 spec 立刻关电脑**。看头 3-5 个 turn 对照前面给的 4 条 checklist。

发现问题就 **tighten the goal**，不要 patch in chat。

一个具体信号：**如果 calibration 连续 3 个 turn 都不需要干预，可以放心 AFK 了**。还在干预 = spec 还没收敛，继续 tighten。

### 动作 5：AFK handoff + 审 artifacts

**输入**：通过 calibration 的 spec + triad
**输出**：完成的工作 + 你的 review

启动方式取决于框架：

- **Claude Code**：`/goal <full strong-goal text>` + 加 turn budget（见 [[claude-code-goal]]）
- **Codex**：`/goal <text>` + 用 `/goal pause` / `/goal resume` 监控
- **Sandcastle**：`sandcastle.run({ promptFile, completionSignal, maxIterations })`（见 [[sandcastle]]）

回来之后要审什么：

1. **EXPERIMENTS.md** —— 它尝试了什么 / 哪些 work / 哪些不
2. **validation 是否真跑过** —— 不只看"PASS"字样，看 exit code
3. **boundaries 是否被遵守** —— `git diff` 显示的文件清单是否在 scope 内
4. **SCRATCHPAD.md 后半段** —— 如果有迷茫 / 反复，下次的 spec 需要更明确

**HITL vs AFK 的边界**（见 [[hitl-vs-afk-classification]]）：Matt 的 `/to-issues` 给每个 backlog item 打 HITL / AFK label。**判断规则一句话：done 是否需要人的 taste？需要 → HITL；不需要 → AFK**。

适合 AFK 的：migration / backlog clearing / file splitting / brute-force testing / bounded exploration（这是 George 给的 5 个 natural fit，见 [[goal-template]]）。

不适合 AFK 的：架构决策 / UX copy / API 公开接口设计 / 新功能 framing / 需要 taste 的任何东西。

---

## Part 3：四个反模式（grep 你自己的 prompt）

讲完 *该怎么做*，最后讲 *不该怎么做*。这四条是从 George + OpenAI + Chris 三个源里收敛出来的、最值得拿去 grep 自己最近 prompt 的反模式。

### 反模式 1：形容词式 goal

"better / cleaner / easier / smarter / more polished" —— **任何形容词都是给自己挖坑**。Agent 无从证明 "more polished"，所以它会优化任何容易证明的指标，结果跟你想要的可能毫无关系。

修法：把每个形容词替换成 observable behavior。

- ❌ "improve onboarding"
- ✅ "after signup, users land on a setup checklist; first incomplete step is expanded; completing workspace-profile marks it done without full-page refresh"

### 反模式 2：中途在 chat 里追加指令

转换 3 已经讲过。再重申一次因为太常见 —— 看到 agent 跑偏，**不要**在 chat 里说 "对了，还要 X"。Pause → rewrite goal → resume。

为什么人会犯这个错：因为 chat 追加比 rewrite goal 快。但快带来的代价是 —— 下次 context reset，X 没了。**短期省 30 秒，长期亏 30 turn**。

### 反模式 3：把 exploration loop 偷偷跑 production work

George 原话：

> "The dangerous version is asking an exploratory loop to silently become a production loop."

exploration goal 应该输出 **learning（notes / docs）**，不是 production code。两者混在一起 = 你最后不知道哪些是"我想看看"的产出，哪些是"已经决定要 ship"的产出。

修法：exploration goal 的 acceptance criteria 必须明确 *输出 = 一个 doc / report*，**不允许碰 production 文件**。

### 反模式 4：把 implementation preference 包装成 product goal

PM 视角下最值得警惕的反模式。

- ❌ "refactor into cleaner architecture"
- ❌ "make the code more maintainable"

这些是 **工程审美**，不是 **产品需求**。Agent 拿到这种 goal，会优化它自己觉得"cleaner"的方向，可能跟你想缓解的具体痛点完全无关。

修法：**说出 refactor 要缓解的那个具体痛点**。

- ✅ "split AccountSettings.tsx so billing / profile / notification 可以独立测试。每个 module 拥有自己的 form state。现有行为不能变。done 的标志是每个 module 有自己的 test 文件"

PM 的工作不是描述实现，是描述 *为什么这次实现是必要的*。

---

## 收尾：跨厂商收敛 = PM craft 升级窗口

回看 Part 1 列的几个收敛点：

- **`/goal` 命令**：Anthropic 和 OpenAI 在 4 周内独立 ship 几乎相同的 API（见 [[claude-code-goal]] 跨厂商对比表）
- **6/7-element strong goal**：George + OpenAI 独立给出几乎相同的 contract 结构
- **三文件 durable memory**：5 个独立来源独立发明同一个 pattern
- **"tighten the goal, don't patch"**：OpenAI 官方文档 + George 文章独立写下同一条规则

当一个东西在 4 周内被三家以上独立 reinvent，**它就不是 vendor feature 了，是 industry pattern**。PM 该把它当稳定原型来用。

这意味着什么？

**意味着 PM craft 的杠杆变大了**。以前你写 ticket，效果取决于 engineer 能不能理解你；现在你写 spec，效果取决于你能不能写得让 agent 反复执行 + harness 能验证 + 你能审 artifacts。后者是**远高于普通 ticket** 的标准 —— 但 **PM 本来就该会**。验收标准、定义完成、范围边界、回归测试 —— 这些都是 PM 工具箱里已经有的东西，只是过去你可以含混，现在 agent 把含混直接变成了 token 税。

George 那句 thesis 值得贴在显示器上：

> "Agentic coding does not remove product thinking. It punishes vague product thinking faster."

**它不是要 PM 变工程师**。它只是要 PM 把 PM 本来该做的事情真的做了。

---

## 实操路径

这套方法论值不值得花时间学，最快的判断方式不是再读三篇文章，是 **跑一次**。

配套的实操指南（[[pm-long-horizon-blog2video-practice-guide|drafts/pm-long-horizon-blog2video-practice-guide.md]]）拿 blog2video pipeline 里的 **chapter splitter** 作为练习 case，把上面 5 个动作完整走一遍：

- 怎么 grill 模糊的"我想要好 chapter"成 spec
- 6-section goal 长什么样
- PLAN / EXPERIMENTS / SCRATCHPAD 怎么 seed
- calibration 时具体在看什么
- 跑完后审 artifacts 看什么

跑通一次之后，回来把真实数据填到本文章 —— spec 用时、calibration 干预次数、AFK turn 数、第二次跑省了多少时间 —— **这是把本文从"翻译方法论"升级成"带 case study 的中文 PM 视角文章"的关键素材**。

> 📌 Case study 区段（待补）
>
> 本节留给跑通 chapter splitter 之后回填：
> - 真实 spec 长什么样
> - calibration 干预了几次、修了什么
> - AFK 跑了几个 turn、produce 了几个 successful chapter
> - 跟手工 chapter splitting 的时间对比

---

## 来源

本文方法论部分基于以下 wiki 页面（每个都挂到了文中具体论点）：

- [[source-nurijanian-goal-for-pms]] — George 的 PM-native framing（thesis 锚点）
- [[agent-ready-requirements]] / [[goal-template]] — 7-component + 6-section template
- [[claude-code-goal]] — Claude Code `/goal` 官方
- [[source-openai-codex-cookbook-trilogy]] — OpenAI 三联文（6-element / Repair / Improvement）
- [[source-openai-long-horizon-tasks-codex]] — OpenAI long-horizon awareness 层（freeze the target）
- [[source-openai-codex-use-case-follow-goals]] — OpenAI operational 层（5-step / tighten the goal）
- [[source-chrishayduk-codex-goals-effectively]] — Chris Hayduk 三 tip + 200-checklist
- [[agentic-loop-tracking-files]] — PLAN / EXPERIMENTS / SCRATCHPAD pattern
- [[idea-to-afk-agent-flow]] — Matt Pocock 5 phase（interactive→AFK escalation 引述）
- [[grill-with-docs]] — Matt 的 discovery skill
- [[hitl-vs-afk-classification]] — Matt 的 per-issue label
- [[ralph-wiggum]] — Ralph 历史脉络
- [[sandcastle]] — Matt 的 AFK 框架

跨厂商收敛点的 timeline：

- 2025-07 [[ralph-wiggum|Ralph Wiggum]] 原型问世（Geoffrey Huntley）
- 2026-04 Claude Code `/goal` 官方上线
- 2026-05-05 OpenAI long-horizon 博客
- 2026-05-09 OpenAI Codex `/goal` use case
- 2026-05-09 ~ 05-12 OpenAI Cookbook 三联文
- 2026-05-11 Chris Hayduk 188K-view X 帖
- 2026-05-17 George `/goal for PMs` 文章
