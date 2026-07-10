# Ingest Candidates: Best Practices for Claude Fable 5
> 人圈选后才 `/ingest`。方法论/模型行为类话题**强烈优先官方源**；第三方解读标注确认。
> 已对 `raw/` 去重：命中标「已在库，勿重复 ingest」并默认不勾。

## 官方源（强烈优先）
- [ ] https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 — **权威最佳实践页**，§6 几乎每条 tip 的原始出处；最该进库。
- [ ] https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 — API 层事实骨架（model ID / 1M·128k / 定价 / adaptive-thinking-only / refusals·fallback·billing）。
- [ ] https://www.anthropic.com/news/claude-fable-5-mythos-5 — 官方发布公告 + partner benchmark（Stripe/Cognition/Hebbia）。
- [ ] https://www.anthropic.com/news/redeploying-fable-5 — 下架→重部署事件时间线（安全 + 出口管制 + 误拒率代价）。

## 第三方 / 独立（ingest 前确认）
- [ ] https://simonwillison.net/2026/Jun/9/claude-fable-5/ — 最佳独立实测（真实成本 $110/天，可信可引）。(第三方,ingest 前确认)
- [ ] https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026 — 家族「哪个何时用」路由框架。(第三方·社区共识,ingest 前确认；含未核实定价)
- [ ] https://the-decoder.com/claude-fable-5-the-first-mythos-model-is-powerful-expensive-and-heavily-filtered/ — 平衡新闻分析，擅长安全/过滤角度。(第三方,ingest 前确认)
- [ ] https://x.com/milesdeutscher/status/2064882870037225762 — 官方 guide 最高触达科普转译（形式参考用）。(第三方,ingest 前确认)
- [ ] https://x.com/nateherk/article/2072431375530008871 — 「工程师实际怎么 prompt Fable」长文。(第三方,ingest 前确认)

## 已在库（勿重复 ingest）
- [x] ~~https://x.com/trq212/status/2073100352921215386~~ — Thariq「Finding Your Unknowns」→ **已在库** `raw/2026-07-08-fable-finding-your-unknowns.md`，勿重复 ingest；直接引用现有 raw 源。
