# Ingest candidates — AI coding agent 上下文窗口管理入门

> 已对 `raw/` 去重。源纯度：本话题为方法论/机制类 → 强烈优先官方源，第三方解读标注。

## 官方 / 一手源（优先）
- [ ] https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — **官方一手**，attention-budget + 6 大机制的权威定义源；本话题事实脊梁 + 写作骨架标杆。**最高优先。**
- [ ] https://openai.com/index/unrolling-the-codex-agent-loop/ — **官方一手（OpenAI）**，Codex `/responses/compact` + `encrypted_content` + prefix caching；跨工具对照唯一硬源。⚠️ 本次 fetch 403，ingest 时可能需手动粘贴正文；**角度1 落笔前须逐字核验。**
- [ ] https://www.trychroma.com/research/context-rot — **一手研究（Chroma）**，18 模型 context rot 实证；「越满越笨」的量化背书。
- [ ] https://cursor.com/docs — **官方（Cursor）**，Rules 常驻 vs Skills 动态加载的上下文装配模型；第三家对照。⚠️ docs 重定向变薄，ingest 时确认取到正文；**角度1 落笔前须逐字核验。**
- [ ] https://cursor.com/blog/agent-best-practices — **官方（Cursor）**，best-practice bullets，补 docs 页。
- [ ] https://simonwillison.net/tags/context-engineering/ — **一手（作者本人站）**，quarantine/pruning/summarization 词汇脚手架；入门概念地图弹药。

## 已在库（勿重复 ingest）
- https://claude.com/blog/using-claude-code-session-management-and-1m-context —（已在库：`raw/2026-04-16-thariq-claude-code-session-management-1m.md`）5 选项框架原始出处。
- https://x.com/bcherny/status/2038454336355999749 —（已在库：`raw/2026-04-09-bcherny-claude-code-best-practices.md`，含该 status）subagent/隐藏特性。

## 第三方（ingest 前确认，优先用上面官方源替代）
- [ ] https://codex.danielvaughan.com/2026/04/21/codex-cli-prompt-caching-maximise-cache-hits-cost-reduction/ —（第三方，ingest 前确认）Codex 缓存实操，derivative；优先用官方 unrolling-the-codex-agent-loop。
- [ ] https://www.buildthisnow.com/blog/guide/mechanics/context-management —（第三方，ingest 前确认）continue/rewind/clear/compact/subagent 入门解释，derivative；仅供结构参考。
- [ ] https://howborisusesclaudecode.com/ —（第三方聚合，勿 ingest）优先原始 X thread（已在库）。
