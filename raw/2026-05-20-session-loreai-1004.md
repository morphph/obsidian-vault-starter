# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the daily AI newsletter edition for 2026-05-20, dominated by Google I/O and a major Anthropic talent acquisition.

**Key Exchanges:**
- Built full newsletter JSON with 25 items across LAUNCH, TOOL, RESEARCH, INSIGHT, TECHNIQUE, and QUICK_LINKS sections
- Dual hero structure: Karpathy joining Anthropic + Google's Gemini 3.5 / Gemini Omni double launch at I/O

**Decisions Made:**
- **Pick of the Day:** DeepMind cell rejuvenation (id 39694) — chosen because it represents AI-for-science graduating from benchmarks to actual biological discovery
- **Model Literacy topic:** Multi-Token Prediction (MTP) — tied to llama.cpp speed gains for Qwen3.6, practical concept readers can use to evaluate local-model claims
- **Headline hook:** Led with Karpathy + Google I/O as the dual narrative, not one or the other

**Lessons Learned:**
- Heavy news days (Google I/O) require careful prominence assignment — not everything Google announces deserves hero status; Gemini 3.5 and Omni got hero, the rest (Project Genie, I/O roundup) went regular
- Anthropic had a dense day too: self-hosted sandboxes (TOOL hero), Stainless acquisition, KPMG + PwC enterprise deals, Mythos validation — spreading across sections prevents Anthropic overload in any one section

**Action Items:**
- Wiki pages likely needed: [[karpathy-at-anthropic]], [[gemini-3-5]], [[gemini-omni]], [[anthropic-stainless-acquisition]], [[claude-self-hosted-sandboxes]], [[deepmind-cell-rejuvenation]]
- Update existing wiki pages: [[anthropic]] (Karpathy hire, Stainless acquisition, KPMG/PwC deals, self-hosted sandboxes), [[google-deepmind]] (Gemini 3.5, Omni, Project Genie, Gemini for Science), [[openai]] (compute futures, SynthID adoption)
- Track pattern: Big Four consulting firms as enterprise AI kingmakers (KPMG 276K + PwC expanded = two of four locked by Anthropic)
- Track pattern: Vertical integration trend — both Anthropic (Stainless) and Mistral (Emmi AI) acquiring to own full stack