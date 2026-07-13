# AI 结对编程时代的 code review 该长什么样 — 深度调研报告
> depth: quick · generated: 2026-07-12 · tools: WebSearch, WebFetch | skipped: deep-research(quick 下未启用), last30days, bird, summarize(VPS-only 本机缺失)
> ⚠️ 互动数据：X / YouTube 全部为「推断·未实测」（本机无 bird/summarize），已逐条标注
> ⚠️ headless run（WF3 driver 调起）：plan checkpoint skipped；无消歧实体，直接扫外

## TL;DR
- **"review 是新瓶颈" 已从观点变成一手数据**：Anthropic 官方称今年每工程师代码产出 +200%，Boris Cherny 连续两月 100% AI 代码、日均 20+ PR —— 写代码变便宜，理解与验证变成最贵的一环。
- **共识正在成形**：人从「逐行读」升到「on the loop（抽样抽查架构/意图/安全）」，机械审查（格式/lint/常见 bug）交给 AI；**拒绝来源偏见**（代码来自资深工程师还是 agent 不重要，只问「能跑吗、安全吗」）。
- **最硬的增值角度是「异质 review + 别把 AI 审 AI 当终点」**：一项研究里 4 个 AI 审查工具并跑，93.4% 的 bug 只被其中一个抓到；Osmani/Greptile 同时警告闭环自审的 "borrowed confidence"。
- **我们该切**：vault 里 [[verification-loops]]/[[cross-modal-review]]/[[self-evaluation-bias]] 三块 Tier-1 锚点，正好是这套外部叙事的「原理层」——别人给现象和工具，我们能给「为什么多模型异质审查有效」的机制解释。这是 Dispatch 类第三方调研给不了的配比。

## 0. Vault 已有锚点（查内）
本话题对 vault 是**新地**：`drafts/` 无 code-review 成稿，`raw/` 无直接 code-review 源 → **外部为主、内部做原理骨架**。但有一批高相关 Tier-1 概念页可直接引用免重复核验：

| 内部锚点 | 一句话：我们已经怎么讲过 | 对本话题的作用 |
|---|---|---|
| [[verification-loops]] | 规则/视觉/LLM-as-judge 三类验证，2-3× 质量提升 | AI code review 就是 verification-loop 的一种落地 |
| [[cross-modal-review]] | Opus(精度)+GPT-5.5(召回)+DeepSeek(genericness) 三模型审同一输出 | **异质多模型 review 的原理层**，正对 Osmani「93.4% bug 只被一个工具抓到」 |
| [[self-evaluation-bias]] | agent 过度自信地批准自己的平庸产出 | 「AI 审 AI」为何危险的机制解释 = borrowed confidence |
| [[iterative-repair-loop]] | OpenAI Cookbook：Review(不改)→Repair(改副本)→Validate(端到端跑) | review 与修复分离的结构范式 |
| [[quality-gate-loop]] | 打分→低于阈值就重写→人过一遍「灵魂」 | review 作为质量闸的通用形态 |
| [[software-entropy]] | "the repo wins"——AI 放大既有代码质量 | 为何 review 焦点上移到架构/系统知识 |
| [[hitl-vs-afk-classification]] | 逐 issue 标注 Human-in-loop vs AFK | 决定「哪些代码人必须审」的分诊规则 |
| [[agent-improvement-flywheel]] | trace→feedback→eval→optimize 闭环 | review 发现如何回流改进 harness |

> 无重复 draft 风险：作者未写过 code-review 稿；仅 `drafts/_review-wf3-fable5-best-practices.md` 是 WF3 review 产物，与本话题无关。

## 1. 这个话题是什么 — 事实轴
**定义**：AI 结对编程时代的 code review = 当 AI agent 写下大部分代码后，人类审查的重心从「检查作者的机械正确性」转向「重建缺失的意图 + 守住架构/安全/系统知识」，同时把机械审查外包给专门的 AI 审查 agent。

逐条对一手源核验（✅一手可信 / ⚠️转引待核 / ❌矛盾）：

