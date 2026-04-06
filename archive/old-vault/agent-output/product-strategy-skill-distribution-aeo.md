---
category: 产品策略
source: agent
created: 2026-03-12
description: blog2video 做成可分发 Skill + Skill 作为 AEO 载体的完整策略分析
---

## 方向2：把 blog2video 做成可分发的 Skill

### 先理解一下现在的 Skill 分发生态

现在 Skill 的分发已经不是概念了，是一个真实运转的市场。目前有三层分发渠道：

**第一层：Anthropic 官方 Claude Marketplace。** 3月6号刚上线，limited preview，目前只面向有 Anthropic 年度消费承诺的企业客户。首批6个合作伙伴：GitLab、Harvey、Lovable、Replit、Rogo、Snowflake。关键是——Anthropic 目前不抽佣，这意味着他们现在更看重生态锁定而不是交易收入。

**第二层：Claude Code Plugin Marketplace。** 这个更贴近你。开发者可以创建自己的 marketplace，用 `/plugin marketplace add` 让其他用户安装。本质上就是一个 Git 仓库加一个 `marketplace.json` 配置文件，任何人都可以搭建和分发。

**第三层：社区聚合站。** 像 SkillHub 已经聚合了 7000+ 个 skill，兼容 Claude、Codex、Gemini 和 OpenCode。SkillsMP 聚合了 400,000+ 个 skill，从公开的 GitHub 仓库抓取。

而且这里有一个关键事实：**SKILL.md 已经成为跨平台标准格式。** 不只是 Claude Code 用，Cursor、Gemini CLI、Codex CLI、甚至 Antigravity IDE 都兼容。所以你做一个 skill，分发覆盖面远大于 Claude 单一平台。

### 你的 blog2video 怎么适配这个生态

你的 blog2video 本质是一个能力：**给我一篇博客文章，帮我转成一个可发布的短视频。** 这个能力对大量内容创作者、独立开发者、营销团队来说是有明确价值的。

目前你在做的 Agent Economy 适配——llms.txt、MCP server、npm package——每一个都是一个独立的"被发现"渠道。现在加上 SKILL.md 格式就是多了一条全新的分发通道，而且可能是最自然的一条，因为 **skill 的使用场景天然就是 agent 在执行任务的时候调用它**。

具体怎么做：

**第一步：把 blog2video 的核心能力封装成 SKILL.md。**

```
blog2video/
├── SKILL.md          # 核心指令：怎么把博客变成视频
├── scripts/
│   ├── extract.py    # 从 URL 提取文章内容
│   ├── storyboard.py # 生成分镜脚本
│   └── render.py     # 调用你的 API 渲染视频
├── references/
│   └── style-guide.md # 视频风格指南、模板说明
└── assets/
    └── templates/     # 默认视频模板
```

SKILL.md 里的 description 要这样写（参考 skill-creator 的"pushy"原则）：

```yaml
---
name: blog2video
description: >
  Convert blog posts, articles, or any long-form text content into
  short-form video. Use this skill whenever the user mentions
  turning written content into video, creating video summaries,
  repurposing blog posts, content repurposing for social media,
  or making video versions of articles. Also trigger when the user
  has a URL and wants to create visual content from it.
---
```

**第二步：用 skill-creator 的 eval 框架来验证质量。**

这是这次更新给你的直接好处。在你发布 blog2video skill 之前，你可以：

- 写 10-15 个测试 prompt（"把这篇关于 AI 的文章做成 60 秒视频"、"我有个技术博客想做成 YouTube Shorts"等等）
- 用 skill-creator 的 A/B comparator 测试：有 skill vs 没 skill，输出质量差多少
- 用 description 优化器确保触发率达标

这就是"经过 eval 验证的高质量 skill"和"随手写的 SKILL.md"的差别。在一个 7000+ skill 的市场里，**质量验证本身就是差异化**。

**第三步：打包分发。**

