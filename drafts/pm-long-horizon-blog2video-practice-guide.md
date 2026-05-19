---
type: draft
status: practice-guide
created: 2026-05-19
last-updated: 2026-05-19
target-audience: vfan（个人 practice first；跑通后再回填 case study 到主文）
companion-article: drafts/pm-long-horizon-methodology.md
case-project: blog2video — chapter splitter (narration.md → video_1_script.md)
source-policy: 与主文一致 —— 只引用 OpenAI / Anthropic 官方 docs + Ralph Wiggum 社区经典 + Matt Pocock 公开材料
based-on:
  - wiki/claude-code-goal.md
  - wiki/source-openai-codex-cookbook-trilogy.md
  - wiki/source-openai-codex-use-case-follow-goals.md
  - wiki/source-openai-long-horizon-tasks-codex.md
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

我想要 build 一个 chapter splitter。输入是 docs/input/narration.md，
输出是带 [SLIDE N] markers + timecodes 的 docs/output/video_1_script.md。
帮我把"什么是好 chapter"问清楚。
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

**第一次校准信号**：grill 过程中如果你发现自己 30% 以上的问题都答 "我不知道，agent 你建议"，说明你脑子里这个 feature 没想清 —— 这本身就是这一步的价值。把这些"自己没想清"的点单独 mark 一下，它们就是你未来 spec 最容易出问题的部位。

**预期产出**：~50 行 markdown，是你的 chapter contract v0。

---

## 动作 2 — 写 strong goal

> 对应主文 Part 2 动作 2。

打开 `docs/chapter-spec.md`，按主文给的"OpenAI 5-step + 6-element 组合"模板转成可以丢给 `/goal` 的命令。下面是一个起点模板（你可能要根据动作 1 grill 的实际结果调整）：

```
/goal 给 docs/input/narration.md 生成 docs/output/video_1_script.md，
符合 docs/chapter-spec.md 的全部 acceptance criteria

Source of truth:
- read docs/chapter-spec.md (FROZEN — do not modify)
- read docs/input/narration.md
- follow docs/Plan.md
- update docs/Implement.md status block after each milestone
- append turn-level thinking to docs/Implement.md scratchpad

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
- only edit docs/Plan.md, docs/Implement.md
- do not modify raw/* (anything)
- do not modify docs/input/narration.md
- do not modify docs/chapter-spec.md (this is the FROZEN spec)

Loop behavior:
- after generating each chapter, run `npm run validate-chapter-format`
- update docs/Plan.md milestone status: which criteria passed / failed
- if validation fails, retry once with adjusted approach (log both attempts in Implement.md)
- emit <promise>COMPLETE</promise> when all chapters pass validation
- stop after 20 turns if blocked, write blocker reason to Implement.md
```

**第二次校准信号**：写完这个 goal 后，**读一遍找形容词**。grep "good" / "clean" / "natural" / "smooth" 这些词，每出现一处 → 替换成 observable behavior。

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

**这一步耗时**：第一次写 spec + validator 估计 1-2 小时。这是 strong goal 的一次性成本，后面每个视频跑 chapter splitting 都白赚。

---

## 动作 3 — 建 durable file triad

> 对应主文转换 2（In-context→On-disk）和 Part 2 动作 3。
>
> 三文件按 OpenAI 官方 long-horizon coherence 博客的命名（[[source-openai-long-horizon-tasks-codex]]）：Prompt.md / Plan.md / Implement.md。

```bash
cd path/to/blog2video/
# Prompt.md 已经存在了（就是 chapter-spec.md，先 alias 一下，或保持 chapter-spec.md 也行）
touch docs/Plan.md docs/Implement.md
```

**`docs/Plan.md` seed**：

