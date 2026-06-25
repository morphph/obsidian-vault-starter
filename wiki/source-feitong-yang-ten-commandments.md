---
type: source-summary
created: 2026-06-25
last-updated: 2026-06-25
sources:
  - raw/2026-06-21-feitong-yang-ten-commandments-product.md
tags: [product, zero-to-one, pmf, ai-building, founder]
---

# Source: The Ten Commandments for Building Product

**来源：** https://x.com/feitong_yang/status/2068822981946794438（X Article）
**作者：** Feitong Yang @feitong_yang
**发布时间：** 2026年6月21日
**数据：** 34,835 views · 75 likes · 252 bookmarks · 8 reposts

---

## 要点解读

### 1. 元信息

**作者：** Feitong Yang，工程师 + 认知科学家背景，feitong.phd 写作。他写的不是理论——是坐在局里两年、经历三次失败和一次成功的 operator 笔记。这不是 VC 视角，不是研究员视角，是创始工程师视角：每一个决策现场都有他。

**在作者整体输出中的位置：** 这是一篇完整论文，不是推文合集。在 X 上以 Article 格式发布，说明作者有意写出可供长期参考的内容，而不是博流量。252 个 bookmarks 对应 34K views 是 0.72% bookmark rate，极高——人们存档的东西。

**源的性质确认：** 这是 Feitong Yang 本人账号发布的原创文章，不是第三方解读。直接 ingest 无需确认。

---

### 2. 核心论点（Thesis）

作者主张：从零到一构建产品的过程中，存在一种根本性疾病——**所有看起来像进步、实际上是在回避与现实痛苦接触的行为**。AI 的出现让这种疾病更危险，因为它让"假进步"的成本变得几乎为零。这十条戒律是对具体幻觉的防御，不是成功的配方。

一句话核心：**AI 把建设的成本降到地板，但没有降低市场的裁决成本；判断力（而非产能）才是 AI 时代真正的稀缺资源。**

---

### 3. 论证结构

**骨架：**
```
根疾病：任何回避与现实第一手接触的行为
  ├── AI 让这个病变得更危险（更廉价的幻觉）
  └── 十条戒律 = 对十种具体幻觉的防御

第一组（深度递进的同一个失败）：
  1. 你对产品是真的 committed 还是只爱这个 idea？
  2. 你在用自我表达代替对用户的认知吗？
  3. 你知道你的用户具体是谁吗（不是泛称）？

第二组（建设过程中的幻觉）：
  4. 突破 ≠ 产品，Translation is the job
  5. 你不能把"如何使用产品"这个问题扔给用户
  6. 不是所有功能等价，"再加一个功能再发布"是逃避

第三组（衡量和分发层的幻觉）：
  7. 活动 ≠ 结果，要提前面对市场的裁决
  8. 你没有 1000 个用户前不要为 100 万人建系统
  9. 好产品不会自卖，你是它的传教士

第十条（元层面）：
  10. 注意力是火花，产品是燃料，别混淆
```

这个论证结构的迁移价值：它给了一套**诊断框架**——任何时候你觉得自己在"进步"，可以用这个骨架检查：我是在与现实接触，还是在回避？

---

### 4. 关键概念字典

**产品-现实回避 (Product Reality Evasion)**
- **是什么：** 所有"感觉像进步，实际上是原地踏步"的行为——让别人做用户研究然后给你 findings、读 log 代替直接观察用户、AI 生成代码后不见用户就算"完成"
- **为什么重要：** 这是整篇文章的根论点；十条戒律每一条都是它的一个具体变体
- **直觉/类比：** 就像在健身房站在体重秤旁边拍自己"准备好了"的照片，感觉在健身，但从没举起过铁
- **适用场景：** 任何 zero-to-one 产品阶段；AI 时代尤其危险
- **失败模式：** 把"建设"（capability）等同于"产品"（met need）；把 LOC 等同于产品进展

---

**突破 vs 产品 (Capability vs Product)**
- **是什么：** 能力（capability）是输入，不是成品。产品是把能力翻译成一个被满足的需求。翻译本身是第三个独立的工作，不是研究或工程的副产品
- **为什么重要：** AI 时代最危险的幻觉之一——模型能力的飞跃让人以为 breakthrough = product 是自动发生的。ChatGPT 创造了这个神话，但连 OpenAI 自己也不是直接从研究跳到产品的（GPT-3 API 2020 → ChatGPT 2022，中间两年在做 translation）
- **直觉/类比：** 锤子是能力，钉钉子解决的问题是产品。有一把好锤不代表你知道哪里该钉、该为谁钉
- **作者自己的错误：** Minecraft agent 能在 agent 间协作建造 300+ 道具，在 X 和 HN 上爆了，但"从来不清楚这份关注反映了任何人实际上有的需求"
- **失败模式：** 研究 infrastructure + 产品 infrastructure 耦合太早；"下午 AI 就能 demo 一个突破"成为不接触用户的借口