- **Anthropic Code Review：大 PR(>1000 行) 84% 出结论、均 7.5 问题；小 PR(<50 行) 31%、均 0.5；工程师标「错误」的发现 <1%** — https://claude.com/blog/code-review — ✅verified（一手）
- **Anthropic 今年每工程师代码产出 +200%，review 成瓶颈** — Boris Cherny 官方 X + blog — https://x.com/bcherny/status/2031089411820228645 — ✅verified（一手自述）
- **Cursor BugBot：每月 >200 万 PR、110,000+ 仓库；Autofix(2026-02) 35%+ 补丁被合；6-10 起审查 ~90 秒、多抓 10% bug、成本 -22%；`/review` 把审查前移成 push 前闸门** — https://cursor.com/bugbot — ✅verified（一手，自测口径）
- **GitHub Copilot code review 支持 Low/Medium 分级 review effort，并融合 ESLint/CodeQL 等确定性工具 + agentic tool-calling 抓全项目上下文** — https://docs.github.com/en/copilot/concepts/agents/code-review — ✅verified（一手）
- **Cloudflare 生产用最多 7 个专门 reviewer（安全/性能/质量/文档/发布/合规/内部 Codex）+ coordinator 去重定级** — https://blog.cloudflare.com/ai-code-review/ — ✅verified（一手）
- **异质多模型有效性：4 个 AI 审查工具并跑，93.4% 的 bug 只被其中一个抓到** — Osmani 引一项研究 — https://addyosmani.com/blog/agentic-code-review/ — ⚠️unconfirmed（转引，原研究链接待回溯）
- **AI 生成代码问题密度约为人写的 1.7×；CodeRabbit 精度约 49%（最佳召回）** — Osmani 引 — ⚠️unconfirmed（厂商研究）
- **AI 生成的 PR 占比一年内 1% → 27.6%** — Greptile/多篇聚合 — https://www.greptile.com/blog/ai-code-review-bubble — ⚠️unconfirmed（二手聚合）
- **Faros AI(2026-03)：代码 churn +861%、缺陷率 9%→54%、review 时长 +441.5%、零审合并 +31.3%** — Osmani 引 — ⚠️unconfirmed
- **GitClear：AI 使 raw 产出 4×，真实生产力仅 +~12%** — Osmani 引 — ⚠️unconfirmed