```bash
# 打包成 .skill 文件
python -m scripts.package_skill ./blog2video

# 创建你自己的 marketplace
mkdir -p bella-ai-marketplace/.claude-plugin
# 配置 marketplace.json，加入 blog2video plugin
# 推到 GitHub

# 用户安装：
/plugin marketplace add bella/ai-tools-marketplace
```

同时你也可以把 SKILL.md 提交到 SkillHub 和 SkillsMP 这种聚合站，以及 `anthropics/skills` 官方仓库。

**第四步：形成从 skill 到你的 API 的漏斗。**

这是最关键的商业逻辑。blog2video skill 的免费版可以生成 storyboard 和脚本，但**渲染成最终视频需要调用你的 API**。这就形成了一个自然的转化漏斗：

```
开发者在 Claude Code 里用 blog2video skill（免费）
    ↓ 生成了 storyboard，觉得不错
    ↓ 要渲染成视频，需要 API key
    ↓ 注册你的 B2B 平台，获得 key
    ↓ 成为付费用户
```

这跟 SaaS 的 freemium 模式一模一样，但分发渠道变了——不是通过 Google 搜索或 Product Hunt，而是通过 agent 在执行任务时自动发现你的能力。

---

## 方向3：Skill 作为 AEO（Answer Engine Optimization）载体

### 先理解 AEO 的核心逻辑

传统 SEO 是：用户 Google 搜索 → 点进你的网站 → 成为客户。
AEO 是：**用户问 AI → AI 引用你的内容作为答案 → 用户找到你。**

这个变化正在加速。Google 的全球搜索市场份额已经跌破 90%，Gartner 预测到 2026 年传统搜索量会下降 25%。ChatGPT 有超过 4 亿周活跃用户。

目前 AEO 的主要技术手段是：

1. **llms.txt** — 放在网站根目录的 markdown 文件，告诉 AI 你的网站有什么重要内容。当用户问 AI 问题时，AI agent 会检查你的 llms.txt，用 2k-10k token 的精炼内容代替爬取整个 HTML 网站。
2. **MCP server** — 让 AI agent 可以直接跟你的服务交互（查库存、调 API 等）
3. **结构化内容** — Schema markup、FAQ 格式等让 AI 容易提取的内容结构

### 但这里有个盲区：llms.txt 和 MCP 都是"被动的"

llms.txt 的问题在于：**AI 要先知道你的域名才会去查你的 llms.txt。** 如果 AI 根本不知道 `yourdomain.com` 的存在，它永远不会去读你的 llms.txt。这就跟 SEO 里你做了完美的 on-page optimization 但没有 backlinks 是一个道理——搜索引擎根本不来。

MCP 也类似。用户需要先手动连接你的 MCP server，AI 才能调用。它是一个很好的"能力暴露"机制，但不是"被发现"机制。

### Skill 填补了"主动被发现"的缺口

这就是 Skill 作为 AEO 载体最有意思的地方。llms.txt 和 MCP 都是等 AI 来找你，而 Skill 是**直接坐在 AI 的工具箱里**。

想象一下这个场景：一个开发者在 Claude Code 里说"我需要把我的博客文章变成社交媒体视频"。Claude 做了什么？

1. Claude 扫描自己的 `available_skills` 列表
2. 看到你的 blog2video skill 的 description 匹配了
3. **主动读取你的 SKILL.md**
4. 按照你的指令引导用户完成任务
5. 任务过程中调用了你的 API

在这整个流程里，用户从来没搜索过你，从来没访问过你的网站，从来没手动连接你的 MCP server。**你的 skill 就是你的落地页，description 就是你的 SEO title。**

### 三层 AEO 策略的组合

所以对你的 B2B 产品来说，最完整的 AEO 策略是三层叠加：

**第一层（被动发现）：llms.txt**

在你的 API 文档站和 [[LoreAI]] 都部署 llms.txt。内容不需要复杂——

