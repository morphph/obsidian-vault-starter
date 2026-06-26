# research/ — 调研工作区(非 vault)

`/research` skill 的输出目录。**这不是 vault 的一部分。**

## 这是什么

每次 `/research "<topic>"` 跑完,在这里建一个 `<topic-slug>/` 子目录,产出:

```
research/<topic-slug>/
  report.md             调研综合(A 事实锚定 + B 竞品缺口 + 制胜写法)
  outline.md            文章大纲(以 audience-profile.md 为品味锚)
  ingest-candidates.md  建议进 vault 的外部原文清单(每条:一句理由 + URL)
  meta.json             机器记录(slug / topic / sha256 / tools-used / warnings)
```

下游:
- `ingest-candidates.md` → 人圈选 → `/ingest` 进 `raw/`(才成 Tier-1)。
- `report.md` + `outline.md` → `/draft research/<slug>/` 写博客。

## Tier 与边界(重要)

- **调研报告本身 = Tier-4 衍生品**:归档可检索,但**排除出 vault、排除出选题输入**(否则选题会引用自己的调研结论 → 塌缩)。
- **报告引用的外部原文 = Tier-3**:圈选后经 `/ingest` 才进 `raw/` 成 Tier-1。
- `/research` **不自动 ingest、不写 `wiki/log.md`、不 push、不发布**。只产候选清单,人圈选后才 `/ingest`。

> **⚠️ gbrain Tier-1 sync 必须排除本目录(`research/`)。**
> 否则机器按 engagement 挑的调研素材会被当 Tier-1 收,稀释 vault 的作者品味锚,并造成同文双路入库(重复 atoms)。gbrain sync 的监听范围应只含 `raw/`。此排除配置在本仓之外,需在 gbrain 侧确认。

## `_reference/`

回归 fixture(如 content-ops 的 `outputs/codex-guide/PILOT.md`)。`/research` 的产出应与 PILOT 同形(两轨调研 + 候选清单)。fixture 待从 content-ops 拷入。
