# Best Practices for Claude Fable 5 — 深度调研报告
> depth: standard · generated: 2026-07-08 · tools: WebSearch, WebFetch | skipped: deep-research(冗余,直取一手源已交叉核验), last30days/bird/summarize(VPS-only,本机缺失)
> ⚠️ 互动数据：X/YouTube 全部为「推断·未实测」（本机无 scanner），已逐条标注
> ⚠️ 知识截止：本机训练截止 2026-01，Fable 5 于 2026-06 发布 → §1 事实**全部依赖外部一手源**，已逐条挂官方 URL + 核验状态

## TL;DR
Claude Fable 5（`claude-fable-5`，2026-06-09 GA）是 Anthropic 面向**最难的长时程任务**的旗舰模型：1M context、$10/$50 定价、只有 adaptive thinking、raw CoT 永不返回。它的最佳实践和前代**反着来**——**给目标不给步骤、给理由不给清单**，因为它被造来吸收模糊、自己想「怎么做」；过度规定反而拉低产出。三个对 builder 最要命的落地点：①**effort 是主拨盘**（默认 high，first-shot 正确性优先才 xhigh）；②**必须给 refusal → Opus 4.8 兜底**（善意的 cyber/bio 任务也可能被安全分类器拒，返回 HTTP 200 的 `stop_reason:"refusal"`）；③**迁移前先改 harness**（超时拉长、异步查进度、别显示剩余 token 倒计时——会让它提前收尾）。我们的增值：把「官方 prompting guide + Simon Willison 实测 + Thariq 一手 field guide」三源合成一张**中文 builder 的迁移清单**，市面 X 科普帖没做到这个纵深。

## 0. Vault 已有锚点（查内）
- [[claude-model-family]] — 我们已把 Sonnet/Opus/Haiku 的能力/成本分层讲过；Fable 5 是这条线的**新顶层**，本报告是对该页的自然延伸。
- [[claude-opus-4-7]] · [[xhigh-effort-level]] · [[task-budgets]] · [[adaptive-thinking]] — Opus 4.7 引入的 effort/task-budget/adaptive-thinking 三件套，Fable 5 **继承并放大**（effort 成主拨盘、adaptive thinking 成唯一模式）。旧页的框架可直接迁移复用。
- [[thariq]] · [[source-thariq-session-management-1m]] · [[html-as-output-format]] — Thariq 是 Fable 5 的一手 driver；他的 1M-context / HTML-as-output 旧观点在 Fable 语境下依然成立。
- [[verification-loops]] · [[self-evaluation-bias]] — Fable 官方推荐「fresh-context verifier subagent > 自我批判」，正是我们已追踪的 verification-loops 在新模型上的印证。
- **raw 已有源**：`raw/2026-07-08-fable-finding-your-unknowns.md`（Thariq「Finding Your Unknowns」，已入库）。
- ⚠️ **drafts/ 无 Fable 5 成稿** → 这是**首次覆盖该话题**，无重复 draft 风险。

## 1. 这个话题是什么 — 事实轴
> 逐条对官方源核验。⚠️ 全部来自外部（超本机知识截止），下游 writer 只许穿透引用这些原始 URL。

