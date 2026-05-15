---
type: source-summary
created: 2026-05-15
last-updated: 2026-05-15
sources:
  - raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md
tags: [wiki, source, codex, openai, loop, goal-mode]
---

# Source: Chris Hayduk — Using Codex Goals Effectively

## Summary
Long-form X article by **Chris Hayduk** (@ChrisHayduk, FDE Life Sciences @ OpenAI), 2026-05-11. **188K views, 2,736 bookmarks** (bookmark-to-like ratio ~2.3×, high reference-saving intent). Three-tip playbook for using Codex's `/goal` command — which is the **OpenAI parallel to [[claude-code-goal|Claude Code's `/goal`]]**. The advice is vendor-agnostic: it's about loop dynamics, not Codex-specific. First **OpenAI-insider source** in our wiki, useful as a cross-vendor validation point.

## Source
- **URL:** https://x.com/chrishayduk/status/2053807198870880743
- **Posted:** 2026-05-11 11:59 AM
- **Engagement (at fetch, 2026-05-15):** 188,209 views · 2,736 bookmarks · 1,173 likes · 129 RT · 25 replies
- **Bookmark-to-like ratio:** ~2.33× (high reference-saving intent)
- **Fetch method:** Playwright MCP

## 要点解读

### 1. **第一个洞察：模型越聪明，prompt 反而要写得越具体（在 loop 模式下）**
Chris 开篇就给了一个反直觉的观察：
> "Models have gotten so good over the past ~6 months that many of us have gotten lazy as prompters in our everyday workflows... This prompting style, however, is **a major failure mode I've seen when using goal mode**."

平时聊天用 GPT-5.5，你随便说一句它都能懂。但 `/goal` 模式下这种 vague prompt 直接破坏 loop。

**为什么：** Loop 模式核心是循环 —— 执行 → 打分 → 检查是否满足目标 → 继续 or 终止。**第三步（"是否满足"）是关键。** 如果目标是 "make my code better"，agent 根本无法判断何时算 better、何时算 better enough。结果两种失败模式：
- **过早放弃**（agent 工作几分钟就觉得"够好了"，停了）
- **永不停止**（agent 不停乱改，追逐一个不可能达成的目标）

正确做法：**量化目标**。例：
> "Reduce the runtime of the code contained in [file] by 20% without causing any regressions in existing unit tests and integration tests."

明确目标（20% runtime 减少）+ 明确约束（不能让现有测试 regression）。

### 2. **200 条清单技巧 ⭐ —— 把定性目标变成定量目标**
最有迁移价值的一段。Chris 给了个真实例子：把一篇 NeurIPS 论文 preprint 转成 ICML workshop format。ICML 的格式约束在一个 LaTeX 文件里，**不可直接 grade**。

他让 Codex 把这些规则**提取成一个 markdown 清单 —— 200 多条格式和风格规则**。然后目标变成：
> "Change the NeurIPS paper to ICML format based on the provided checklist.md without changing any of the technical content."

**关键洞察：** 每条规则单独看可能仍然 vague（"figures should have proper captions"），**但 Codex 推理"某一条是否完成"的能力比推理"整体目标是否模糊"的能力强得多**。

加分操作：**让 model 完成时把 checkbox 勾掉**。这样 model 自己在文件系统里持久化进度，你也能视觉跟踪。

**通用模式：** 把"质量好坏"→ "若干检查点是否都过了"。这其实就是 [[sprint-contracts]] 的轻量级实现 —— evaluator/generator 在执行前就清单化什么叫"完成"。

### 3. **第二个洞察：feedback loop 速度本身就是 leverage**
> "In order for your agent to evaluate its actions against your goal, it will need some mechanism by which to test its changes. **The faster you can run this test, the faster your model will get feedback on its progress.**"

具体例子（他自己在做的）：搜索更好的 protein structure model 架构。原本完整训练要**几天**才能打分一次。他改用一个小数据集 + 小模型，**评分时间从天降到分钟**。同样的 loop 跑一晚，能尝试的架构多 10-100 倍。

**通用建议：** 找任何方法加速 feedback loop —— **只要不严重损害评分质量**。

**对本 vault 的启示：** 如果 future 给 `/draft` 加 quality-gate-loop（[[quality-gate-loop]]）—— 每一遍 score+rewrite 不能太慢。否则 loop 永远不能收敛。Chris 的原则是这一类工作的硬规则。

