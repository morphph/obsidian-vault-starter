# Ingest candidates — 低成本多模型 Fable harness

> 圈选后才走 `/ingest`。**源纯度**：方法论/观点类话题**强烈优先一手源**（作者本人帖/repo/官方定价页）；第三方解读标注、ingest 前确认。
> 已对 `raw/` 去重：无命中（raw 仅有 `2026-07-08-fable-finding-your-unknowns.md`，是相邻 source 非本话题）。
> ⚠️ 多数一手源为 X 帖，正文被墙(HTTP 402)——ingest 时需登录浏览器抓取（同 vault 既有 Fable 帖的处理法）。

## 一手 / 官方（优先）
- [ ] https://x.com/mitchellh/status/2072715852944957531 — **最高优先**：三段式 harness + 「$50+→几美元」金句的一手出处（Hashimoto）。整个角度的锚。
- [ ] https://x.com/mitchellh/status/2074862990214787301 — 一手 freshness 信号：作者已把默认 planner/judge 换成 Sol/GPT-5.6（「模型名会过期」的实据）。
- [ ] https://x.com/RLanceMartin/article/2075641284635799865 — 一手（=种子）：Lance「Cost effective harnesses with Fable」文；正文被墙，ingest 标「body 未实测」。
- [ ] https://x.com/RLanceMartin/article/2064397389189071163 — 一手：Lance「Designing loops with Fable 5」，judge 段 73% vs 7–33% 数据来源。
- [ ] https://aider.chat/2024/09/26/architect.html — 一手（先例基石）：architect/editor 分离，benchmark + 谱系。
- [ ] https://aider.chat/2025/01/24/r1-sonnet.html — 一手：R1+Sonnet「64.0% polyglot SOTA at 14× less cost」。
- [ ] https://github.com/continuedev/continue/issues/3928 — 一手：社区 R1-architect + Sonnet-editor 先例。
- [ ] https://platform.claude.com/docs/en/about-claude/pricing — 官方定价锚（Fable $10/$50）。
- [ ] https://developers.openai.com/api/docs/models/gpt-5.5 — 官方定价锚（GPT-5.5 $5/$30）。

## 第三方（ingest 前确认；仅作算账/话语参照，勿当权威）
- [ ] https://thenewstack.io/claude-fable-cost-model-triage/ — (第三方) 「$9 vs $1.50 · model triage」标题模板 + 直观价差。
- [ ] https://blog.dativo.io/p/fable-5-as-the-architect-cheaper — (第三方) worked cost math（整任务 $6.77 拆解）。
- [ ] https://www.digitalapplied.com/blog/fable-5-hermes-openclaw-planner-brain-setup-2026 — (第三方) $4.50 vs $2.25 + cache 算账。
- [ ] https://www.mindstudio.ai/blog/multi-model-ai-coding-workflow-planning-execution-review — (第三方) 多模型 -85% + 「评审段放 premium 划算」论证（不同模型集）。