---

**用户具体性 (User Specificity)**
- **是什么：** "Minecraft players" 不是用户；"white-collar workers" 不是用户；"all Excel users" 不是用户。用户必须具体到可以名命的子群体，才能决定产品优先级
- **为什么重要：** 没有具体用户 = 所有优先级判断都在对着一个你发明的人做决策
- **三次相同的教训（作者团队）：**
  - Minecraft：说 users = Minecraft 玩家，后来发现"build 党/PvP 党/社交党"是三个不同的产品
  - Fairies：说 users = 白领，诚实的版本是"我们希望他们成为用户；他们自己不这么看"
  - Shortcut：从"所有 Excel 用户"慢慢找到"高标准金融工作者"——这才是真正的 user
- **AI 加速的新陷阱：** vibe coding 让"为所有用户都加一个功能"感觉几乎免费，于是"选用户"这件事变得可以推迟——其实永远不能推迟
- **失败模式：** 用 log/metrics 代替直接观察——"log 告诉你 what，你渴望的是 why"

---

**注意力是火花，产品是燃料 (Attention is Spark, Product is Fuel)**
- **是什么：** 发布带来注意力，但注意力不等于增长。增长来自产品好到让人留下来、带别人来
- **为什么重要：** 很多人把"发布成功"（spike in DAU）当成"产品成功"的信号
- **两个极端：**
  - Humane AI Pin + Rabbit R1：每一个 spark 都点了（百万 views、预售售罄、媒体吹爆），没有燃料——几个月内崩了
  - Cursor（零营销靠口碑）、Claude Code（静默 research preview）、OpenClaw（GitHub 最多 star）：没有制造火花，燃料点燃了自己
- **作者自身验证：** Shortcut 发布视频 DAU 飙升，然后几乎一样快地跌回去。"让客户留下来的，是产品质量；只有产品让我们被保留"
- **直觉：** 在空桶上点火，火花灭掉了。桶里有燃料，任何一点火花都够

---

**传教士型分发 (Missionary Distribution)**
- **是什么：** 产品不会自卖，发布是起跑线不是终点线。你要用传教士的热情把它带到用户面前，因为没有人会替你带着这份信念
- **为什么重要：** "建设感觉高尚，销售感觉肮脏"——创始人系统性地欠投资于分发
- **关键洞察：** 分发的证明不是 signup 或者掌声（这些都是"免费的"）。是付费、是留存、是有人带着别人来
- **付费 vs 留存先后：** 留存和日活往往比收入更先重要；"建立在萎缩使用上的收入是个短故事"

---

### 5. 框架与心智模型

**"用户拥有问题，你拥有解决方案"（Commandment 2 和 3 之间的分界线）**

> "Users own the problem; you own the solution. They are reliable witnesses to their own pain and unreliable architects of the cure."

套用方式：
- 用户访谈时：疯狂挖 problem（用户是可靠证人）
- 设计解决方案时：不要让用户设计方案（用户是糟糕的架构师）
- 错误用法："用户说他们想要 X 功能" → 直接做 X（这是让用户设计方案）
- 正确用法："用户说他们想要 X" → 往下挖，他们真正的 pain 是什么？Y。设计解决 Y 的方案

**"产品是有机体，不是规格书"（Commandment 8）**

产品随用户找到它而生长，不是在找到用户之前就被蓝图规定好。这意味着：
- 找到 PMF 信号之前，任何"为百万用户而建"的架构都是提前消耗资源
- AI coding agents 让"第一天就建最终架构"感觉免费——这是最新的幻觉

**"把最不舒服的时刻提前"（Commandment 7）**

被真实用户拒绝的时刻是不可避免的。你只能选时机。所以：提前发布，提前听到"不"，让后续工作更容易。衡量对的指标：不是 signup，不是掌声，是 **return**（留存）。

---

### 6. 关键数据与例证

