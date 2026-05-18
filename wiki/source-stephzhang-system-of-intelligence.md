---
type: source-summary
created: 2026-05-16
last-updated: 2026-05-18
sources:
  - raw/2026-05-14-stephzhang-system-of-record-to-system-of-intelligence.md
tags: [wiki, source, a16z, enterprise, vc-thesis, system-of-intelligence]
---

# Source: Steph Zhang (a16z) — From "System of Record" to "System of Intelligence"

## Summary
a16z newsletter piece by [[steph-zhang|Steph Zhang]], 2026-05-14. **458K views, 779 bookmarks (BM/L ratio 2.33×, high reference-saving intent).** Strategic VC thesis: the next decade of **enterprise software value migrates from SoR (CRM databases) to SoI (orchestration / reasoning layer above)**. Same shape as Facebook's friend-graph → newsfeed transition. First **a16z-portfolio-thesis** voice in our wiki; maps cleanly onto Garry Tan's [[filing-cabinet-vs-nervous-system]] at a different scale (personal vs enterprise).

## Source Metadata
- **X Post:** https://x.com/steph_zhang/status/2054925688097128603
- **Full article:** https://www.a16z.news/p/from-system-of-record-to-system-of
- **Author:** Steph Zhang (a16z) — Verified
- **Posted:** 2026-05-14 14:03 UTC
- **Engagement (at fetch, 2026-05-16):** 458,353 views · 779 bookmarks · 334 likes · 71 RT · 30 replies
- **Bookmark-to-like ratio:** ~2.33×
- **Format:** a16z newsletter excerpt (X long-form thread)
- **Fetch method:** Playwright MCP
- **Companion piece:** "Is Software Losing Its Head?" (a16z, separate article)

---

## 要点解读（12-Section Comprehensive Study Guide）

### 1. 元信息

- **作者**：Steph Zhang（@steph_zhang）—— Verified
  - 身份定位：a16z 投资人（具体职位未在 bio 直接披露，但所在出版物 a16z.news 是 a16z 的 newsletter）
  - 立场：**这是 portfolio-thesis 文章** —— a16z 投了一堆 SoI 创业公司，这篇是给整个 thesis 做"intellectual scaffolding"
- **来源**：a16z 的 newsletter，通过 X 长文 distribution
- **发表时间**：2026-05-14 14:03 UTC
- **影响力指标**：
  - 458,353 views
  - 779 bookmarks
  - 334 likes
  - 71 reposts
  - 30 replies
  - **Bookmark-to-like ratio: 2.33×** —— 高于普通 X 内容（0.1-0.3×），低于 Khairallah 的 3.4× 但远超 mass-market 标准
- **在 a16z 内容矩阵的位置**：companion piece to "Is Software Losing Its Head?" —— a16z 在 systematically 给 enterprise software 的 AI 转型搭一套理论框架。这是其中一篇

### 2. 核心论点（Thesis）

**作者主张**：在 enterprise software 领域，**owning the database**（System of Record / SoR）从 2003 起是 20 年的赢家策略（Salesforce $140B、HubSpot $9B），**但 AI 让这条护城河在迁移**。**因为** AI agent 能同时从 CRM + 日历 + Slack + email + product telemetry + billing 等十几个系统拉数据并 synthesize，**人类一次只能看一个地方**的物理约束消失了 ——**所以** 下一个十年的 enterprise 价值会积累在 **reasoning / orchestration layer (System of Intelligence / SoI)** 上面，**CRM 不会死但会变成 legacy furniture，从用户主界面降级为 agent 透过它读取数据的 input。**

简化压缩包：**"AI 让 colocation gravity 翻转成 orchestration gravity；下一个十年的价值在 reasoning layer，不在 database。"**

### 3. 论证结构

文章的逻辑骨架（教科书式的 VC thesis 结构）：

