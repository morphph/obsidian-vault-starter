# 低成本多模型 agent harness（Fable 脑 + 便宜手 + Fable 评审）— 深度调研报告
> depth: standard · generated: 2026-07-12 · tools: WebSearch·WebFetch·deep-research engine | skipped: bird/last30days/summarize（VPS-only,本机缺失）
> ⚠️ 互动数据：X/YouTube 全部为「推断·未实测」（本机无 scanner），已逐条标注
> ⚠️ 知识截止：本机训练截止 2026-01；Fable 5(06)、GPT-5.5、Lance/Hashimoto 本组帖均**超截止** → §1 事实全部依赖外部一手源，逐条挂 URL + 核验状态
> ⚠️ **headless 调起**：按 Headless rule 执行——plan checkpoint skipped、消歧自决并记录（见文末注记）

## TL;DR
把「一个贵模型从头跑到尾」拆成三段：**Fable 5 @ xhigh 做规划/架构 → 更便宜的订阅制 coder（如 GPT-5.5）做执行 → Fable 5 @ 低 effort 再做评审**。经济命题是把典型 **$50+ 的单次复杂往返压到几美元**——因为绝大多数 token 花在「执行」这一段，而执行不需要顶层智能；顶层智能只在「拆解」和「判断」两处稀疏使用。⚠️ 这个 $50→几美元 的具体数字来自 **Mitchell Hashimoto（@mitchellh）** 的一条帖（非种子源署名的 Lance Martin），单一实践者、X 正文被墙未能一手核验，**当「示例数据点」而非 benchmark**。真正多源可靠的两根支柱是：①**角色分工谱系**——「贵 planner + 便宜 coder」不是 Fable 才有的新招，aider 的 architect/editor 早在 2024 就做到「SOTA at 14× less cost」；②**评审段经济学**——Lance Martin 实测 fresh-context verifier 抓到 **73%** 的种子缺陷，而同上下文自我批判只有 7–33%，且「判断比生成便宜」，所以让最贵的模型只做评审反而省钱。我们的增值：把「Hashimoto 的 harness 结构 + Lance 的 judge 数据 + aider 的两年谱系 + 官方定价」合成一张**中文 builder 的 model-triage 落地图**，并诚实标注它的脆弱处（模型名会过期）。

## 0. Vault 已有锚点（查内）
- ⚠️ **强 dedup 对象**：`research/best-practices-for-claude-fable-5/`（2026-07-08，depth standard）已覆盖 Fable 5。其 §6#16「路由经济学」= **intra-Anthropic**「80–90% 流量留便宜 Sonnet/Opus、只把最难长时程升级到 Fable」。**本报告的新增量 = 跨厂商三段式（Fable 脑 + 非-Anthropic 便宜手 + Fable 评审）+ 可量化省钱 + judge 段经济学**——是那条路由判断的**正交升级**，不是重复。对应的 draft `drafts/best-practices-for-claude-fable-5.*`（**仍卡在 Gate 1，无 take、未发布**），角度是「Opus→Fable 迁移清单」，与本话题不同。
- [[cross-modal-review]] — Garry Tan 的「同一产出、跨厂商三模型评审」（Opus 精度 / GPT-5.5 召回 / DeepSeek 去泛化）。**本话题是它的成本工程化近亲**：cross-modal-review 讲「跨家评审抓不同错」，本报告讲「把贵模型压到只做评审这一段来省钱」。GPT-5.5 在该页已作「recall 档」出现——同一模型、不同用法。
- [[llm-judgment-vs-scripts]] · [[thin-harness-fat-skills]] — 规划/执行/判断分层的母框架；本话题是「按 token 成本给每一层配不同价位模型」的具体化。
- [[verification-loops]] · [[self-evaluation-bias]] — Lance 的 73% vs 7–33% 数字，正是这两页在 Fable 上的**量化背书**：fresh-context 评审 > 自评。
- [[claude-model-family]] · [[claude-opus-4-7]]/[[xhigh-effort-level]]/[[task-budgets]] · [[prompt-cache-optimization]] — 定价分层、effort 拨盘、cache 省成本三条旧线，本报告直接复用。
- [[agent-vs-workflow]] — 三段式「plan→act→judge」本质是 Anthropic 五模式里的 **Evaluator-Optimizer + Orchestrator-Workers** 的成本版。
- **raw 已有源**：`raw/2026-07-08-fable-finding-your-unknowns.md`（Thariq，是 source 非已发角度）。

