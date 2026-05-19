---
type: draft
status: ready-for-review
created: 2026-05-19
last-updated: 2026-05-19
target-audience: 想用 AI 自主开发的 PM / 独立 builder / 非全职工程师
framing: 三个心智转换 + 一个 PM 工作流 + 四个反模式
source-policy: 只引用第一手官方源（OpenAI Codex 官方 docs + Anthropic Claude Code 官方 docs）和已公开社区方法论（Geoffrey Huntley 的 Ralph Wiggum，Matt Pocock 的 idea-to-AFK 流程 / grill-with-docs / Sandcastle）
based-on:
  - wiki/claude-code-goal.md
  - wiki/source-openai-codex-cookbook-trilogy.md
  - wiki/source-openai-long-horizon-tasks-codex.md
  - wiki/source-openai-codex-use-case-follow-goals.md
  - wiki/ralph-wiggum.md
  - wiki/idea-to-afk-agent-flow.md
  - wiki/grill-with-docs.md
  - wiki/hitl-vs-afk-classification.md
  - wiki/sandcastle.md
companion-guide: drafts/pm-long-horizon-blog2video-practice-guide.md
tags: [drafts, methodology, pm, long-horizon, afk, claude-code-goal, chinese]
---

# 长跑任务（long-horizon task）的 PM 方法论：让 AI agent 跑通一件事，不是按一个按钮

## 开场

过去半年，你大概看过这种演示视频：一句 prompt + 启动一个 loop + agent 自己写一晚上代码 + 早上起来 merge。这个工作模式叫 **AFK（away-from-keyboard）coding** —— 字面意思就是"人不在键盘前"。模型在没有人监督的情况下跑长跑任务（long-horizon task），跑完出门看猫，回来检查结果。

听起来像奇迹。但你自己试就知道，十次有八次得到的不是奇迹 —— 是一堆看起来认真做了、实际不对的 commit。错误的代价还特别高：因为你不在场，agent 不会停下来问你；它会一路沿着自己的理解做下去，错的方向上能跑 20 turn、30 turn，把不对的东西反复打磨到逻辑自洽。

这个失败模式不是 model 的问题。是 **PM 的工作没做完，就被翻译成了 agent 的指令**。

这篇文章的主张：**AFK 不是入口，是奖励**。按下 `/goal` 那个按钮之前，PM 的工作已经做了 80%。写 spec、定义验收标准、把状态外置、看头几轮校准 —— 每一步都是行业内已经收敛的工程实践，只是大多数 demo 视频把它们都省略了，只展示了最后那个"奇迹"瞬间。

下面用三个心智转换把那 80% 拆开讲清楚。每个转换都对应一类"大多数人用 agent 时没做对"的具体动作 —— 你看完应该能 grep 自己最近 10 个 prompt，认领其中至少一个。

---

## Part 1：三个心智转换

### 转换 1：从 Prompt 到 Contract（从对话到合同）

PM 都熟悉一个东西，叫**验收标准**（acceptance criteria）。给同事看的 ticket，验收标准可以含混 —— *"用户应该能更方便地管理通知"* —— 因为同事会问你。

给 agent 跑的 ticket 没有"问你"这一步。Agent 看不懂会按它猜的样子做下去，做 30 turn。

这就是普通 prompt 和 contract 的根本区别（在执行层，OpenAI Codex 官方文档把这两件事明确区分，见 [[source-openai-codex-cookbook-trilogy]]）：

| Prompt | Contract |
|---|---|
| Stateless：每次问完就完 | Stateful：跨多 turn 维持目标 |
| "请帮我做 X" | "做到 Y 状态才停止" |
| 委托劳动 | 委托结果 |
| 失败模式：努力但不收敛 | 失败模式：缺了 contract，loop 退化回 prompt |

Prompt 请求努力。Contract 定义努力何时停止。

**Contract 该包含什么**：OpenAI 在 Codex Cookbook 里给了一个 **6-element strong goal** 形式化框架（见 [[source-openai-codex-cookbook-trilogy]]）。每一项都对应一类常见失败模式的预防：