```markdown
# Plan: Chapter Splitter v0

## Direction
Take narration.md → produce video_1_script.md with [SLIDE N] markers,
满足 docs/chapter-spec.md 全部 acceptance criteria。

## Milestones

### M1 — Identify chapter boundaries
- Pass condition: 找出 N 个 candidate boundaries（基于 heading / paragraph topic shift）
- Validation: candidate count 在 [⌈article_words / 300⌉, ⌈article_words / 100⌉] 区间

### M2 — Enforce length constraints
- Pass condition: 每个 chapter word count 在 [100, 300] 之间
- Validation: `npm run validate-chapter-format -- --length-only`

### M3 — Shape into hook + 论点 + 例证
- Pass condition: 每个 chapter 第 1 句是 hook 形式
- Validation: heuristic check（问号 / 数字 / 反常识开头）

### M4 — Insert [SLIDE N] markers
- Pass condition: 每个 chapter ≥ 1 个 [SLIDE N]
- Validation: marker count check

### M5 — Final validation pass
- Pass condition: `npm run validate-chapter-format` exit 0
- Validation: full validator + 抽 3 个 chapter 人眼 review

## Known risks
- Article 太短 (< 6 chapters worth): spec 没说怎么办，calibration 时遇到要补
- 含代码块: narration 里如果有 inline code，chapter 切分要尊重边界
- 多语言混排: 中英文混排时 word count 计算需校准

## Open questions
- (留给 calibration 时发现的)
```

**`docs/Implement.md` seed**（agent 的操作 runbook + 实时 log）：

```markdown
# Implement: Chapter Splitter

## How this agent operates

Tools allowed: Read, Write, Edit, Bash (only for npm test/validate commands).
NOT allowed: editing files outside the Boundaries list in /goal.

Per-turn protocol:
1. Read docs/chapter-spec.md (FROZEN source of truth)
2. Read docs/Plan.md for current milestone
3. Read this file's "Attempt log" below — DO NOT repeat previous failed approaches
4. Execute the smallest meaningful change toward current milestone
5. Run validation, log result here in "Attempt log"
6. Update docs/Plan.md milestone status

## Stop conditions
- Emit <promise>COMPLETE</promise> when all M1-M5 milestones pass
- Stop after 20 turns total, write blocker to "Blocker log" below

## Attempt log

<!-- Agent appends. Format:

### Attempt N — <one-line title>
**Approach:** <what you tried>
**Result:** <pass/fail + which criteria>
**Conclusion:** <next step>

-->

## Scratchpad (chronological)

<!-- Agent appends turn-level thoughts here. Auditor reads this to spot drift. -->

## Blocker log

<!-- Only filled if agent stops due to blocker. -->
```

**为什么按这个命名而不是别的**：主文转换 2 给的"三波独立 reinvent 同一 pattern"信号 —— 取 OpenAI 官方命名是因为它把"建什么 (Prompt)"和"怎么建 (Implement)"分得最清楚，PM review 时一眼能找到要看的东西。

---

## 动作 4 — Calibrate 头 3-5 turn

> 对应主文转换 3（Fire-and-forget → Calibrate-then-forget）和 Part 2 动作 4。

启动：

```
claude
> /goal <粘贴动作 2 的全文>
```

**坐着看头 5 个 turn**。每个 turn 完，你做以下事：

1. 看 `Implement.md` Scratchpad 最新 entry —— agent 在想什么？
2. 看 `Implement.md` Attempt log 最新 entry —— 它尝试了什么 / 结果？
3. 看实际生成的 `video_1_script.md` —— 跟你想要的差多远？

**预期会发现以下问题之一**（基于跨源经验总结）：

- **问题 A**：agent 把第一段 narration 直接当 hook，没做 hook framing。修法：在 spec 里明确"hook 必须是问题 / 反常识陈述 / 数字 / 场景之一"
- **问题 B**：chapter 时长测量用了 character count 不是 word count。修法：在 spec 里写明"use word count × 200 WPM = seconds"，并在 validator 里 lock 死
- **问题 C**：validator 没 catch 到 "in this episode" 这种变体元描述。修法：扩展 validator 的 negative-pattern grep 列表
- **问题 D**：agent 把多个相邻 chapter 写得论点重复（context rot 的早期信号）。修法：在 spec 里加 "Read Implement.md Attempt log before each new chapter to avoid redundant arguments"
- **问题 E**：agent 改了 `docs/chapter-spec.md` 自己（boundary 违反 + 冒犯了 FROZEN 规则）。修法：在 boundaries 里再强调一次，加 git pre-commit hook 阻止

