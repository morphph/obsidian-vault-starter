# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Composing the daily AI newsletter (May 5, 2026 edition) covering industry news, model releases, and strategic analysis.

**Key Exchanges:**
- Newsletter assembled from multiple source categories: Anthropic moves, model benchmarks, enterprise signals, open-source economics, and builder tools

**Decisions Made:**
- **Pick of the Day**: DeepSeek V4 Pro's 10x cost advantage over closed frontier models chosen as the headline strategic signal — framed as a pricing inflection point, not just a benchmark win
- **Top 3 stories**: Anthropic's creative partner positioning, Unity's MCP/agentic AI beta, DeepSeek V4 Pro's benchmark claims
- **Model Literacy section**: MoE (Mixture of Experts) economics explained — "how many parameters fire per token" as the real cost metric

**Lessons Learned:**
- Open-source cost curve compressing faster than closed labs can monetize — enterprise buyers gaining real negotiating leverage for the first time
- "Parameter count" is no longer a useful proxy for model capability or cost (MoE routing means only a fraction activates per token)
- Benchmark reliability is degrading: Mollick flags prohibitive cost + variance between harness vs. API usage — losing signal on capabilities when stakes are highest
- Context engineering (prompts, rules, memory, retrieval) is the real differentiator between mediocre and production-grade agent setups, not the model itself
- Agent security is now an M&A category (Cisco/Astrix) — autonomous agents create new attack surfaces

**Action Items:**
- Ingest into wiki: DeepSeek V4 Pro (benchmarks, MoE cost economics, open-source frontier shift)
- Ingest into wiki: Sierra ($150M ARR, $15B valuation, AI customer service agents as proven revenue category)
- Ingest into wiki: Unity MCP integration (game engine + agentic AI ecosystem convergence)
- Ingest into wiki: Anthropic SDK v0.98.0 enterprise auth stack (Managed Agents APIs, Workload Identity Federation, OAuth)
- Ingest into wiki: Claude Code v2.1.128 release
- Update wiki: Anthropic page — creative partner positioning as strategic shift
- Update wiki: Benchmark reliability concerns (Blueprint-Bench 2, Mollick's measurement crisis flag)
- Track: White House AI model guardrails executive order — potential deployment/compliance impact