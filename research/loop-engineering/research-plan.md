# Research Plan: Loop Engineering（焦点 Designing loops with Fable 5）

> depth: standard · ⚠️ 互动数据：X/YouTube 本机无 scanner（bird/last30days/summarize），将标「推断·未实测」
> 查内已发现：vault 有 ~30 个 loop/harness Tier-1 锚点，但**没有「Loop Engineering」命名概念页**，也**没有任何 Fable 页**。
> → 本次扫外**只补这两个缺口 + 渠道受欢迎度**，不重复扫 ralph/harness/verification 等已有组件。

## 渠道① Web / 官方站   ← 现在最硬的实测源
- 查询：
  - `"loop engineering" Addy Osmani`（命名/定义性原文）
  - `loop engineering AI coding agent blog 2026`
  - `"designing loops" Fable agent`
  - `anthropic Fable 5 announcement`（官方发布页 → 事实锚定）
  - `anthropic harness design long-running` site:anthropic.com（核对我们已有 raw 的官方源是否更新）
  - `openai "unrolling the codex agent loop"` site:openai.com
  - `"loop engineering" OR "harness engineering" latent.space`
- 点名直查：anthropic.com · openai.com · addyosmani.com · martinfowler.com · latent.space · stevekinney.com
- 搜法：官方文档 / 原始出处优先；Fable 5 的事实（模型 ID / 定价 / 基准）只认 anthropic.com

## 渠道② X / Twitter
- 查询：
  - `"loop engineering" min_faves:50 site:x.com`
  - `"designing loops" agent site:x.com`
  - `"designing loops with fable" site:x.com`
  - `loop engineering Boris Cherny site:x.com`
  - `Fable 5 loop design site:x.com`
  - `"agentic loops" min_faves:100 site:x.com`
- 搜法：按收藏(bookmark)加权（收藏=想存来重读，信号比赞更硬）；抓 long-article 格式；记 作者@handle + 互动 + 是否长文
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」（靠被引用频率/作者影响力反推排序，并注明是反推）

## 渠道③ YouTube
- 查询：
  - `loop engineering AI agent 2026`
  - `designing loops Fable 5`
  - `"Fable 5" loop design test`
  - `agentic loop coding tutorial 2026`
  - `stop prompting agents build loops`
- 搜法：近 60 天优先；按观看/互动；实操 > 理论
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」

## 消歧块（焦点实体）
- **"Fable 5" = `claude-fable-5`**，Anthropic 最新公开旗舰模型（据 Dispatch 参照报告，发布于 2026-06-09，首个面向大众的 "Mythos 级"）。**已知，无需暂停消歧**——但其具体事实（模型 ID / 定价 / 上下文窗口 / 基准）一律以 **anthropic.com 官方页**为准核验，标 ✅/⚠️。vault 现无 Fable 页，属新实体。
- "Loop Engineering" = Addy Osmani（2026-06 前后）为这一波「从 prompt agent → design loops」运动命名的概念，非歧义。

## 综合契约（提醒后面 step 5）
- report.md 按双轴综合：事实轴（Fable 5 / Loop Engineering 定义锚 anthropic.com / addyosmani.com）+ 增长轴（按渠道排 Top-N + 形式拆解 + 角度）
- §0 带入查内的 ~30 个 vault 锚点——**我们的制胜角度建立在「已有组件地图」上**，不从零解释
- 候选源对 raw/ 去重（raw/ 已有 harness-design / anatomy-of-harness / bcherny / ralph 等）；拿不到的数据标「推断·未实测」，绝不瞎编