```markdown
# YourCompany LLM API

> Multi-model LLM API gateway serving Claude, GPT, Gemini
> with unified endpoints, competitive pricing, and
> Chinese/English bilingual support.

## API Documentation
- [Quick Start](https://docs.yourcompany.com/quickstart)
- [Model Comparison](https://docs.yourcompany.com/models)
- [Pricing](https://docs.yourcompany.com/pricing)

## Tools
- [blog2video API](https://docs.yourcompany.com/blog2video)
- [MCP Server](https://docs.yourcompany.com/mcp)
```

当有人问 AI "有什么好的多模型 LLM API gateway" 或者 "怎么便宜地用 Claude API" 的时候，如果 AI 恰好爬到了你的站，llms.txt 让它能迅速理解你是做什么的。

**第二层（连接后能力暴露）：MCP Server**

用户手动连接了你的 MCP server 之后，AI agent 可以直接调用你的 API——查价格、跑模型、生成内容。这是能力层面的集成。

**第三层（主动被发现）：Skill 分发**

这是最主动的一层。你的 [[blog2video]] skill 被安装到某个开发者的 Claude Code 或 Cursor 之后，每当他遇到"博客转视频"的需求，你的 skill 就自动被调用。不需要他去搜索，不需要他记住你的域名。

**三层的关系是互补的：**

- llms.txt 覆盖的是"AI 恰好在搜索相关话题"的场景（概率性）
- MCP 覆盖的是"用户已经知道你并主动接入"的场景（确定性但需要初始动作）
- Skill 覆盖的是"用户根本不知道你但恰好需要你的能力"的场景（这是纯增量）

Skill 这一层最有价值的原因在于：**它是唯一一个不需要用户先知道你就能触达他们的渠道。** 就像 App Store 时代，用户不需要知道 Instagram 这个域名，只要在商店搜"photo filter"就能发现它。现在 Skill Marketplace 就是 Agent Economy 的 App Store。

### 一个更激进的想法：LoreAI 内容本身就是 Skill

你的 [[LoreAI]] 每天产出 AI 行业新闻和分析。现在这些内容是以博客/newsletter 的形式发布在 loreai.dev 上。但如果你把"每日 AI 新闻摘要"做成一个 skill 呢？

```yaml
---
name: ai-news-daily
description: >
  Get today's AI industry news summary from LoreAI. Use whenever
  the user asks about latest AI news, recent AI developments,
  what happened in AI today, or needs a briefing on AI industry
  trends. Also trigger for questions about specific AI companies
  or products that might have recent news.
---
```

这个 skill 的底层逻辑是：用户问"最近 AI 有什么新闻" → Claude 触发你的 skill → skill 调用 [[LoreAI]] 的 API 获取今天的摘要 → 返回给用户 → 用户觉得有价值 → 订阅 [[LoreAI]]。

**你的内容变成了一个可以被 agent 主动调用的服务，而不是一个等着被人类浏览器访问的网页。** 这就是 AEO 的终极形态——你不是在优化自己被 AI 引用的概率，你是直接把自己变成了 AI 工具链的一部分。

---

### 总结

| | llms.txt | MCP Server | Skill |
|---|---|---|---|
| 发现方式 | AI 搜索时碰到你的站 | 用户手动连接 | Agent 自动匹配需求 |
| 需要用户先知道你？ | 不一定，但概率性 | 是 | **不需要** |
| 分发渠道 | 你自己的域名 | 你自己的域名 | Marketplace + 社区聚合站 + GitHub |
| 用户触达量 | 取决于你的 domain authority | 取决于你的推广 | 取决于 skill 质量和 description 精准度 |
| 商业转化路径 | AI 引用 → 访问网站 | 直接 API 调用 | skill 内嵌 API 调用 |
| 跨平台 | 仅支持 llms.txt 的 AI | 仅支持 MCP 的 AI | Claude, Cursor, Gemini, Codex... |

方向2和方向3不是二选一，它们是同一个增长策略的不同层。Skill 是主动获客，llms.txt 是被动 SEO，MCP 是深度集成。三层一起做，你的产品就在 Agent Economy 里实现了全渠道覆盖。