| 数据点 | 支撑的论点 |
|--------|-----------|
| Feitong 团队 Minecraft agent 能协作建造 300+ 道具 | Commandment 4：技术突破 ≠ 产品需求 |
| Sam Altman 承认 ChatGPT 早期留存"atrocious"；但有任何留存就是好信号 | Commandment 7：早期留存 > 早期爆发 |
| OpenAI GPT-3 API 2020 → ChatGPT 2022，中间两年做 translation | Commandment 4：research → product 是第三个独立工作 |
| Garry Tan 37K lines/day across 5 projects, 72-day streak（开发者发现里面有 bloat 和 rookie mistakes） | Commandment 7：LOC 是 throughput，不是价值 |
| Humane AI Pin + Rabbit R1：百万 views 预售售罄 → 几个月崩掉 | Commandment 10：注意力是火花不是燃料 |
| Cursor：零营销靠口碑规模化 | Commandment 10：燃料点火 |
| Shortcut DAU spike after launch video → rapid fallback | Commandment 10：作者自身验证 |
| Shortcut 成功 user = 高标准金融 Excel 用户（不是随便打开 Excel 的人） | Commandment 3：用户具体性 |

---

### 7. 关键引语

> "Every evasion that promises to spare you painful, first-hand contact with reality is an illusion that feels like progress and isn't."
> （所有承诺让你避开痛苦第一手现实接触的回避，都是感觉像进步实则不是的幻觉。）

> "AI makes this more dangerous, not less. It lowers the cost of building so far that the old ways of avoiding reality now look like extraordinary productivity."
> （AI 让这件事更危险，不是更安全。它把建设成本压得如此之低，以至于旧式的现实回避现在看起来像非凡的生产力。）

> "A capability is an input, not a finished good. A product is the translation of that input into a met need, and the translation... is the entire job, not a footnote to the breakthrough."
> （能力是输入，不是成品。产品是把这个输入翻译成被满足的需求，而翻译本身……才是全部工作，不是突破的注脚。）

> "Users own the problem; you own the solution. They are reliable witnesses to their own pain and unreliable architects of the cure."
> （用户拥有问题，你拥有解决方案。他们是自身痛苦的可靠见证人，是治疗方案的糟糕设计师。）

> "A product enters a user's mental space through a single clear wedge... 'It does everything' is not a wedge, it is a fog."
> （产品通过一个清晰的楔子进入用户心智……"它什么都能做"不是楔子，是一团雾。）

> "Logs tell you what; you are starving for why."
> （Log 告诉你是什么；你渴望的是为什么。）

> "When building gets this cheap, building stops being the thing that separates you; judgment does — knowing who you are for, what they need, and whether they will come back and pay. AI automated the part that was never the hard part. The hard part is still yours."
> （当建设变得这么便宜，建设就不再是让你与众不同的东西；判断力才是——知道你为谁而建、他们需要什么、他们是否会回来并付费。AI 自动化了从来不是最难的那部分。最难的那部分还是你的。）

---

### 8. 实操指南

从十条中提炼出可执行 checklist：

**在开始之前：**
- [ ] 我是否愿意亲自去找用户、亲自被拒绝？如果答案是"让 PM 去做然后给我报告"，commit 不存在
- [ ] 我是在构建产品，还是回答研究问题？两件事需要不同资源和不同成功标准

**定义用户时：**
- [ ] 能不能把"用户"说到比"Minecraft players"更具体的级别？具体到：他们在做什么特定的事、为什么他们需要这个、他们怎么评价好坏
- [ ] 去实际坐在他们旁边，看他们怎么用——不是问卷，是观察

**设计产品时：**
- [ ] 用户第一眼是否看得出来怎么用？（affordance 测试）如果不行，这是你的设计问题，不是用户的理解问题
- [ ] 这个功能是为谁服务的？我能说出那个具体用户的名字和他的具体 pain 吗？

**发布时：**
- [ ] 我是否在追加"再一个功能"来推迟发布？这是逃避市场裁决的信号
- [ ] 发布后我要衡量的是 **return**（回头），不是 signup 或 views

**分发时：**
- [ ] 我是否在亲自卖，还是在期待产品自卖？
- [ ] 我制造的是火花（launch moment）还是在建燃料（product quality + retention）？两者都需要，但不能混淆

---

### 9. 对比与反对意见

**作者明确反对什么：**
- "让 AI 在找到用户之前就搭建正确架构" — 这是最新的幻觉
- "LOC 作为进展衡量标准" — 直接点名 YC 掌门人的 37K/day boast
- "把用户研究外包出去然后做决策" — 外包的是你唯一的本职工作
- "注意力=增长" — Humane AI Pin 的解析

**主流做法对比：**
- vs vibe coding 作为生产力指标：文章认为 vibe coding 是好工具但危险武器，它压低了建设成本，同时也压低了幻觉的成本
- vs "好产品会自己传播"：文章彻底否认——"superior distribution routinely beats a superior product"
- vs "先做 MVP 再迭代"：文章不反对这个，但强调 MVP 必须真的接触真实用户，不是内部自嗨的 MVP

