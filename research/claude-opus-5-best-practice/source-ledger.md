# Source Ledger: Claude Opus 5 Best Practice

> as_of: 2026-07-29
> channels searched: Anthropic / Claude official web, GitHub release, System Card,
> practitioner blogs, independent benchmark reports, X original posts
> primary search languages: English; Chinese used for comparison framing
> important access limits: Every 部分付费；X 未使用统一 API 样本，不能声称全平台 Top-N；
> YouTube 页面受限，未用视频摘要承载关键事实

## Claim records

## C-001 — 发布日期与官方定位

- **Claim:** Claude Opus 5 于 2026-07-24（周五）发布；Anthropic 称其接近 Fable 5
  的前沿智能、价格减半，并设计为 everyday use。
- **Kind:** timeline | comparison
- **Status:** verified
- **Time sensitivity:** low
- **Primary source:** https://www.anthropic.com/news/claude-opus-5
- **Supporting sources:** https://github.com/anthropics/claude-code/releases/tag/v2.1.219
- **Counter-evidence:** none found
- **Search boundary:** 查官方公告日期并用日历核对星期；没有把官方比较改写成独立测评结论。
- **Used in report:** Executive Summary；§1
- **Notes:** “comes close”不能写成全面超过 Fable 5；2026-07-24 是周五，不是黄金案例的周四。

## C-002 — 上下文、同步输出与 Batch 输出

- **Claim:** Opus 5 为 1M context、同步 Messages 最大输出 128k；300k 仅适用于带
  `output-300k-2026-03-24` beta 的 Message Batches API，并有平台限制。
- **Kind:** metric
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/about-claude/models/overview
- **Supporting sources:** https://platform.claude.com/docs/en/build-with-claude/batch-processing
- **Counter-evidence:** none found
- **Search boundary:** 分别核对 models overview 与 Batch 文档；没有把 beta Batch 上限写成同步默认。
- **Used in report:** §1；§5
- **Notes:** Batch 不支持 Fast；不符合 ZDR，结果通常保留 29 天；平台可用性应在部署前重查。

## C-003 — 标准价、缓存价、Batch 与 Fast

- **Claim:** 标准价 $5/$25；cache hit $0.50、5m write $6.25、1h write $10；
  Batch $2.50/$12.50；Fast $10/$50。
- **Kind:** metric
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/about-claude/pricing
- **Supporting sources:** https://platform.claude.com/docs/en/build-with-claude/fast-mode
- **Counter-evidence:** none found
- **Search boundary:** 只使用当前官方价目；没有使用未给 harness 的 per-task 成本数字。
- **Used in report:** §1；§5
- **Notes:** cache hit 的 90% 输入折扣不能描述成所有缓存请求的 90%；新 tokenizer 可能改变实耗。

## C-004 — Effort 五档与默认 high

- **Claim:** Opus 5 有 low、medium、high、xhigh、max 五档；API 与 Claude Code 默认 high，
  官方建议从 high 开始并按自己的 eval 调整。
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/effort
- **Supporting sources:** https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5
- **Counter-evidence:** https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium
- **Search boundary:** 检查官方默认值、全部档位、FrontierCode 非单调案例与第三方 effort 对比。
- **Used in report:** Executive Summary；§2；§4
- **Notes:** 单项 benchmark 在 medium 达峰不支持“全局默认 medium”；Max 与 Medium 也有质量/速度取舍。

## C-005 — Thinking 默认开启与关闭限制

- **Claim:** Thinking 默认 adaptive/on；关闭只允许 high 及以下，xhigh/max 会返回 400；
  `max_tokens` 同时容纳 thinking 与可见输出。
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5
- **Supporting sources:** https://platform.claude.com/docs/en/build-with-claude/effort
- **Counter-evidence:** none found
- **Search boundary:** 核对迁移与错误条件，不从旧模型 thinking 行为类推。
- **Used in report:** §1；§2
- **Notes:** 官方还记录 thinking-disabled 偶发 tool call 文本化/XML 伪影；低 effort 通常优于关闭。

## C-006 — Prompt、scope、verbosity 与 delegation

- **Claim:** 对复杂 coding 应 upfront 给完整 task spec；窄任务显式限 scope；输出长度单独指定；
  subagent 只用于真正独立的大 lane 并设 deterministic cap。
