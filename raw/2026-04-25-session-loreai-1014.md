# Session Capture: loreai

**Date:** 2026-04-25
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generating and reviewing an AI builder newsletter digest for April 25, 2026

**Key Exchanges:**
- Newsletter covers major AI news: DeepSeek V4 at 1/20th cost of Opus 4.7 (MoE architecture), GPT-5.5 API at $30/1M output tokens, Anthropic Project Deal (real-money LLM negotiation study), Google's potential $40B Anthropic investment
- Model literacy section explains Mixture of Experts (MoE) architecture as the driver behind cheap-but-capable models like DeepSeek V4

**Decisions Made:**
- Pick of the Day: Anthropic Project Deal — framed as the alignment-for-commerce angle, not just a research novelty
- Newsletter sections: top 3 stories → quick hits → model literacy → pick of the day

**Lessons Learned:**
- MoE is the recurring answer to "why is this model cheap but good" — worth tracking as a recurring pattern in cost disruptions
- Project Deal surfaces a real product question: agentic commerce requires defining agent negotiation behavior (aggressive vs. relationship-preserving), which is an alignment problem, not a technical one
- GPT-5.5 and DeepSeek V4 represent opposite strategic bets: premium margin vs. volume/cost disruption — useful frame for tracking the frontier pricing wars

**Action Items:**
- Consider ingesting Project Deal paper into wiki when the full paper drops (currently only social post)
- Anthropic TypeScript SDK v0.91.1 has a security patch for CMA memory file permissions — update if using managed agent memory in production
- Track Google $40B Anthropic investment as it develops (Bloomberg report, unconfirmed)