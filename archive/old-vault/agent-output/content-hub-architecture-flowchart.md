---
type: architecture-flowchart
date: 2026-03-11
status: draft
source: agent
related: [[LoreAI]], [[blog2video]]
---

# LoreAI V2 Content Hub — 内容流转架构图 v3

## 核心理念

> Canonical ≠ Blog。Canonical = Narrative（叙事化深度分析）。
> Blog、Video、Social Post 都是从 Narrative 平行派生的 output format。
> 不同类型的内容走不同复杂度的链路。

---

## 架构总览

```mermaid
graph TB
    subgraph HUB["🏠 LoreAI V2 Content Hub"]
        direction TB

        subgraph P0["链路 0️⃣ — 自动日报 (现有，不改)"]
            direction LR
            RSS["15+ Sources<br/>RSS / Twitter / GitHub<br/>HN / Reddit"]
            CRON["4am SGT Cron<br/>Claude Opus 筛选"]
            DAILY["28 items/day<br/>中英双语摘要<br/>5 个分类"]
            NL["Newsletter<br/>邮件订阅者"]
            RSS --> CRON --> DAILY --> NL
        end

        subgraph PA["链路 A — 人工精选外部内容"]
            direction LR
            SRC_A["外部 Source<br/>官方博客 / Influencer<br/>YouTube / Dev.to"]
            S0["Step 0<br/>内容提取"]
            S05["Step 0.5<br/>深度分析"]
            NAR_A["Narrative<br/>📦 内容原子"]
            SRC_A --> S0 --> S05 --> NAR_A
        end

        subgraph PB["链路 B — Deep Research 原创"]
            direction LR
            TOPIC["手动输入<br/>Topic"]
            DR["Gemini<br/>Deep Research"]
            NAR_B["Narrative<br/>📦 内容原子"]
            TOPIC --> DR --> NAR_B
        end

        subgraph PC["链路 C — 开发笔记 (轻量直发)"]
            direction LR
            DEV["开发实践"]
            CLAUDE["与 Claude<br/>协作撰写"]
            PUB_C["直接发布<br/>loreai.dev"]
            DEV --> CLAUDE --> PUB_C
        end
    end

    subgraph DIST["📤 Distribution Layer"]
        direction LR
        BLOG_ZH["中文 Blog<br/>loreai.dev/zh/"]
        BLOG_EN["英文 Blog<br/>loreai.dev/en/"]
        VIDEO["Video Script<br/>→ 视频渲染"]
        SOCIAL["Social Post<br/>短文 + 金句"]
    end

    subgraph CHANNEL["📡 发布渠道"]
        direction LR
        WEB["loreai.dev"]
        NEWS["Newsletter"]
        XHS["小红书<br/>品牌: AI精读"]
        WX["微信视频号<br/>品牌: AI精读"]
        TW["Twitter"]
        JK["即刻"]
    end

    NAR_A --> BLOG_ZH
    NAR_A --> BLOG_EN
    NAR_A --> VIDEO
    NAR_A --> SOCIAL

    NAR_B --> BLOG_ZH
    NAR_B --> BLOG_EN
    NAR_B --> VIDEO
    NAR_B --> SOCIAL

    BLOG_ZH --> WEB
    BLOG_EN --> WEB
    BLOG_ZH --> NEWS
    VIDEO --> XHS
    VIDEO --> WX
    SOCIAL --> TW
    SOCIAL --> JK

    DAILY -.->|"现有链路<br/>保持不变"| WEB
```

---

## 链路 A 详解：人工精选外部内容

```mermaid
graph LR
    SRC["🔗 外部 Source"]
    S0["Step 0<br/>内容提取<br/>原文 → 结构化"]
    S05["Step 0.5<br/>深度分析<br/>中文视角 + 观点提炼"]
    NAR["📦 Narrative<br/>内容原子"]

    SRC --> S0 --> S05 --> NAR

    NAR --> ZH["中文 Blog<br/>为阅读 + SEO 优化"]
    NAR --> EN["英文 Blog<br/>为阅读 + SEO 优化"]
    NAR --> VS["Video Script<br/>为听觉优化<br/>口语化 + 节奏感"]
    NAR -.-> SP["Social Post<br/>可选"]

    VS --> RENDER["视频渲染"]
    RENDER --> XHS["小红书 / 微信<br/>品牌: AI精读"]
    ZH --> LOREAI["loreai.dev"]
    EN --> LOREAI
```

**升级点：** 之前 blog2video 只产出视频。现在从 Narrative 同时产出 Blog + Video。

---

## 链路 B 详解：Deep Research 原创内容

```mermaid
graph LR
    T["💡 手动输入 Topic"]
    DR["Gemini<br/>Deep Research<br/>产出调研报告"]
    NAR["📦 Narrative<br/>叙事化分析<br/>+ 个人开发视角"]

    T --> DR --> NAR

    NAR --> ZH["中文 Blog"]
    NAR --> EN["英文 Blog"]
    NAR --> VS["Video Script"]
    NAR -.-> SP["Social Post<br/>可选"]
```