- **Kind:** mechanism | synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Supporting sources:** https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- **Counter-evidence:** none found
- **Search boundary:** 区分官方直接建议与本报告整理的 task-contract 模板。
- **Used in report:** 先改这 7 件事；§3
- **Notes:** 表格与模板是 researcher synthesis，来源没有逐字给出同一格式。

## C-007 — 删除重复验证不等于删除质量 Gate

- **Claim:** 应移除 legacy 的重复 self-verification 提示，但保留 tests、静态检查、生产 Gate
  和高风险人审。
- **Kind:** synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Supporting sources:** https://www.anthropic.com/claude-opus-5-system-card
- **Counter-evidence:** https://www.coderabbit.ai/blog/opus-5-model-review
- **Search boundary:** 搜索“verification”官方措辞，并用 System Card 与独立 code-review 失败数据检查边界。
- **Used in report:** §3.2；§7
- **Notes:** “保留外部质量 Gate”是由官方 self-verification 建议和反证共同推出的安全性 synthesis。

## C-008 — 不应整套删除旧 prompts / skills

- **Claim:** Opus 5 对现有 Opus 4.8 prompts 通常可直接工作；旧配置应逐项审计和 AB，
  而非根据单一团队经验全部删除。
- **Kind:** comparison | synthesis
- **Status:** probable
- **Time sensitivity:** medium
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Supporting sources:** https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- **Counter-evidence:** https://every.to/context-window/sometimes-you-have-to-delete-everything
- **Search boundary:** 同时检查官方兼容性说法和 Every 的失败案例；未将任一侧泛化为所有系统。
- **Used in report:** §3.3
- **Notes:** 结论是迁移策略，不是保证；某些历史 scaffold 的确可能需要大幅清理。

## C-009 — Claude Code v2.1.219 行为

- **Claim:** v2.1.219 加入 Opus 5，并设为 default Opus model；这不等于所有账户的 overall
  default；该版还有 Fast 和 nested subagent 相关变化。
- **Kind:** timeline | mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://github.com/anthropics/claude-code/releases/tag/v2.1.219
- **Supporting sources:** https://code.claude.com/docs/en/fast-mode
- **Counter-evidence:** none found
- **Search boundary:** 使用具体 release tag，不从过期的 model-config 摘要推断当前账户可用性。
- **Used in report:** §4
- **Notes:** `/model` 的实际选项仍受账户、计划与 rollout 影响。

## C-010 — Fast 是最多 2.5x OTPS，不是整体时延

- **Claim:** Fast 使用相同模型、最高提升 2.5x output tokens/sec；它是 research preview，
  $10/$50，API 有 provider 限制，且不是 time-to-first-token 保证。
- **Kind:** metric | mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/fast-mode
- **Supporting sources:** https://code.claude.com/docs/en/fast-mode
- **Counter-evidence:** none found
- **Search boundary:** 核对指标定义、价格、beta、平台和 cache 行为。
- **Used in report:** §4；§5
- **Notes:** Claude Code 最好开场启用是成本建议，不是“中途禁止切换”。

## C-011 — CodeRabbit 39.3% 的正确解释

- **Claim:** 39.3% 是 Opus 5 xhigh 的 actionable-comment precision；同一评测中 known-issue
  coverage、full-stream precision 低于 baseline，nitpicks 明显更多，因此不适合唯一 safety net。
- **Kind:** metric | comparison
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://www.coderabbit.ai/blog/opus-5-model-review
- **Supporting sources:** none
- **Counter-evidence:** none; source itself contains the trade-off
- **Search boundary:** 读取完整方法和所有相邻指标，没有从摘要或单个最高数字推结论。
- **Used in report:** §6
- **Notes:** baseline 是 CodeRabbit production model mix，不是“所有模型历史最高”的统一基准。

## C-012 — 高风险任务仍需外部控制

- **Claim:** Opus 5 更强的 agentic safety 不等于免疫；医疗、法律、金融和不可逆生产动作仍需
  领域评测、权限边界、可追溯证据与人工 Gate。