**隐含的限制/边界条件：**
- 这篇文章专门关于 **zero-to-one**，不是 scaling 阶段
- Research 有合理的 research infrastructure 需求——作者不是说"永远不建基础设施"，是说"别在找到 PMF 之前就为百万用户建"
- 注意力（launch moment）有价值——作者不是说不做发布，是说发布不能代替产品质量

---

### 10. 与 wiki 知识的连接

**强连接：**
- [[software-entropy]] — "AI 加速了建设，也加速了判断力缺失的放大"。文章是软件熵的产品层延伸："the repo wins" 变成 "the product is still an organism"
- [[source-garry-tan-loc-controversy]] — 文章 Commandment 7 直接引用 Garry Tan 的 37K lines/day 事件作为"活动≠结果"的反例。两个来源从不同角度谈同一现象
- [[openclaw]] — 文章 Commandment 10 把 OpenClaw 列为"产品是燃料"的正面案例（GitHub 最多 star 的非聚合器项目）
- [[claude-code]] — 同 Commandment 10 引用，"quiet research preview folded into a model release"作为燃料案例
- [[ralph-wiggum]] — 隐含：Ralph 的 AFK coding loop 不是 product reality evasion 的吗？文章会说：关键是 loop 的 outcome 是什么，ship → real user contact → measure retention 才闭环

**强化：**
- 深化了 [[agent-vs-workflow]] 的"名命你在做什么"精神——研究 vs 产品是类似的"先诚实再行动"框架
- 深化了 [[quality-gate-loop]] 的"结果导向"——文章给了更完整的"什么叫真正的 outcome"（return, not vanity）

**挑战/补充：**
- 对 [[html-as-output-format]] 有间接补充：Thariq 谈 output format 改善 agent 效果；Feitong 说 affordance 是最重要的产品设计 — 两者都是"形式即功能"的不同应用
- 轻微补充 [[four-files-context-architecture]] 的"Identity file"概念：Feitong 的"具体用户"要求本质上是 Identity file 里应该有的

**可继续探索：**
- shortcut.ai 的产品演化值得 ingest（他们的正式 blog/产品页）
- Sam Altman 与 Vinod Khosla 的那个 2025 访谈（关于 ChatGPT 早期 atrocious retention + 任何留存都是好信号的论述）值得单独 ingest

---

### 11. 对 vfan 的启示

你在做的：LoreAI (SEO 内容平台) + blog2video (AI 精读视频流水线) + AI 知识库。这篇文章的每一条都与你直接相关。

**短期（本周可做）：**
- **Commandment 3：** LoreAI 的"用户"是谁？说"做 SEO 内容的人"和说"Minecraft players"一样模糊。本周的练习：能不能命名一个具体的人，他/她在用 LoreAI 做什么具体的事、有什么具体的 pain？
- **Commandment 7：** blog2video 的 outcome 指标是什么？Views 是注意力，不是 outcome。是否有人在看完一个视频后回来看下一个？这是 return 的最小可测形式

**中期（接下来 2-4 周）：**
- **Commandment 5（affordance）：** 当你把 LoreAI 或 blog2video 展示给一个不认识你的人，他们第一眼知道它是干什么的吗？如果需要解释，这是设计问题，不是他们的问题
- **Commandment 9（传教士）：** 你是 AI 内容领域有 credibility 的 builder。你是否在把 blog2video 带到它的用户面前，还是在等它被发现？

**长期（方向被验证后）：**
- **Commandment 4：** 你在做的很多事在技术上是 capability（用 AI 做视频转换、知识图谱），但 product 问题一直是：谁的具体需求被满足了？如果某一天某个用户说"这个改变了我消费内容的方式"并且持续回来——那才是从 capability 到 product 的 translation 发生了
- **Commandment 10：** 你在建燃料，不只是制造火花。知识库这件事本身是一个长期燃料项目。坚持比爆发更重要

---

### 12. 一句话总结

> AI 把建设的成本压到地板，但硬的部分——知道为谁建、他们需要什么、他们会不会留下来——还是你的。

---

## 收尾互动

读完这篇文章之后，想问你三件事：

1. **哪一条最打中你？** 十条中有没有一条你觉得"这说的就是我/我们现在在做的事"？
2. **是否需要 ingest 相关源？** 两个候选：
   - Sam Altman x Vinod Khosla 2025 对谈（关于 ChatGPT 早期 atrocious retention 那段）
   - shortcut.ai 官网/博客（Feitong 团队对他们产品的正式表述）
3. **这次解读的哪部分对你最有用？** 帮助我校准未来 ingest 的侧重点

---

## Source Log

| Date | Source | What changed |
|------|--------|-------------|
| 2026-06-25 | raw/2026-06-21-feitong-yang-ten-commandments-product.md | Created; full Chinese study guide |
