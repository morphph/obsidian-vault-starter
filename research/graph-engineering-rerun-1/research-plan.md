# Research Plan: Graph Engineering — X Evidence Rerun

> depth: standard
> reader: 能使用 Claude Code / Codex / API、但不是资深系统工程师的 AI builder
> as_of: 2026-07-29
> primary languages: English, Chinese

## Research boundary

研究 2026 年 agent 社区语境中的 **Graph Engineering**，即把
agent loop、确定性步骤、工具、验证器与人工闸门组织成显式控制拓扑。知识图谱
（knowledge graph）只用于消歧。

本次不是扫描内容市场，也不选择写作角度。核心研究问题是：

> Graph Engineering 在当前 agent 社区中到底指什么、从哪里来、哪些部分是旧工程的新
> 命名、哪些实践值得 AI builder 采用？

方法扩展问题是：直接 X 原帖观察能否改善起源时间线、社区阵营、争议与互动证据。

## Question map

1. 上一轮通过第三方时间线复核的 X 原帖，能否直接读到正文、作者和发布时间？
2. Peter Steinberger 的传播指标能否从 `proxy` 升级为 `observed`？
3. X 上有哪些独立定义、实践主张和批评？
4. 高互动内容是否在传播不同含义的 `Graph Engineering`？
5. 直接观察是否改变关于起源、机制或实际建议的核心结论？

## Surface routing

1. **专用 X connector / API / MCP：** 当前会话中没有 X connector。已确认 X 官方提供
   hosted X MCP，但本机未配置 X Developer App 凭据，因此本轮不调用。
2. **登录态 Chrome：** Chrome 正在运行，但 ChatGPT Chrome Extension 未安装，不能
   连接其登录态。
3. **内置浏览器：** X 搜索页要求登录；已知原帖的公开详情页可以直接读取正文、时间、
   可见互动数据和部分回复。
4. **Public Web：** 用于发现或复核候选 URL、延伸文章和一手官方材料。
5. **第三方快照：** 只作 `proxy`，不得覆盖直接原帖观察。

## X query and candidate boundary

计划中的原生查询族：

- exact: `"graph engineering"`
- chronology: `"graph engineering" since:2024-01-01 until:2026-07-30`
- origin counter-search: `"graph engineering" until:2026-07-04`
- definitions: `"graph engineering" means` / `"graph engineering" is`
- criticism: `"graph engineering" hype` / `"graph engineering" state machine`
- named sources: Peter Steinberger, Itamar Friedman, Hamel Husain, Miles Deutscher,
  Eric Siu, Paweł Huryn, Codez

实际限制：

- X 原生搜索被登录墙阻断，所以没有把 `Top` 或 `Latest` 结果当作完整样本。
- 候选集来自本轮已知 canonical URL seed list 和 public Web 发现。
- 直接核验 8 个 X URL：7 个公开 post 可读，1 个 X Article 不可读。
- 因候选集不是平台全量或随机样本，互动数只允许描述“本次预选样本中”，不能写
  `X Top 5`。

## Other evidence lanes

- **Origin and discourse:** Josh C. Simmons、X 原帖、LangChain 回应、同期解释与批评。
- **Mechanism:** Anthropic agent patterns、LangGraph、AutoGen GraphFlow。
- **Counter-evidence:** Google agent-scaling study、Cognition multi-agent essays。
- **Disambiguation:** agent execution graph versus knowledge graph engineering。

这些非 X 结论沿用上一轮已深读的一手来源，并重新检查是否被新的社区证据改变。

## Adversarial checks

- 反查 2026-07-04 和 2026-07-18 之前的语义前身。
- 不把高互动等同于事实正确或术语首创。
- 对“Anthropic 工程师发布 PDF”等 affiliation claim 搜索一手出处。
- 把 X Article 不可读标为 `unavailable`，不从转述恢复成“已核验原文”。
- 区分 agent 控制拓扑与 knowledge graph memory。
- 只在同一观察窗口、同一预选候选集内比较互动。

## Quality checks

- 每个 load-bearing claim 有直接来源或明确 synthesis 状态。
- 社交互动有观察时点、surface、精度和样本边界。
- 高互动不提高事实权重。
- X discovery lane 明确标为 incomplete，不冒充全量搜索。
- 报告服务读者理解，不包含 skill A/B 评价或内容选题建议。
