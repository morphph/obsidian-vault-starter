# Session Capture: loreai

**Date:** 2026-04-26
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** AI newsletter digest compiled for 2026-04-26, covering major model launches, tool updates, and industry insights.

**Key Exchanges:**
- Newsletter digest generated covering 23 items across 6 sections: LAUNCH, TOOL, INSIGHT, RESEARCH, TECHNIQUE, BUILD
- Headline hook: DeepSeek-V4 million-token context + Google's $40B Anthropic deal
- Pick of the day: AI agents reproducing scientific papers and finding errors in human originals (item 29257)

**Decisions Made:**
- Model literacy concept for this issue: "Effective Context Length vs. Advertised Context Window" — framed around DeepSeek-V4's 1M token claim and why effective context is the metric that matters for builders choosing between V4, GPT-5.5, and Claude

**Lessons Learned:**
- GPT-5.5 Pro API priced at $30/1M output tokens — highest frontier API tier ever; DeepSeek undercuts at ~1/20th the cost
- DeepSeek-V4 is notable as the first open-weight model where million-token context is explicitly designed for agentic workloads, not just document ingestion
- Even Meta (most vertically integrated AI company) had to buy external compute (Amazon Graviton, multi-billion deal) for agent-scale inference
- Claude Code v2.1.117+ fixed over-calling Grep/Glob by switching to native file operations — four months of user complaints resolved
- LamBench: all frontier models struggle on lambda calculus (formal reasoning resistant to memorization) — exposes a benchmark gap
- Kimi Code ships as drop-in Claude Code CLI replacement (2 env vars, 100 tokens/sec, 262K context) — Chinese labs competing on dev tools

**Action Items:**
- Consider ingesting DeepSeek-V4 and GPT-5.5 pricing details into wiki for model comparison tracking
- Google's $40B Anthropic investment + 5GW compute deal worth updating `anthropic.md` wiki page