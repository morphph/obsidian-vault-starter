---
type: source-summary
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
tags: [wiki, source, agentic, resolvers, governance]
---

# Source: Garry Tan — Resolvers: The Routing Table for Intelligence

## Summary
Long-form X article by [[garry-tan|Garry Tan]] (YC President & CEO), 2026-04-15. **Follow-up to [[thin-harness-fat-skills]]** (2026-04-11): in that piece he defined five primitives; resolvers got the least attention, so this piece zooms fully in. Introduces four companion patterns — [[trigger-evals]], [[check-resolvable]], [[context-rot]], self-healing RLM — and reframes resolvers as **the governance / management layer** of an agent system. Ends with open-source drop: [[gbrain]] + [[gstack]] + [[openclaw]]/Hermes Agent.

## Source
- **URL**: https://x.com/garrytan/status/2044479509874020852
- **Posted**: 2026-04-15 18:14 UTC
- **Author**: Garry Tan (@garrytan)
- **Engagement (at fetch time)**: 47 replies · 156 reposts · 1,159 likes · 3,211 bookmarks · 293K views
- **Fetch method**: Playwright MCP (x.com is JS-heavy; WebFetch is gated)

## 要点解读

### 1. Resolver 到底是什么：把 20,000 行 CLAUDE.md 砍到 200 行的秘密
Garry 承认他的 CLAUDE.md 曾经 **20,000 行** —— 每一个踩过的坑、每一个约定、每一个 Claude Code 的怪癖都塞进去。结果不是让模型变聪明，而是让模型"被淹死"（drowning it）。注意力下降，响应变慢，Claude Code 自己反过来让他砍。**"当 AI 让你闭嘴的时候，你真的说太多了。"**

修复方案：**200 行的决策树**（"是人？→ /people/；是公司？→ /companies/；政策分析？→ /civic/"），配上指向每个文档的指针。20,000 行知识还在仓库里，但按需加载。

**一句话定义：Resolver 是 context 的路由表 —— 当出现任务类型 X，优先加载文档 Y。**

这不是 prompt engineering，是 **context governance**。模型不是因为变聪明才更准，而是因为你不再用噪音蒙住它的眼睛。

### 2. Resolver 是分形的（resolvers are fractal）—— 这是让所有东西串起来的关键
Resolver 不只在顶层。它在每一层都存在，三种类型：

- **Skill resolver**（在 `AGENTS.md`）：任务类型 → skill 文件。"帮我查签名" → executive-assistant。"吸收这篇 PDF" → pdf-ingest。
- **Filing resolver**（在 `RESOLVER.md`）：内容类型 → 目录。人 → `people/`；公司 → `companies/`；政策分析 → `civic/`。
- **Context resolver**（在每个 skill 内部）：skill 内部的子路由。executive-assistant 里 email triage 走一条、scheduling 走另一条、signature tracking 走第三条。

[[claude-code]] 早就在这个模式上了 —— 每个 skill 的 `description` 字段就是它的 resolver 入口。你不需要记住 `/ship` 存在，描述字段自己会匹配意图。**It's resolvers all the way down.**

实操启示：同一个架构原理从 5 个 skill 扩到 50 个、从 1000 个文件扩到 25000 个，都是这一个模式。

### 3. 引爆一切的 Manidis 误归档故事 —— "资源盘"式 degradation 的真实机制
Garry 让 agent 吸收 Will Manidis 那篇"No New Deal for OpenAI"（OpenAI 产业政策的锋利分析）。agent 丢进了 `sources/`。

**错。** `sources/` 是给 CSV / API 导出 / 爬来的原始数据用的。这篇是政策分析，应该进 `civic/`。

根因：idea-ingest skill 在内部硬编码了 `brain/sources/` 作为默认目录，**根本没读 resolver**。Garry 一审计 —— 13 个写入 brain 的 skill，**只有 3 个引用 resolver**，其他 10 个都有自己私下的归档逻辑。

这就是杀死 agent 系统的模式：**不是戏剧性的失败，而是缓慢静默的漂移**。信息去到错误的位置，关联不成立，知识库从"结构化智能层"沦落成"装了 14,700 个文件的杂物抽屉"。

修复方法很重要 —— **不是逐个修 10 个 skill（那是打地鼠）**。而是：
1. 一个共享的 `_brain-filing-rules.md` 文档，记录所有常见误归档
2. 一条强制规则：任何写入 brain 的 skill，开头两行必须写：*"创建任何新 brain 页面之前，先读 `brain/RESOLVER.md` 和 `skills/_brain-filing-rules.md`。按主题归档，不是按 skill 名字或源格式归档。"*

**一条规则，十个 skill 一起修好。修完之后零误归档。**

**对本 vault 的启示：** 我们的 ingest skill 现在也类似 —— `.claude/commands/ingest.md` 里有自己的归档逻辑；如果新增 `/ingest-podcast` 之类，很可能也会重蹈覆辙。值得做一次本地版的"filing rules"审计。

### 4. 三个彼此咬合的治理层：Trigger Evals + check-resolvable + Context Rot
这是整篇文章的工程核心。一个只有 resolver 的系统 **必然会腐烂**，所以需要上面套三层：

