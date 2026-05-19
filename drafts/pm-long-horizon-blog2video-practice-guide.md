---
type: draft
status: practice-guide
created: 2026-05-19
last-updated: 2026-05-19
target-audience: vfan（个人 practice first；跑通后再回填 case study 到主文）
companion-article: drafts/pm-long-horizon-methodology.md
case-project: blog2video — chapter splitter (narration.md → video_1_script.md)
based-on:
  - wiki/goal-template.md
  - wiki/agent-ready-requirements.md
  - wiki/agentic-loop-tracking-files.md
  - wiki/claude-code-goal.md
  - wiki/idea-to-afk-agent-flow.md
  - wiki/grill-with-docs.md
  - wiki/blog2video.md
tags: [drafts, practice-guide, blog2video, claude-code-goal, pm-workflow]
---

# 实操指南：用 blog2video chapter splitter 跑通一次 PM long-horizon workflow

> 📌 **使用说明**：这不是发表文章，是给你（vfan）个人按步骤跑通主方法论的 practice guide。每个动作都对应 [[pm-long-horizon-methodology|主文]] Part 2 里 5 个动作之一。
>
> 跑完后填底部的"复盘记录"，那些数据就是 case study 素材，可以回填到主文。

---

## 为什么挑这个 case

[[blog2video]] 现有 pipeline 里 `narration.md → video_1_script.md` 这一步要做 chapter splitting（插入 `[SLIDE N]` markers + timecodes）。这个任务符合 strong goal 的 5 个特征：

1. **可量化 done**：脚本被 chapter 分割完整 / 每个 chapter 满足格式 / manifest 能生成
2. **machine-verifiable**：格式检查脚本可写
3. **bounded**：只动 `docs/output/`，不动 `raw/`
4. **真实业务价值**：每个视频都要做，做好一次复用无数次
5. **不需要纯 taste**：质量主要由 checklist 决定，主观成分少

所以这是 PM workflow 的 ideal practice candidate。

主文 Part 2 给的工作流（5 个动作）下面会逐个走一遍。你可以从动作 1 开始按步骤做，也可以先通读建立 mental model 再开始。

---

## 动作 1 — Grill：把"我想要好 chapter"变 spec

> 对应主文转换 1（Prompt→Contract）和 Part 2 动作 1。

打开你的 blog2video repo，跑：

```
/grill-with-docs

我想要 build 一个 chapter splitter。输入是 docs/input/narration.md，输出是带 [SLIDE N] markers + timecodes 的 docs/output/video_1_script.md。帮我把"什么是好 chapter"问清楚。
```

预期 agent 会问类似这样的问题（每个带它的推荐答案）：

- 每个 chapter 时长目标？（推荐 30-60 秒，按 200 WPM ≈ 100-200 字英文 / 150-300 字中文）
- chapter 内部结构？（推荐 hook + 论点 + 例证三段）
- 第一个 chapter 有什么硬性约束？（推荐：必须 8 秒内带出 thesis）
- 最后一个 chapter 有什么硬性约束？（推荐：必须以 CTA 结尾）
- 总 narration / 文章长比例？（推荐 ≤ 1/3）
- 哪些"反 pattern"禁止？（推荐：no "summary" / "overview" / 元描述）
- chapter 之间允许内容重复吗？（推荐：禁止）
- 视觉切换最小单位？（推荐：每 chapter ≥ 1 个 `[SLIDE N]`）
- narration 输入的字数下限 / 上限？（边界 case 早问早收益）

**操作**：让 agent 问到它觉得问够了（**不要打断**），最后产出落到 `docs/chapter-spec.md`。

**第一次 calibration 信号**：grill 过程中如果你发现自己 30% 以上的问题都答 "我不知道，agent 你建议"，说明你脑子里这个 feature 没想清 —— 这本身就是这一步的价值。把这些"自己没想清"的点单独 mark 一下，它们就是你未来 spec 最容易出问题的部位。