**关键决策：Video 从 Narrative 分叉，不从 Blog 分叉。**
- Blog 为阅读优化（长段落、小标题、SEO 关键词）
- Video Script 为听觉优化（短句、口语化、节奏感）
- 两者平行派生，避免 blog → video 的格式转换损耗

---

## 链路 C 详解：开发笔记直发

```mermaid
graph LR
    DEV["🛠️ 开发实践<br/>Building Journal"]
    WRITE["与 Claude<br/>协作撰写"]
    PUB["loreai.dev/zh/<br/>building-xxx"]

    DEV --> WRITE --> PUB
```

**最短链路，零中间步骤。** 写完即发，不走 Narrative，不生成视频。

---

## 链路 0 详解：自动日报（现有，保持不变）

```mermaid
graph LR
    SOURCES["15+ Sources<br/>RSS / Twitter<br/>GitHub / HN / Reddit"]
    CRON["4am SGT Cron"]
    FILTER["Claude Opus<br/>筛选 + 摘要<br/>中英双语"]
    BATCH["Daily Batch<br/>28 items × 5 categories"]
    SITE["loreai.dev<br/>Vercel SSG 重建"]
    NL["Newsletter<br/>邮件订阅者"]

    SOURCES --> CRON --> FILTER --> BATCH --> SITE --> NL
```

**这条链路完全不变。** 它是 LoreAI 的基础内容层，与链路 A/B/C 共存。

---

## 四条链路对比

| | 0️⃣ 自动日报 | A 精选外部 | B Deep Research | C 开发笔记 |
|---|---|---|---|---|
| **输入** | 15+ RSS/API | 人工选 URL | 人工选 Topic | 开发经验 |
| **处理** | Claude 筛选+摘要 | Step 0 → 0.5 → Narrative | Deep Research → Narrative | Claude 协作撰写 |
| **Canonical** | Daily batch item | Narrative | Narrative | Blog 本身 |
| **Blog** | ✅ 摘要卡片 | ✅ 中英深度文章 | ✅ 中英深度文章 | ✅ 直发 |
| **Video** | ❌ | ✅ 从 Narrative | ✅ 从 Narrative | ❌ |
| **Social** | ❌ | ✅ 可选 | ✅ 可选 | ❌ |
| **自动化** | 全自动 | 半自动 | 半自动 | 手动 |
| **状态** | ✅ 已上线 | 🔨 待建 | 🔨 待建 | 🔨 待建 |

---

## 关键设计决策

| 决策 | 选择 | 原因 |
|------|------|------|
| Canonical 是什么 | Narrative（叙事化分析） | 最灵活的中间产物，可派生任何格式 |
| Video 从哪分叉 | 从 Narrative，不从 Blog | 避免"阅读格式→听觉格式"的转换损耗 |
| 自动日报改不改 | 不改 | 已稳定运行，与新链路独立共存 |
| 开发笔记走什么链路 | 直发 | 轻量内容不需要 Narrative 层 |
| Video 品牌 | 保持 "AI精读" | 社交媒体已有品牌认知 |
| 分发决策谁做 | 人工决定 | 不是所有内容都适合所有格式 |

---

## 数据流示例

### 例 1：Anthropic 发了 Claude 4 博客（链路 A）
```
Anthropic blog URL
  → Step 0（提取英文原文 + 结构化）
  → Step 0.5（深度分析：技术解读 + 开发者影响）
  → Narrative
      ├→ 中文 Blog → loreai.dev/zh/claude-4-deep-dive
      ├→ 英文 Blog → loreai.dev/en/claude-4-deep-dive
      ├→ Video Script → AI精读视频 → 小红书/微信
      └→ Social Post → Twitter thread + 即刻
```

### 例 2：研究 "AI Agent 架构模式"（链路 B）
```
Topic: "AI Agent 架构模式"
  → Gemini Deep Research（产出调研报告）
  → Narrative 生成（加入个人开发实践视角）
      ├→ 中文 Blog → loreai.dev/zh/ai-agent-patterns
      ├→ 英文 Blog → loreai.dev/en/ai-agent-patterns
      └→ Video Script → AI精读深度解析 → 小红书
```

### 例 3：写了一个 MCP Server 的开发心得（链路 C）
```
开发笔记
  → 与 Claude 协作撰写
  → 直接发布 → loreai.dev/zh/building-mcp-server
```

### 例 4：每日自动日报（链路 0，现有）
```
15+ sources 每日更新
  → 4am SGT cron 触发
  → Claude Opus 筛选 28 items
  → 生成中英双语摘要
  → Vercel SSG 重建 → loreai.dev
  → Newsletter 推送
```
