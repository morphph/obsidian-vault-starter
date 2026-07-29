# Source Ledger: Claude Opus 5 Best Practice — Rerun 1

> as_of: 2026-07-29
> channels: Anthropic / Claude official docs, GitHub release, System Card, independent evaluation,
> practitioner articles, X first-party oEmbed, YouTube original pages
> access limits: X engagement unavailable；Every partly paywalled；YouTube comparison set limited
> to the 11 URLs in the provided reference

## Claim records

## C-001 — 发布与定位

- **Claim:** Opus 5 于 2026-07-24（周五）发布；官方称其接近 Fable 5 前沿智能、价格减半，
  并为 everyday use 设计。
- **Kind:** timeline | comparison
- **Status:** verified
- **Time sensitivity:** low
- **Primary source:** https://www.anthropic.com/news/claude-opus-5
- **Supporting sources:** none
- **Counter-evidence:** none found
- **Search boundary:** 官方定位，不改写为独立证明或全面超过 Fable。
- **Operational contract:** announcement only；不承载 API runtime contract
- **Used in report:** Executive Summary；§1
- **Notes:** 2026-07-24 是周五。

## C-002 — 模型、上下文与输出

- **Claim:** API ID `claude-opus-5`；1M context；同步输出 128k；300k 只适用于有 beta
  header 的 Message Batches。
- **Kind:** metric
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/about-claude/models/overview
- **Supporting sources:** https://platform.claude.com/docs/en/build-with-claude/batch-processing
- **Counter-evidence:** none found
- **Search boundary:** 分开核对同步与 Batch surface。
- **Operational contract:** Claude API；300k 需 Batches、`output-300k-2026-03-24`；
  provider、ZDR、结果保留限制需执行时复查
- **Used in report:** §1
- **Notes:** 不把 Batch beta 写成通用 max output。

## C-003 — Effort 默认与 thinking

- **Claim:** 五档 effort，默认 high；官方建议从 high control 开始；thinking disabled 只允许
  high 及以下。
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/effort
- **Supporting sources:** https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5
- **Counter-evidence:** https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium
- **Search boundary:** 核对全部档位、默认值、错误条件和非单调 benchmark。
- **Operational contract:** Claude API / Claude Code；xhigh/max + thinking disabled 返回 400；
  xhigh/max 应给较大 max_tokens
- **Used in report:** §1；§3
- **Notes:** “默认 medium”已拒绝；按 workload sweep。

## C-004 — Prompt 与自我验证

- **Claim:** 复杂任务 upfront 给完整规格；单独控制 verbosity/scope/delegation；删重复
  self-check prompt，但不删 tests 和 safety Gates。
- **Kind:** mechanism | synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Supporting sources:** https://www.anthropic.com/claude-opus-5-system-card
- **Counter-evidence:** https://www.coderabbit.ai/blog/opus-5-model-review
- **Search boundary:** 区分 prompt scaffolding 与 external verification。
- **Operational contract:** all surfaces；执行前冻结 acceptance；高风险动作保留 human Gate
- **Used in report:** 12 分钟清单；§4；§8
- **Notes:** 保留 tests/Gates 是基于官方建议与反证的安全 synthesis。

## C-005 — 旧 Skills 应逐项 AB

- **Claim:** 不应从 Every 单一案例推出批量删除；应一次清理一种冗余并对固定任务 AB。
- **Kind:** synthesis
- **Status:** probable
- **Time sensitivity:** medium
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Supporting sources:** https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- **Counter-evidence:** https://every.to/context-window/sometimes-you-have-to-delete-everything
- **Search boundary:** 同时检查官方“4.8 prompts 可工作”和 practitioner 冲突案例。
- **Operational contract:** reversible local experiment；保留旧配置；用 pass/token/retry 作为 Gate
- **Used in report:** 12 分钟清单；§4；§8
- **Notes:** 某些复杂历史 scaffold 可能确需大删，但必须由 eval 决定。

## C-006 — 标准、缓存、Batch 与 Fast 价格

- **Claim:** 标准 $5/$25；cache hit $0.50、5m write $6.25、1h write $10；
  Batch $2.50/$12.50；Fast $10/$50。