**身份与发布**
- **`claude-fable-5` 是 Anthropic「最强的广泛发布模型」，定位「a Mythos-class model made safe for general use」** — [官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — ✅ verified
- **2026-06-09 GA，上线 Claude API + AWS Bedrock + Google Vertex + Microsoft Foundry** — 同上 — ✅ verified
- **姊妹模型 Mythos 5（`claude-mythos-5`）= 同一底层但去掉安全分类器，仅经 Project Glasswing 限量发布** — 同上 — ✅ verified
- **家族分层：Sonnet 5（执行）→ Opus 4.8（判断）→ Fable 5（最难的长时程升级）**，Fable 是顶层 — [DigitalApplied](https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026) — ⚠️ unconfirmed（社区综合，多源一致但非官方措辞）

**规格与定价（官方）**
- **默认 1M-token context；单次请求最多 128k output tokens** — [官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — ✅ verified
- **$10 / M input，$50 / M output；prompt-caching 九折优惠；US-only 推理加价 1.1×** — 同上 + anthropic.com/claude/fable — ✅ verified
- **30 天数据保留，无 zero-data-retention 选项（被列为「Covered Model」）** — 同上 — ✅ verified

**effort / thinking / budget 控制**
- **effort 是首要的智能/延迟/成本拨盘：low / medium / high / xhigh；默认 `high`；`xhigh` 用于「first-shot 一次做对」的关键任务** — [官方 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) — ✅ verified
- **adaptive thinking 是唯一 thinking 模式**：不支持 `thinking:{"type":"disabled"}`，无 extended-thinking 预算；**raw chain-of-thought 永不返回**，只给 `summarized` 或 `omitted`（默认）thinking block — 同上 — ✅ verified
- **task budgets 处于 beta**（`task-budgets-2026-03-13` header） — ✅ verified
- 还支持：memory tool、code execution、programmatic tool calling、context editing、compaction、vision — ✅ verified

**安全 / 拒答（集成关键）**
- **对 3 个领域跑安全分类器：进攻性网络安全、生物/生命科学、reasoning-extraction（试图套取 summarized thinking）** — [官方 intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — ✅ verified
- **拒答返回 `stop_reason:"refusal"`，且是成功的 HTTP 200（不是 error），并指明哪个分类器触发；官方建议服务端/客户端 fallback 到 Opus 4.8** — 同上 — ✅ verified
- **保护措施平均在 <5% 会话触发；拒答（出 output 前）不计费；fallback 退还 prompt-cache 切换成本** — 同上 — ✅ verified
- ⚠️ **善意的 cyber/bio 工作也可能误触分类器（false positive）** — 同上 — ✅ verified

**相对 Opus 4.8 的行为变化（官方文档）**
- 更长时程自主（可多天目标导向运行）、well-specified 问题上更高 first-shot 正确率、显著更强 vision、更好的找 bug 召回、更主动派发/维持并行 subagent、更好处理模糊 — [官方 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) — ✅ verified
- **单次请求在 high effort 下可跑数分钟；自主运行可延续数小时 → 迁移前先调 client 超时/streaming/进度 UI** — 同上 — ✅ verified

> [!warning] 姊妹模型定价不一致
> 二手源对 Sonnet 5 报价矛盾（$2/$10 vs $3/$15）。**只有 Fable 的 $10/$50 是官方确认的**。做 family 定价对比时，Sonnet/Opus 价一律标「二手·待核」。

## 2. 焦点实体深挖 — Fable 5 在 Claude 5 家族里的位置
- Fable 5 不是「更快的 Opus」，而是**能力/成本都更高的另一档**：Simon Willison 实测称其「a beast — slow, expensive」，一天烧掉 $110，但一次完成「several days' worth of work」（[链接](https://simonwillison.net/2026/Jun/9/claude-fable-5/)，✅ 实操）。
- **路由经济学**（社区共识，⚠️ 非官方）：80–90% 流量留在便宜的 Sonnet/Opus，只把**最难的长时程任务**升级到 Fable 的 $10/$50 档 — [DigitalApplied](https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026)。
- **redeploy 事件（值得知道的背景）**：Fable 5 曾于 **2026-06-12 下架**（美国出口管制 + Amazon 报告的一个绕过安全措施的越狱），**2026-07-01 完整重新部署**，改进的分类器在 >99% 情况下拦住该技术（代价是更多 false positive）— [anthropic.com/news/redeploying-fable-5](https://www.anthropic.com/news/redeploying-fable-5) — ✅ verified。→ 对 builder 的含义：**误拒率上升是这次修复的已知代价**，兜底逻辑更不能省。

## 3. X / Twitter — Top N（增长轴 · 渠道层）
> ⚠️ 互动数据「推断·未实测」（本机无 bird）；下列均为长文/thread 形式为主

### #1 @trq212（Thariq，Claude Code @ Anthropic）— 一手 driver 的 field guide
- 链接 https://x.com/trq212/status/2073100352921215386 · X native Article · 2026-07-04
- 互动：3.35M views · 20,168 bookmarks · 8,885 likes（**实测**，captured 于 raw 文件）— 是本清单里唯一有实测数的
- 核心内容：「Finding Your Unknowns」——把 agentic coding 的瓶颈重构为「厘清 unknowns 的能力」；Known/Known-Unknown/Unknown-Known/Unknown-Unknown 四象限；Fable 是第一个「产出被我澄清 unknowns 的能力卡住」的模型。
- **写作风格拆解**：精读级 · 第一方视角 · 概念框架（四象限）+ 配套 HTML 交互 artifact。给写稿的弹药：**「the map is not the territory」这类金句 + 可复用的四象限模型**。⚠️ **已在库**（§0）。

### #2 @milesdeutscher — 官方 guide 的最高触达科普转译
- 链接 https://x.com/milesdeutscher/status/2064882870037225762 · thread · 互动「推断·未实测」（体感高）
- 核心内容：把官方 prompting guide 平民化——「Fable 不该像其他模型那样被 prompt，它被造来自主运行」；先讲 effort 选择。
- **写作风格拆解**：清单式 · 钩子开头（"Anthropic posted a FULL GUIDE…"）· 高转发结构。学它的**「官方文档→10 条清单」转译打法**。

### #3 @nateherk — 工程师实操长文
- 链接 https://x.com/nateherk/article/2072431375530008871 · X Article · 「推断·未实测」
- 核心内容：「How Anthropic Engineers Actually Prompt Fable 5」——把工程 prompting patterns 提炼成长文。
- **写作风格拆解**：实操 · 「内部人怎么做」框架（authority hook）。

#### 补充值得关注
| 作者 | 链接 | 形式 | 一句定位 |
|------|------|------|---------|
| @PawelHuryn | https://x.com/PawelHuryn/article/2064979937543549362 | X Article | PM 导向的「Ultimate Guide v2」（safeguards + subagents） |
| @ProductFaculty (Moe Ali) | https://x.com/ProductFaculty/status/2073306835696894413 | post | 格言式：让 Fable 读你自己的聊天记录/skills，找你工作流的盲点 |
| @PrajwalTomar_ | https://x.com/PrajwalTomar_/article/2065408713448640890 | X Article | 逆向钩子「You're Prompting Fable 5 Wrong」 |

## 4. Web / 博客 — Top N（增长轴 · 渠道层）
（Web 有实测发布日期/作者，通常无互动数属正常）

### #1 官方 Prompting Guide — **权威最佳实践页**（必读 + 必 ingest）
- 链接 https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 · Anthropic · 2026-06
- 核心内容：effort 分级、长 turn、指令遵循、grounding progress claims、subagents、memory 系统、send-to-user tool、scaffolding 重构——**§6 几乎每条最佳实践的原始出处**。
- **写作风格拆解**：技术权威 · 可直接复制的 prompt 片段。

### #2 官方 Introducing Fable 5 & Mythos 5（docs）
- 链接 https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 · 2026-06-09
- 核心内容：API 层真相——model ID、1M/128k、定价、adaptive-thinking-only、refusals/fallback/billing、支持特性。**§1 事实骨架**。

### #3 官方发布公告
- 链接 https://www.anthropic.com/news/claude-fable-5-mythos-5 · 2026-06-09 · blog
- 核心内容：定位 + benchmark（Stripe 5000 万行迁移、Cognition FrontierCode、Hebbia Finance）+ 安全框架。**写作风格：数据背书式发布公告**——学它「用 partner 案例做证据」。

### #4 Simon Willison「Initial impressions」— 最佳独立实测
- 链接 https://simonwillison.net/2026/Jun/9/claude-fable-5/ · 2026-06-09 · 长文 review
- 核心内容：动手实测——「a beast, slow, expensive」，一天 $110，真实任务（CPython-on-WASM、human-in-the-loop 暂停/续跑）。
- **写作风格拆解**：实操叙事 · 独立可信 · **真实成本数字**（写稿最有说服力的弹药）。

### #5 DigitalApplied「哪个模型何时用」+ #6 the-decoder「powerful, expensive, heavily filtered」
- https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026（决策框架·表格）· https://the-decoder.com/claude-fable-5-the-first-mythos-model-is-powerful-expensive-and-heavily-filtered/（平衡的新闻分析，擅长「过滤/安全」角度）

## 5. YouTube — Top N（增长轴 · 渠道层）
> ⚠️ 观看/互动「推断·未实测」（本机无 summarize/last30days）
- **覆盖稀薄，如实报告**：Fable <1 个月大，文本/文档主导，无权威深度教程。
  - https://www.youtube.com/watch?v=6ERUGFurDHY —「Intent-driven development with Claude Code & Fable 5」walkthrough，~2026-07 初，契合「给目标不给步骤」主题。
  - https://www.youtube.com/shorts/iiJzeA_XyIo —「How to Use Claude Fable 5」quick-tips short，深度低。
- **对我们的含义**：YouTube 是**空窗**——若做视频（blog2video 管线），现在几乎无竞争。

## 6. 核心洞察 + 最佳实践
> **溯源标注纪律**：每条标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游 writer 只许穿透引用原始出处，绝不引本报告。

**5 条跨渠道洞察**
1. **Fable 的最佳实践与前代反向**——从「精确规定步骤」转向「给目标 + 给理由，让它自己想怎么做」。这是所有官方 + 社区源的**共识主轴** [外部: prompting guide]。前代为弱模型搭的 prescriptive skill 现在是**枷锁**，需 audit + prune —— 正是 [内部/Tier-1: assumptions-expire] 的又一实证。
2. **安全分类器是新的一等集成风险**：refusal 走 HTTP 200、善意任务也可能误触、redeploy 后误拒率还升高了 → **兜底到 Opus 4.8 不是可选项** [外部: introducing-fable-5 · redeploying-fable-5]。
3. **「长」改变了 harness 契约**：数分钟到数小时的运行让 client 超时、异步查进度、进度 UI 成为迁移前置项；**别显示剩余 token 倒计时**（触发 context-anxiety 式提前收尾）[外部: prompting guide] —— 呼应 [内部/Tier-1: context-anxiety] [内部/Tier-1: task-budgets]。
4. **verifier > 自我批判**：官方推荐用 fresh-context verifier subagent，而非让模型自评 —— [内部/Tier-1: verification-loops] [内部/Tier-1: self-evaluation-bias] 在新模型上被官方背书。
5. **成本结构逼你做路由**：$10/$50 让「全流量上 Fable」不经济；80–90% 留 Sonnet/Opus、只升级最难长时程任务 [外部: digitalapplied]（⚠️ 社区共识非官方）。

**可执行最佳实践清单**（全部 [外部: prompting guide]，另标者除外）
1. **给目标不给清单**——Fable 会自己补「怎么做」；过度规定拉低产出；先 audit/prune 旧的 prescriptive skill。
2. **给理由**：用模板「I'm working on [大任务] for [谁]. They need [产出使能什么]. With that in mind: [请求]」。
3. **effort 是主拨盘**：默认 `high`；first-shot 正确性 > 速度时 `xhigh`；日常降 `medium/low`（仍胜前代 xhigh）。
4. **抑制高 effort 的过度发挥**：一句「do the simplest thing that works well，别超需求地重构/加抽象/处理不可能的情况」。
5. **结论前置**：最终总结先给 outcome/TLDR；用一句简洁指令，别枚举所有反模式（指令遵循够强）。
6. **grounding 进度**：要求它把每条进度 claim 对照实际 tool 结果核验——几乎消除长跑中的假状态报告。
7. **划边界**：用户是在 think-out-loud 时，交付=你的评估，别擅自动手改。
8. **放开用并行 subagent**：优先 async（非阻塞）编排；long-lived subagent 靠 cache read 省成本；用 fresh-context verifier 而非自评。
9. **建 memory 系统**（Markdown）：一课一文件、顶部一行摘要、记下纠正+确认的做法；让 Fable 复盘旧会话来 bootstrap。
10. **显式 checkpoint 规则**：只在破坏性/不可逆动作、真实 scope 变更、只能人做的输入时暂停——别枚举每种情况。
11. **自主管线加 system reminder**：「你在自主运行、用户没盯着」——防它停在问权限、或以「I'll now run X」的承诺结尾却不真调工具。
12. **别让它复述推理**——会触发 reasoning_extraction 拒答分类器、推高 fallback；读 summarized `thinking` block 即可。
13. **建 `send_to_user` tool**：长 async agent 用它把逐字交付/进度送达用户而不结束 turn（tool input 永不被 summarize）；必须配 system-prompt 指令否则模型很少调。
14. **迁移操作**：拉长 client 超时、改成异步查运行、**别暴露剩余 context/token 倒计时**（会让 Fable 提前收尾或建议开新会话）。
15. **往高打**：把你**最难的未解问题**丢给 Fable，让它 scope + 问澄清问题；只拿简单任务测会低估它。
16. **路由经济学** [外部: digitalapplied]：~80–90% 流量留 Sonnet/Opus，只升级最难长时程任务到 Fable。
17. **一定接 refusal → Opus 4.8 兜底**（服务端或客户端）[外部: introducing-fable-5]。

## 7. 对内容创作的启示 — 增长轴 → 排序的内容角度
**这是两轴相乘的地方，也是 /draft 的入口。**

### 时机窗口
Fable 5 才发布不到一个月（2026-06-09），刚经历下架→重部署（07-01），**热度正在爬坡**：官方 guide 已出、X 科普帖在抢转译红利、但**中文纵深内容 + YouTube 几乎空窗**。**现在就是切入窗口**——趁官方 guide 新、二手转译还浅，用「一手源合成 + 中文 builder 迁移视角」抢占；再晚会被科普帖淹没。

### 排序的内容角度（每个 = 一个内容赌注）

#### 角度1（推荐）《从 Opus 到 Fable：一个中文 builder 的迁移清单》
- **缺口**：X 上全是「官方 guide 转译」科普帖，没人做**「我原来这么用 Opus，换 Fable 该改哪几处」的迁移视角**；中文纵深为零。
- **受欢迎度证据**：官方 guide + milesdeutscher 转译帖（体感高转发，「推断·未实测」）证明「怎么 prompt Fable」是热题；Simon Willison 实测证明有实操需求。
- **参考写法**：学 milesdeutscher 的「官方文档→清单」转译 + Simon 的「真实成本数字」叙事 → 我们改成**「迁移前/后对照 + 每条挂官方出处」**。
- **渠道 + 形式**：中文博客长文（GEO 优化：每条 best practice 挂官方链接 = +40% AI 引用率；带 $10/$50、<5%、128k 等具体数字 = +37%）。
- **依赖**：§1 全部事实 + §6 清单；候选源 #1（prompting guide）#2（intro）#4（Simon）。

#### 角度2 《Fable 5 的「拒答」会咬你：安全分类器 + Opus 4.8 兜底实操》
- **缺口**：安全/过滤角度只有 the-decoder 泛泛谈，**没人写「集成层怎么处理 refusal」的实操**（HTTP 200 + stop_reason + fallback 代码）。
- **受欢迎度证据**：redeploy 事件本身有新闻性；the-decoder「heavily filtered」定位说明这是关注点。
- **参考写法**：the-decoder 的平衡分析 → 我们改成**「给 builder 的兜底 checklist + 伪代码」**。
- **渠道 + 形式**：中英双语技术短文 / X 长文。
- **依赖**：§1 安全段 + §2 redeploy 事件；候选源 #2 #5。

#### 角度3 《给目标不给步骤：Thariq 的「四象限 unknowns」怎么用在 Fable 上》
- **缺口**：把 Thariq 的一手概念框架（already in vault）× 官方「give goals not steps」原则**接起来**——概念 + 落地，X 上两者分离。
- **受欢迎度证据**：Thariq 帖 3.35M views · 20,168 bookmarks（**实测**）——最硬的受欢迎度信号。
- **参考写法**：Thariq 的精读级 + 四象限模型 → 我们加**「每象限对应一条 Fable prompting 动作」**。
- **渠道 + 形式**：中文精读长文（可复用已有 raw 精读）+ blog2video 视频脚本（YouTube 空窗，先发优势）。
- **依赖**：`raw/2026-07-08-fable-finding-your-unknowns.md`（已在库）+ §6 清单第 1、10、11 条。

### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
|------|------|---------|
| [[thariq]] (@trq212) | Claude Code @ Anthropic，Fable 日常 driver | 一手模型行为 + 概念框架（unknowns）；已在 vault |
| @milesdeutscher | 高触达 AI 科普 | 官方文档→清单的转译打法参考 |
| Simon Willison | 独立技术 blogger | 最可信的独立实测 + 真实成本数字 |
| @nateherk / @PawelHuryn | 工程/PM 长文作者 | prompting patterns 的不同受众切法 |

### 内容形式参考库
- **长文学谁**：Simon Willison（实操叙事 + 真实数字）· 官方 prompting guide（可复制 prompt 片段结构）。
- **视频学谁**：YouTube 空窗——无范本，等于先发者定义形式（blog2video 机会）。
- **X 学谁**：milesdeutscher（官方→清单钩子转译）· Thariq（精读级 + 概念框架，实测最高互动）。

## 附录：关键时间线
| 日期 | 事件 |
|------|------|
| 2026-06-09 | Claude Fable 5 + Mythos 5 GA 发布；官方 prompting guide + intro docs 上线 |
| 2026-06-09 | Simon Willison 实测「Initial impressions」；milesdeutscher 等科普转译帖起量 |
| 2026-06-12 | Fable 5 下架（美出口管制 + Amazon 报告越狱绕过安全措施） |
| 2026-07-01 | Fable 5 完整重新部署（改进分类器，>99% 拦截该技术，代价：误拒率升高） |
| 2026-07-04 | Thariq「Finding Your Unknowns」X Article 发布（3.35M views·20,168 bookmarks，已入库） |
| 2026-07-08 | 本调研（Fable 发布未满 1 月，中文纵深/YouTube 仍空窗）|
