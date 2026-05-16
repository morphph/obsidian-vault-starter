# Session Capture: loreai

**Date:** 2026-05-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Composing/finalizing the daily AI newsletter for May 16, 2026.

**Key Exchanges:**
- Newsletter covers: OpenAI unbundling Codex from Zed for all ChatGPT subscribers, a 30B-A3B MoE model hitting Olympiad gold on consumer hardware, and MCP vs code-first agent token efficiency (10x gap)
- Anthropic commits $200M to Gates Foundation — largest philanthropic commitment by any AI lab
- OpenAI merges ChatGPT/Codex/API teams under Brockman into unified-app strategy
- Grok V9 finishes training at 1.5T parameters (3x V8)
- UK AISI confirms Mythos Preview solves both cyber ranges end-to-end — first model to do so

**Decisions Made:**
- MoE explanation chosen as Model Literacy section — explains total vs active parameters as the new evaluation framework
- MCP vs code-first token benchmark chosen as Pick of the Day — the 158k vs 15k token finding on Monday.com's GraphQL API, with recommendation: MCP for long-tail integrations, tight SDK bindings for high-frequency agent workflows

**Lessons Learned:**
- MoE architecture insight: 30B-total/3B-active means frontier reasoning on consumer GPUs — "how many parameters?" is now an incomplete question, ask total (knowledge capacity) AND active (compute cost)
- MCP token overhead is real and measurable: 10x tokens, 4x steps vs direct SDK for same task — interoperability and efficiency are in tension
- LeCun's heuristic: LLMs strongest where language IS the reasoning substrate (math, code, logic), weakest where language merely describes another medium (physical, spatial)
- Ontario audit: AI medical note-takers routinely get basic clinical facts wrong — verification layers aren't optional in high-stakes domains

**Action Items:**
- Ingest key items into wiki: Anthropic $200M Gates commitment, OpenAI unified-app reorg, MoE active parameter concept, MCP token overhead benchmark
- Next week: GPT 5.6 vs Gemini 3.2 announcements expected — track for next newsletter