- **Kind:** metric
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/about-claude/pricing
- **Supporting sources:** https://platform.claude.com/docs/en/build-with-claude/fast-mode
- **Counter-evidence:** none found
- **Search boundary:** 使用当前官方价目，不用无 harness 的 per-task 估算。
- **Operational contract:** Claude API；Fast research preview/provider restrictions；Batch no Fast；
  cache write/read 分开计价
- **Used in report:** §1；§7
- **Notes:** 价格和可用性执行前重查。

## C-007 — Fast 的 2.5x 指标

- **Claim:** Fast 使用相同模型，最高 2.5x output tokens/sec，不保证 TTFT 或整任务 2.5x。
- **Kind:** metric | mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://platform.claude.com/docs/en/build-with-claude/fast-mode
- **Supporting sources:** https://code.claude.com/docs/en/fast-mode
- **Counter-evidence:** none found
- **Search boundary:** 核对指标名称、价格、access 与 cache。
- **Operational contract:** API research preview；Claude Code 受 usage credits/admin/account；
  同一会话中途切换会有 cache 成本
- **Used in report:** §1；§7
- **Notes:** “最好开场启用”是成本建议，不是语法禁令。

## C-008 — Claude Code 版本锚点

- **Claim:** `v2.1.219` 引入 Opus 5 并设为 default Opus model，不是所有账户 overall default。
- **Kind:** timeline | mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://github.com/anthropics/claude-code/releases/tag/v2.1.219
- **Supporting sources:** none
- **Counter-evidence:** none found
- **Search boundary:** 不从旧 model-config 页面推断当前 entitlement。
- **Operational contract:** Claude Code >= v2.1.219；以 `/model` 当前可见项验证账户可用性
- **Used in report:** 12 分钟清单
- **Notes:** release 还提供 subagent 深度控制相关变化。

## C-009 — CodeRabbit 指标

- **Claim:** 39.3% 是 xhigh actionable precision；coverage/full-stream precision 低于 baseline，
  nitpicks 92 对 23，不支持唯一 safety net。
- **Kind:** metric | comparison
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://www.coderabbit.ai/blog/opus-5-model-review
- **Supporting sources:** none
- **Counter-evidence:** source itself contains the trade-off
- **Search boundary:** 阅读全部相邻指标、方法和结论。
- **Operational contract:** CodeRabbit-specific harness；约 100 issue patterns、3 configs；
  不外推为所有 code review
- **Used in report:** §6
- **Notes:** production baseline 是 model mix；39.3% 不是 low effort。

## C-010 — System Card 的高风险边界

- **Claim:** Opus 5 agentic safety 总体改善但非免疫；官方还记录 factual-claim hallucination
  略高于 Opus 4.8，因此高风险任务仍需领域控制与人审。
- **Kind:** comparison | synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://www.anthropic.com/claude-opus-5-system-card
- **Supporting sources:** https://code.claude.com/docs/en/permission-modes
- **Counter-evidence:** none found
- **Search boundary:** 核对 safety 与 hallucination 两侧，不从 benchmark 推出部署安全。
- **Operational contract:** deployment governance；canary、rollback、least privilege、human Gate
- **Used in report:** 12 分钟清单；§8
- **Notes:** 当前 landing 指向 194 页 PDF；黄金案例称 40 页错误。

## C-011 — 社区长任务反例

- **Claim:** 首周实践既有“daily driver”，也有旧 scaffold 冲突和长任务不完整反例。
- **Kind:** synthesis
- **Status:** probable
- **Time sensitivity:** high
- **Primary source:** https://x.com/emollick/status/2080709278441033746
- **Supporting sources:** https://x.com/danshipper/status/2080700057892815114
- **Counter-evidence:** https://x.com/mikeyk/status/2080702940445397167
- **Search boundary:** 代表性原帖，不使用 Top-N；来源角色和 affiliation 分开。
- **Operational contract:** practitioner hypotheses only；需本地 workload eval
- **Used in report:** §2；§5
- **Notes:** Mike Krieger 属 Anthropic 内部采用；Dan 的多渠道是一条 evidence chain。

## C-012 — YouTube 传播与 per-task 成本

- **Claim:** 固定 11 视频中 AI Search 观看最高；Pat 的方法更可复核；其五个任务中 Opus 5
  比 Fable 总成本约低 28%，不是固定 50%。
