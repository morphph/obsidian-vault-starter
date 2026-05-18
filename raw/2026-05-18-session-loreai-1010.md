# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Produced the 2026-05-18 daily AI newsletter (Anthropic/Claude-focused digest).

**Key Exchanges:**
- Newsletter successfully generated covering: enterprise AI spending shift, LeCun world model timeline, local inference cost analysis, open-source model wave, and developer tooling updates.

**Decisions Made:**
- Led with Ramp enterprise spending data (Anthropic > OpenAI) as the anchor story — chosen because real transaction data > surveys, and it signals a structural shift from experiment to production budgets.
- "今日精选" expanded the Ramp story into a strategic framework: budget category placement determines stickiness, code tools win because ROI is easiest to quantify.

**Lessons Learned:**
- **Local inference cost myth busted:** Apple Silicon per-token cost (including depreciation + electricity) exceeds cloud API pricing — "本地推理免费" is wrong. Worth updating wiki if a page on inference economics exists.
- **Model routing emerging as default multi-agent pattern:** Opus for frontend, GPT-5.5 for backend, Gemini for vision — no single model dominates all tasks, routing layer is the new architecture primitive.
- **Open-source model density:** May 2026 is the most concentrated open model release month ever (Gemma 4, DeepSeek V4, Kimi K2.6, MiMo 2.5, GLM-5.1). Selection complexity is now a real problem.

**Action Items:**
- Wiki pages to create/update: Anthropic enterprise adoption (Ramp data), LeCun world model timeline (12-18mo from May 2026 → target ~Q3 2027), model routing pattern, `claude-code-setup` plugin.
- Monitor: Meta FAIR KempeLab researcher departure — next move signals talent flow direction.
- Monitor: ArXiv enforcement policy — first academic "teeth" against AI-generated papers, may cascade to other venues.