### 内部「旧判断回收」（供 Gate-1 写新 take 参照/推翻）
- 旧判断（best-practices 报告 §6#16）：**「省钱靠留在便宜的 Claude 档」**。本报告的新证据推它一步：**省钱的更大杠杆是「跨厂商按段分诊」——把最贵智能只放在 plan+judge 两个稀疏点，执行段外包给更便宜的手**。旧判断没错，但只用了一半的牌。

## 1. 这个话题是什么 — 事实轴
> 逐条对官方/一手源核验。⚠️ 全部外部（超本机知识截止）；下游 writer 只许穿透引用这些原始 URL，绝不引本报告。

**核心命题（种子）**
- **三段式 harness：Fable xhigh 规划 → GPT-5.5(订阅) 执行 → Fable xhigh 评审；「planning+judge 成本在几美元量级 vs 典型 $50+ 的全程往返」** — [@mitchellh](https://x.com/mitchellh/status/2072715852944957531)（**注意：这是 Hashimoto 原话，非种子署名的 Lance**）— ⚠️ unconfirmed（X 正文被墙 402，逐字引用来自搜索面、非一手抓取；单一实践者、非 benchmark）
- **种子 URL 实为 Lance Martin「Cost effective harnesses with Fable」长文**——主张 harness 要学会「何时才花顶层智能」，Fable 只碰 plan + review、执行跑更便宜的档 — [@rlancemartin](https://x.com/RLanceMartin/article/2075641284635799865) + 伴随帖「i measured performance vs cost on a few different evals with Fable 5」([2075642836805194222](https://x.com/RLanceMartin/status/2075642836805194222)) — ⚠️ unconfirmed（正文未能一手抓取，主旨据搜索面重构）

**评审段经济学（这是最硬的一根支柱）**
- **fresh/independent-context verifier 抓到 ~73% 的种子缺陷，同上下文自我批判仅 7–33%；grader 跑 `effort:low` 即可，因为「判断证据比生产证据便宜」** — [Lance「Designing loops with Fable 5」2026-06-10](https://x.com/RLanceMartin/article/2064397389189071163) — ✅ 广泛引用（一手正文未抓取，但多处一致）。→ 这解释了「为什么该把最贵模型放去做评审」：评审段 token 少、可低 effort，单位成本低而拦截率高。

**官方定价锚（做 triage 算账的地基）**
- **Fable 5 = $10/M in · $50/M out** — [platform.claude.com/…/pricing](https://platform.claude.com/docs/en/about-claude/pricing) — ✅ verified（多源一致，含 vault 内部 best-practices 报告）
- **Opus 4.8 = $5/M in · $25/M out** — 多源 — ✅ verified
- **GPT-5.5 = $5/M in · $30/M out**；batch/flex $2.50/$15；>272K 长上下文档 $10/$45 — [developers.openai.com/…/gpt-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) — ✅ verified
- **Sonnet 5 = 引导价 $2/$10（至 2026-08-31）之后 $3/$15；新 tokenizer 每 token 多吐 1.0–1.35×** — 官方 + finout — ✅ verified（tokenizer 会吃掉一部分名义降价）
- **更便宜的替代 coder（第三方报价）**：DeepSeek V4 Flash $0.14/$0.28、Qwen3.5-Plus $0.40/$2.40 — morphllm — ⚠️ third-party
- **「订阅制 coder」**：Hashimoto 原话点名 GPT-5.5「(subscription)」当**平价定额的手**——即用 ChatGPT/Codex 订阅额度写代码、绕开 per-token API 账单。⚠️ 官方 Codex 订阅具体档价未能一手锚定，标「未实测」。

**一次同任务实测对比（第三方新闻）**
- **同一编码任务：Fable $9 vs GPT-5.5 $1.50（~6×），文章把「model triage」称为新技能** — [The New Stack](https://thenewstack.io/claude-fable-cost-model-triage/) — ⚠️ headline-verified（正文有墙）。这是「贵脑/便宜手」价差的直观量级。

**Fable 集成侧事实（沿用 vault best-practices 报告，穿透引用官方）**
- effort 拨盘 low/medium/high/xhigh，默认 high、xhigh 用于 first-shot 正确；adaptive-thinking-only、raw CoT 永不返回；refusal 走 HTTP 200 `stop_reason:"refusal"`、官方建议 fallback Opus 4.8；2026-06-12 下架→07-01 重部署（误拒率升高为代价）— [官方 prompting guide / intro / redeploying-fable-5] — ✅ verified。→ **对本 harness 的含义：三段式里 Fable 的两段都要接 refusal 兜底；执行段用非-Anthropic coder 反而天然规避了 Fable 分类器误拒。**

> [!warning] 署名订正（影响整个角度的诚实性）
> 种子任务把「Fable planner + GPT-5.5 coder + Fable judge / $50→几美元」整体归给 **Lance Martin**。核验后：**具体三段结构 + $50 数字 = Mitchell Hashimoto（@mitchellh）**；**Lance 的贡献 = 评审段经济学（73%）+ effort 分诊纪律**。种子 URL 本身确是 Lance 的「Cost effective harnesses with Fable」文。报告全程**分开署名**，$50 数字标为单一实践者示例。

## 2. 焦点实体深挖 — 「三段式分诊 harness」这个模式
**它不是 Fable 独有的新发明，而是一条两年谱系的最新一格。**
- **aider architect/editor（2024-09，先例基石）**：把「推理」和「编辑」拆给两个模型——o1-preview(architect) + o1-mini/deepseek(editor) = **85.0% SOTA**；后来 R1(architect) + Sonnet(editor) = **64.0% polyglot SOTA「at 14× less cost」**（[aider architect](https://aider.chat/2024/09/26/architect.html) · [R1+Sonnet](https://aider.chat/2025/01/24/r1-sonnet.html)）— ✅ benchmark verified。⚠️ 常被引的「比 architect-alone 便宜 30–50%」**不在 aider 原文**，仅第三方解读有，标 ❌ 未证。
- **Continue #3928 / Cline·Roo-Code plan-act**：社区早就在「plan 模式用强推理、act 模式用便宜编辑」——[continue#3928](https://github.com/continuedev/continue/issues/3928)。Fable 的新意不在「拆」，而在**把 planner/judge 那一档抬到足够贵（$50/M out），使这套套利落差变得戏剧性**。
- **Fable 时代的「谁当脑」正在漂移**：Hashimoto 已发帖说拿到 GPT-5.6/Sol 早期权限、**Sol 现在是他的默认 planner/judge**（[2074862990214787301](https://x.com/mitchellh/status/2074862990214787301)）。→ **模式（角色分工）是耐用的，模型名是易朽的**——这必须写进结论，否则文章一发布就在半衰期上。

## 3. X / Twitter — Top N（增长轴 · 渠道层）
> ⚠️ 互动「推断·未实测」（本机无 bird）；X 正文多被墙(402)，引语来自搜索面

### #1 @mitchellh（Mitchell Hashimoto，Ghostty/HashiCorp 创始人）— **本角度的金句源**
- 链接 https://x.com/mitchellh/status/2072715852944957531 · 单帖 · ~2026-07 初(推断) · 「推断·未实测」
- 核心：逐字「Fable xhigh as planner/architect, GPT 5.5 xhigh (subscription) as coder, then Fable xhigh again as judge… planning+judge in the ~few dollar range vs typical $50+ full round trips」。
- **写作风格拆解**：第一人称、无炒作、**claim→config→成本差一口气讲完**。给写稿的弹药：这种「个人战果 + 精确配置 + 一个成本数字」的节奏是所有相关帖的共同句法，直接学。
- ⚠️ 配套需知：#2 他的 freshness caveat + #3 他的「Fable 慢且贵」怀疑帖——同一人，保持诚实用。

### #2 @rlancemartin（Lance Martin，LangChain）— **judge 经济学 + 谱系导师声**
- 链接 https://x.com/RLanceMartin/article/2075641284635799865（种子）+ judge 文 https://x.com/RLanceMartin/article/2064397389189071163 · X 长文 · 「推断·未实测」
- 核心：harness 要学「何时才花顶层智能」；fresh-context verifier 73% vs 自评 7–33%；grader 用低 effort。
- **写作风格拆解**：教师腔、小写、证据先行（"here's some of the lessons i learned"）。学它**「量化 + 反直觉但有据」**的立论。

### #3 @mitchellh freshness caveat / 怀疑帖 — **诚实的反声**
- https://x.com/mitchellh/status/2074862990214787301（"Sol is my default now… plans/judges just as good as Fable"）· https://x.com/mitchellh/status/2064773611647574429（"Fable… slow and expensive; 'loops are all you need' 是显而易见的"）
- 用途：给文章加「模型名会过期 / 别神化」的免疫层。

#### 补充值得关注
| 作者 | 链接 | 形式 | 一句定位 |
|------|------|------|---------|
| @milesdeutscher | https://x.com/milesdeutscher/status/2072934621583687837 | 帖 | 「用 Fable 5 不破产的 cheat code」——邻近(省钱)但非跨厂商 harness |
| CJ Zafir | （二手,未定位原帖） | — | Fable plan / Codex 5.5 execute / Fable review，周额度烧掉约减半 ⚠️二手 |

## 4. Web / 博客 — Top N（增长轴 · 渠道层）
（Web 有实测发布日期/作者，无互动数属正常）

### #1 The New Stack —「Model triage is the new AI skill」（$9 vs $1.50）
- https://thenewstack.io/claude-fable-cost-model-triage/ · 第三方新闻 · **写作风格：两个硬数字 + 一个命名技能（"model triage"）= 秒级可引用**。这是标题模板范本。

### #2 aider 官方 blog —「Separating code reasoning and editing」+「R1+Sonnet」
- https://aider.chat/2024/09/26/architect.html · https://aider.chat/2025/01/24/r1-sonnet.html · **一手** · benchmark 表 +「SOTA at 14× less cost」——**我们文章要借的正是这个修辞动作，且有两年 pedigree**。

### #3 第三方 worked-cost 解读（全部标第三方，仅作算账参照）
- dativo「Fable as the architect」https://blog.dativo.io/p/fable-5-as-the-architect-cheaper — 整任务 **$6.77**（planner $4.40 + 双 executor $2.37）；Fable 规划/评审、Opus 4.8 或 Codex 执行。
- digitalapplied「Planner Brain in Hermes/OpenClaw」https://www.digitalapplied.com/blog/fable-5-hermes-openclaw-planner-brain-setup-2026 — 单个 200K/50K 任务 **$4.50 Fable vs $2.25 Opus**，开 90% 输入 cache ≈ $2.70。
- MindStudio 多模型工作流 https://www.mindstudio.ai/blog/multi-model-ai-coding-workflow-planning-execution-review — 单模型 $1.51 → 多模型 **$0.23（-85%）**；「评审段 token 少，把 premium 模型放这里反而划算」= **frontier-as-judge 的算账背书**（⚠️不同模型集）。

## 5. YouTube — Top N（增长轴 · 渠道层）
> ⚠️ 观看/互动「推断·未实测」（本机无 summarize/last30days），WebSearch only
- **覆盖薄，如实报告**：无一条**精确讲「planner→便宜 coder→judge 跨厂商三段式 + $50→$X」**的视频。存在的都是邻近选题：
  - 「Make Fable 5 80% Cheaper (Usage Cheat Codes)」https://www.youtube.com/watch?v=p8ypBeNXQ8E · 「How To Make Fable 5 95% Cheaper」https://www.youtube.com/watch?v=1jPBkT-mgz0 —— Fable 省钱通用技，非跨厂商 harness。
  - 「Nobody Could Define 'Loop Engineering'… (Fable 5)」https://www.youtube.com/watch?v=ss09UQpGmck（Lance 派生）· 「Multi-Agent Architecture That Actually Ships — Factory」https://www.youtube.com/watch?v=ow1we5PzK-o（泛多模型编排）。
- **对我们的含义**：YouTube 是**空窗**——若做视频（blog2video 管线），几乎无正面竞争，先发者可定义「model triage 三段式」这一形式。

## 6. 核心洞察 + 最佳实践
> **溯源标注纪律**：每条标 `[内部/Tier-1: 页名]` 或 `[外部: URL]`；下游 writer 只许穿透引用原始出处，绝不引本报告。

**6 条跨渠道洞察**
1. **省钱的真杠杆是「按段分诊」，不是「换更便宜的模型」**：token 大头在执行段，顶层智能只在 plan+judge 稀疏使用 → 把 Fable 压到这两点、执行外包给便宜手 [外部: @mitchellh · thenewstack]。这把 vault 旧判断（intra-Anthropic 80–90% 留便宜档 [内部/Tier-1: claude-model-family]）升级成**跨厂商三段式**。
2. **让最贵的模型只做评审，反而是省钱的**：judge 段 token 少、可 `effort:low`，而 fresh-context 评审 73% vs 自评 7–33% [外部: Lance「Designing loops」] —— [内部/Tier-1: verification-loops][内部/Tier-1: self-evaluation-bias] 的量化实证；也是 [内部/Tier-1: cross-modal-review]「贵评审只用在贵产出上」的成本落地。
3. **这套是两年谱系的最新一格，不是 Fable 发明**：aider architect/editor 2024 就「SOTA at 14× less cost」[外部: aider]；Fable 的新意是把 planner/judge 那档抬到 $50/M out，使套利落差戏剧化 [内部/Tier-1: assumptions-expire] 的反向注解（能力涨→分工的经济价值涨）。
4. **模型名会过期，角色分工不会**：金句源本人已把默认 planner/judge 换成 Sol/GPT-5.6 [外部: @mitchellh 2074862990]。文章必须把「Fable/GPT-5.5」讲成**当期实例**、把「贵 planner + 便宜 coder + 贵 judge」讲成**耐用结构**。
5. **执行段用非-Anthropic coder 顺带规避 Fable 误拒**：Fable refusal 走 HTTP 200 且重部署后误拒升高 [外部: redeploying-fable-5]；三段式里执行不经 Fable 分类器，天然少踩雷；但 Fable 的两段仍要接 Opus 4.8 兜底 [内部/Tier-1: claude-model-family]。
6. **算账要连 tokenizer 和 cache 一起算**：Sonnet 5 新 tokenizer 每 token 多吐 1.0–1.35× [外部: finout]；long-lived planner 靠 prompt-cache 省钱 [内部/Tier-1: prompt-cache-optimization]。名义单价不等于到手账单。

**可执行最佳实践清单**
1. **先分诊，后选模**：把任务按段拆成 plan / execute / judge，问「这一段需要顶层智能吗」——只有 plan+judge 需要 [外部: @mitchellh]。
2. **planner = Fable xhigh**：吸收模糊、输出实施计划（HTML/Markdown），把最可能改的决策前置 [内部: best-practices-fable5 §6]。
3. **coder = 便宜订阅/低价 API 档**（GPT-5.5 / Codex 订阅 / Sonnet 5 / DeepSeek）：按计划批量写，占 80%+ token [外部: @mitchellh · morphllm]。
4. **judge = Fable(或同级) 低 effort、fresh context**：不要同上下文自评（7–33%），要独立窗口（73%）[外部: Lance]。
5. **两处 Fable 段都接 refusal → Opus 4.8 兜底**；执行段绕开 Fable 分类器 [外部: redeploying-fable-5]。
6. **把「$50→几美元」当假设去实测**：跑自己的 eval 对比（Lance 明确「measured performance vs cost on evals」），别照搬单条帖的数字 [外部: Lance 2075642836]。
7. **cache + tokenizer 纳入账**：planner 长驻靠 cache read；换 coder 时按新 tokenizer 重算 token 量 [内部: prompt-cache-optimization]。
8. **写死角色、留空模型名**：harness 配置用「PLANNER_MODEL / CODER_MODEL / JUDGE_MODEL」变量，方便下个季度换脑（Sol 已在门口）[外部: @mitchellh 2074862990]。

## 7. 【建议角度】—— Gate-1 强制契约（作者读完直接做选择题）
> 2–4 个角度，每个含六件：①标题候选 ②thesis ③为什么是我们/为什么现在 ④与「已表达角度清单」prior_coverage 关系 ⑤骨架 ⑥渠道建议。作者选定后经 `/research outline <slug> angle:N` 细化。
> **时机窗口**：Fable 发布满月、redeploy 尘埃落定、Hashimoto/Lance 的帖刚点燃「model triage」话语，但**中文纵深=零、YouTube=空窗**，且金句源已开始换模型 → **现在切、快切**，用「结构耐用 + 当期实例」的写法抢在被科普帖淹没前。

### 角度1（推荐）《Model triage：把 $50 的 Fable 单跑，拆成几美元的「贵脑+便宜手+贵评审」》
- **① 标题候选**：主《别买更强的模型，买更聪明的分工：Fable 三段式 harness 把 $50 往返压到几美元》/ 备《Model triage 入门：一张图看懂 plan-execute-judge 的成本套利》
- **② thesis**：省钱的杠杆不是「换便宜模型」，而是**按段分诊**——顶层智能只花在 plan+judge 两个稀疏点，执行段外包给便宜的手；这不是 Fable 发明的新招，而是 aider 两年前就验证过的结构，Fable 只是把落差拉大到戏剧性。
- **③ 为什么我们/为什么现在**：X 上有金句(Hashimoto)、有数据(Lance 73%、aider 14×、thenewstack $9/$1.50)但**四散且英文**；无人合成成「中文 builder 的落地图 + 诚实的谱系与半衰期」。发布满月、话语刚起、中文空窗。
- **④ prior_coverage 关系**：对 best-practices-fable5 §6#16「intra-Anthropic 80–90% 留便宜档」= **正交升级**（跨厂商三段式 + judge 经济学），非重合；对卡在 Gate-1 的迁移清单 draft = 不同角度（那篇讲「怎么用 Fable」，本篇讲「怎么少用 Fable 来省钱」）。明确推进。
- **⑤ 骨架**：1) 一句话价值 + 谁该读（独立 builder / 团队 lead 各一入口）；2) 反直觉主张：贵模型只做两件事；3) 三段式图 + 每段配什么模型/effort（Fable xhigh / GPT-5.5 订阅 / Fable low）；4) 算一笔账（$10/$50 vs $5/$30 vs cache，落到「几美元 vs $50」并标示例数据点）；5) 谱系：aider architect/editor 14× 的两年 pedigree；6) 半衰期免疫：模型名会过期（Sol 已在门口），写死角色留空模型名；7) 迁移 checklist。
- **⑥ 渠道**：中文博客长文（GEO：每条挂官方定价链接 +40%；带 $10/$50/$9/$1.50/73%/14× 具体数字 +37%）+ 可派生 blog2video 视频脚本（YouTube 空窗先发）。