```
1. Open with vivid analogy（建立 frame）
   → "Facebook 的 friend graph → newsfeed 的转变"
2. Apply the analogy to enterprise（迁移 frame）
   → "CRM 也在经历同样的事"
3. Day in the life vignette（让 thesis 具体可感）
   → "AE 早上打开电脑，看到一组他没编程的 agents 在工作"
4. Historical setup（建立 baseline）
   → "Salesforce/HubSpot 凭什么赢了 20 年：他们 own the database"
5. The mechanism explanation（解释为什么变了）
   → "Old gravity = colocation; New gravity = orchestration"
6. Counter-intuitive evidence（让 thesis 更强）
   → "CRM usage 在 AI 时代反而 UP 了"
7. Switching cost analysis（量化护城河迁移）
   → '"all data in Salesforce" → "all reasoning in our AI layer"'
8. Foundation model is not the GTM app（架构论断）
   → "model 不是 product, harness 才是 product"
9. Labor / pricing implication（产业影响）
   → "software-to-labor ratio 翻转，但目前 pie 在长不在砍人"
10. Forward-looking vignette（未来 VP of Sales 一天）
    → 让读者代入未来感受
11. Final insight: institutional memory becomes shippable
    → 一个高浓度的 emotional hook
12. Conclusion: where the next decade's value lives
    → "next generation of companies being built on top of this emerging layer"
```

**骨架洞察**：这是**专业 VC thesis writing 的范本**。共 12 个 narrative beats，每个都服务于"为什么我们投的 SoI startups 会赢"这个底层目标。**Day-in-the-life vignettes 出现两次**（一次过去/现在，一次未来）—— 这是高质量 thesis writing 的 signature move：用具体场景让抽象论断可感。

### 4. 关键概念字典

> **System of Record (SoR) — 记录系统**
> - **是什么**：以"持久化和管理 operational data"为核心价值的软件系统。CRM、ERP、HRIS 都是 SoR
> - **为什么重要**：过去 20 年企业软件赢家的共同特征 —— Salesforce、HubSpot、ServiceNow、Workday 都是 SoR。**他们赢是因为他们 own the data**
> - **直觉/类比**：像档案室 —— 公司所有 records（contracts, calls, deals, employees）都存进去。**离开档案室的代价 = 损失全部历史记忆**
> - **适用场景**：任何需要"long-term operational memory"的企业流程
> - **反面/失败模式**：用 SoR 当 user-facing primary interface 时 —— UI 复杂、workflows 死板、为多数 user 不友好（"hostages, not customers"）

> **System of Intelligence (SoI) — 智能系统 ⭐ 核心新概念**
> - **是什么**：sitting **above** the SoR，**reads from multiple SoRs and orchestrates action**，并 increasingly 把 SoR 当作 commodity infrastructure。**用户的 primary interface**
> - **为什么重要**：作者的整篇文章建立在"下一个十年价值在这一层"。**所有论证都服务于这个概念**
> - **直觉/类比**：像 Facebook 的 newsfeed —— friend graph 还在底下，但你不是直接跟 graph 互动了，你跟 newsfeed 互动
> - **适用场景**：任何 enterprise 流程，agent 能拉多个 SoR 数据 + synthesize + take action
> - **反面/失败模式**：把 SoI 当成"另一个 SoR"做（新建立一个数据库做用户的 primary interface）→ 重复 Salesforce 模式，被下一代 SoI 颠覆
> - **wiki**：见 [[system-of-intelligence]]

> **Colocation Gravity vs Orchestration Gravity — 重力机制**
> - **是什么**：在软件时代，价值集中（"gravity"）来自 **colocation** —— 人一次只能看一个地方，所以所有相关 context 必须挤在一个数据库。**在 AI 时代**，价值集中来自 **orchestration** —— agent 同时拉多源数据，context 住哪儿都行，**synthesis** 才是 moat
> - **为什么重要**：这是作者**解释 why now 的核心机制**。没有这个 mechanism explanation，"SoR 会被颠覆"只是一个 narrative；有了这个 mechanism，它变成了**可证伪的 thesis**
> - **直觉/类比**：城市发展的两种模式 —— 旧时代是"市中心 colocation"（所有功能挤在市中心，因为通勤成本高）；新时代是"分布式 orchestration"（远程工作 + 物流网络让"住哪儿"不重要）
> - **适用场景**：分析任何"为什么 incumbents 现在变得脆弱"的 thesis
> - **反面/失败模式**：在 high-latency / unreliable-integration 环境里 —— 如果 agent 拉多源数据每次都超时或出错，orchestration gravity 不成立，colocation 仍然赢

