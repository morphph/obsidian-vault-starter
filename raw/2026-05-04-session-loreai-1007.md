# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the 2026-05-04 daily AI newsletter covering Ollama v0.23, o1 clinical trial results, and Agents SDK 2.0.

**Key Exchanges:**
- Newsletter produced covering: Ollama v0.23 Claude Desktop integration, Harvard ER triage trial (o1 67% vs doctors 50-55%), Codex mega-update (GPT-5.5, browser control), Altman pushing Agents SDK 2.0, Anthropic-Fractile chip deal, Oscars AI policy, tool-input repair layers

**Decisions Made:**
- 今日精选 picked the o1 ER diagnosis story — strongest narrative tension (tech vs policy vs institutional resistance), highest reuse value as a reference point for clinical AI debates
- 模型小课堂 covered Tool-Input Repair Layers — directly actionable for builder audience, tied to the DeepSeek vs Opus 4.7 story

**Lessons Learned:**
- Tool-input repair layer pattern: a cheap model + JSON validation/repair layer can beat expensive models at tool calling — bottleneck is format compliance, not intelligence (Ahmad Awais breakdown)
- MCP has 5 underused primitives beyond tool calling: Prompts, Resources, Sampling, Roots, Notifications — most devs only use ~20% of the protocol
- Self-evolving Claude Code Skills pattern: automated eval loop + prompt rewriting + winner retention → 32/50 to 47/50 overnight

**Action Items:**
- Ingest Ollama v0.23 release, Anthropic-Fractile chip story, and Harvard o1 ER trial into wiki when raw sources are saved
- Track Codex Security plugin vs Claude Security public beta — "dual rivalry" framing worth a wiki page
- NanoClaw (28.5k stars, Anthropic Agents SDK-based) worth a wiki entry as fastest-growing agent framework