- **Kind:** synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://www.anthropic.com/claude-opus-5-system-card
- **Supporting sources:** https://code.claude.com/docs/en/permission-modes
- **Counter-evidence:** none found
- **Search boundary:** 检查 System Card 的 hallucination 与 prompt injection 边界；没有从能力
  benchmark 推出部署安全。
- **Used in report:** 先改这 7 件事；§3.2；§7
- **Notes:** System Card 报告总体更准确，但 factual claims hallucinate slightly more than Opus 4.8。

## C-013 — 社区首周体验互相矛盾

- **Claim:** 早期 practitioner 同时报告作品质量领先、协作体验烦躁、旧 scaffold 冲突等现象；
  这些案例提示要自测，但不能建立全局默认。
- **Kind:** synthesis
- **Status:** probable
- **Time sensitivity:** high
- **Primary source:** https://www.chatprd.ai/how-i-ai/my-surprising-verdict-on-claude-opus-5
- **Supporting sources:** https://every.to/vibe-check/opus-5
- **Counter-evidence:** https://every.to/context-window/sometimes-you-have-to-delete-everything
- **Search boundary:** 仅称“代表性/高信号”，不声称 X 或社区 Top-N。
- **Used in report:** §6
- **Notes:** 发布仅五天；版本、prompt、skill 和产品表面不同，不能直接合并为模型固有属性。

## Source records

## S-001 — Introducing Claude Opus 5

- **URL:** https://www.anthropic.com/news/claude-opus-5
- **Author / publisher:** Anthropic
- **Published / updated:** 2026-07-24
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-001
- **Limitations:** 发布方材料；benchmark 与客户引语不是独立验证。

## S-002 — Claude models overview

- **URL:** https://platform.claude.com/docs/en/about-claude/models/overview
- **Author / publisher:** Anthropic
- **Published / updated:** live docs；accessed 2026-07-29
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-002, C-003
- **Limitations:** 价格、模型列表和平台支持会变化。

## S-003 — Prompting Claude Opus 5

- **URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Author / publisher:** Anthropic
- **Published / updated:** live docs；accessed 2026-07-29
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-006, C-007, C-008
- **Limitations:** 官方通用建议；仍需用户 workload eval。

## S-004 — Effort

- **URL:** https://platform.claude.com/docs/en/build-with-claude/effort
- **Author / publisher:** Anthropic
- **Published / updated:** live docs；accessed 2026-07-29
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-004, C-005
- **Limitations:** 默认值和支持表面可能变化。

## S-005 — What’s new in Claude Opus 5

- **URL:** https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5
- **Author / publisher:** Anthropic
- **Published / updated:** live docs；accessed 2026-07-29
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-002, C-004, C-005
- **Limitations:** 产品迁移文档，不是独立能力评测。

## S-006 — The new rules of context engineering

- **URL:** https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- **Author / publisher:** Thariq Shihipar / Anthropic
- **Published / updated:** 2026-07-24
- **Role:** official | explainer
- **Source class:** first-party
- **Claims supported:** C-006, C-008
- **Limitations:** “删除 80%”来自 Anthropic 内部 Claude Code eval，不代表所有外部仓库。

## S-007 — Claude Opus 5 System Card

- **URL:** https://www.anthropic.com/claude-opus-5-system-card
- **Author / publisher:** Anthropic
- **Published / updated:** 2026-07-24
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-007, C-012
- **Limitations:** 当前 landing 指向 194 页 PDF；官方自评，且版本可能继续更新。

## S-008 — Claude Code v2.1.219

- **URL:** https://github.com/anthropics/claude-code/releases/tag/v2.1.219
- **Author / publisher:** Anthropic / Claude Code
- **Published / updated:** 2026-07-24
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-009
- **Limitations:** 版本锚点不能保证每个账户的 rollout 和 plan entitlement。

## S-009 — Opus 5 model review

- **URL:** https://www.coderabbit.ai/blog/opus-5-model-review
- **Author / publisher:** CodeRabbit
- **Published / updated:** 2026-07-24
- **Role:** practitioner | critic
- **Source class:** independent analysis
- **Claims supported:** C-007, C-011
- **Limitations:** CodeRabbit 有代码审查产品利益；约 100 个 issue patterns、特定 harness；
  production baseline 是 model mix。