> **Friend Graph → Newsfeed Analogy — 类比框架 ⭐ 最有迁移价值**
> - **是什么**：Facebook 的演化模式 —— 老 gravity (friend graph) 没死但变成 input；新 gravity (newsfeed) 成了用户的 primary surface 和价值核心
> - **为什么重要**：**这是整篇文章的"intuition pump"**。读者一旦接受 friend-graph → newsfeed 的类比，就自动同意 CRM → SoI 的论断（因为结构同构）
> - **直觉/类比**：本身就是个 analogy —— 类比的类比 = recursive
> - **适用场景**：任何 "incumbent storage layer + emerging synthesis layer" 的产业分析
> - **反面/失败模式**：**Misapplied analogy** —— Facebook 是 consumer / single-vendor，CRM 是 B2B / multi-vendor。Steph 没讨论这个 disanalogy（Facebook 自己 build 了 newsfeed；Salesforce 让别人 build SoI 吗？还是自己 build？） —— **这是文章的弱点**

> **"Hostages, not Customers" — 高 switching cost 的极端表述 (Alex Rampell)**
> - **是什么**：Salesforce/HubSpot 的客户被高 switching cost 锁住，**不是因为产品好，是因为离不开 —— 离开就丢失多年累积的 operational context**
> - **为什么重要**：这个词条让读者意识到 SoR 的护城河本质上是"data hostage 模式" —— 一旦 SoI 提供了让 data portable 的能力，这种锁定就脆弱了
> - **直觉/类比**：像养老院 —— 不是因为你喜欢这里所以留，是因为搬家成本太高所以留
> - **适用场景**：分析任何 B2B SaaS 的 retention
> - **反面/失败模式**：Salesforce 自己出 AgentForce 把 reasoning layer 内化 —— 用 hostage 模式延伸到 SoI

> **The Foundation Model is Not a GTM Application — 架构论断**
> - **是什么**：Foundation model（GPT-5、Claude Opus、Gemini）不是 product。**Model 和 customer 之间还需要大量 unglamorous + domain-specific 工作**：orchestrating across 多系统、encoding sales/marketing 实际逻辑、permissions、合规、跟 Fortune 500 IT 集成
> - **为什么重要**：这条论断**呼应了 Garry Tan 的"naked models are stupider"** —— 同一个洞察从 builder 视角和 VC 视角都说出了
> - **直觉/类比**：Oracle 数据库引擎 ≠ CRM。Engine 是发动机，CRM 是车。**Model 是发动机，SoI 是车。**
> - **适用场景**：任何 AI 产品 strategy 讨论
> - **反面/失败模式**：直接卖 foundation model 给企业（OpenAI API only）→ 企业需要自己 build SoI → 大多数企业不会做 → 真正的 enterprise 价值流到了 SoI 公司
> - **wiki 对应**：[[thin-harness-fat-skills]] 的"engine vs car" + Garry Tan 的"Naked Models Are Stupider"

### 5. 框架与心智模型

**核心框架：SoR vs SoI Two-Tier Architecture**

```
┌────────────────────────────────────────────────────────┐
│  User-facing interface (where value capture happens)   │
│                                                         │
│  SOFTWARE ERA:                       AI ERA:           │
│  ┌──────────────────┐               ┌──────────────────┐│
│  │ CRM UI           │               │ SoI Orchestrator  ││
│  │ (Salesforce app) │     →         │ (Reasoning agent) ││
│  └────────┬─────────┘               └─────┬─────────────┘│
│           │                               │              │
│           ▼                               ▼              │
│  ┌──────────────────┐               ┌──────────────────┐│
│  │ CRM Database     │  ←  becomes   │ CRM (as input)    ││
│  │ (the moat)       │               │  + Calendar       ││
│  └──────────────────┘               │  + Slack          ││
│                                     │  + Email           ││
│                                     │  + Telemetry       ││
│                                     └──────────────────┘│
└────────────────────────────────────────────────────────┘
```

**怎么套用（举例：vfan 的 LoreAI 内容平台）**：
- **如果 LoreAI 当 SoR 做**：SEO content database + AI 优化 —— 跟 Notion / Webflow 等内容 SoR 竞争 → 红海
- **如果 LoreAI 当 SoI 做**：reasoning layer that pulls from your existing CMS / Google Drive / brand guidelines / past analytics, and orchestrates content generation across blog/social/video → 蓝海
- **关键 question**：你是想 own the data（SoR）还是 own the workflow（SoI）？两者价值评估完全不同

**Switching Cost Migration 框架**：

| 时代 | Switching cost 在哪 | 解释 |
|------|---------------------|------|
| SoR 时代 | 数据 | "We can't leave Salesforce — 8 years of customer history in there" |
| SoI 时代 | 工作流 + 推理 + 累积语境 | "We can't leave this AI layer — it knows how we sell, what works, the texture of our deals" |

