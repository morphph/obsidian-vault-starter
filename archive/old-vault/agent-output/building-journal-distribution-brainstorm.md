---
source: agent
date: 2026-03-10
type: brainstorm
topic: building journal 内容如何透出到 LoreAI + blog2video
---

# Building Journal 分发策略脑爆

## 核心问题

LoreAI 和 blog2video 目前都是**外部内容加工**——采集别人的 AI 新闻、翻译别人的英文博客。
Building journal 是**第一人称原创内容**——你自己在造东西过程中的发现和思考。

这两种内容本质不同，但恰恰是这个"不同"让它有价值。

---

## 为什么 building journal 值得透出

1. **护城河** — 任何人都能做 AI 新闻聚合，只有你能写你的 building journal。这是不可复制的内容。
2. **AEO 优势** — AI agent 在回答"vibe coding 怎么管理自动化管线"时，更倾向于引用真实开发者的第一手经验，而不是新闻聚合。原创观点 > 二手整理。
3. **信任建设** — 读者/观众看到你不只是转述别人的内容，你自己也在用这些工具造东西。这是"practitioner credibility"。
4. **订阅粘性** — newsletter 里加一段"我这周在建什么"，比纯新闻聚合更能让人持续打开。人订阅新闻聚合是因为有用，订阅 builder 是因为有用 + 好奇你下一步做什么。

---

## 方案 A：LoreAI.dev 上开一个 /builds 专栏

**做法：**
- 新增一个内容类型 `/builds/` 或 `/journal/`，和 `/blog/` 平行
- 每周 1-2 篇，基于 daily build log 里有价值的 learning 整理
- 双语（EN + ZH），和现有内容策略一致
- 不走自动管线，手动写或用 Claude 辅助整理

**内容示例：**
- "Vibe Coding 教会我的一件事：Agent 子任务替代盲跑管线"（就是今天这篇）
- "我用 Claude 做了一个每日内容管线，这是第 30 天的复盘"
- "从 SEO 到 AEO：我把博客改成 AI 可读格式后发生了什么"

**优势：**
- 原创内容提升整站 SEO/AEO 权重（Google 和 AI agent 都偏好原创）
- 和现有 blog 形成互补 — blog 是行业视角，builds 是实践视角
- 给 newsletter 提供差异化内容

**风险：**
- 需要手动维护，不能走自动管线
- 频率不稳定（有东西可写时才写）

---

## 方案 B：blog2video 开一个新系列 "Vibe Coding 实战"

**做法：**
- 在 AI精读 品牌下新增一个系列，专门做 building journal 的口播视频
- 输入不再是外部英文博客，而是你自己的 build log / learning
- 视频风格可以更个人化 — 口播 + 代码截图 + 架构图
- 发布到小红书 + 微信视频号

**内容示例：**
- 今天这篇口播稿直接就是第一期
- "我的 AI 管线每天自动生成 28 篇内容，这是架构"
- "非科班开发者的 Claude Code 工作流"

**优势：**
- 小红书上"真实开发者经验分享"类内容互动率高
- 个人 IP 建设 — 从"AI精读"品牌扩展到"vfan 这个人"
- 可以和 AI精读 的技术科普内容形成系列矩阵

**风险：**
- 和 AI精读 的"英文博客精读"定位有偏差，需要考虑是否用同一账号
- 口播视频的制作流程和当前 blog2video pipeline 不同（不是翻译外部内容）

---

## 方案 C：融入现有内容流，不单独开新栏目

**做法：**
- Newsletter 里加一个固定 section："本周我在建什么" / "Builder's Corner"
- Blog 里偶尔写一篇 building journal 风格的文章，打上 `category: builds` tag
- 视频里偶尔穿插一期 building journal，不单独开系列

**优势：**
- 最低成本，不需要新建任何页面/栏目
- 自然融入现有内容流
- 可以先试水，看读者反应再决定是否独立出来

**风险：**
- 没有独立入口，不容易被发现和积累
- 混在新闻内容里可能定位模糊

---

## 我的建议：A + B 组合，C 作为起步

**第一步（本周）：** 用方案 C 试水
- 今天的口播稿 → blog2video 渲染成视频 → 发小红书
- 同时整理成一篇英文 blog post → 发 LoreAI.dev 的 /blog/，tag 打 `builds`
- 下期 newsletter 里加一段简短提及

**第二步（观察 2 周）：** 看数据
- 小红书：这期视频的互动率 vs 常规 AI精读 视频
- LoreAI：这篇 blog 的阅读量 vs 常规新闻博客
- Newsletter：打开率有没有变化

**第三步（如果数据好）：** 升级为 A + B
- LoreAI.dev 开 `/builds/` 专栏，和 `/blog/` 平行
- blog2video 开"Vibe Coding 实战"系列
- 两边内容互相引流：视频 CTA → loreai.dev/builds，blog 底部嵌入视频