## S-010 — My surprising verdict on Claude Opus 5

- **URL:** https://www.chatprd.ai/how-i-ai/my-surprising-verdict-on-claude-opus-5
- **Author / publisher:** Claire Vo / ChatPRD
- **Published / updated:** 2026-07-25
- **Role:** practitioner
- **Source class:** independent analysis
- **Claims supported:** C-013
- **Limitations:** 个人小样本盲测；作者经营 AI 产品，主观标准权重较高。

## S-011 — Sometimes You Have to Delete Everything

- **URL:** https://every.to/context-window/sometimes-you-have-to-delete-everything
- **Author / publisher:** Every
- **Published / updated:** 2026-07-26；updated 2026-07-29
- **Role:** practitioner | critic
- **Source class:** independent analysis
- **Claims supported:** C-008, C-013
- **Limitations:** 部分付费；单一团队的历史 scaffold，标题不应被当成通用迁移指令。

## S-012 — Artificial Analysis: Opus 5 Max vs Medium

- **URL:** https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium
- **Author / publisher:** Artificial Analysis
- **Published / updated:** accessed 2026-07-29
- **Role:** critic | explainer
- **Source class:** independent analysis
- **Claims supported:** C-004
- **Limitations:** 聚合 benchmark 不能代替用户任务集；配置与站点方法可能更新。

## S-013 — Claude Code permission modes

- **URL:** https://code.claude.com/docs/en/permission-modes
- **Author / publisher:** Anthropic
- **Published / updated:** live docs；accessed 2026-07-29
- **Role:** official
- **Source class:** first-party
- **Claims supported:** C-012
- **Limitations:** 产品安全控制会变化；classifier/permission mode 不是业务风险证明。

## Content signals

观察边界：X 无专用 connector，当前无可用浏览器实例；使用 X 官方
`publish.x.com/oembed` 读取正文、作者和发布日期。观察时间 2026-07-29 16:47 +08:00。
oEmbed 不返回互动指标，长帖可能截断。报告因此没有使用 “Top X posts” 或按互动排名。

## M-001 — Thariq Shihipar：删减 Claude Code system prompt

- **URL:** https://x.com/trq212/status/2080710971228918066
- **Channel:** X
- **Surface:** first-party oEmbed API
- **Query / sort:** direct URL
- **Author / handle:** Thariq Shihipar / @trq212；Anthropic 工程师
- **Published at:** 2026-07-24
- **Observed at:** 2026-07-29 16:47 +08:00
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** unavailable
- **Likes / reactions:** unavailable
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** none
- **Proxy basis:** omitted
- **Comparable set:** none；未排名

## M-002 — Dan Shipper：旧 skills/plugins 的冲突

- **URL:** https://x.com/danshipper/status/2080700057892815114
- **Channel:** X
- **Surface:** first-party oEmbed API
- **Query / sort:** direct URL
- **Author / handle:** Dan Shipper / @danshipper；Every
- **Published at:** 2026-07-24
- **Observed at:** 2026-07-29 16:47 +08:00
- **Post type:** post
- **Text access:** partial
- **Views / impressions:** unavailable
- **Likes / reactions:** unavailable
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** none
- **Proxy basis:** omitted
- **Comparable set:** none；与 Every 文章/视频同一来源链

## M-003 — Claire Vo：产出与互动体验分裂

- **URL:** https://x.com/clairevo/status/2080703735878336983
- **Channel:** X
- **Surface:** first-party oEmbed API
- **Query / sort:** direct URL
- **Author / handle:** Claire Vo / @clairevo；ChatPRD / How I AI
- **Published at:** 2026-07-24
- **Observed at:** 2026-07-29 16:47 +08:00
- **Post type:** post
- **Text access:** partial
- **Views / impressions:** unavailable
- **Likes / reactions:** unavailable
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** none
- **Proxy basis:** omitted
- **Comparable set:** none；与 ChatPRD / How I AI 同一来源链

## M-004 — Ethan Mollick：长任务反例

