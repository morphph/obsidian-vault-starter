# 黄金案例 × 基线 × 优化版：质量验收

> benchmark: `/Users/yufanp/Downloads/opus5bestpractice.md`
> baseline: `research/claude-opus-5-best-practice/`
> optimized: `research/claude-opus-5-best-practice-rerun-1/`
> rubric fixed before rerun；每项 0–10；2026-07-29

## 结论

优化版达到并超过黄金案例的读者价值标准，同时把它从“强使用指南”升级为“可执行、可证伪、
可审计的研究报告”。黄金案例 **56.5/80**，基线 **67.0/80**，优化版 **73.0/80**。

## 同尺度评分

| 维度 | 黄金案例 | 基线 | 优化版 | 优化版证据 |
|---|---:|---:|---:|---|
| 读者价值 / 结论前置 | 8.5 | 8.5 | 9.5 | 三个默认动作 + 12 分钟入口 |
| 可扫读性 / 认知顺序 | 9.0 | 8.0 | 9.5 | 技术契约 → 路由 → effort → prompt → evidence → rollout |
| 具体可执行性 | 8.0 | 8.5 | 9.5 | decision contract、两小时 eval、生产 canary |
| 来源质量 / 角色多样性 | 6.5 | 8.5 | 9.0 | 官方、独立评测、实践者、反例分层 |
| Claim traceability | 4.5 | 9.0 | 9.5 | 12 个 claim 含 operational contract |
| 社区渠道丰富且不伪排名 | 7.5 | 8.0 | 8.5 | X oEmbed + YouTube exact snapshot + evidence-chain 去重 |
| 反证 / 不确定性 / 风险 | 4.0 | 8.5 | 9.0 | CodeRabbit、Ethan、失效条件、human Gate |
| 时效 / 技术契约准确性 | 8.5 | 8.0 | 8.5 | surface/version/beta/provider/price 前置 |
| **总分** | **56.5** | **67.0** | **73.0** | **91.3/100** |

评分是对本次固定 rubric 的编辑审计，不是外部统计结论。优化版未拿满的主要原因是发布只有五天、
X engagement 无法观察、Fast/Batch/plan entitlement 仍在变化，而不是用更多文字掩盖这些限制。

## Preserve：黄金案例哪些优点被保留

- 开头直接回答“怎么用”，而不是先堆研究过程。
- 规格、价格、模型路由、具体命令和场景表。
- X、YouTube、官方文档与独立实践的多渠道覆盖。
- 对 AI builder 的具体行动建议和资源索引。

## Correct：哪些关键错误被修正

| 黄金案例结论 | 问题 | 优化版处理 |
|---|---|---|
| 2026-07-24 周四发布 | 日期星期错误；实际周五 | 直接修正并进 ledger |
| 日常默认 medium | 官方默认与起始建议是 high | high control + workload sweep |
| CodeRabbit 39.3% 证明低 effort 够用 | 实为 xhigh；coverage/full-stream 更差 | 同时报告 precision、coverage、nitpicks |
| 删除旧 Skills / workflows 重建 | 单团队案例过度外推 | 每次删一类、固定任务 AB、可回滚 |
| 300k 最大输出 | 混淆同步和 Batch beta | 明示 Batches、beta header、provider/ZDR |
| Fast 2.5x / 必须开场 | 把 OTPS 写成整体速度；成本建议绝对化 | OTPS、research preview、2x 价、端到端验证 |
| X Top 高互动 | 无指标、时间、查询和 comparable set | 代表性原帖；engagement unavailable |
| Mike Krieger 作为独立技术领袖 | 遗漏 Anthropic CPO/Labs 身份 | 标成机构内部采用 |
| 长程任务全面优于 Fable | 遗漏 Ethan / Every 相反体验 | 把路由写成可证伪假设 |
| Auto mode 大部分时间无需确认 | classifier 不是业务安全保证 | canary、rollback、最小权限、human Gate |
| System Card 40 页 | 当前官方 landing 为 194 页 | 不用页数承载结论，记录版本限制 |

## Add：Research Skill 新增了什么

1. **Golden reference protocol：** 参考稿只做编辑 benchmark，不自动继承事实。
2. **Technical-contract lane：** 固定核验 surface、version、prerequisite、provider/plan/beta、as_of。
3. **Recommendation risk gate：** 删除、自治、生产、迁移、付费、高风险领域必须可逆试验与人审。
4. **Claim lint：** superlative、精确数字、引语、身份、版本、价格、命令必须进 ledger 或软化。
5. **Source dependency：** 记录 affiliation；同一人的 X/视频/文章只算一条 evidence chain。
6. **Decision contract：** 建议必须说明 when、action、evidence、boundary、verification。
7. **Invalidation：** 报告明确什么新证据会改变建议。

## 高严重度 Gate 验收

- [x] 没有把黄金案例当事实来源。
- [x] 已知日期、metric、identity、version、price、beta 错误均已纠正或加边界。
- [x] 没有未限定的 Top-N、best、only、always、never。
- [x] 删除与生产建议均有 AB/canary/rollback/human Gate。
- [x] 冗余自检提示与 executable quality controls 已明确分开。
- [x] X access/metric 限制和发布五天的 freshness 风险已公开。
- [x] 四个必需 research artifacts 齐全；comparison 为额外验收 artifact。

## 是否还需要第三轮

当前没有高严重度缺口，优化版总分高于黄金案例 16.5 分，因此不需要为了“多跑一轮”而制造
第三轮。后续只有在 X 指标可直接观察、官方契约发生变化或用户提供真实 workload eval 时，
才值得刷新，而不是继续改写同一批证据。
