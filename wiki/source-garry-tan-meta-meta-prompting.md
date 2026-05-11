---
type: source-summary
created: 2026-05-11
last-updated: 2026-05-11
sources:
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
tags: [wiki, source, agentic, personal-ai, gbrain]
---

# Source: Garry Tan — Meta-Meta-Prompting: The Secret to Making AI Agents Work

## Summary
Long-form X article by [[garry-tan|Garry Tan]] (YC President & CEO), 2026-05-09. **1.1M views, 9,630 bookmarks.** Sixth piece in his agent-building series and the **most personal** — moves from abstract framework (resolvers, thin harness, fat skills) to **"here's what this looks like when applied to me"** with concrete examples: book-mirror, meeting-prep, 100K-page brain, 100+ skills, 100+ daily crons. The biggest single insight is **[[skillify-meta-skill|/skillify]] — the meta-skill that creates skills** — finally made operational. Closes with: "the future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools."

## Source
- **URL:** https://x.com/garrytan/status/2053127519872614419
- **Posted:** 2026-05-09 14:58 UTC
- **Engagement (at fetch, 2026-05-11):** 1.1M views · 9,630 bookmarks · 3,045 likes · 492 RT · 108 replies
- **Fetch method:** Playwright MCP
- **Series position:** 6/?. Earlier pieces in series:
  - [[source-garry-tan-thin-harness-fat-skills|Fat Skills, Fat Code, Thin Harness]] (2026-04-11) — in wiki
  - [[source-garry-tan-resolvers|Resolvers]] (2026-04-15) — in wiki
  - "The LOC Controversy" (~2026-04-17) — NOT yet ingested
  - "Naked models are stupider" (~2026-04-18) — NOT yet ingested
  - "The skillify manifesto" (~2026-04-21) — NOT yet ingested

## 要点解读

### 1. **"Meta-Meta-Prompting" 这个标题其实是误导 —— 真正的内容是"我把抽象架构落到自己身上"**
前面 5 篇都是抽象框架（resolver / thin harness / fat skills / 模型不是车）。这一篇是 **"系统跑在 Garry 自己身上 6 个月后长什么样"** —— 具体到他妈妈来自缅甸、他在 YC 的角色、深夜跟治疗师讨论的话题。

这篇的杠杆点不是新概念，是**让所有抽象概念有了一个统一的工程范例 (worked example)**。从此引用 GBrain / skillify / cross-modal-eval 这些 wiki 概念，都有了一个"在 Garry 身上是这样的"的具象锚点。

### 2. **Book Mirror —— 整篇文章最高杠杆的实操模式 ⭐**
开篇就是惊艳的例子：他让 AI 给 Pema Chödrön 的《When Things Fall Apart》做了 book mirror —— 提取 22 章，每章用 sub-agent 做两件事：
- (左) 总结作者观点
- (右) 映射到他**自己的真实生活**（家族史、YC 工作、上周某个 founder 对话、19 岁跟室友的 IM 聊天记录）

输出：**30,000 字的两栏 brain page。**

关键洞察：
> "A $300/hour therapist reading this book and applying it to my life couldn't do this in 40 hours, because **they don't have the full graph of my professional context, my reading history, my meeting notes, and my founder relationships all loaded and cross-referenceable.**"

Garry 现在做了 **20+ 本**。每本都比前一本更丰富 —— 因为 brain 在长。**"The twentieth knew about all nineteen."**

**为什么这个模式重要：**
• 这是把 [[diarization]] 用在**别人的思想**上的版本（而不是用在某个人身上）
• 它需要**结构化的个人 context graph** + **per-section retrieval**，普通 RAG 做不到
• 第一版有 3 个事实错误 → 加 cross-modal eval → 修一次，所有未来 book mirror 自动受益（compounding）

**对本 vault 直接启示：** 我们的 `/ingest` 现在做**左栏（提取/结构化）**，缺**右栏（映射到本 vault 已有内容）**。加上右栏 = 我们就有了 vault-aware book-mirror。比如吸收 resolver 文章时，自动 cross-ref 已有的 [[resolvers]] / [[check-resolvable]]，标记重复和矛盾。

我新建了 [[book-mirror]] 抓住这个 pattern。

### 3. **Skillify (`/skillify`) —— 终于揭晓"if I ask twice you failed"的操作机制**
Garry 之前一直说"重复出现就该 skill 化"，但**没说怎么 skill 化**。这一篇终于揭示了：
> "Skillify is a **meta-skill that creates new skills.** When I encounter a workflow I'm going to repeat, I say 'skillify this' and it examines what just happened, extracts the repeatable pattern, writes a tested skill file with triggers and edge cases, and **registers it in the resolver.**"

这是文章标题 "meta-meta-prompting" 的真正所指：
- Level 0 = prompting (你写 prompt)
- Level 1 = meta-prompting (模型为自己写 prompt，也就是 skill)
- Level 2 = **meta-meta-prompting (模型写"写 prompt 的 skill"，也就是 skillify)**

**关键的 4 步流程（"How to Start"）：**
1. 做一件有趣的事（不要先规划 skill 架构）
2. 跟 agent 一起迭代到 output 满意
3. `/skillify` —— 提取 pattern → 写 SKILL.md → 注册到 RESOLVER.md
4. `check_resolvable` —— 验证新 skill 被路由表能触达

**"That loop turns one-off work into compounding infrastructure."**