- **Kind:** metric | synthesis
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://www.youtube.com/watch?v=RCsBJz4W4bA
- **Supporting sources:** https://www.aiformortals.co/blog/opus-5-vs-opus-4-8-vs-fable-5
- **Counter-evidence:** none; workload variance is documented
- **Search boundary:** 只在黄金案例固定 11 URLs 内比较；指标观察于 2026-07-29。
- **Operational contract:** specific five-build harness；不可推广为通用 per-task discount
- **Used in report:** §5
- **Notes:** “研究可复核性更强”是定性判断，不是观看量排名。

## Source records

## S-001 — Anthropic launch

- **URL:** https://www.anthropic.com/news/claude-opus-5
- **Author / publisher:** Anthropic
- **Published / updated:** 2026-07-24
- **Role:** official
- **Source class:** first-party
- **Affiliation / dependency:** model vendor
- **Evidence chain:** launch X posts and customer quotes derive from this release
- **Claims supported:** C-001
- **Limitations:** vendor-reported benchmarks and positioning.

## S-002 — Models / pricing / product docs

- **URL:** https://platform.claude.com/docs/en/about-claude/models/overview
- **Author / publisher:** Anthropic
- **Published / updated:** live；accessed 2026-07-29
- **Role:** official
- **Source class:** first-party
- **Affiliation / dependency:** model vendor
- **Evidence chain:** pricing, what's-new, Batch, Fast and cache pages form one official docs family
- **Claims supported:** C-002, C-003, C-006, C-007
- **Limitations:** fast-moving runtime contract.

## S-003 — Opus 5 prompting guide

- **URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Author / publisher:** Anthropic
- **Published / updated:** live；accessed 2026-07-29
- **Role:** official | explainer
- **Source class:** first-party
- **Affiliation / dependency:** model vendor
- **Evidence chain:** official context-engineering article is complementary, not independent
- **Claims supported:** C-004, C-005
- **Limitations:** general advice still needs workload eval.

## S-004 — Claude Code v2.1.219

- **URL:** https://github.com/anthropics/claude-code/releases/tag/v2.1.219
- **Author / publisher:** Anthropic / Claude Code
- **Published / updated:** 2026-07-24
- **Role:** official
- **Source class:** first-party
- **Affiliation / dependency:** product vendor
- **Evidence chain:** changelog and code docs describe same product
- **Claims supported:** C-008
- **Limitations:** does not prove account entitlement.

## S-005 — Opus 5 System Card

- **URL:** https://www.anthropic.com/claude-opus-5-system-card
- **Author / publisher:** Anthropic
- **Published / updated:** 2026-07-24
- **Role:** official
- **Source class:** first-party
- **Affiliation / dependency:** model vendor and evaluator
- **Evidence chain:** launch safety summary derives from system card
- **Claims supported:** C-004, C-010
- **Limitations:** vendor evaluation; document may update.

## S-006 — CodeRabbit model review

- **URL:** https://www.coderabbit.ai/blog/opus-5-model-review
- **Author / publisher:** CodeRabbit
- **Published / updated:** 2026-07-24
- **Role:** practitioner | critic
- **Source class:** independent analysis
- **Affiliation / dependency:** commercial code-review vendor
- **Evidence chain:** article is the primary test; later summaries are repetitions
- **Claims supported:** C-004, C-009
- **Limitations:** proprietary harness; production baseline is model mix.

## S-007 — Every / Dan Shipper

- **URL:** https://every.to/context-window/sometimes-you-have-to-delete-everything
- **Author / publisher:** Every
- **Published / updated:** 2026-07-26；updated 2026-07-29
- **Role:** practitioner | critic
- **Source class:** independent analysis
- **Affiliation / dependency:** AI media/product company; early model access
- **Evidence chain:** Dan X + Every Vibe Check + Every YouTube are one underlying test
- **Claims supported:** C-005, C-011
- **Limitations:** partly paywalled; one team's complex historical setup.

## S-008 — Claire Vo / ChatPRD