1. **Outcome** —— 完成时什么应该 true
2. **Verification surface** —— 哪些 test / benchmark / artifact 证明成功
3. **Constraints** —— 什么不能 regress
4. **Boundaries** —— 允许动哪些 files / tools / data
5. **Iteration policy** —— 失败后怎么选下一步
6. **Blocked stop condition** —— 什么情况下停下来报告 blocker

PM 该怎么用？把你最近 5 个 `/goal` 命令拉出来，按这 6 条 grep —— 缺哪条，agent 在那条上就会 hallucinate。

**反共识的点**：很多人以为 "strong goal" 是 "写得很长的 goal"。**Strong goal 的关键不是字数，是是否包含可检验的退出条件**。两行写清楚 "`npm test` exits 0，no files outside `src/auth/` are changed" 远胜于一段抒情。

OpenAI 给的强 goal 模板范例（来自 Cookbook 的 strong-goal 章节）：

> "Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Use only the checkout service and related tests. Between iterations, record changes, benchmark results, and next experiments to attempt. If blocked, stop with attempted paths, evidence, and blockers."

把这条范例的 6 个 element 标注出来，你会发现它读起来像合同条款 —— 因为它就是合同条款。PM 这个职业本来就在写合同（产品交付物的合同），只是合同的"对手方"从同事变成了 agent。

Anthropic 的 [[claude-code-goal|Claude Code `/goal` 官方文档]]给的"writing an effective condition"三件套是同一组件的精简版：**one measurable end state + a stated check + constraints that matter**。两家厂商的 contract 形状已经独立收敛 —— 这是 PM 该认真对待的"行业原型"信号，不是某家的 vendor 偏好。

---

### 转换 2：从 In-Context 到 On-Disk（从对话内存到磁盘记忆）

第一个转换解决"目标在哪"。第二个解决"agent 跑到一半，目标会不会被它自己忘记"。

会。这是 agent loop 最致命的失败模式之一，叫 **context rot**（上下文腐烂）。

机制简单：每个 turn 之间，对话上下文会被 compact（压缩），关键信息可能被 summarize 掉。模型在 hour 50 时可能已经不记得 hour 1 时定义的目标了。OpenAI 官方在 long-horizon coherence 博客（见 [[source-openai-long-horizon-tasks-codex]]）里把这件事讲得很直接：

> "Freeze the target so the agent doesn't build something impressive but wrong."
> 冻结目标，让 agent 不至于建出一个"impressive 但 wrong"的东西。

**解药很反直觉**：把 agent 的"工作记忆"从 in-context 搬到**磁盘上的 markdown 文件**。这些文件每个 turn 都会被重新 load，所以它们是 **跨 compaction 唯一可信的状态载体**。

**这里有一个值得 PM 重视的"原型信号"**：三个独立来源、不同上下文、不同时间，**独立发明了同一个 pattern**：

| 来源 | 三文件命名 | 时间 |
|---|---|---|
| Geoffrey Huntley 的 [[ralph-wiggum|Ralph Wiggum]]（社区经典 autonomous coding loop） | `PRD.md` + `progress.txt` + `AGENTS.md` | 2025-07 |
| Matt Pocock 的 idea-to-AFK 流程（开源 `mattpocock/skills`，87K stars，见 [[grill-with-docs]]） | `CONTEXT.md` + skills 文件 | 2026-04 |
| OpenAI 官方 long-horizon coherence 博客（见 [[source-openai-long-horizon-tasks-codex]]） | `Prompt.md` + `Plan.md` + `Implement.md` | 2026-05 |

**当三波完全独立的人在不同问题上独立重新发明同一个 pattern，PM 应该把它当成稳定原型来用**，而不是再问"哪家工具更好"。这是行业级 design pattern，不是某家的 feature。

取 OpenAI 官方的三文件命名（因为最完整地把三种职责分开）：

- **`Prompt.md`** —— spec + 交付物 + 接受标准。**冻结**，agent 不能动。这是 agent 每个 turn reload 的 source of truth。
- **`Plan.md`** —— 工作分解到 milestone，每个 milestone 有自己的 validation 条件。可演进。
- **`Implement.md`** —— agent 的操作行为手册：用什么工具 / 怎么记录进度 / 什么时候 stop。规定 agent **怎么工作**，跟 agent **建什么**（Prompt.md）独立 evolve。