### 角度2《为什么该让最贵的模型只做评审：fresh-context judge 的 73% 经济学》
- **① 标题候选**：《把 Fable 放去当裁判：73% 的抓错率，最低的 effort，最省的账》
- **② thesis**：直觉是「贵模型该干最难的活（写代码）」，但数据反过来——**judge 段 token 少、可低 effort、fresh context 抓错率 73%（自评仅 7–33%）**，把顶层智能放评审是投产比最高的一格。
- **③ 为什么我们/为什么现在**：Lance 的 73% 是最硬的一手数字，但埋在长文里没人给 builder 翻译成「所以你的 harness 该这么摆」；接 cross-modal-review 已有读者基础。
- **④ prior_coverage 关系**：是 [[verification-loops]]/[[self-evaluation-bias]]/[[cross-modal-review]] 的**量化续集**（旧页讲原理，本篇给 Fable 实测数字 + 成本论证）；vault 无成稿覆盖此数字。推进。
- **⑤ 骨架**：1) 反直觉钩子：最贵的模型别写代码；2) 73% vs 7–33% 数据 + 为什么 fresh context 关键；3) 为什么 judge 便宜（token 少 + eff:low + 判断<生成）；4) 落地：judge 段怎么配（独立窗口 / 打回阈值 / 与 cross-modal 三家评审的关系）；5) 边界：judge 也会误判、别无限循环。
- **⑥ 渠道**：中英双语技术短文 / X 长文（数据驱动、可被 AI 引用）。