- **URL:** https://www.chatprd.ai/how-i-ai/my-surprising-verdict-on-claude-opus-5
- **Author / publisher:** Claire Vo / ChatPRD
- **Published / updated:** 2026-07-25
- **Role:** practitioner
- **Source class:** independent analysis
- **Affiliation / dependency:** AI product founder; early evaluator
- **Evidence chain:** X + How I AI video + article are one personal blind test
- **Claims supported:** C-011
- **Limitations:** six task types; 70% personal taste weighting.

## S-009 — Ethan Mollick X posts

- **URL:** https://x.com/emollick/status/2080709278441033746
- **Author / publisher:** Ethan Mollick
- **Published / updated:** 2026-07-24
- **Role:** practitioner | critic
- **Source class:** community
- **Affiliation / dependency:** none found material to this claim
- **Evidence chain:** two same-day posts are one evaluator's experience
- **Claims supported:** C-011
- **Limitations:** personal tasks; X oEmbed has no engagement metrics.

## S-010 — Pat Simmons independent builds

- **URL:** https://www.aiformortals.co/blog/opus-5-vs-opus-4-8-vs-fable-5
- **Author / publisher:** Pat Simmons / AI for Mortals
- **Published / updated:** 2026-07-25
- **Role:** practitioner
- **Source class:** independent analysis
- **Affiliation / dependency:** AI education/content creator
- **Evidence chain:** YouTube and companion article are one five-build test
- **Claims supported:** C-012
- **Limitations:** five tasks; model/task variance; no universal cost ratio.

## Content signals

## M-001 — Dan Shipper X

- **URL:** https://x.com/danshipper/status/2080700057892815114
- **Channel / surface:** X / first-party oEmbed
- **Observed at:** 2026-07-29 16:47 +08:00
- **Text / metrics:** partial / engagement unavailable
- **Signal status / precision:** observed / none
- **Comparable set:** none；representative, not ranked
- **Dependency:** Every article/video same evidence chain

## M-002 — Ethan Mollick X

- **URL:** https://x.com/emollick/status/2080709278441033746
- **Channel / surface:** X / first-party oEmbed
- **Observed at:** 2026-07-29 16:47 +08:00
- **Text / metrics:** complete / engagement unavailable
- **Signal status / precision:** observed / none
- **Comparable set:** none；counterexample, not ranked
- **Dependency:** same evaluator's launch-day tests

## M-003 — AI Search YouTube

- **URL:** https://www.youtube.com/watch?v=RCsBJz4W4bA
- **Channel / surface:** YouTube / original page metadata
- **Observed at:** 2026-07-29 16:42 +08:00
- **Text / metrics:** partial / 398,935 views, 10,197 likes, 958 comments
- **Signal status / precision:** observed / exact-ui
- **Comparable set:** highest views only within the reference's fixed 11 videos
- **Dependency:** content quality not inferred from engagement

## M-004 — Pat Simmons YouTube

- **URL:** https://www.youtube.com/watch?v=z_7J_iKuSzU
- **Channel / surface:** YouTube / original page + companion article
- **Observed at:** 2026-07-29 16:42 +08:00
- **Text / metrics:** partial / 65,924 views, 2,231 likes, 232 comments
- **Signal status / precision:** observed / exact-ui
- **Comparable set:** fixed 11 videos；not ranked by evidence quality
- **Dependency:** article/video one test

## Contradictions and resolution

- **Effort:** one FrontierCode result favors medium; official guidance and other evals do not support
  a universal medium default. Resolution: high control + workload sweep.
- **Old prompts:** official guide says 4.8 prompts generally work; Every reports strong conflict.
  Resolution: reversible per-scaffold AB, not wholesale deletion or forced preservation.
- **Long tasks:** institutional users report daily-driver success; independent practitioners report
  early stopping/incompleteness. Resolution: treat long-task routing as a falsifiable hypothesis.
- **Code review:** actionable precision rises while coverage and full-stream precision fall.
  Resolution: measure all three and keep an independent safety net.

## Open questions

- 首周行为会如何随 Claude Code point releases、prompts 和 access rollout 稳定？
- 不同真实 workload 的 effort frontier 与 tokenizer 实耗是什么？
- Fast、300k Batch、provider、ZDR、plan entitlement 和价格何时变化？
- Auto mode 在不同权限模型下的误批、漏拦截和人工中断成本缺少公开可泛化数据。