PM 的角色因此变了一件事：**以前 spec 是"给工程师看的内部沟通文档"，现在 spec 是"agent 的执行接口"**。

PM 的 deliverable 没消失，**它升级了**。Spec 写得好不好不再是"团队对齐效率"问题，**它直接决定 agent 这一晚跑出来的东西能不能 ship**。这恰恰是 PM craft 的升级窗口 —— 不是 PM 被 AI 取代，是 PM 的杠杆变大了。

---

### 转换 3：从 Fire-and-forget 到 Calibrate-then-forget（从一键到先校准）

第三个转换是大多数 demo 视频不告诉你的部分 —— **AFK 不是"按一下就走"，是"先看头几轮，再走"**。

Spec 写在纸上时永远完美。但 spec 真正可用，是在它跟实际 agent 跑过几轮之后 —— 模型在工作过程中会暴露 spec 里所有模糊处。**这一步行业里有正式名字**，OpenAI Codex 官方 use-case 文档（见 [[source-openai-codex-use-case-follow-goals]]）写得很直接：

> "Tighten vague goals rather than adding ad hoc instructions mid-run."
> 跑偏时收紧模糊的 goal，**不要**在中途追加临时指令。

translate 成实操：**写完 spec 不要立刻关电脑**。启动 loop，**坐着看头 3-5 个 iteration**。这不是"不信任 agent"，是知道 *任何 spec 都需要先经历模型的实际工作场景检验*。新员工 onboarding 第一周你也要坐旁边看 —— 不是因为不信任他，是因为你的工作指令需要被实际工作检验。

**校准时具体在看什么**：

| 你看到什么 | 立刻做什么 |
|---|---|
| agent misunderstand 了目标 | Stop → edit spec → restart |
| agent 写错的 test 来 bless 错的行为 | Stop → fix validation 协议 → restart |
| agent 改了不该改的文件 | Stop → 加 scope boundary → restart |
| agent 反复问同一个问题 | Stop → spec 有 ambiguity，明确化 |

**"tighten the goal" 这条规则非常反直觉但极重要**。你看到 agent 跑偏，第一反应通常是在 chat 里追加："对了，还要 …"。**不要这么做**。原因：

- chat 里的 ad hoc 指令是 conversation-level state
- 下次 compaction / context reset 时，它会消失
- agent 又会跑偏成同一个样子
- 你以为修了，其实没修

正确做法：**pause loop → 完整 rewrite 你的 `/goal` 命令 → resume**。把修正写进 durable file，不要让它停留在对话气泡里。

跨厂商收敛 +1 —— **OpenAI Codex 官方 docs 和 Anthropic Claude Code 官方 docs 都独立写下了"tighten the goal, don't patch with chat"这条规则**。这不是某家的偏好，是行业级 best practice。

[[matt-pocock|Matt Pocock]] 的开源 skills 库给了一个不同但同源的角度（见 [[idea-to-afk-agent-flow]]）：他把校准不当一个 phase，而当一个**渐进式 escalation**：

```
Interactive（人盯着，错了立刻拉回） → Live-data 调试界面 → 收敛 → AFK
```

Matt 的 [[sandcastle|Sandcastle]] 框架（4.5K stars）甚至把这件事 API 化 —— `createWorktree()` 同一个 worktree 先 `.interactive()` 跑，然后 `.run()` 转 AFK。**同一个 prompt 经过 interactive 检验才允许进 AFK**。

OpenAI 的 "tighten the goal" + Matt 的 interactive-to-AFK escalation = **同一件事的两种讲法**：AFK 之前必须有人在场看 agent 跑。**这一步不能跳**。

---

## Part 2：一个完整的 PM 工作流（5 个动作）

三个心智转换是 *为什么*。下面给 *怎么做* —— 一个完整的 PM workflow，5 个动作。每个动作都对应上面某个转换的具体落地。

### 动作 1：把模糊想法 grill 成 spec

**输入**：脑子里的模糊愿望（"我们要做个 X"）
**输出**：写下来的 acceptance criteria + 必要的 ADR