- **URL:** https://x.com/emollick/status/2080709278441033746
- **Channel:** X
- **Surface:** first-party oEmbed API
- **Query / sort:** direct URL
- **Author / handle:** Ethan Mollick / @emollick；独立实践者
- **Published at:** 2026-07-24
- **Observed at:** 2026-07-29 16:47 +08:00
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** unavailable
- **Likes / reactions:** unavailable
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** none
- **Proxy basis:** omitted
- **Comparable set:** none；未排名

## M-005 — Mike Krieger：机构内部采用

- **URL:** https://x.com/mikeyk/status/2080702940445397167
- **Channel:** X
- **Surface:** first-party oEmbed API
- **Query / sort:** direct URL
- **Author / handle:** Mike Krieger / @mikeyk；Anthropic Labs，前 CPO
- **Published at:** 2026-07-24
- **Observed at:** 2026-07-29 16:47 +08:00
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** unavailable
- **Likes / reactions:** unavailable
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** none
- **Proxy basis:** omitted
- **Comparable set:** none；机构内部采用，不作为独立证明

## M-006 — 黄金清单中的 YouTube 视频

- **URL:** https://www.youtube.com/watch?v=RCsBJz4W4bA
- **Channel:** YouTube
- **Surface:** original page metadata
- **Query / sort:** 用户黄金清单内的固定 11 个视频；非全平台搜索样本
- **Author / handle:** AI Search
- **Published at:** 2026-07-27
- **Observed at:** 2026-07-29 16:42 +08:00
- **Post type:** video
- **Text access:** partial
- **Views / impressions:** 398,935
- **Likes / reactions:** 10,197
- **Comments / replies:** 958
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** exact-ui
- **Proxy basis:** omitted
- **Comparable set:** 仅黄金案例列出的 11 个视频；此集合内观看量最高，不代表全平台 Top

## M-007 — Pat Simmons：可复核独立构建对比

- **URL:** https://www.youtube.com/watch?v=z_7J_iKuSzU
- **Channel:** YouTube
- **Surface:** original page metadata + public companion article
- **Query / sort:** 用户黄金清单内的固定 11 个视频；非全平台搜索样本
- **Author / handle:** Pat Simmons
- **Published at:** 2026-07-25
- **Observed at:** 2026-07-29 16:42 +08:00
- **Post type:** video
- **Text access:** partial
- **Views / impressions:** 65,924
- **Likes / reactions:** 2,231
- **Comments / replies:** 232
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** exact-ui
- **Proxy basis:** companion article exposes prompts, outputs, token, cost, and time
- **Comparable set:** 黄金案例的 11 个视频；研究可复核性为定性判断，未做数值排名

## Contradictions

### D-001 — Effort 变化是否使缓存失效

- Anthropic 当前 Effort / Prompt Caching 文档称改变 effort 会使 cached prefix 失效。
- CodeRabbit 文章称可在不中断缓存的情况下中途改变 effort。
- **Resolution:** 对 API 技术契约以截至 2026-07-29 的官方文档为准；将第三方说法记为过时或
  harness-specific，不据其优化生产缓存。

### D-002 — 旧 prompts 是否应该重建

- 官方 Prompting Guide 称现有 Opus 4.8 prompts 通常可直接使用。
- Every 报告其旧 skills/plugins 与 Opus 5 明显冲突，进行了大幅拆除。
- **Resolution:** 两者可以同时成立；采用逐项审计、AB test 和可逆回滚，不做全局删除规则。

### D-003 — Code review 更精确还是更差

- CodeRabbit 的 actionable-comment precision 在 xhigh 高于其 production baseline。
- 同一评测的 issue coverage 和 full-stream precision 更低，nitpicks 更多。
- **Resolution:** 明确指标分母与目标；把 Opus 5 当 second reviewer 候选，而非唯一 safety net。

## Open questions

- 发布五天后的 practitioner 体验是否会随 Claude Code 小版本和官方 prompt 更新稳定下来？
- 不同任务族的 low→max effort 曲线是什么；公开 benchmark 无法替代个人 workload。
- Fast、300k Batch、provider 支持、计划权限和 Sonnet introductory pricing 何时变化？
- Claude Code Auto mode 在不同仓库权限模型下的误批率与人工中断成本尚无公开、可泛化数据。
- X 原帖的互动量是时间快照，不是证据质量；没有同一查询样本就不能生成平台 Top-N。