**预期产出**：~50 行 markdown，是你的 chapter contract v0。

---

## 动作 2 — 写 strong goal

> 对应主文 Part 2 动作 2。

打开 `docs/chapter-spec.md`，用 [[goal-template|George 的 6-section template]] 转成可以丢给 `/goal` 的命令。下面是一个起点模板（你可能要根据动作 1 grill 的实际结果调整）：

```
/goal 给 docs/input/narration.md 生成 docs/output/video_1_script.md，符合 docs/chapter-spec.md 的全部 acceptance criteria

Source of truth:
- read docs/chapter-spec.md (FROZEN — do not modify)
- read docs/input/narration.md
- follow docs/PLAN.md
- update docs/EXPERIMENTS.md after each attempt
- append to docs/SCRATCHPAD.md continuously

Acceptance criteria:
- 每个 chapter narration 在 30-60 秒（按 200 WPM 计算 word count）
- 每个 chapter 三段结构：hook (1 sentence) + 论点 (2-3 sentences) + 例证 (1-2 sentences)
- 第一个 chapter 必须 8 秒内带出 thesis（即前 25 words 内）
- 最后一个 chapter 必须以 CTA 结尾（关键词："如果你..." / "关注" / "订阅" / "下一篇"）
- 总 narration 时长 ≤ 原文阅读时长 × 1/3
- negative case: 不出现 "summary" / "overview" / "in this section" / "in this chapter" 等元描述
- 每个 chapter 至少 1 个 [SLIDE N] marker
- chapter 之间禁止内容重复（同一论点不重复出现）

Validation:
- npm run validate-chapter-format docs/output/video_1_script.md exits 0
- npm run build-manifest docs/output/video_1_script.md exits 0

Boundaries:
- only edit docs/output/video_1_script.md
- only edit docs/EXPERIMENTS.md, docs/SCRATCHPAD.md
- do not modify raw/* (anything)
- do not modify docs/input/narration.md
- do not modify docs/chapter-spec.md (this is the FROZEN spec)

Loop behavior:
- after generating each chapter, run `npm run validate-chapter-format`
- update docs/EXPERIMENTS.md with: attempt # / approach / which criteria passed / which failed
- if validation fails, retry once with adjusted approach (record both in EXPERIMENTS.md)
- emit <promise>COMPLETE</promise> when all chapters pass validation
- stop after 20 turns if blocked, write blocker reason to EXPERIMENTS.md
```

**第二次 calibration 信号**：写完这个 goal 后，**读一遍找形容词**。grep "good" / "clean" / "natural" / "smooth" 这些词，每出现一处 → 替换成 observable behavior。

**先写一个 validate-chapter-format 脚本**。这个脚本本身就是你的 spec 的可执行形态。建议大致结构：

```ts
// scripts/validate-chapter-format.ts
// 输入: docs/output/video_1_script.md
// 输出: exit 0 / exit 1 + stdout 列出失败原因
//
// 检查项：
// 1. 每个 [SLIDE N] 段 word count 在 100-300 之间（30-60s @ 200 WPM，中英混合放宽）
// 2. 每个 chapter 第 1 句是 hook（启发式：以问号 / 数字 / 反常识陈述开头）
// 3. 第一个 chapter 前 25 words 包含 thesis 关键词（spec 里列出）
// 4. 最后 chapter 包含 CTA 关键词
// 5. 总 word count ≤ 原文 word count × 1/3
// 6. grep -i "summary|overview|in this section|in this chapter" 不存在
// 7. 每个 [SLIDE N] 之间有非空内容
```

**这一步耗时**：第一次写 spec + validator 估计 1-2 小时。这就是 George 说的"PM 工作量增加 2-5×"。**这是一次性成本，后面每个视频跑 chapter splitting 都白赚**。

---

## 动作 3 — 建 durable file triad

