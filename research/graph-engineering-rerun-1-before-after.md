# Graph Engineering Research: Before / After

> 比较对象：
> - before: `research/graph-engineering/`
> - after: `research/graph-engineering-rerun-1/`
> - golden reference: 用户提供的 Graph Engineering 报告

## 结果摘要

浏览器方案带来的主要价值是**证据升级与错误发现**，不是让报告无条件增加更多帖子。

| 维度 | Before | After | 实质影响 |
|---|---|---|---|
| 直接可读 X 原帖 | 核心正文/指标主要经第三方复核 | 7 个原帖正文可读；1 个 Article 不可读 | provenance 显著改善 |
| Peter 互动数据 | proxy，约 2.7m–3.0m views | observed：3.1m views 等完整 UI 指标 | 放大角色得到直接证据 |
| 2024 语义前身 | 原帖 URL + 二手时间线复核 | Itamar 原帖全文直接可读 | 起源 claim 更稳 |
| 独立批评 | 有批评结论，原始社交证据弱 | Paweł 原帖和可见回复直接读取 | 社区地图更平衡 |
| 定义漂移 | 报告已区分 knowledge graph | 找到 478k views 的高互动混淆实例 | 从抽象消歧升级为传播风险 |
| “Anthropic PDF” | baseline 未采用；golden 当推荐内容 | affiliation 标为 unsupported | 修正 golden 的关键风险 |
| Top-N | 拒绝无样本排名 | 只列同一观察窗口的预选集合 | 保留增长信号，不伪造平台排名 |
| 官方机制 | 证据充足 | 核心结论不变 | 说明浏览器应定向补社交证据 |

## 定量变化

- 直接尝试的 X URL：8
- 原帖正文直接读取：7
- 直接观察到 view count：7
- 直接观察到较完整互动组：6
- 保持 `unavailable` 的 X Article：1
- 从 proxy 升级为 observed 的核心 metric record：Peter 1 条
- 新增直接 critic record：1
- 新增高互动概念混淆/错误归属 record：1

## 相对 golden example

Golden example 的优势是读者能快速看到 X、YouTube 和博客的代表内容，渠道感很强。但它把
预选内容写成 `X Top 5`，没有声明完整比较集，而且把 Codez 的“Anthropic 工程师 PDF”
作为推荐解释。

重跑保留了 golden 的优点：

- 给出作者、原帖、核心观点与互动信号；
- 让社区阵营和传播事件具体可见；
- 发现对非专家有帮助的简洁定义。

同时修复了它的风险：

- 不把预选集合说成平台 Top-N；
- 互动数带观察时间与 UI 精度；
- 高互动不获得更高事实权重；
- 原帖无法读取就标 `unavailable`；
- affiliation 与“首创”必须反查一手来源；
- 把概念混淆本身写进报告，而不是无条件推荐。

## 对 skill 的验证结论

新增 X 协议在本例中有效，原因是它强制执行了四件以前没有操作化的事：

1. 先选择 surface，再声明访问边界；
2. 直接打开原帖，而不是停在搜索摘要或第三方时间线；
3. 把正文、时间、指标、观察时点和精度一起放进 ledger；
4. 对高互动且带有 `official / first / Anthropic` 等风险词的帖子做反向核验。

它没有解决的部分：

- 未登录时 X 原生搜索仍不可用；
- Chrome Extension 尚未安装，无法利用用户登录态；
- 官方 X MCP 还没有 Developer App 凭据；
- 因此 discovery recall 仍弱于 direct verification。

下一次最有价值的 A/B 不是再重写报告，而是接通一种完整发现面：

1. 优先测试安装后的 Chrome 登录态 `Latest/Top` 搜索；
2. 若需要 full archive 和结构化重复运行，再配置官方 X MCP 只读访问；
3. 比较它们新增的独立原帖是否真正改变 claim，而不只增加链接数量。
