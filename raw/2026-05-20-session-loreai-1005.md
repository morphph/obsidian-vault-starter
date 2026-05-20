# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-20, covering a high-density news day (Karpathy joining Anthropic, Google I/O 2026, Claude managed agents updates).

**Key Exchanges:**
- Newsletter successfully compiled from multiple sources covering: Karpathy→Anthropic move, Google I/O 2026 full product drop (Gemini 3.5, Gemini Omni, Project Genie, Chrome DevTools agent mode), Claude managed agents self-hosted sandboxes, OpenAI compute futures, DeepMind cell rejuvenation discovery, Anthropic acquiring Stainless, KPMG + PwC Claude deployments

**Decisions Made:**
- Pick of the Day: DeepMind cell rejuvenation result chosen over the bigger headline items (Karpathy, Gemini) — rationale was "AI-for-science graduating from benchmarks to biology" is more consequential long-term
- Model Literacy section covered Multi-Token Prediction (MTP) — tied to llama.cpp/Qwen3.6 speed gains in the quick links
- Karpathy move framed as talent-war signal rather than just a hiring announcement

**Lessons Learned:**
- Anthropic now has 2 of Big Four consulting firms (KPMG 276k employees + PwC expanded) — pattern: enterprises picking one frontier provider and going deep, not hedging
- Stainless acquisition + Mistral/Emmi acquisition happening days apart suggests industry consensus that models alone aren't the moat — vertical integration is the play
- HTML discovered as surprisingly effective output format for Claude Code workflows (from Anthropic's own blog)

**Action Items:**
- Wiki pages likely needed: Karpathy (update with Anthropic move), Gemini 3.5, Gemini Omni, Stainless acquisition, Claude managed agents self-hosted sandboxes, Project Genie
- Track Big Four adoption: KPMG ✅, PwC ✅, Deloitte ?, EY ? — "two down, two to go"
- Track Mythos validation: Cloudflare independent audit confirms 11x vulnerability discovery claims on production code