### 4. **第三个洞察 ⭐⭐ —— 三个 markdown 文件作为外置工作记忆**
最实操、最具迁移价值的一段。Chris 说 `/goal` 模式可以让 GPT-5.5 跑**几天**。即使 compaction 再强，模型在几天的时间跨度上也维持不住连贯。

解决方案：**把工作记忆从 context 移到磁盘上**。他给 agent 三个 markdown 文件：

| 文件 | 内容 | 用途 |
|------|------|------|
| **PLAN.md** | High-level 计划 + 方向 | agent 偶尔读，自我对齐 |
| **EXPERIMENTS.md** | 每次实验的 title + 描述 + 结果 | **最重要的一个** —— 防止重复失败的尝试 |
| **SCRATCHPAD.md** | 实时按时间顺序的想法流 | **你**审计 agent 思路用，发现跑偏就在 PLAN.md 里干预 |

Chris 原话："**EXPERIMENTS.md is the most important of the three**" —— 因为它让 agent 和你都能 review 之前的尝试和为什么成功/失败。

**这一段是 long-running loop 工程实践的核心。** 我新建了 [[agentic-loop-tracking-files]] 把这个 pattern 抓住。

### 5. **跨厂商收敛信号 —— Codex `/goal` ≈ Claude Code `/goal`**
最值得记的一点：Codex 现在有 `/goal` 命令，**和 Claude Code 的 `/goal` 几乎是同一个东西**。

| Dimension | Claude Code `/goal` | Codex `/goal` |
|---|---|---|
| 触发方式 | `/goal <condition>` | `/goal <condition>` |
| 机制 | 小快 model (Haiku) 作为 evaluator 检查每个 turn | Codex 内部 loop 检查每个 action |
| 失败模式 | 模糊条件 → 永不结束 / 过早结束 | 模糊条件 → 同样的两个失败模式 |

**这是 agentic CLI 产品在跨厂商收敛**。OpenAI 和 Anthropic 都意识到"长时间 autonomous loop"是 next-gen 用户需求，且采用了相似的 API（一个 slash command + 一个目标条件 + 内部 loop 机制）。

Chris 的 3 条 tip 都跨厂商适用：
1. 量化目标
2. 紧 feedback loop
3. 三文件追踪

也就是说：**这是 agentic loop 设计的通用原则，不是 Codex 专属。** 应用到 Claude Code `/goal`、`/ralph-loop`、甚至我们自己未来可能写的 loop skill，都成立。

### 6. **作者背景值得记 —— OpenAI 内部视角**
Chris 是 **FDE (Forward Deployed Engineer), Life Sciences @ OpenAI**。FDE = 嵌入到特定客户/领域里的工程师（类似 Palantir 的 FDE 角色）。**他写的 "internally at OpenAI" 暗示他不只在 side project 用 goal mode，OpenAI 内部的实际生产工作流也在用。**

这是我们 wiki 第一个 OpenAI 内部源。之前都是 Anthropic / Claude Code / Y Combinator 侧的。这种 cross-vendor balance 健康 —— 可以让我们看到收敛点（如这次的 `/goal`）和差异点（未来可能出现的）。

## Pages created from this source
- [[chris-hayduk]] — entity (first OpenAI-insider in wiki)
- [[agentic-loop-tracking-files]] — concept (PLAN.md + EXPERIMENTS.md + SCRATCHPAD.md pattern)
- [[source-chrishayduk-codex-goals-effectively]] — this page

## Pages updated from this source
- [[claude-code-goal]] — cross-vendor convergence note (Codex `/goal` parallel); Chris's 3 tips applied; "three tracking files" as anti-anti-pattern
- [[sprint-contracts]] — 200-checklist trick as canonical example of qualitative→quantitative conversion
- [[verification-loops]] — "tight feedback loop" emphasis (Chris's protein-structure days→minutes example)
- [[index]], [[log]]

## Connections
- Related: [[chris-hayduk]], [[agentic-loop-tracking-files]], [[claude-code-goal]], [[sprint-contracts]], [[verification-loops]], [[quality-gate-loop]], [[skillify-meta-skill]], [[ralph-wiggum]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-15 | raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md | Initial creation |
