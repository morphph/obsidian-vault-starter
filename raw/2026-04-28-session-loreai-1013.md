# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Production of the daily AI newsletter for April 28, 2026 — a heavy news day anchored by the Microsoft-OpenAI partnership restructuring.

**Key Exchanges:**
- Newsletter compiled from multiple source categories: industry moves, research papers, technique posts, build guides, and model literacy analysis
- Two-pass process visible: raw source items were reorganized and expanded into a polished newsletter with editorial framing

**Decisions Made:**
- **Pick of the Day: Microsoft-OpenAI exclusivity ending** — framed as "the AI layer is commoditizing," signaling that platform distribution (Azure, GitHub, Office) is the real moat, not model access. Builder takeaway: don't marry any single provider's API.
- **Model Literacy theme: Agent Orchestration patterns** — three approaches compared: Symphony (centralized dispatch), MiMo-V2.5 (long-horizon tool chaining, 1,000+ calls), Dirac (lightweight scaffolding). Conclusion: coordination design > model capability.

**Lessons Learned:**
- GitHub Copilot shifting to consumption-based pricing — end of all-you-can-eat AI coding; teams should audit usage now
- Specs → GPT-Image-2 mockup → code pipeline beats direct code gen — visual intermediate step dramatically improves frontend output
- Dirac topping TerminalBench with Gemini 3 Flash proves agent architecture matters as much as underlying model size
- Claude Pro now gates Opus behind extra-usage toggle — check model config
- Cross-border AI M&A is now geopolitical (Beijing blocking Meta's Manus AI acquisition)

**Action Items:**
- Wiki pages to create/update: Microsoft-OpenAI relationship, agent orchestration patterns (Symphony/MiMo/Dirac), GitHub Copilot pricing changes, GPT-realtime-1.5 voice-as-controller, Xiaomi MiMo-V2.5
- Track: Ineffable Intelligence ($1.1B seed from David Silver), VibeVoice (voice-to-code), Google×Kaggle AI agents course (June 2026)
- Track personnel move: Matt Schrage (Fig/AWS → Cognition/Devin)