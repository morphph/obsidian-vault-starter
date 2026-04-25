# Session Capture: loreai

**Date:** 2026-04-25
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a daily AI digest newsletter (2026-04-25) covering major launches, investments, and research across the AI frontier.

**Key Exchanges:**
- Assistant produced a full newsletter draft covering DeepSeek V4, GPT-5.5, Google–Anthropic investment, Anthropic research, and tooling updates.

**Decisions Made:**
- Newsletter format used: sections LAUNCH / INSIGHT / RESEARCH / TOOL / TECHNIQUE / BUILD / MODEL LITERACY / QUICK LINKS / PICK OF THE DAY
- Included a "Model Literacy" explainer on MoE architecture to contextualize DeepSeek's pricing disruption

**Lessons Learned:**
- **DeepSeek V4**: MoE architecture enables frontier-level performance at ~1/20th the cost of Opus 4.7; open weights (Pro variant) on HuggingFace. Key datapoint for cost-performance tracking.
- **GPT-5.5**: $30/1M output tokens — most expensive frontier API tier ever. Directly contradicts DeepSeek's pricing direction.
- **Google → Anthropic $40B**: Bloomberg-reported, would be largest AI investment in history. Google already led prior rounds; Amazon is co-backer.
- **Anthropic + Amazon**: 5 GW compute expansion locked in — datacenter-city scale.
- **Project Deal (Anthropic research)**: Claude negotiated real transactions in a real office marketplace — first controlled study of LLM economic behavior with genuine stakes. Finding: AI negotiation strategies diverge from human expectations in meaningful ways.
- **Claude Code update**: Web/mobile UX refresh, CMD+Shift+F desktop file browser added.
- **Anthropic Rate Limits API**: Programmatic per-org/workspace rate limit queries now available.
- **Sakana AI Fugu**: First commercial product — multi-agent orchestration, beta.
- **Superpowers framework**: 166K-star agentic skills framework, composable skill modules pattern.
- **Qwen3.6-27B on Raspberry Pi**: Edge AI capability gap continues collapsing.

**Action Items:**
- Consider ingesting this digest into `raw/` for wiki processing (DeepSeek V4, GPT-5.5, Anthropic Project Deal, Google investment are all wiki-worthy entries)
- Update or create wiki pages: `deepseek.md`, `gpt-5.md`, `anthropic.md`, `mixture-of-experts.md` with 2026-04-25 data