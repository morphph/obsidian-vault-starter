# Outline: 别让 AI 审自己的代码——异质 review 与 borrowed confidence 陷阱
> 基于角度: report §7 角度 1（推荐）· 目标渠道/形式: 中文博客长文（GEO 友好）→ 摘 X 中文长文 + 小红书图文
> 作者角度闸选定: angle 1 · 修正意见:「smoke-auto」· headless（WF3 driver）细化，不暂停

## prior_coverage（强制字段——对「已表达角度清单」逐条声明关系）
- 已表达角度清单为空 → **无旧角度——首次覆盖该话题**（`drafts/` 无 code-review 成稿；`raw/` 无直接 code-review 源，见 report §0）。
- 唯一近邻 `drafts/_review-wf3-fable5-best-practices.md` 是 WF3 review 产物，与本话题无关，**不构成重复**。
- 复用关系（概念页做骨架，非成稿角度）：[[cross-modal-review]]、[[self-evaluation-bias]] 仅作原理锚点引用，不搬运任何既有成稿论点 → **无重合无增量之虞**。

## take（作者的选择即 take——由角度 1 thesis + 作者修正「smoke-auto」合成，非占位）
1. **thesis**：AI 结对时代，写代码已经变便宜，真正的护城河是「有没有人真的理解这段代码」；而单模型闭环自审（AI 写、同一类 AI 审）会把「系统的确定性」偷换成「你的确定性」——通过了 review，却没有任何人重建过意图。
2. **不同意主流叙事哪点**：Anthropic/Cursor 已把「派一队 agent 审每个 PR」推成默认做法，主流叙事默认「多 agent + 验证步骤 = 审查解决了」；本文反对——**同源多 agent 有相关盲点**，Osmani 引「4 工具并跑、93.4% bug 只被其中一个抓到」正是证据，闭环自审的失败模式叫 borrowed confidence，最隐蔽因为它看起来一切正常。
3. **出路**：异质多模型（不同厂商/不同强项，对应 [[cross-modal-review]] 三轴：精度 / 召回 / genericness）+ coordinator 去重定级 + 人 **on the loop**（抽样深审意图/架构/安全），而非 in the loop（逐行）也非完全 off the loop（交给 AI 自审）。
4. **对 AI builder 的含义**：非资深 builder 今天就能配的最小异质栈——两家不同厂商的审查工具并跑 + 一次人工抽样，比追一个「最强单模型」更抗盲点；review 的价值不在抓机械 bug，在于强制至少一个人（或一个异构视角）真正理解了改动。
5. **作者修正折叠**：本 outline 由 headless smoke-e2e 通道（修正意见「smoke-auto」）细化，修正为流程性标记而非内容改向，故 take 忠实沿用角度 1 thesis，未做立场偏移。

> 每个主张段都要能挂回本 take 的第 1–4 点；writer 无 take 不开工——此 take 已就位。

## 结构（逐节: 论点 + 挂哪些 report 论断/出处 + 预估篇幅占比）

1. **开场·现象钩子** — 论点：写代码变便宜、review 成新瓶颈，于是「派一队 agent 审每个 PR」正在变成默认动作 — 证据：[外部: claude.com/blog/code-review]（多 agent + 验证步骤、<1% 误报口径）[外部: x.com/bcherny/status/2031089411820228645]（每工程师 +200%、review 成瓶颈，一手自述）— **写法学 Boris Cherny：第一人称硬数据开场（+200%）一句立命题** — ~12%

2. **翻转·把默认动作变成问题** — 论点：如果写代码的和审代码的是同一类 AI，谁真正理解了这段代码？ — 证据：[外部: x.com/simonw/status/2020161285376082326]（"cognitive debt" = 拥有没写也没理解的代码；Strong DM 两原则）— ~12%

3. **命名陷阱·borrowed confidence + 相关盲点** — 论点：闭环自审最贵的失败模式不是漏 bug，而是把「系统的确定性」偷换成「你的确定性」；同源模型盲点相关，一起瞎 — 证据：[外部: addyosmani.com/blog/agentic-code-review]（"borrowed confidence"；4 工具 93.4% bug 只被一个抓到 · ⚠️转引，原研究链接待回溯，写稿时标口径）[外部: greptile.com/blog/ai-code-reviews-conflict]（AI 审 AI 的相关盲点、二阶效应才是战场）— **本节是文章题眼，术语要立住** — ~20%

4. **机制层·为什么自审偏差是必然（我们的原理增值）** — 论点：自评估天然偏袒自己的平庸产出，多模型异质审查之所以有效是三轴互补而非投票多数 — 证据：[内部/Tier-1: self-evaluation-bias]（agent 过度自信批准自己的产出 = borrowed confidence 的机制解释）[内部/Tier-1: cross-modal-review]（Opus 精度 + GPT-5.5 召回 + DeepSeek genericness 三轴审同一输出）— **这段是 Dispatch 类第三方调研给不了的配比：别人给现象，我们给「为什么有效」** — ~20%

5. **处方·怎么配一套抗盲点的 review** — 论点：异质多模型并跑 + coordinator 去重定级 + 人 on-the-loop 抽样深审 — 证据：[外部: blog.cloudflare.com/ai-code-review]（生产最多 7 专门 reviewer + coordinator 去重定级，异质编排范本）[外部: addyosmani]（on the loop 抽样 vs in the loop 逐行）[内部/Tier-1: hitl-vs-afk-classification]（哪些改动人必须审的分诊思想）— ~18%

6. **落地清单·非资深 builder today 能做的最小版** — 论点：不必上 7 个 reviewer，两家不同厂商工具并跑 + 一次人工抽样就已抗盲点；高风险变更强制 linear walkthrough — 证据：[外部: cursor.com/bugbot]（`/review` 前移成 push 前闸门，抓 bug 最便宜的点）[外部: danicat.dev/posts/20260303-code-reviews-in-2026]（拒绝来源偏见：只问能跑吗/安全吗）[内部/Tier-1: agent-improvement-flywheel]（review 发现回流改进 harness/规则文件）— **收尾给可复制清单，落到 audience-profile 的「能上手但非资深」读者** — ~18%

> 溯源纪律（承 report §6）：writer 只许**穿透引用**上列原始出处（`[外部: URL]` / `[内部/Tier-1: 页名]`），**绝不引用本报告或本 outline 本身**（防报告引报告的自举塌缩）。⚠️转引项（93.4%、问题密度 1.7× 等）落稿时须标「转引·原研究待回溯」，不得当作已核实一手数据。

## headless 细化注记
- WF3 driver 以 headless 方式调起，无人应答 → 按 Headless 铁律不暂停、不问。
- 角度已由作者 `choose-angle` 选定为 angle 1，无需再消歧；修正意见「smoke-auto」判定为 smoke-e2e 流程标记（非内容改向），已在 take 第 5 点透明折叠，立场未偏移。
- 仅产出本 outline.md 一个文件；不调研、不 ingest、不写 wiki/log、不 push。
