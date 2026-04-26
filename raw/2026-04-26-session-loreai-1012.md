# Session Capture: loreai

**Date:** 2026-04-26
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Newsletter drafting session — formatted and completed the April 26, 2026 AI builder digest.

**Key Exchanges:**
- User provided the second half of a newsletter (research, technique, build, model literacy, quick links, pick of the day sections); assistant generated the complete formatted newsletter including top three lead stories

**Decisions Made:**
- Lead stories chosen: DeepSeek-V4 million-token context, GPT-5.5 Microsoft Copilot rollout, AI agents reproducing papers and surfacing errors
- Model literacy concept preserved verbatim: advertised context window vs. effective context length — "lost in the middle" problem persists even at frontier scale

**Lessons Learned:**
- GPT-5.5 launched at $30/1M output tokens — most expensive frontier API tier ever; thinking mode tops all major benchmarks
- DeepSeek-V4: 1M token context with MoE routing; first open-weight model where advertised context may equal effective context
- Meta signed multi-billion Amazon Graviton CPU deal for agentic inference — validates hybrid cloud thesis even for vertically-integrated players
- Google invested $40B in Anthropic — largest AI investment in history
- LamBench (lambda calculus tests) exposes formal reasoning gap frontier models can't paper over with pattern matching
- Claude Code v2.1.117+ fixed over-calling grep/glob (native file operations)
- OpenAI open-sourced monitorability evals — safety commons contribution
- Beijing requiring prior approval for US investment in Chinese tech firms

**Action Items:**
- None explicitly mentioned