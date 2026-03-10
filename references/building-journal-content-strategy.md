---
source: agent
date: 2026-03-10
tags: [content-strategy, building-journal, vibe-coding]
related: ["[[LoreAI]]", "[[blog2video]]"]
---

# Building Journal 内容策略

## 核心定位

现有内容是**外部内容加工**（新闻聚合、博客翻译），building journal 是**第一人称原创**。
两层内容矩阵：

1. **Curator 层** — AI精读 + LoreAI newsletter = 帮别人筛选和解读
2. **Builder 层** — building journal = 自己在用 AI 造东西的过程

Builder 层是护城河 — 不可复制、AEO 友好、建立 practitioner credibility。

## 分发方案

### LoreAI.dev — `/builds/` 专栏
- 和 `/blog/` 平行的新内容类型
- 每周 1-2 篇，基于 daily build log 里的 learning 整理
- 双语，不走自动管线
- 示例："Vibe Coding 教会我的一件事：Agent 子任务替代盲跑管线"

### blog2video — "Vibe Coding 实战" 系列
- AI精读 品牌下的新系列
- 输入 = 自己的 build log（不是外部博客）
- 口播 + 代码截图 + 架构图 → 小红书 + 微信视频号

### Newsletter — "本周我在建什么" section
- 每期加一段 Builder's Corner
- 引用 /builds/ 内容，不是复制

### 飞轮
```
daily build log → 口播稿 → blog2video 视频 → 小红书/微信
                         → 双语 blog post → loreai.dev/builds/
                         → newsletter Builder's Corner
                         → 视频观众 → 订阅 → 信任 ↑ → 留存 ↑
```

## 执行节奏

1. **本周**：方案 C 试水 — 口播稿发视频 + blog post 打 builds tag + newsletter 提及
2. **观察 2 周**：对比互动率/阅读量 vs 常规内容
3. **数据好则升级**：开 /builds/ 专栏 + "Vibe Coding 实战" 系列

## 参考：Simon Willison 的 Agentic Engineering Patterns

Simon Willison（simonwillison.net）做了一个类似但互补的事：
- **他的定位**：资深工程师，从上往下，教专业开发者用好 agent（Pattern 文档化）
- **你的定位**：非科班 builder，从下往上，分享通过 vibe coding 自然习得工程概念的过程
- 受众几乎不重叠，话题相关

### 可借鉴
- Evergreen guide with chapters 格式（不是一次性文章，持续更新）
- Newsletter = 发现层，Blog = 永久参考（跨平台有层次，不是复制粘贴）
- 明确声明"这是我自己的经验，不是 AI 生成的"

### 你的差异化优势
- 有视频渠道（他只有文字）
- 中文市场空白
- "从零到一"叙事比"专家教你"对更大受众有共鸣
- 可引用他的 pattern + 分享 builder 视角的理解（信源 credibility + 独特视角）

## 相关资源
- 口播稿初稿：`agent-output/vibe-coding-script.md`
- 完整脑爆：`agent-output/building-journal-distribution-brainstorm.md`
- Simon Willison's guide: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