新建 [[skillify-meta-skill]] 捕获这个 pattern。

**反直觉的关键点：** "Don't start by planning your skill architecture. Start by doing a thing." —— 与工程师本能（先设计后实现）相反。理由：**只有先做过一次你才知道哪个 pattern 值得固化**。和 Thariq 警告"别急着写 /html skill" 是同一个原则。

### 4. **"Filing Cabinet vs Nervous System" —— 极其精准的对比 ⭐**
> "This is the difference between having a filing cabinet and having a nervous system. The filing cabinet stores things. The nervous system connects them, flags what's changed, and surfaces what's relevant to right now."

这个对比直击大部分 Notion / Obsidian 用户的痛点 —— 你以为你有 second brain，其实只有 storage。

**nervous system 的 4 个性质：**
1. 存储 ✓
2. **自动 linking**（每次写入触发 entity propagation，零 LLM 调用）
3. **propagation**（meeting note 不是终点 —— 会自动更新所有提到的人/公司的 page）
4. **recency 感知**（标记 stale info、矛盾、open threads）
5. **context loading**（"你 10 分钟后要见这个人，这里是相关 dossier"）

**判断你的 KB 是 filing cabinet 还是 nervous system 的简单测试：**
> "你的 knowledge base 在你睡觉时做什么？"
> • 什么都不做 → filing cabinet
> • 跑 crons / 自动 propagation / 主动 surface → nervous system

新建 [[filing-cabinet-vs-nervous-system]] 捕获这个 framing。

**对本 vault 老实评估：** 我们今天**更接近 filing cabinet**。propagation 不自动（依赖每次 ingest 时人为决定）、recency 不主动检测、context loading 没有。这是个长期改造方向。

### 5. **生产数据更新（关键 milestone）**
- **GBrain：100,000 pages**（4/15 文章里是 17,888 → 4/19 是 25K → 现在 100K，**6× 增长在 1 个月内**）
- **100+ skills**（之前是 26，然后 39）—— 文末说 GBrain 现在 ship **39 个 installable**，他个人 100+
- **100+ crons/day** 自动运行
- **GStack：87,000 ⭐**（4/15 是 72K → 4/21 是 78.7K → 现在 87K，仍在加速）
- **97.6% recall on LongMemEval** —— 自称"best retrieval system benchmarked"，且**没有 LLM 在 retrieval loop 里**（这点非常重要 —— 完全 deterministic，cheap）

### 6. **模型可互换 —— 多模型分工的运营化**
> "The skill decides which model to call for which task. **The harness doesn't care.**"

具体分工：
- **Opus 4.7 1M** —— precision（事实检查）
- **GPT-5.5** —— recall / exhaustive extraction
- **DeepSeek V4-Pro** —— creative / 第三视角 / 检测 "generic"
- **Groq + Llama** —— speed

Cross-modal eval 用三个不同 family 的模型互评，是 [[verification-loops]] 在内容质量上的具象化。**生产里看起来 cross-modal 已经是 GBrain 的核心 skill 之一**（叫 `cross-modal-eval` 或 `cross-modal-review`）。

### 7. **Karpathy LLM Wiki —— GBrain 的祖先**
惊喜：Garry 透露 GBrain 灵感来自 Karpathy 写的一个 LLM Wiki gist。"I got inspired by Karpathy's LLM Wiki, implemented it in OpenClaw, and extended it into GBrain."

(链接：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

**这个谱系很有意思：**
- Karpathy → 概念 (LLM-driven wiki)
- Garry → 工程实现 (GBrain + skills 生态)
- **本 vault** → 个人简化版（手动写 wiki 页面 + 一个 ingest skill）

如果以后扩展，沿着 GBrain 的方向是有先例的。

### 8. **结尾的哲学论断（值得记一下）**
> "The future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools."
> "The difference is the difference between **keeping a journal and having a nervous system**."

这跟 4/15 那篇 resolver 文末的"个人软件新黎明"一脉相承。但更尖锐：**centralized AI tools 不会 compound 到你身上 —— 你只是在租用 capability**。

## Pages created from this source
- [[skillify-meta-skill]] — concept (meta-skill that creates skills)
- [[book-mirror]] — concept (two-column chapter-by-chapter book→life mapping)
- [[filing-cabinet-vs-nervous-system]] — concept (the framing that distinguishes active KB from passive storage)
- [[source-garry-tan-meta-meta-prompting]] — this page

## Pages updated from this source
- [[garry-tan]] — 6th article in series + production scale update (100K pages, 100+ skills, 100+ crons)
- [[gbrain]] — 39 ship-with skills, 100K pages, Karpathy attribution, 97.6% LongMemEval recall, cross-modal-eval as canonical skill
- [[gstack]] — 87K stars (up from 78.7K)
- [[resolvers]] — `/skillify` as production primitive that registers new skills into RESOLVER.md
- [[verification-loops]] — cross-modal-eval as production multi-model verification
- [[index]], [[log]]

## Connections
- Related: [[garry-tan]], [[skillify-meta-skill]], [[book-mirror]], [[filing-cabinet-vs-nervous-system]], [[gbrain]], [[gstack]], [[openclaw]], [[resolvers]], [[check-resolvable]], [[thin-harness-fat-skills]], [[diarization]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-11 | raw/2026-05-09-garry-tan-meta-meta-prompting.md | Initial creation |
