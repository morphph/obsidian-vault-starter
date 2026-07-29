# research/ — 调研工作区（非 vault）

`/research` skill 的输出目录。**这不是 vault 的一部分。**

## 这是什么

每次 `/research "<topic>"` 跑完，在这里建立一个 `<topic-slug>/` 子目录，产出：

```
research/<topic-slug>/
  research-plan.md      问题地图、渠道选择、时间边界、消歧与反证计划
  report.md             面向读者的事实、机制、起源、社区争议与实际意义
  source-ledger.md      claim 级证据、来源角色、冲突、访问限制与互动状态
  ingest-candidates.md  值得人工复核、之后可能进入 vault 的外部原文
```

三个原则：

- **按证据角色采集**：官方/一手来源、原始作者、社区传播、实践、解释与批评不能混为一类。
- **按读者认知路径综合**：先回答是什么，再解释起源、机制、边界、争议和实际意义。
- **把验证元数据留在 ledger**：报告保持可读；互动数据只写 `observed`、`proxy` 或
  `unavailable`，没有可比样本就不写 Top-N。

`/research` 只负责理解话题，不负责研究内容市场或选择写作角度。下游边界：

- `/topic research/<slug>/`：分析市场覆盖、内容表现和空白，产出候选角度。
- 人选择角度后，`/topic` 产出 `topic-brief.md` 与 `outline.md`。
- `/draft`：基于选定的 topic brief、outline 和研究证据写文章。
- `ingest-candidates.md`：人圈选后才通过 `/ingest` 进入 `raw/`。

## Tier 与边界(重要)

- **调研报告本身 = Tier-4 衍生品**:归档可检索,但**排除出 vault、排除出选题输入**(否则选题会引用自己的调研结论 → 塌缩)。
- **报告引用的外部原文 = Tier-3**:圈选后经 `/ingest` 才进 `raw/` 成 Tier-1。
- `/research` **不自动 ingest、不写 `wiki/log.md`、不发布**。只产候选清单，人圈选后才
  `/ingest`。

> **⚠️ gbrain Tier-1 sync 必须排除本目录(`research/`)。**
> 否则机器按 engagement 挑的调研素材会被当 Tier-1 收,稀释 vault 的作者品味锚,并造成同文双路入库(重复 atoms)。gbrain sync 的监听范围应只含 `raw/`。此排除配置在本仓之外,需在 gbrain 侧确认。

## `_reference/`

历史回归材料仅用于审计旧产物的优缺点，不定义当前 `/research` 的结构。当前契约以
`.agents/skills/research/SKILL.md` 和其 `references/` 为准。