> 对应主文转换 2（In-context→On-disk）和 Part 2 动作 3。

```bash
cd path/to/blog2video/
touch docs/PLAN.md docs/EXPERIMENTS.md docs/SCRATCHPAD.md
```

`docs/PLAN.md` seed：

```markdown
# Plan: Chapter Splitter v0

## Direction
Take narration.md → produce video_1_script.md with [SLIDE N] markers,
满足 docs/chapter-spec.md 全部 acceptance criteria。

## Strategy
1. First pass: identify natural chapter boundaries (topic shifts via heading / paragraph breaks)
2. Second pass: enforce length constraints (split too-long chapters, merge too-short)
3. Third pass: shape each chapter into hook + 论点 + 例证 structure
4. Fourth pass: insert [SLIDE N] markers within each chapter
5. Validation pass: run format checker, fix any failures, log to EXPERIMENTS.md

## Known risks
- Article 太短 (< 6 chapters worth): spec 没说怎么办，calibration 时遇到要补
- 含代码块: narration 里如果有 inline code，chapter 切分要尊重边界
- 多语言混排: 中英文混排时 word count 计算需校准

## Open questions
- (留给 calibration 时发现的)
```

`docs/EXPERIMENTS.md` 留空（agent 会按下面模板写）：

```markdown
# Experiments Log

<!-- Agent will append entries below. Format:

## Attempt N — <short title>
**Approach:** <one sentence>
**Result:** <pass/fail + which criteria>
**Conclusion:** <next step>

-->
```

`docs/SCRATCHPAD.md` 留空（agent 实时 append）。

---

## 动作 4 — Calibrate 头 3-5 turn

> 对应主文转换 3（Fire-and-forget → Calibrate-then-forget）和 Part 2 动作 4。

启动：

```
claude
> /goal <粘贴动作 2 的全文>
```

**坐着看头 5 个 turn**。每个 turn 完，你做以下事：

1. 看 `SCRATCHPAD.md` 最新 entry —— agent 在想什么？
2. 看 `EXPERIMENTS.md` 最新 entry —— 它尝试了什么 / 结果？
3. 看实际生成的 `video_1_script.md` —— 跟你想要的差多远？

**预期会发现以下问题之一**（基于跨源经验总结）：

- **问题 A**：agent 把第一段 narration 直接当 hook，没做 hook framing。修法：在 spec 里明确"hook 必须是问题 / 反常识陈述 / 数字 / 场景之一"
- **问题 B**：chapter 时长测量用了 character count 不是 word count。修法：在 spec 里写明"use word count × 200 WPM = seconds"，并在 validator 里 lock 死
- **问题 C**：validator 没 catch 到 "in this episode" 这种变体元描述。修法：扩展 validator 的 negative-pattern grep 列表
- **问题 D**：agent 把多个相邻 chapter 写得论点重复（context rot 的早期信号）。修法：在 spec 里加 "Read EXPERIMENTS.md before each new attempt to avoid redundant arguments"
- **问题 E**：agent 改了 `docs/chapter-spec.md` 自己（boundary 违反）。修法：在 boundaries 里再强调一次，加 git pre-commit hook 阻止

**关键**：每次发现问题，**pause loop，rewrite goal**，不要在 chat 里追加。这就是 [[source-openai-codex-use-case-follow-goals|tighten the goal]] 的实操。

**Calibration 完成标志**：连续 3 个 turn 你不需要干预，spec 已经收敛，可以 AFK。

---

## 动作 5 — AFK + 审 artifacts

> 对应主文 Part 2 动作 5。

通过 calibration 后，可以放心 AFK：

```bash
# 方法 A: Claude Code /goal + turn budget
claude -p "/goal <完整 goal text>" --max-turns 20
```

```ts
// 方法 B: Sandcastle（如果想用 Matt 的 framework）
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/chapter-splitter.md", // 把 goal 完整文本放这
  completionSignal: "<promise>COMPLETE</promise>",
  maxIterations: 20,
});
```