### 角度3《模型名会过期，角色分工不会：从 aider architect/editor 到 Fable 三段式的两年谱系》
- **① 标题候选**：《别为「Fable + GPT-5.5」写代码：耐用的是结构，不是型号》
- **② thesis**：所有「用 X 当脑 + Y 当手」的帖都在教你**当期型号**，可金句源本人一个月就换了脑（Sol）；真正该学的是**跨模型角色分工这条两年谱系**——把它写成变量而非常量。
- **③ 为什么我们/为什么现在**：这是给前两个角度上的「保鲜层」，也是差异化——市面帖全在追型号，无人写「怎么让你的 harness 扛住下一次模型迭代」。呼应 [[assumptions-expire]] 我们已有的读者共识。
- **④ prior_coverage 关系**：延伸 [[assumptions-expire]]/[[thin-harness-fat-skills]] 到「成本-角色」维度；vault 无此谱系稿。首次覆盖谱系视角。
- **⑤ 骨架**：1) 反炒作钩子：帖子里的型号已经过期了；2) 谱系时间线（aider 2024 → Continue/Cline → Fable 2026）；3) 抽出不变量：plan/execute/judge 三角 + 价位分诊；4) 工程落地：PLANNER/CODER/JUDGE 变量化 + eval 常驻；5) 下一格预测（Sol/GPT-5.6）。
- **⑥ 渠道**：中文博客长文（观点/框架向）；X thread 派生。