模糊愿望和 strong contract 之间隔着一座桥，桥的名字叫 **interview**。Matt Pocock 在他的开源 skills 库里把这件事做成了一个具体技能叫 [[grill-with-docs|/grill-with-docs]]：agent 一次问一个问题（每个问题都带它的推荐答案），用户接受或修正，**所有决定 inline 写入 CONTEXT.md**（领域词汇表 + ADR）。

PM 视角的要点：

- 不要试图一次性想清楚 —— 没人能做到
- 一次回答一个问题，每个问题都带 *"我建议是 X，你接受吗"*
- 模型能从代码 / 现有 wiki 答出来的，**不要问你**
- 关键术语 inline 落地（"materialization cascade" 这种领域词汇）

Matt 自己 report 的真实数据：一次 grill 通常 16-50 个问题，30-90 分钟。**这个时间不是浪费 —— 这是你的 strong goal 的成本**。

收益是：spec 一次写好可以复用，agent 跑出来的东西可预测。值不值得 trade，看你这个 task 会跑多少次。

### 动作 2：写 strong goal

**输入**：动作 1 的 spec
**输出**：一个可以丢给 `/goal` 的完整命令

OpenAI Codex 官方 use-case 文档（见 [[source-openai-codex-use-case-follow-goals]]）给的 **5-step setup** 是最快的 launch checklist：

1. 命名 objective + stopping condition
2. 指向 source materials
3. 定义 validation artifacts
4. 要求 checkpoint reporting
5. 启动后用 `/goal` 命令监控

把 5-step 当快速启动 checklist，把转换 1 的 6-element strong goal 当 spec 的内部结构。我建议组合使用：