跑完回来审：

1. **`EXPERIMENTS.md`** —— 它尝试了什么 / 哪些 work / 哪些不
2. **`npm run validate-chapter-format` exit code** —— 真跑过 / 跑通（不只看"PASS"字样）
3. **`git diff --stat`** —— 改动文件清单是否在 boundaries 内
4. **抽 3 个 chapter 看论点完整性** —— 这是唯一需要你 taste 的步骤
5. **`SCRATCHPAD.md` 后半段** —— 如果有迷茫 / 反复，下次 spec 需要更明确

---

## Calibration 信号 cheat sheet

| 看到 | 修哪里 |
|---|---|
| agent 反复在 EXPERIMENTS.md 试同一个错误 | EXPERIMENTS.md 模板加 "lessons learned" 字段，强制 agent 读历史 |
| 跑了 5 turn 还在第一个 chapter 上磨 | spec 太严，先放宽 acceptance criteria，AFK 后再 tighten |
| validator pass 但 chapter 看着 still bad | spec 有 gap，validator 没 catch → 加 validation 规则 |
| agent 改了 docs/chapter-spec.md | boundary 违反，加 git pre-commit hook 阻止 + spec 重申 |
| SCRATCHPAD 显示 agent confused 关于 narration 输入格式 | spec 缺 input contract，补一段描述 narration 预期格式 |
| chapter 数远超预期（10+ 个） | spec 没限上限，加 "max chapter count" |
| chapter 之间论点重复 | spec 加 "Read EXPERIMENTS.md before each new attempt" |

---

## 复盘记录（跑完填这里 → 回填到主文 case study 区段）

> 这是把 practice 转 case study 的关键素材。跑完一次后，按下面 prompt 写下来。
> 这些数据会让主文从"翻译方法论"升级成"带真实案例的中文 PM 视角文章"。

**Spec 阶段**：
- [ ] 这次 grill 用时（分钟）：
- [ ] Grill 总问题数：
- [ ] 你答 "agent 你建议" 的占比：
- [ ] 最终 chapter-spec.md 行数：
- [ ] Validator 脚本写了多久：

**Calibration 阶段**：
- [ ] 干预了几次：
- [ ] 每次干预修了 spec 哪一条（按时间列）：
  1.
  2.
  3.
- [ ] Calibration 总耗时：
- [ ] 第几个 turn 之后开始连续 3 turn 不需干预：

**AFK 阶段**：
- [ ] 总 turn 数：
- [ ] 失败 attempt 数（看 EXPERIMENTS.md）：
- [ ] 成功 attempt 数：
- [ ] 总 wall clock 时间：
- [ ] 最终 validation 是否 pass：
- [ ] 你抽查 chapter 后的 taste 评分（1-5）：

**ROI 数据**：
- [ ] 这次（spec + validator + AFK）总时间：
- [ ] 你以前手做一次 chapter splitting 大概多久：
- [ ] 第二次跑（用同一 spec，不同 narration）需要多久：

**Spec evolution 数据**：
- [ ] grill 阶段没想到、calibration 才补的 acceptance criteria（这是 spec 漏洞 catalog）：
  -
  -
  -
- [ ] AFK 阶段被 EXPERIMENTS.md 暴露的 spec 漏洞（如果有）：
  -

**意外发现**：
- [ ] 哪些预期之外的事情发生了（agent 用了你没想到的方法 / 出现了 spec 没覆盖的边界 case）：
  -

---

## 来源

- 主文: [[pm-long-horizon-methodology|drafts/pm-long-horizon-methodology.md]]
- 配套 wiki: [[goal-template]], [[agent-ready-requirements]], [[agentic-loop-tracking-files]], [[claude-code-goal]], [[idea-to-afk-agent-flow]], [[grill-with-docs]]
- 项目背景: [[blog2video]]
