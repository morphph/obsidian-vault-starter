# research/ — 调研工作区(非 vault)

`/research` skill 的输出目录。**这不是 vault 的一部分。**

## 这是什么

每次 `/research "<topic>"` 跑完,在这里建一个 `<topic-slug>/` 子目录,产出:

```
research/<topic-slug>/
  research-plan.md      检索计划(按渠道拆 + 每渠道原生搜法 + 消歧 + 检查点)
  report.md             一份到底的调研报告。结构对齐参考报告:
                          §1 这话题是什么(事实轴) · §2 焦点实体深挖
                          §3-5 X / Web / YouTube 各渠道 Top-N(增长轴,含写作风格拆解)
                          §6 核心洞察 · §7 排序的内容角度(增长轴→/draft 入口) · 附录时间线
  ingest-candidates.md  建议进 vault 的外部原文清单(每条:一句理由 + URL)
  meta.json             机器记录(slug / topic / sha256 / tools-used / warnings)
```

两个原则:**采集按渠道**(每渠道用该渠道原生搜法),**综合按双轴**(事实轴锚官方源 / 增长轴排
Top-N + 角度)。拿不到的互动/观看数据标「推断·未实测」,绝不编造。

**两种产物模式**(`mode:` 参数,只影响 step 5 交付形状,采集 step 1-4 相同):
- **`mode:report`**(默认)= 上面的选题决策文档,末尾 Gate-1 建议角度喂选题。
- **`mode:guide`**(话题含 指南/教程/上手/进阶/guide/tutorial 时自动建议)= **常青读者指南**:
  产出 `facts.md`(核验台账,住所有研究元话术)+ `<slug>-guide.md` 或成对 `<slug>-overview.md` +
  `<slug>-advanced.md`(头部契约 → 心智模型 → 能力映射/职责边界 → 每主题处方 → 端到端工作流 →
  分阶段计划 → 可复制模板 → 检查清单 → 官方索引)。**不产渠道 Top-N、不产建议角度**——指南本身即交付物。
  骨架与硬性配额见 `.claude/skills/research/references/guide-template.md`。样例:`research/codex/`。

下游:
- `ingest-candidates.md` → 人圈选 → `/ingest` 进 `raw/`(才成 Tier-1)。
- `report.md` §7 挑一个角度 → `/draft research/<slug>/` 写博客(无单独 outline.md;§7 角度即骨架)。

## Tier 与边界(重要)

- **调研报告本身 = Tier-4 衍生品**:归档可检索,但**排除出 vault、排除出选题输入**(否则选题会引用自己的调研结论 → 塌缩)。
- **报告引用的外部原文 = Tier-3**:圈选后经 `/ingest` 才进 `raw/` 成 Tier-1。
- `/research` **不自动 ingest、不写 `wiki/log.md`、不 push、不发布**。只产候选清单,人圈选后才 `/ingest`。

> **⚠️ gbrain Tier-1 sync 必须排除本目录(`research/`)。**
> 否则机器按 engagement 挑的调研素材会被当 Tier-1 收,稀释 vault 的作者品味锚,并造成同文双路入库(重复 atoms)。gbrain sync 的监听范围应只含 `raw/`。此排除配置在本仓之外,需在 gbrain 侧确认。

## `_reference/`

回归 fixture(如 content-ops 的 `outputs/codex-guide/PILOT.md`)。`/research` 的产出应与 PILOT 同形(两轨调研 + 候选清单)。fixture 待从 content-ops 拷入。