**关键洞察**：**数据可以 export，工作流和"系统对你的理解"几乎不可能 export**。SoI 的 switching cost 可能比 SoR 更高。

### 6. 关键数据与例证

按重要性排序：

| 数据 | 支撑什么观点 | 用途 |
|---|---|---|
| **Salesforce ~$140B / HubSpot ~$9B** | "SoR 是 20 年的赢家策略；价值高度集中" | 设置 stakes —— 这是个万亿级 enterprise software 市场重新分配 |
| **CRM usage 在 AI 时代反而 UP（来自 a16z GTM survey）** | "SoR 不会死，但角色变了" | counter-intuitive 数据点，让 thesis 更精细（不是"SoR 会死"是"SoR 角色降级"）|
| **Software 占 GTM total spend 5-10%（其余是 payroll）** | 量化 "software 一直是 junior partner to labor" | 设置背景 —— AI 是第一次有可能改这个比例 |
| **"hostages, not customers" (Alex Rampell)** | 描述 SoR 锁定的本质 | quotable 短语，传播度高 |
| **458K views / 779 bookmarks / 2.33× BM/L** | 证明这个主题有 enterprise 受众关注 | 印证选题方向 |
| **20+ agents running on top of Salesforce**（引用的 Quote tweet）| 证明 SoR + AI 的现状 | 反过来支撑论点 —— "agent 已经在 SoR 上跑了，问题是 agent 在谁的 control 下" |

**注意**：作者**没给具体 case study —— 没说哪家 SoI startup 已经实际颠覆了 Salesforce**。这是文章的弱点。VC 文章常见手法：用强 narrative + 历史类比代替实证。读者要保持 awareness。

### 7. 关键引语

> **"In the software era, the gravity in enterprise software came from colocation. But in the AI era, gravity will come from orchestration."**
> 软件时代企业软件的重力来自 colocation（colocation）。但 AI 时代重力来自 orchestration（编排）。
> ⭐ 全文最浓缩的论断。直接量化"why now"。

> **"First prize is a Cadillac. Second prize is a set of steak knives."**
> 一等奖是 Cadillac，二等奖是一套牛排刀。
> ⭐ 描述 SoR 时代赢家通吃。**Glengarry Glen Ross 经典台词**。文化引用增加 memorability。

> **"Switching costs shift accordingly. 'All of our customer data is in Salesforce' becomes 'all of our workflows, our reasoning, our accumulated institutional context live in our AI layer.'"**
> Switching cost 随之迁移。"我们所有客户数据在 Salesforce 里"变成"我们所有工作流、推理、累积的机构语境在我们的 AI layer 里"。
> ⭐ Switching cost 迁移的最清晰表述。

> **"A foundation model is not, by itself, a GTM application, any more than Oracle's database engine was a CRM."**
> 基础模型自己不是 GTM 应用，就像 Oracle 数据库引擎自己不是 CRM。
> ⭐ 跨厂商共识的强表述 —— Garry Tan、Tw93、Steph Zhang 都说了一遍。

> **"This is the newsfeed. It's the valuable thing now."**
> 这就是 newsfeed。它现在是有价值的东西。
> ⭐ 把整个 analogy 浓缩到 7 个词。文章的 emotional climax。

> **"Institutional memory becomes something a company can actually ship."**
> 机构记忆变成公司可以 ship 的东西。
> ⭐ Closing emotional hook。对 SaaS founder 来说极具煽动力。

> **"Just as the feed increased the TAM of social media to 'everything of interest', the agent revolution expands what software can plausibly charge for, and does it without gutting the labor budget that funds most GTM work today."**
> 就像 newsfeed 把社交媒体的 TAM 扩展到"一切有趣的东西"，agent 革命扩展了软件可以合理收费的边界，而且没有砍掉资助大部分 GTM 工作的 labor budget。
> ⭐ 给 SaaS founders 的 economic optimism —— "pie grows, not shrinks"。

### 8. 实操指南

文章没给明确"how to"步骤（VC thesis 通常不给 —— 它的"实操"是"找 SoI startup 投资"），但可以反推出 **build SoI vs build SoR 的判断 framework**：

**Build SoI Checklist**（如果你是 founder 想 build SoI 公司）：
- [ ] Your product reads from N existing SoRs（不是替代它们）
- [ ] Your value comes from synthesis + orchestration（不是 data storage）
- [ ] Your switching cost lives in workflows + reasoning（不是 data）
- [ ] You can articulate "what we do for the user" without saying "we store X"
- [ ] You have a story for why agents will pull from your layer instead of going direct to SoR