### 关键人物值得跟踪
| 人物 | 角色 | 关注理由 |
|------|------|---------|
| Mitchell Hashimoto (@mitchellh) | Ghostty/HashiCorp 创始人 | 三段式金句源 + 诚实的模型漂移信号（Sol）；builder 圈高可信度 |
| Lance Martin (@rlancemartin) | LangChain | judge 经济学(73%) + evals 方法论；本话题的「导师声」 |
| aider (Paul Gauthier) | aider.chat | architect/editor 谱系基石 + 可引 benchmark |
| Miles Deutscher (@milesdeutscher) | 高触达 AI 科普 | Fable 省钱转译打法参考 |

### 内容形式参考库
- **长文学谁**：aider blog（benchmark 表 +「14× less cost」修辞）· Lance（量化+反直觉）。
- **X 学谁**：Hashimoto（claim→config→成本差一口气）· milesdeutscher（省钱钩子转译）。
- **视频学谁**：YouTube 空窗——无正面范本，先发定义「model triage 三段式」形式（blog2video 机会）。

## 附录：关键时间线
| 日期 | 事件 |
|------|------|
| 2024-09-26 | aider 发布 architect/editor 分离（先例基石；后续 R1+Sonnet「14× less cost」） |
| 2026-06-09 | Claude Fable 5 GA（$10/$50，vault 已核） |
| 2026-06-10 | Lance「Designing loops with Fable 5」（fresh-context verifier 73% vs 7–33%） |
| 2026-06-12 | Fable 下架（出口管制 + 越狱绕过） |
| ~2026-06 下旬 | Hashimoto「Fable 慢且贵」怀疑帖 |
| 2026-07-01 | Fable 完整重部署（误拒率升高为代价） |
| ~2026-07 初 | **Hashimoto 三段式「$50+→几美元」帖**（Fable plan / GPT-5.5 订阅 execute / Fable judge） |
| ~2026-07 | Lance「Cost effective harnesses with Fable」文 + evals 伴随帖（=种子 URL） |
| ~2026-07 | Hashimoto「Sol/GPT-5.6 已是我的默认 planner/judge」（模型漂移信号） |
| 2026-07-12 | 本调研（中文纵深/YouTube 仍空窗；金句源已开始换脑） |

---
**headless 消歧自决记录**：
1. 「Fable 5」=`claude-fable-5`（无歧义，vault 已核）。
2. 「GPT-5.5」当「便宜订阅 coder」类别、非硬约束；已同时记录 Codex/Sonnet 5/DeepSeek/Qwen 同位替代。
3. **署名订正（最重要）**：种子把三段式 + $50 数字归 Lance；核验后归 **Hashimoto(@mitchellh)**，Lance = judge 经济学(73%)。$50 数字为单一实践者、X 正文被墙(402)未一手核实 → 全程标 ⚠️「示例数据点/推断·未实测」，不当 benchmark。
4. 「$50+→几美元」= 单次复杂任务往返量级（非月费），Hashimoto 用词「full round trips」略含糊（每任务/每会话未明），已在 §1 标注。
5. plan checkpoint skipped（headless，无人应答）。