**(a) [[trigger-evals|Trigger Evals]]（等同于性能考核）**
50 个样本输入 + 预期 skill 输出的测试套件。两种失败：false negative（该触发没触发）、false positive（不该的触发了）。两者都能改 markdown 描述修好，不改代码。
> Garry 原话："如果你不能证明正确的 skill 对正确的输入触发了，你没有系统，你有一堆 skill 和一次祈祷。"

**(b) [[check-resolvable]]（等同于合规审计） —— 最原创的发明**
一个"元 skill"，顺着 `AGENTS.md → skill 文件 → 代码`整条链走，找出"不可达的 skill"（存在但没有 resolver 入口）。他跑完第一次，在 40+ skill 里找出 **6 个不可达 —— 15% 的能力是黑的**。例：签名追踪 skill 完美工作，但 resolver 里没有 "check my signatures" 的触发条件。**"医院里有外科医生，但目录里没列。"**

这比没有 skill 更糟 —— 没有是诚实的（你知道要去建），有但不可达是**错觉**（你以为系统能处理签名，它不能，直到出事那一刻你才发现）。

**(c) [[context-rot|Context Rot]]（漂移曲线）**
Resolver 会**腐烂**：Day 1 完美；Day 30 有 3 个新 skill 没进 resolver（凌晨 3 点 sub-agent 建的）；Day 60 两个触发描述和用户实际说法不匹配（skill 叫 "track this flight"，用户说 "is my flight delayed?"）；Day 90 resolver 成了历史文物。

**判断标志：** 你开始用 "read skills/flight-tracker/SKILL.md" 直接点名调 skill，因为 resolver 不认识你的意图了。**"系统能跑是因为我知道该调哪个。那不是系统，那是一个人带着文件柜。"**

### 5. 终局：自愈 resolver（RLM 循环）+ 管理层比喻
YC 的一个 CTO 在 office hours 里问 Garry："能不能用 RLM 解决 context rot？" —— 一个强化学习式的循环，观察每次任务派发：哪个 skill 触发了、哪个没触发、哪些意图没匹配上。定期（可能每晚，可能每周）**根据流量证据自动重写 resolver**。

800 次派发后：系统发现 "is my flight on time" 从来没触发 flight-tracker，但 "check my flight" 一直触发。它自动改写触发描述。**"不是人类维护表格。表格自己维护自己。"**

[[claude-code]] 的 [[dreaming|AutoDream]] 系统（空闲时间 memory consolidation）已经是一个原始版本。把它专门应用到 resolver，就得到一个**随使用量进化的路由表**。Garry 把这称为 **"agent governance 的终局"**。

**最大胆的 reframe（我觉得这是全文最有价值的一段）：**
> Resolver 不是技术 pattern。它是**管理**。
> - Skills = 员工
> - Resolver = 组织架构图 + 升级路径
> - Filing rules = 内部流程
> - check-resolvable = 审计与合规
> - Trigger evals = 绩效考核
>
> "问题不是模型不够聪明。问题是我们一直在建一个没有管理层的组织 —— 一堆有才华的员工和一句'希望他们自己会协调'的美好愿望。"
>
> **Resolver 就是那一层缺失的管理层。**

### 6. 开源三件套：GBrain + GStack + OpenClaw/Hermes Agent
文末 Garry 把自己生产系统（处理 200 输入/天，25,000 文件）的完整架构开源：

| 层 | 项目 | 职责 |
|---|---|---|
| 知识层 | **[[gbrain]]** (github.com/garrytan/gbrain) | 开箱即用的 RESOLVER.md + 决策树 + disambiguation 规则 + 内置 [[check-resolvable]] |
| Skills 层 | **[[gstack]]** (github.com/garrytan/gstack, **72K+ stars**) | markdown fat skills 库，调 GBrain 的知识 |
| Harness 层 | [[openclaw]] / Hermes Agent | 跑 loop、管 session、跑 cron |

> 这不是 SaaS 产品，是架构。源码开源，skill 是 markdown，brain 是你自己的 git repo。任何一块明天消失，你的知识以明文文件形式活下来。
>
> **"这是个人软件的新黎明。你自己为自己造的软件，但有 fat skills + fat code + thin harness，也就是你自己的 mini-AGI。未来已经在这儿了，我希望它也在你口袋里。"**

## Pages created from this source
- [[check-resolvable]] — concept (meta-skill that audits resolver reachability)
- [[trigger-evals]] — concept (50-sample eval suite for routing correctness)
- [[context-rot]] — concept (resolver decay curve Day 1 → Day 90)
- [[gbrain]] — entity (Garry's open-source knowledge-base scaffold)
- [[gstack]] — entity (72K-star open-source skills library)

## Pages updated from this source
- [[resolvers]] — massive expansion: fractal layers, Manidis misfiling, invisible-skill problem, governance stack, management reframe, self-healing RLM
- [[garry-tan]] — second article; creator of GBrain/GStack; 200 inputs/day, 25K-file personal agent
- [[thin-harness-fat-skills]] — added follow-up cross-reference
- [[openclaw]] — Hermes Agent as alt name; GBrain/GStack relationship clarified
- [[claude-code]] — AutoDream as primitive self-healing resolver

## Connections
- Related: [[garry-tan]], [[resolvers]], [[trigger-evals]], [[check-resolvable]], [[context-rot]], [[gbrain]], [[gstack]], [[openclaw]], [[thin-harness-fat-skills]], [[dreaming]], [[documentation-layers]], [[context-management]], [[context-noise-governance]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
