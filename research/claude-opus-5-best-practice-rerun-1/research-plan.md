# Research Plan: Claude Opus 5 Best Practice — Rerun 1

> depth: deep
> as_of: 2026-07-29 (Asia/Singapore)
> reader: 会用 Claude Code / API、但不是资深系统工程师的 AI builder
> optimized skill: `.agents/skills/research/SKILL.md` at commit `0dc493a`
> baseline: `research/claude-opus-5-best-practice/`
> editorial benchmark: `/Users/yufanp/Downloads/opus5bestpractice.md`

## Decision to support

读者看完后应能决定：哪些任务先用 Opus 5，effort 如何校准，旧 prompts / Skills 哪些该删、
哪些必须保留，以及 Fast、cache、Batch 和 Auto mode 在什么边界内使用。

## Fixed comparison rubric

黄金案例、基线和 rerun 均按以下八项各 0–10 分：读者价值、可扫读性、可执行性、来源质量、
claim traceability、社区渠道丰富度、反证与风险边界、时效与技术契约准确性。

通过标准：总分不低于黄金案例；已知事实和归因错误全部修正；没有高严重度 ledger 缺口；
删除、自治、生产和高风险领域建议均有可逆试验、rollback 与人工 Gate。

## Preserve / correct / add

### Preserve

- 黄金案例的结论前置、规格/成本表、具体命令、角色化建议和资源索引。
- 基线的官方/实践者/反证分层、effort sweep、CodeRabbit 指标纠错和证据失效条件。

### Correct

- 日期星期、medium 默认、39.3% 指标、300k/fast 技术边界。
- “删除全部 Skills”“Auto mode 大部分时间不用确认”“长程全面优于 Fable”等过度建议。
- X “Top 高互动”无 comparable set、隐藏 affiliation、同一人多渠道重复计数。

### Add

- API、Claude Code、Batch、Fast 的 surface/version/prerequisite/limit/verify 契约。
- 每条建议的 when/action/evidence/boundary/verification。
- 来源 affiliation 与 evidence chain。
- 12 分钟迁移、两小时 eval、生产 canary 三个行动层级。
- “什么证据会改变建议”。

## Evidence lanes

1. Technical contract：官方 models、pricing、effort、prompting、cache、Batch、Fast、Claude Code release。
2. Capability and limits：发布公告与 System Card；厂商 benchmark 明示为 vendor-reported。
3. Community：X first-party oEmbed、YouTube 页面指标、practitioner 方法与相反体验。
4. Adversarial：CodeRabbit、Artificial Analysis、Ethan Mollick、Every；核查 source dependency。

## Access boundary

X 没有专用 connector，浏览器实例不可用；正文通过 X first-party oEmbed 观察，互动指标 unavailable。
YouTube 指标为 2026-07-29 16:42 +08:00 页面快照。社区发布仅五天，不生成全平台 Top-N。

