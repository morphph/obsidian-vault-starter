# Research Plan: Claude Opus 5 Best Practice

> depth: deep
> as_of: 2026-07-29 (Asia/Singapore)
> reader: 会用 Claude Code / API、但不是资深系统工程师的 AI builder
> baseline skill: `.agents/skills/research/SKILL.md` at commit `666d1b7`

## Research objective

回答一个实用问题：Claude Opus 5 相比 Opus 4.8、Sonnet 5 和 Fable 5 到底改变了什么，
使用者应如何调整模型选择、effort、提示词、CLAUDE.md、工具、subagent、验证和成本策略。

用户提供的 `/Users/yufanp/Downloads/opus5bestpractice.md` 只作为可读性与覆盖面的黄金案例，
不作为事实来源。所有进入报告的关键事实必须回到官方、一手或可说明限制的社区原始材料。

## Question map

1. Opus 5 的正式定位、发布日期、模型 ID、价格、上下文、最大输出和可用平台是什么？
2. 它与 Fable 5、Sonnet 5 的边界是什么；“日常主力”在什么条件下成立？
3. effort 的五档分别控制什么；官方为什么建议从 `high` 开始并以自己的 eval 调整？
4. thinking 默认开启、关闭限制、`max_tokens` 与 thinking-disabled 输出伪影意味着什么？
5. Opus 5 的长程执行、自我验证、代码审查、视觉与 office 能力应如何转成工作流设计？
6. 旧的 verification、verbosity、scope、subagent 和 CLAUDE.md 规则会怎样妨碍它？
7. prompt caching、Batch API、Fast mode 各自优化什么，价格和可用性边界是什么？
8. Claude Code 的版本、`/model`、`/effort`、`/fast` 与订阅/usage credits 有哪些实际限制？
9. 社区首周实践在哪些地方支持官方建议，在哪些地方互相矛盾？
10. 哪些 benchmark、人物身份、Top-N、成本数字和“必须做”建议不能据现有证据下结论？

## Ambiguities to resolve

- “best practice”可指 API prompting、Claude Code 配置、模型路由或个人工作方式；报告将分层处理，
  但不把某一表面的设置强行推广到所有表面。
- “Opus 5 比 Fable 5 更好”可能指特定 benchmark、成本效率或主观体验，不代表总体能力。
- 社区发布仅约五天，首日体验可能受旧 prompts、skills、产品表面和 effort 设置影响。
- X 的“Top”若没有同一查询、观察窗口和可比指标，只能写代表性或高信号，不能写平台排名。

## Evidence lanes

### Lane A — 官方规格与迁移

- Anthropic 发布公告、Claude Platform release notes
- Models overview、What's new、Pricing、Effort、Fast mode、Prompt caching
- Claude Code changelog、官方产品/配置文档
- System Card 仅用于能力和限制边界，不把厂商 benchmark 当独立验证

### Lane B — 社区原始实践

- X 原帖：官方账号、Claude Code 团队、早期试用者、批评者
- YouTube / podcast / 原作者文章：只把亲测经验当 practitioner evidence
- 记录原帖正文、时间、直接可见互动、观察表面与限制

### Lane C — 独立分析与反证

- 检查 benchmark 方法、偏好与“人格”争议、迁移失败、过度自动化和成本误区
- 对 `best`、`top`、`first`、精确分数、人物身份、版本和价格做反向检索
- 将模型发布方的测评、客户引语和第三方实测分开

## Search lanes and reproducibility

- Official web: exact product/model names + pricing/effort/thinking/fast/cache/batch/migration
- Claude Code: release `2.1.219+`, model config, effort and fast-mode docs
- X query families: exact term, named-source, practice, criticism, old-skill conflict, effort
- YouTube/blog: exact title + author; only deeply read items used in report
- Search languages: English primary, Chinese secondary

## Freshness and access boundary

- 截止 2026-07-29；发布五天后的快照，不预测后续默认值或产品可用性。
- 官方页面可能无稳定更新时间，ledger 记录本次访问日期。
- 专用 X connector/API 当前不可用；优先浏览器直读原帖。搜索卡、镜像和转述一律标
  `proxy`，看不到的互动数据标 `unavailable`。
- 个性化 feed 不进入样本；X `Top` 只用于候选发现，不支持平台 Top-N。

## Adversarial checks

- 核对黄金案例的 `300K Batch output`、四档 effort、medium 默认、Fast mode 开启时机、
  Claude Code 默认模型/计划可用性、`/code-review` 与 Auto mode 建议。
- 区分“官方说模型会自我验证”与“高风险任务不再需要外部验收”。
- 区分删除冗余旧规则与删除所有 skills / safety constraints。
- 检查社区相反体验是否来自不同任务、旧 scaffold 或表面设置。
- 不从单一 benchmark 推出医疗、法律或金融的部署安全性。

## Completion criteria

- 四个 research artifacts 齐全。
- 每个规格、价格、默认值、breaking change 与工作流建议都有邻近直接来源。
- 报告给出可复制的 Claude Code/API 设置路径、迁移清单和分场景决策框架。
- 社区部分既有实践者也有批评，且不伪造 Top-N。
- 明确列出黄金案例中被纠正或降级的高风险结论。