**Build SoR Checklist (anti-pattern in 2026+)**：
- [ ] You're building "a better CRM" / "a Notion alternative" / "another database"
- [ ] Your switching cost lives in data lock-in
- [ ] You're competing with $140B incumbents on their home field
- [ ] You don't have a story for why your data layer specifically is needed

**Avoid SoR Trap**：如果你在 build new SoR，**承认你在打 Salesforce 的游戏**。要么找一个 Salesforce 不在的 niche（minor SoR），要么转 SoI strategy。

### 9. 对比与反对意见

| 对比对象 | 作者立场 | 隐含信念 |
|---|---|---|
| **vs "SoR 会死"** | 拒绝 —— SoR 不会死，**变成 input**。CRM 还在，但变 legacy furniture | 数据持久化的需求永存；变的是用户接口 |
| **vs "AI 会砍 sales 人员"** | 拒绝 —— 至少目前没看到。Pie 在长，不是 labor budget 在缩 | 软件 augmentation 提高 ROI → 总投入增加而非减少 |
| **vs "Salesforce 会被颠覆"** | 部分同意但精细化 —— Salesforce 不会消失，**会被绕过到 API layer** | Incumbents 有 inertia 但不会消亡；新公司在他们头顶建价值层 |
| **vs "Foundation model 公司会赢"** | 拒绝 —— Model 是 engine，SoI 才是 car。**Application layer 才是创业机会** | Foundation model 是 commodity infrastructure 不是 product |
| **vs "做 SoR 还能赚到大钱"** | 拒绝（2026+）—— SoR 时代的 Cadillac 已经被瓜分；新的 Cadillac 在 SoI 层 | 历史不会重复但会押韵 —— newsfeed 之后再没人能 build 出第二个 Facebook |

**作者明确反对**：
1. 继续 build new SoR 公司（"first prize is a Cadillac"，但奖已经发完了）
2. 单卖 foundation model 给企业（"engine is not a car"）
3. 把 AI 主要 framing 成 cost-cutting 而非 capability expansion（错失了 TAM expansion 的故事）

**作者隐含承认的限制**（他没明说但能推断）：
- **没讨论 Salesforce 内部反击战略**（AgentForce / Einstein / Slack AI 等）—— 大概率 a16z 投了 SoI startup 所以不想强调 incumbent 的反击能力
- **没量化 SoI 的 switching cost 多高** —— 只说"会变高"，没数据
- **没讨论数据 portability 法规风险** —— 如果 GDPR / 数据 portability 法律变严，SoI 的"agent 跨 SoR 拉数据"可能受限
- **没讨论 multi-tenant SoI 怎么 build** —— 单个公司的 SoI vs 行业级 SoI 有完全不同的难度
- **类比的 disanalogy**：Facebook 是 single-vendor（FB 自己 build newsfeed），CRM 是 multi-vendor（谁来 build SoI？Salesforce 自己？还是 startup？）—— 这个问题没 address

### 10. 与 wiki 知识的连接

**强连接**：
- [[steph-zhang]] — 作者实体（首篇 a16z 内容）
- [[system-of-intelligence]] — 这篇创造的概念页（最高迁移价值）
- [[filing-cabinet-vs-nervous-system]] — **同一原理的个人尺度版本**。Garry Tan 写给 builder，Steph 写给 VC，本质是同一个洞察

**强化已有概念**：
- 强化 [[thin-harness-fat-skills]]：Steph 的"Foundation Model is not GTM app"完全等同于 Garry 的"engine vs car"。**这是跨厂商收敛信号 +1**
- 强化 [[gbrain]]：GBrain 是个人尺度的 SoI；Steph 的论断让 GBrain 的 thesis 在企业层也成立
- 强化 [[harness-design]]：Harness 不只是技术架构，也是商业架构 —— 在企业层 = SoI = 价值积累点
- 强化 [[claude-managed-agents]]：Anthropic 是在 build SoI infrastructure 给企业用。Steph 的论点说明 Anthropic 的战略选择是对的
- 强化 [[multi-agent-architecture]]：Khairallah 的 [[3-agent-starter-team]] 是个人版 SoI；企业版需要 N>>3 的 agent orchestration