**关键**：每次发现问题，**pause loop，rewrite goal**，不要在 chat 里追加。这就是 OpenAI Codex 官方文档（[[source-openai-codex-use-case-follow-goals]]）的 "tighten the goal" 模式 —— 短期省 30 秒的 chat patch，长期亏 30 turn。

**Calibration 完成标志**：连续 3 个 turn 你不需要干预，spec 已经收敛，可以 AFK。

---

## 动作 5 — AFK + 审 artifacts

> 对应主文 Part 2 动作 5。

通过 calibration 后，可以放心 AFK：

```bash
# 方法 A: Claude Code /goal + turn budget（见 wiki/claude-code-goal）
claude -p "/goal <完整 goal text>" --max-turns 20
```

```ts
// 方法 B: Sandcastle（如果想用 Matt Pocock 的 framework，见 wiki/sandcastle）
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

1. **`Plan.md` milestone 完成状态** —— M1-M5 哪些 pass / 哪些 fail
2. **`Implement.md` Attempt log** —— agent 尝试了什么 / 哪些 work / 哪些不
3. **`npm run validate-chapter-format` exit code** —— 真跑过 / 跑通（不只看 "PASS" 字样）
4. **`git diff --stat`** —— 改动文件清单是否在 boundaries 内
5. **抽 3 个 chapter 看论点完整性** —— 这是唯一需要你 taste 的步骤
6. **`Implement.md` Scratchpad 后半段** —— 如果有迷茫 / 反复，下次 spec 需要更明确

---

## Calibration 信号 cheat sheet

| 看到 | 修哪里 |
|---|---|
| agent 反复在 Attempt log 试同一个错误 | Implement.md protocol 加 "Read Attempt log before each turn" 强制 |
| 跑了 5 turn 还在第一个 chapter 上磨 | spec 太严，先放宽 acceptance criteria，AFK 后再 tighten |
| validator pass 但 chapter 看着 still bad | spec 有 gap，validator 没 catch → 加 validation 规则 |
| agent 改了 docs/chapter-spec.md | boundary 违反，加 git pre-commit hook 阻止 + spec 重申 FROZEN |
| Scratchpad 显示 agent confused 关于 narration 输入格式 | spec 缺 input contract，补一段描述 narration 预期格式 |
| chapter 数远超预期（10+ 个） | spec 没限上限，加 "max chapter count" |
| chapter 之间论点重复 | Implement.md 强制"先读 Attempt log 再写新 chapter" |

---

## 复盘记录（跑完填这里 → 回填到主文 case study 区段）

> 这是把 practice 转 case study 的关键素材。跑完一次后，按下面 prompt 写下来。
> 这些数据会让主文从"行业方法论综述"升级成"带真实案例的中文 PM 视角文章"。

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
- [ ] 失败 attempt 数（看 Implement.md Attempt log）：
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
- [ ] AFK 阶段被 Attempt log 暴露的 spec 漏洞（如果有）：
  -

**意外发现**：

- [ ] 哪些预期之外的事情发生了（agent 用了你没想到的方法 / 出现了 spec 没覆盖的边界 case）：
  -

---

## 来源

- 主文：[[pm-long-horizon-methodology|drafts/pm-long-horizon-methodology.md]]
- 官方 docs：[[claude-code-goal]], [[source-openai-codex-cookbook-trilogy]], [[source-openai-codex-use-case-follow-goals]], [[source-openai-long-horizon-tasks-codex]]
- 社区材料：[[idea-to-afk-agent-flow]], [[grill-with-docs]], [[sandcastle]]
- 项目背景：[[blog2video]]
