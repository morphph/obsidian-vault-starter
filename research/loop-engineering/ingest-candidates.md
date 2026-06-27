# Ingest Candidates — Loop Engineering / Fable 5

> 人圈选后才 `/ingest`。优先官方/作者一手源；第三方解读标注 `(第三方,ingest 前确认)`。
> 已对 `raw/` 去重：命中的标 `(已在库,勿重复 ingest)` 且默认不勾。

## 一手 / 官方（优先）

- [x] `https://addyosmani.com/blog/loop-engineering/` — **命名源 + 一个循环的 5 组件解剖**。最高优先级新概念页。(作者一手)
- [x] `https://www.anthropic.com/news/claude-fable-5-mythos-5` — Fable 5 官方发布（定价/订阅/安全）。(官方)
- [x] `https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5` — 官方规格表（模型 ID/1M/128k/拒答/自适应思考）。**最强事实锚**。(官方)
- [ ] `https://x.com/RLanceMartin/article/2064397389189071163` — **焦点原文「Designing loops with Fable 5」**。⚠️ **暂不可 ingest**：x.com 对抓取返回 402，需带认证抓取（浏览器 MCP / 手动粘贴）后才能入库。(作者一手，Anthropic 内部) — **首要内容目标，当前不可一手核验**。
- [ ] `https://x.com/steipete/status/2063697162748260627` — 「design loops, don't prompt」火种帖。(作者一手，短)
- [ ] `https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents` — 验证>自批评原则，loop 设计底座。(官方) ⚠️ 与已有 [[harness-design]] 查重后再定。

## 第三方解读（ingest 前确认）

- [ ] `https://www.latent.space/p/ainews-is-harness-engineering-real` — 把 loop 放在 harness「上一层」的定位透镜。(第三方,ingest 前确认)
- [ ] `https://x.com/mvanhorn/article/2063865685558903149` — "WTF Is a Loop? Steinberger vs Cherny" 社区辩论地图。(第三方,ingest 前确认)
- [ ] `https://www.oreilly.com/radar/loop-engineering/` — O'Reilly Radar 版，较可靠二手。(第三方,ingest 前确认)
- [ ] `https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules` — schedules/goals/subagents 实操 how-to。(第三方,ingest 前确认)
- [ ] `https://openai.com/index/unrolling-the-codex-agent-loop/` — Codex 循环逐回合拆解（OpenAI 侧对位）。(官方，但 codex cookbook 已在 raw/，查重后再定)

## 已在库（勿重复 ingest）

- [ ] ~~`https://www.anthropic.com/engineering/harness-design-long-running-apps`~~ — **(已在库** `raw/2026-04-06-anthropic-harness-design-long-running-apps.md`，对应 [[harness-design]]**，勿重复 ingest)**

## 明确跳过（低权威 SEO 解释文，列此仅为让你跳过）
explainx.ai/* · tosea.ai · mer.vin · eigent.ai · developersdigest · mindstudio · aibuilderclub
