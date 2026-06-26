# research/_reference/ — 回归 fixture

放 `/research` 的产出格式参照 + 回归样例。

## 现有 fixture

- `loop-engineering-report-example.md` —— **`report.md` 的目标形状参照**(来自一次 Cowork
  Dispatch 调研)。结构:§1 这话题是什么 · §2 焦点实体深挖 · §3-5 X/Web/YouTube 各渠道
  Top-N(含写作风格拆解)· §6 核心洞察 · §7 排序的内容角度 · 附录时间线。`/research` 的
  `report.md` 应与它同形。**注意**:此样例里 X/YouTube 的互动数据是「推断」的——我们的版本
  必须把这类数据标「推断·未实测」,不照它那样当事实写。

**待拷入**(来自 content-ops,此会话访问不到那个仓):
- `PILOT.md` —— 一次人肉跑通的 `/research` 样例(两轨:A 事实锚定官方文档 / B 竞品缺口 + 制胜点 + ingest 思路)。建好 skill 后用同一话题(OpenAI Codex 指南)跑一遍,产出应与之同形。
- `draft-zh-v1.md` —— 该话题的下游初稿,看 research → outline → draft 的衔接。

在 fixture 到位前,`/research` 已把两轨格式自包含写死在 `.claude/commands/research.md` 里,skill 可独立运行;「与 PILOT 同形」这条验收待 fixture 到位后再核。