> [!warning] 三个源冲突（下游写稿时保留双方，别单取一边）
> 1. **AI 代码漏洞比例**：Veracode「~45%」(Osmani 引) vs Thoughtworks VibeSec「25% 已确认漏洞」(https://martinfowler.com/articles/vibesec-reckoning.html) —— 口径不同（是否「已确认」），不可互换。
> 2. **瓶颈到底移到哪**：主流「瓶颈 = review/verification」(Cherny/Osmani/Greptile) vs Gergely 引 Dax Raad「瓶颈仍是决定做什么，不是写」(https://x.com/GergelyOrosz/status/2060379273689526727)。
> 3. **AI 审 AI 是否成立**：Anthropic/Cursor「多 agent + 验证步骤有效，<1% 误报」 vs Osmani/Greptile「相关盲点 + borrowed confidence，需异质 + 人在 loop 上」。

## 2. 焦点实体深挖
无单一焦点实体（概念性命题），本节略。事实与工具已在 §1 / §4 核验。

## 3. X / Twitter — Top 5（增长轴 · 渠道层）
> ⚠️ 互动数据「推断·未实测」（本机无 bird）

### #1 Boris Cherny @bcherny — Claude Code 创造者，「review 是新瓶颈」最强一手背书
- 链接 https://x.com/bcherny/status/2031089411820228645 · thread · 2026-03（Code Review 发布）· 互动「推断·未实测」（高热，被 Garry Tan 等转）
- 核心：「一队 agent 深审每个 PR，我们先为自己造。今年 Anthropic 每工程师代码产出 +200%，review 成了瓶颈。」个人用了几周，抓到 skim 会漏的东西。
- **写作风格拆解**：产品内幕 + 第一人称硬数据（+200%）—— 权威背书型开场弹药。

### #2 Boris Cherny @bcherny — 100% AI 代码工作流（极端案例）
- https://x.com/bcherny · 多帖被引 · 2026-01 · 「推断·未实测」（被 Fortune 报道）
- 核心：连续两月 100% AI 生成、零手改、日均 20+ PR；瓶颈从「打字」移到「意图编排」。
- **写作风格拆解**：极端断言 / 红药丸式 —— 用作「写代码已被解决、信任才是护城河」的引爆点。

### #3 Simon Willison @simonw — 「Software Factory」与 cognitive debt
- https://x.com/simonw/status/2020161285376082326 · post · 2026-05 · 「推断·未实测」
- 核心：引 Strong DM 两原则「代码不得由人编写 / 不得由人审查」，追问「一半代码是 agent 写时怎么 review」；命名 "cognitive debt"（拥有没写也没理解的代码）与 "linear walkthroughs"（强制逐行追逻辑）。
- **写作风格拆解**：审慎观察 + 概念命名 —— 给文章造术语的范本。

### #4 Martin Fowler @martinfowler — 策展 Böckeler「harness engineering」
- https://x.com/martinfowler/status/1904553012296659296 · posts · 2026 · 「推断·未实测」
- 核心：反复引 Böckeler「要不断介入、纠正、引导 agent」，把「review 该是什么」放进「AI 如何改变软件交付」的长期框架。
- **写作风格拆解**：策展式引荐 + 克制判断。

### #5 Gergely Orosz @GergelyOrosz — 瓶颈之辩的另一声部
- https://x.com/GergelyOrosz/status/2060379273689526727 · posts/newsletter · 2026 · 「推断·未实测」
- 核心：转 Dax Raad「瓶颈仍是决定做什么，不是做」；「问题不是写代码，而是确保没弄坏别的东西」。
- **写作风格拆解**：数据新闻 + 多方引用 —— 提供对立视角的平衡弹药。

## 4. Web / 博客 — Top 8（增长轴 · 渠道层）

### #1 Anthropic — "Code Review for Claude Code"（官方）
- https://claude.com/blog/code-review · docs+blog · 2026-03-09 · 官方硬数据
- 核心：每个 PR 派一队 agent 并行找 bug，加一个**验证步骤**过滤误报，按严重度排序，输出高信号总览 + 行内评论；「为深度而非速度而造」，Anthropic 自己几乎每个 PR 都在跑。
- **写作风格拆解**：官方克制 + 对比表/量化背书（大小 PR、<1% 误报率）。

### #2 Addy Osmani — "Agentic Code Review"
- https://addyosmani.com/blog/agentic-code-review/ · long-article · 2026-06-15 · 角度金矿
- 核心：写代码变便宜、理解与验证仍贵，review 从「检查推理」变成「重建缺失的意图」，是「当下最高杠杆技能」；主张**异质多模型 review**（4 工具 93.4% bug 只被一个抓到）；警告闭环自审 "borrowed confidence"；人要 "on the loop"（抽样）而非 "in the loop"（逐行）。
- **写作风格拆解**：技术深度 + 数据密集，金句 + 来源标注（承认厂商偏差）—— **本报告最佳写法范本**。

### #3 Addy Osmani — "Code Review in the Age of AI"
- https://addyo.substack.com/p/code-review-in-the-age-of-ai · long-article · 2026-01-05
- 核心：金句「AI writes faster. Humans still have to prove it works.」把 AI 当「高速实习生」需验证；人保留安全关键代码 / 架构 / 业务逻辑 / 最终签核，监督从逐行变战略性。
- **写作风格拆解**：格言式开场 + 统计表（45% 安全缺陷 / 逻辑错误 1.75×）。

### #4 Thoughtworks — "The VibeSec Reckoning"
- https://martinfowler.com/articles/vibesec-reckoning.html · long-article · 2026-05-27
- 核心：「叫 AI 安全 ≠ 强制它安全，prompt 可被覆盖/误解/忽略」；把**确定性控制放进 agentic 循环内**（版本化安全上下文文件、部署前阻断检查、CVE 情报流、secure-by-default 模板）；25% AI 代码含已确认漏洞。
- **写作风格拆解**：务实处方型 + 事故实证，不渲染恐慌。

### #5 Daniela Petruzalek (Google DevRel) — "Code Reviews in the Agentic Era"
- https://danicat.dev/posts/20260303-code-reviews-in-2026/ · blog · 2026-03-06
- 核心：「代码是一次性的，系统知识是永久的」；**拒绝来源偏见**（不看代码来自谁，只看能跑/安全）；人管架构/公共 API/算法选型/依赖安全/可测性，自动化管格式/lint/语法/单行。
- **写作风格拆解**：对话 + 挑衅性观点，二十年经验背书。

### #6 GitHub — Copilot code review（官方 docs）
- https://docs.github.com/en/copilot/concepts/agents/code-review · docs · 2025→2026 持续更新
- 核心：变更 + PR 标题正文 + 自定义指令拼 prompt 送 LLM；**分级 review effort**（Low 快审常见 bug / Medium 路由更高推理模型审复杂逻辑）；融合 ESLint/CodeQL；专门「Review AI-generated code」教程页。
- **写作风格拆解**：规范文档型（能力 + 免责 + 分级）。

### #7 Cursor — BugBot（官方产品页）
- https://cursor.com/bugbot · docs · 2026（6 月更新）· 200 万 PR/月、110K+ 仓库
- 核心：专注逻辑错误/竞态/SQL 注入/CVE，非风格；Autofix 在隔离 VM 起 Cloud Agent 实测并提补丁（35%+ 合入）；`.cursor/BUGBOT.md` 自定义；`/review` 把审查前移成 push 前闸门（抓 bug 最便宜的点）。限制：仅 GitHub。
- **写作风格拆解**：产品迭代叙事 + 自测数据。

### #8 Greptile — "AI Code Review Bubble" + "AI Reviewing AI Code"（逆火视角）
- https://www.greptile.com/blog/ai-code-review-bubble · https://www.greptile.com/blog/ai-code-reviews-conflict · blog · 2025-2026
- 核心：第一层问题（能否抓真 bug）基本已解决，「二阶效应」才是战场；质疑 AI 审 AI 的相关盲点；把整仓索引进图数据库，PR 触到 auth 时把调用点/测试/迁移历史一并拉进 prompt，作为「独立验证层」，无论 PR 来自人还是 agent。
- **写作风格拆解**：反共识 + 机制拆解 —— 「别人不敢说」的角度弹药。

## 5. YouTube — Top 4（增长轴 · 渠道层）
> ⚠️ 观看/互动「推断·未实测」（本机无 summarize/last30days）

### #1 "How I Review AI-Generated Code" — 2026-03-27 · 实操型
- https://www.youtube.com/watch?v=As2xy_cSx00 · 钩子：「70% 团队采用 AI 后代码质量变差——问题不是 AI，是多数团队对 AI 代码没有 review 流程」。写法：痛点开场 + 实操叙事。

### #2 Simon Willison — "Engineering practices that make coding agents work"（Pragmatic Summit）
- https://www.youtube.com/watch?v=owmJyKVu5f8 · 2026 · 会议演讲级权威：把「证明代码可用」置于工作中心，安全相邻代码不能外包。写法：主旨演讲 + 原则清单。

### #3 "Catch Bugs Faster: Cursor BugBot for AI Code Review" — 2026 · 产品演示
- https://www.youtube.com/watch?v=8USlEyGf37E · BugBot 抓 bug + Autofix 演示。写法：产品演示型。

### #4 Anthropic — "Code with Claude 2026" livestream 合集 — 2026-05-06 SF
- Anthropic YouTube 频道 · 含 Code Review / managed agents / proactive workflows；「Anthropic 自己怎么审 agent 输出」的一手素材。写法：官方大会多讲者。

## 6. 核心洞察 + 最佳实践

**洞察（每条挂出处）：**
1. **"review 是新瓶颈" 已被一手数据坐实**，不再是猜测 [外部: claude.com/blog/code-review][外部: x.com/bcherny/...]。
2. **人的角色从 "in the loop"（逐行）升到 "on the loop"（抽样抽查意图/架构/安全）** [外部: addyosmani.com/blog/agentic-code-review]，对应内部 [内部/Tier-1: hitl-vs-afk-classification] 的分诊思想。
3. **异质多模型 review > 单模型闭环自审**：93.4% bug 只被一个工具抓到 [外部: addyosmani]，机制正是内部 [内部/Tier-1: cross-modal-review]（三模型三轴）与 [内部/Tier-1: self-evaluation-bias]（自审偏差）。
4. **"borrowed confidence" 是最隐蔽的失败模式**：AI 审 AI 让系统的确定性变成你的，却没人真正理解代码 [外部: addyosmani][外部: greptile.com/blog/ai-code-reviews-conflict]。
5. **确定性控制要放进 agentic 循环内**（安全上下文文件 + 部署前阻断 + CVE 流），光靠 prompt 叫 AI「注意安全」无效 [外部: martinfowler.com/articles/vibesec-reckoning]。
6. **审查正前移成 push 前闸门**（抓 bug 最便宜的点），而非停在 PR 阶段 [外部: cursor.com/bugbot]。
7. **来源偏见要主动拒绝**：只问「能跑吗、安全吗」，不问代码来自资深工程师还是 agent [外部: danicat.dev]。

**可执行最佳实践清单：**
- 机械层（格式/lint/语法/常见 bug/安全模式）→ 全外包给 AI 审查 agent；人不再看。
- 判断层（架构、公共 API 人体工学、算法选型、依赖与安全暴露、业务逻辑、可测性）→ 人保留，采样式深审。
- 用**异质多模型**（不同厂商/不同强项）并跑，而非单一工具或自审；把发现去重定级（coordinator 模式，见 Cloudflare 7-reviewer）。
- 把安全/架构约束写成**版本化上下文文件**喂进 review 循环，配部署前阻断的确定性检查。
- 审查前移到 push 前闸门；对高风险变更强制「linear walkthrough」逐行追逻辑（防 cognitive debt）。
- review 发现回流改进 harness/规则文件 [内部/Tier-1: agent-improvement-flywheel]。

> **溯源标注纪律（全报告适用）**：每个论断已标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`。下游 writer 只许**穿透引用这些原始出处**，绝不引用本报告本身（防「报告引报告」自举塌缩）。本节内外配比：外部 7 条现象/工具 + 内部 4 条原理锚点 —— 我们的增值在「原理层」。

## 7. 对内容创作的启示 — 增长轴 → 排序的内容角度

### 时机窗口
**正当爆发中段、窗口未过**：Anthropic Code Review(3/9)、Cursor BugBot 提速(6/10)、Osmani《Agentic Code Review》(6/15) 都在近 4 个月，话题热但尚未被「怎么做」类深稿占满——现在多是现象报道和厂商公告，**缺一篇把原理讲清、给非资深 builder 可落地做法的中文稿**。这正是 audience-profile 的「能上手但非资深工程师」读者的空位。

---

## 【建议角度】（角度闸 · 强制契约 · 作者读完做选择题）

> WF3：作者用 `wf3.py choose-angle --task <id> --angle N [--note …]` 选定后，再跑 `/research outline smoke-e2e-07120312 angle:N` 细化 outline。

### 角度 1（推荐）——「别让 AI 审自己的代码：异质 review 与 borrowed confidence 陷阱」
- **① 标题候选**：《AI 写的代码，为什么不能只让 AI 自己审？》/《borrowed confidence：AI 结对时代最贵的一课》
- **② thesis**：单模型闭环自审会把「系统的确定性」偷换成「你的确定性」，而没人真正理解代码；出路是异质多模型 + 人 on-the-loop。
- **③ 为什么是我们 / 为什么现在**：vault 有 [[cross-modal-review]] + [[self-evaluation-bias]] 两块**别人没有的原理锚点**，能把 Osmani 的「93.4% bug 只被一个工具抓到」从现象讲成机制；时机上 Anthropic/Cursor 刚把「AI 审 AI」推成主流做法，逆火视角正稀缺。
- **④ prior_coverage 关系**：**全新**——drafts/ 无 code-review 稿；仅复用 [[cross-modal-review]]/[[self-evaluation-bias]] 概念页做骨架，不重复任何成稿角度。
- **⑤ 3–5 行骨架**：现象（review 成瓶颈→AI 审 AI 成默认）→ 陷阱命名（borrowed confidence + 相关盲点）→ 机制（自审偏差为何必然，引 cross-modal-review 三轴）→ 处方（异质多模型 + coordinator 去重 + 人抽样深审）→ 落地清单（非资深 builder today 能配哪几个工具）。
- **⑥ 渠道建议**：中文博客长文（GEO：Anthropic/Cursor 数据 + Osmani 研究做引用）→ 摘成 X 中文长文 + 小红书图文。

### 角度 2 ——「code review 的重心上移：从逐行读到 on-the-loop」
- **① 标题候选**：《当一半代码是 agent 写的，你该 review 什么？》
- **② thesis**：review 的价值不再是抓机械 bug，而是重建缺失的意图、守住架构与系统知识；机械层全外包，判断层人保留。
- **③ 为什么是我们 / 为什么现在**：audience 正是「能上手但非资深」builder，最需要一张「哪些人审、哪些交给 AI」的分诊表；vault 的 [[hitl-vs-afk-classification]] 正好是分诊思想的原型。
- **④ prior_coverage 关系**：**全新**；复用 [[hitl-vs-afk-classification]]/[[software-entropy]] 概念，与既有 draft 无重叠。
- **⑤ 3–5 行骨架**：旧 review vs 新 review 对比表 → 「拒绝来源偏见」原则(danicat) → 人管什么/AI 管什么的分诊清单 → cognitive debt 与 linear walkthrough(Willison) → 给独立 builder 的最小可行流程。
- **⑥ 渠道建议**：中文博客长文 + 对比表（GEO 友好）→ X 长文。

### 角度 3 ——「把安全塞进循环里：为什么『叫 AI 注意安全』没用」
- **① 标题候选**：《VibeSec：AI 生成代码的安全，不能靠 prompt 求来》
- **② thesis**：prompt 层的安全叮嘱会被覆盖/误解/忽略，唯一可靠的是把确定性控制（版本化安全上下文 + 部署前阻断 + CVE 流）放进 agentic 循环内。
- **③ 为什么是我们 / 为什么现在**：25%–45% AI 代码含漏洞的数据正在传播，但多数中文内容停在「危险」层面，缺「怎么防」的工程处方；Thoughtworks VibeSec 是硬核一手源。
- **④ prior_coverage 关系**：**全新**；可挂 [[verification-loops]] 的规则化验证思想，无重叠。
- **⑤ 3–5 行骨架**：漏洞率数据（标注 25% vs 45% 口径冲突）→ 为何 prompt 安全无效 → 四件确定性控制 → 与 review 循环如何拼 → 独立 builder 的轻量版。
- **⑥ 渠道建议**：中文博客（偏工程）→ 可配一张「安全控制放进循环」流程图（/visualize）。

---

### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
|---|---|---|
| Boris Cherny @bcherny | Claude Code 创造者 | 「review 是瓶颈 / 100% AI 代码」一手数据源 |
| Addy Osmani @addyosmani | Google，AI 工程写作者 | 异质 review + on-the-loop 论述最系统，写法可直接学 |
| Simon Willison @simonw | 独立，AI 工程评论 | cognitive debt / linear walkthrough 术语造词者 |
| Birgitta Böckeler / Martin Fowler | Thoughtworks | harness engineering + VibeSec 安全处方 |
| Gergely Orosz @GergelyOrosz | Pragmatic Engineer | 瓶颈落点的对立声部，平衡弹药 |

### 内容形式参考库
- **长文学谁**：Addy Osmani《Agentic Code Review》—— 技术深度 + 数据密集 + 金句 + 诚实标注厂商偏差，正是 audience-profile 要的「具体压过笼统 + 诚实」。
- **X 学谁**：Boris Cherny —— 第一人称硬数据开场（+200%），一句话立住命题。
- **视频学谁**：「How I Review AI-Generated Code」—— 痛点数据开场（70% 团队质量变差）+ 纯实操。

## 附录：关键时间线
| 日期 | 事件 |
|---|---|
| 2024 H2 | Graphite **Diamond** 发布，AI PR review 早期产品化 |
| 2025 全年 | GitClear 等：AI raw 产出 ~4×、真实生产力 ~12%，「review 跟不上生成」叙事成型 |
| 2025-10-28 | GitHub **Copilot code review** public preview（agentic tool-calling + ESLint/CodeQL） |
| 2026-01-05 | Addy Osmani《Code Review in the Age of AI》 |
| 2026-01/02 | Boris Cherny 公开「连续两月 100% AI 代码、日 20+ PR」；Fortune 报道 |
| 2026-02 | Cursor **BugBot Autofix** 上线 |
| **2026-03-09** | **Anthropic 发布 Claude Code Review**（多 agent + 验证步骤）← 爆发节点 |
| 2026-05-06 | Anthropic **Code with Claude 2026**（SF） |
| 2026-05-27 | Thoughtworks《The VibeSec Reckoning》+ harness engineering |
| 2026-06-10 / 06-15 | Cursor BugBot 提速至 ~90 秒 + push 前闸门；Osmani《Agentic Code Review》系统化 |