**飞轮效果：**
```
你的 daily build log（vault 里的原始素材）
  ↓
整理成口播稿（agent-output/）
  ↓
blog2video 渲染成中文视频 → 小红书 + 微信
  ↓
同时整理成双语 blog post → loreai.dev/builds/
  ↓
Newsletter "本周我在建什么" section 引用
  ↓
视频观众 → loreai.dev 订阅 → newsletter 读者
  ↓
读者看到你不只是转述，你自己也在建 → 信任 ↑ → 订阅留存 ↑
```

---

## 一个更大的叙事角度

你现在的内容矩阵其实有两层：

1. **Curator 层** — AI精读 + LoreAI newsletter = 帮别人筛选和解读 AI 内容
2. **Builder 层** — building journal = 你自己在用 AI 造东西的过程

大多数 AI 内容创作者只做第一层。**两层都做的人很少。** 而 builder 层的内容恰恰是最难被 AI 自动生成的（因为它需要真实的实践经验），也是最容易建立个人品牌的。

长期来看，Curator 层可能会被 AI 工具 commoditize（人人都能做 AI 新闻聚合），但 Builder 层是你的护城河。

---

## Simon Willison 的 Agentic Engineering 系列：参考与差异化

### 他在做什么

Simon Willison（simonwillison.net）2026 年 2 月启动了一个 **Agentic Engineering Patterns** 系列：

- **格式**：blog 上的 "guide" — 一系列 chapter 式文章，不是一次性发完，而是每周 1-2 章持续更新，设计为 evergreen 内容（弱化发布日期，随时可更新）
- **已发布章节**："Writing code is cheap now"、"Red/green TDD" 等
- **叙事定位**：他是 practitioner + teacher，自己在用 Claude Code / Codex 开发（甚至用手机上的 Claude Opus 写 Django），同时把发现的 pattern 文档化
- **受众**：专业软件工程师，想从 coding agent 中获得更好结果的人
- **分发策略**：
  - Blog（simonwillison.net）= 永久参考内容
  - Newsletter（Substack，47,000+ 订阅者）= 发现层 + 编辑策展
  - X / Mastodon = 宣传 + 社区讨论
- **关键原则**：他明确声明内容是自己写的，不是 AI 生成的 — 这建立了 practitioner credibility

### 他的定位 vs 你的定位

这是最关键的发现 — **你们的叙事角度完全互补，不是竞争**：

```
Simon Willison                        vfan
─────────────────────────────────────────────────────────
资深工程师 → 用 agent 加速           非科班 → 通过 vibe coding 学工程概念
从上往下（已有专业知识，用 agent 放大） 从下往上（在实践中自然习得概念）
"Agentic Engineering"（专业工程师的工具） "Vibe Coding 实战"（builder 的学习路径）
英文，面向全球开发者                  中英双语，面向中文开发者/builder
Pattern 文档化（教科书式）            Building journal（第一人称经验）
教你怎么用好 agent                   分享我怎么通过 agent 学会了工程
```

**Simon 的受众是"已经会写代码，想用 agent 写得更好"的人。
你的受众是"正在用 AI 造东西，顺便学会了写代码"的人。**

这两个群体几乎不重叠，但话题相关。

### 可以借鉴的策略

1. **Guide 格式** — Simon 的 "evergreen guide with chapters" 模式值得参考。你可以在 LoreAI.dev 上做一个类似的 `/builds/` guide，每篇是一个独立的 learning，但串成系列
2. **Newsletter 做发现层** — 他的 newsletter 不是 blog 的复制品，而是"编辑策展 + 新章节预告"。你的 newsletter 可以加 "Builder's Corner" section 引用 /builds/ 的内容
3. **明确声明"这是我自己的经验"** — Simon 强调不发 AI 生成的文章。你也可以强调"这些是我真实的 build log，不是 AI 编的故事"
4. **跨平台但有层次** — Blog = 永久参考，Newsletter = 策展，社交媒体 = 宣传。不是同一内容贴三个地方

### 你能做但 Simon 没做的

1. **视频** — Simon 只写文字。你有 blog2video 管线，可以把 building journal 直接变成中文口播视频，多一个触达渠道
2. **中文市场** — Agentic Engineering 的中文内容几乎空白。Simon 的 patterns 是英文的，你可以用中文 builder 视角重新解读
3. **从零到一的叙事** — Simon 写的是"专家怎么用好工具"，你写的是"非专家怎么通过工具成长"。后者对更大的受众有共鸣
4. **引用 + 延伸** — 你可以在内容里引用 Simon 的 pattern（比如 "Red/green TDD"），然后分享你作为非科班 builder 理解这个 pattern 的过程。这既给了信源 credibility，又展示了你独特的视角