```
/goal [一句话目标 + stopping condition]

Source of truth:
- read [spec file (FROZEN)]
- follow [implementation plan]
- update [status file]

Acceptance criteria:
- [observable behavior 1]
- [observable behavior 2]
- [negative case 1]
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

**特别提醒：qualitative goal 怎么办？**

不是所有目标都能一句话量化。"chapter 划分要自然"这种 qualitative 目标，怎么写？

行业里通用的解法叫 **checklist 转化**：让 model 先把"什么算自然"的规则提取成 markdown checklist（可以是 50 条、200 条），目标变成"勾完 N/N 条"。OpenAI Cookbook 里的"Iterative Repair Loop"章节用同一思路把 qualitative review task 转成 structured JSON 评分。

每一条 checkbox 单独看可能仍 *有点* 主观，但 **单条的主观远好于整体的模糊**。"chapter 是否自然"无法判定；"chapter 是否以 hook 开头"可以判定。

PM 在这里的工作：**写 checklist**。又是 PM 本来就会的活，挪到了 agent 上。

### 动作 3：建 durable file triad

**输入**：strong goal
**输出**：3 个空 markdown 文件（Prompt / Plan / Implement），seeded 好

按转换 2 的 OpenAI 官方命名：

```
docs/Prompt.md     （spec + 交付物 + 接受标准，FROZEN）
docs/Plan.md       （milestone + 每个 milestone 的 validation 标准）
docs/Implement.md  （agent 操作行为手册：工具 / 记录格式 / stop 条件）
```

在 `/goal` 命令里**显式引用这三个文件**：

```
Source of truth:
- read docs/Prompt.md (FROZEN — do not modify)
- follow docs/Plan.md
- update docs/Implement.md status block after each milestone
```

在 goal 里明示：**"Read past attempts before proposing the next experiment"** —— 这一句决定了 agent 会不会重复犯错。

OpenAI 在 long-horizon coherence 博客里特别强调一个点：**Prompt.md 必须冻结**，不允许 agent 自己修改。让 agent 修改 Prompt.md = goal drift 几乎必然发生。修 spec 是人的工作。

### 动作 4：Calibrate 头 3-5 turn

**输入**：跑起来的 loop
**输出**：能放心 AFK 的 spec

转换 3 的实操。**不要写完 spec 立刻关电脑**。看头 3-5 个 turn 对照前面给的 4 条 checklist。

发现问题就 **tighten the goal**（rewrite，不要 patch in chat）。

一个具体信号：**如果连续 3 个 turn 你不需要干预，可以放心 AFK 了**。还在干预 = spec 还没收敛，继续 tighten。

### 动作 5：AFK handoff + 审 artifacts

**输入**：通过 calibration 的 spec + triad
**输出**：完成的工作 + 你的 review

启动方式取决于框架：

- **Claude Code**：`/goal <full strong-goal text>` + 加 turn budget（见 [[claude-code-goal]]）
- **Codex**：`/goal <text>` + 用 `/goal pause` / `/goal resume` 监控（见 [[source-openai-codex-use-case-follow-goals]]）
- **Sandcastle**：`sandcastle.run({ promptFile, completionSignal, maxIterations })`（见 [[sandcastle]]）

回来之后要审什么：

1. **Plan.md 的 milestone 完成状态** —— 哪些 pass / 哪些 fail / 哪些跳过
2. **validation 是否真跑过** —— 不只看"PASS"字样，看 exit code
3. **boundaries 是否被遵守** —— `git diff --stat` 显示的文件清单是否在 scope 内
4. **Implement.md status 后半段** —— 如果有迷茫 / 反复，下次 spec 需要更明确

**HITL vs AFK 的边界**（见 [[hitl-vs-afk-classification]]）：Matt Pocock 在 skills 库里给每个 backlog item 打 HITL（human-in-the-loop）或 AFK label。**判断规则一句话：done 是否需要人的 taste？需要 → HITL；不需要 → AFK**。

适合 AFK 的：migration / backlog clearing / file splitting / brute-force testing / bounded exploration（OpenAI Codex 官方文档给的 5 类 natural fit）。

不适合 AFK 的：架构决策 / UX copy / API 公开接口设计 / 新功能 framing / 需要 taste 的任何东西。

---

## Part 3：四个反模式（grep 你自己的 prompt）

讲完 *该怎么做*，最后讲 *不该怎么做*。这四条是从 OpenAI 官方 docs + Anthropic 官方 docs + 社区实践里收敛出来的、最值得拿去 grep 自己最近 prompt 的反模式。

### 反模式 1：形容词式 goal

"better / cleaner / easier / smarter / more polished" —— **任何形容词都是给自己挖坑**。Agent 无从证明 "more polished"，所以它会优化任何容易证明的指标，结果跟你想要的可能毫无关系。

Claude Code `/goal` 官方文档把这条列为 anti-pattern：*"Vague conditions — the evaluator can't judge subjective state."*

修法：把每个形容词替换成 observable behavior。

- ❌ "improve onboarding"
- ✅ "after signup, users land on a setup checklist; first incomplete step is expanded; completing workspace-profile marks it done without full-page refresh"

### 反模式 2：中途在 chat 里追加指令

转换 3 已经讲过。再重申一次因为太常见 —— 看到 agent 跑偏，**不要**在 chat 里说 "对了，还要 X"。Pause → rewrite goal → resume。

为什么人会犯这个错：因为 chat 追加比 rewrite goal 快。但快带来的代价是 —— 下次 context reset，X 没了。**短期省 30 秒，长期亏 30 turn**。

OpenAI 官方 docs 原话：*"Tighten vague goals rather than adding ad hoc instructions mid-run."*

### 反模式 3：把 exploration loop 偷偷跑 production work

OpenAI Codex 官方文档给的 5 种 natural-fit 场景里，exploration 是单独一类 —— 输出应该是 **learning（notes / docs）**，不是 production code。

但实际操作中，PM 经常一边跑 exploration 一边偷偷允许 agent 改 production 文件，结果两者混在一起 —— 你最后不知道哪些是"我想看看"的产出，哪些是"已经决定要 ship"的产出。

修法：exploration goal 的 acceptance criteria 必须明确 *输出 = 一个 doc / report*，**boundary 里禁止碰 production 文件**。

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

回看前面几个收敛点：

- **`/goal` 命令本身**：Anthropic 和 OpenAI 在几周内独立 ship 了几乎相同的 API
- **Strong goal 形式化**：OpenAI 6-element + Anthropic "writing an effective condition" 三件套是同一组件的不同 packaging
- **三文件 durable memory**：Ralph Wiggum（2025-07）/ Matt Pocock 的 CONTEXT.md（2026-04）/ OpenAI 官方 Prompt+Plan+Implement（2026-05）独立发明同一个 pattern
- **"tighten the goal, don't patch"**：OpenAI Codex 官方 docs 独立写下、Matt Pocock 的 interactive→AFK escalation 同源

当一个东西在几周内被多家独立 reinvent，**它就不是 vendor feature 了，是 industry pattern**。PM 该把它当稳定原型来用。

这意味着什么？

**意味着 PM craft 的杠杆变大了**。以前你写 ticket，效果取决于 engineer 能不能理解你；现在你写 spec，效果取决于你能不能写得让 agent 反复执行 + harness 能验证 + 你能审 artifacts。后者是 **远高于普通 ticket** 的标准 —— 但 **PM 本来就该会**。验收标准、定义完成、范围边界、回归测试 —— 这些都是 PM 工具箱里已经有的东西，只是过去 PM 可以含混，现在 agent 把含混直接变成了 token 税。

这并不是要 PM 变工程师。它只是要 PM **把 PM 本来该做的事情真的做了**。模型越聪明，模糊 spec 的代价越高 —— 因为 agent 不会停下来问你，它会沿着错的方向把错的东西越做越深。

模糊 ticket 在 agent 时代要付的，是 token 税。

---

## 实操路径

这套方法论值不值得花时间学，最快的判断方式不是再读三篇文章，是 **跑一次**。

配套的实操指南（[[pm-long-horizon-blog2video-practice-guide|drafts/pm-long-horizon-blog2video-practice-guide.md]]）拿一个真实 content pipeline（blog2video 的 chapter splitter）作为练习 case，把上面 5 个动作完整走一遍：

- 怎么 grill 模糊的"我想要好 chapter"成 spec
- Strong goal 的 6-element 长什么样
- Prompt / Plan / Implement 三文件怎么 seed
- calibration 时具体在看什么
- 跑完后审 artifacts 看什么

跑通一次之后，回来把真实数据填到本文章 —— spec 用时、calibration 干预次数、AFK turn 数、第二次跑省了多少时间 —— 这是把本文从"行业方法论综述"升级成"带真实 case 的 PM 视角文章"的关键素材。

> 📌 Case study 区段（待补）
>
> 本节留给跑通 chapter splitter 之后回填：
> - 真实 spec 长什么样
> - calibration 干预了几次、修了什么
> - AFK 跑了几个 turn、produce 了几个 successful chapter
> - 跟手工 chapter splitting 的时间对比

---

## 来源

本文方法论部分基于以下第一手源（每个论点在文中都已挂到具体位置）：

**官方 docs**：

- [[claude-code-goal]] — Anthropic Claude Code `/goal` 官方文档（writing an effective condition / anti-patterns / use cases）
- [[source-openai-codex-cookbook-trilogy]] — OpenAI Codex Cookbook 三联文（Using Goals / Iterative Repair / Agent Improvement Loop）
- [[source-openai-long-horizon-tasks-codex]] — OpenAI long-horizon coherence 官方博客（"freeze the target" / Prompt+Plan+Implement triad）
- [[source-openai-codex-use-case-follow-goals]] — OpenAI Codex 官方 use-case "Follow a Goal"（5-step setup / "tighten the goal" pattern / lifecycle commands）

**社区经典**：

- [[ralph-wiggum]] — Geoffrey Huntley 创造的 autonomous AI coding loop pattern（2025-07 至今的演化时间线）
- [[idea-to-afk-agent-flow]] — Matt Pocock 的 5-phase idea-to-AFK 方法论
- [[grill-with-docs]] — Matt Pocock 的 discovery skill（interactive grilling + DDD CONTEXT.md）
- [[sandcastle]] — Matt Pocock 的 TypeScript SDK（productize Ralph 模式 + createWorktree interactive→AFK 桥）
- [[hitl-vs-afk-classification]] — Matt Pocock 的 per-issue HITL/AFK 标签 pattern