**挑战/补充**：
- **挑战** [[ryan-sarver]] / "Stella"：Ryan 的 Stella 是**单人 SoI 范例**。Steph 的论点暗示 enterprise SoI 应该 multi-user → Stella 那种"全是 Ryan 的偏好"的设计在企业层不直接复制
- **补充** [[diarization]]：Garry Tan 的 diarization 是"agent 读完所有材料写一页档案"。这一篇说**企业层的 diarization = SoI**。同一原理两个尺度

**扩展方向 / 可继续 ingest 的源**：
- **"Is Software Losing Its Head?"** —— a16z 的 companion piece，作者明确点名。值得 ingest
- **Alex Rampell 的 "hostages, not customers"** 原文 —— 给 SoR 锁定模式的经典分析
- 任何具体的 SoI startup case study（如 11x / Sierra / Decagon 等被 a16z 投的 SoI 公司）

### 11. 对用户（vfan）的启示

基于 vfan 的情况（Singapore growth marketer + AI content builder，LoreAI + blog2video，bilingual EN/ZH）：

#### 短期（本周）
1. **审视你的项目定位**：LoreAI 和 blog2video 当前是 SoR 还是 SoI？
   - **LoreAI**：如果是"另一个内容数据库"则是 SoR（红海）；如果是"reasoning layer that pulls from your CMS / brand voice / past content / analytics → orchestrates content production" 就是 SoI（蓝海）
   - **blog2video**：单纯 transcript-to-video 是 SoR-shaped；加上 "reads your past videos + audience preferences + style guide + current trending topics" 就 SoI-shaped
2. **每个产品的 one-paragraph repositioning**：写一段"我们不是 X SoR，我们是 sitting above your existing tools 的 SoI"

#### 中期（接下来 2-4 周）
1. **如果决定走 SoI 路线，build "many inputs → orchestration → many outputs" 的产品 demo**：
   - blog2video 的 SoI 版：读 LoreAI 的 keyword research + 你的 past videos + audience analytics + 当前 trends → orchestrate chapter / script / thumbnail generation
   - LoreAI 的 SoI 版：读 user's existing CMS + brand guidelines + past performance data → orchestrate cross-channel content production
2. **写**"SoR 还是 SoI" **中文文章** —— 针对中国 indie hacker / SaaS founder，把 Steph 的 thesis 翻译过来 + 加本地化例子（替换 Salesforce 为飞书 / 钉钉 / 金山 / 腾讯文档等中国 SoR）
3. **跟你 X 受众分享 "first prize is a Cadillac" 框架** —— 高度可传播

#### 长期（如果方向被验证后）
1. **Build "Singapore Indie Hacker SoI"**：focused on Singapore / SEA SMB market，做一个垂直 SoI（不是 horizontal）→ 这是 a16z thesis 的 underserved 角落
2. **Productize "vault-as-SoI" pattern**：你现在的 obsidian-vault-starter 本质上是个人 SoI 模板。**打包成 indie hacker SoI starter kit**，配合 Khairallah 的 Four-Files 概念 marketing
3. **Test $5K-$25K consultation 市场**（呼应 Khairallah Week 6 + Steph 这一篇）：给 Singapore SMB 提供"从 SoR 迁移到 SoI"的 consulting，验证企业层是否有付费意愿

### 12. 一句话总结

**"下一个十年的企业软件价值在 reasoning layer，不在 database —— Foundation Model 是发动机，SoI 是车。"**

或更短：**"colocation gravity 翻转成 orchestration gravity —— 你要 own 工作流，不要 own 数据库。"**

---

## Pages created from this source
- [[system-of-intelligence]] — concept (the thesis)
- [[steph-zhang]] — entity
- [[source-stephzhang-system-of-intelligence]] — this page

## Pages updated from this source
- [[filing-cabinet-vs-nervous-system]] — Steph's SoI = enterprise version of Garry Tan's nervous-system framing

## Connections
- Related: [[steph-zhang]], [[system-of-intelligence]], [[filing-cabinet-vs-nervous-system]], [[thin-harness-fat-skills]], [[gbrain]], [[harness-design]], [[multi-agent-architecture]], [[3-agent-starter-team]], [[claude-managed-agents]], [[four-files-context-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-14-stephzhang-system-of-record-to-system-of-intelligence.md | Initial creation (8-section structure) |
| 2026-05-18 | (refresh) | Full rewrite using 12-section comprehensive Chinese study guide structure |
