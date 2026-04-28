# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** AI news intelligence sweep for April 27-28, 2026 — 21 curated items from HN, Twitter, RSS feeds.

**Key Exchanges:**
- Microsoft and OpenAI ended their exclusive revenue-sharing deal — the foundational AI partnership is being restructured
- David Silver (AlphaGo) raised $1.1B seed for Ineffable Intelligence — largest European seed ever (Sequoia + Lightspeed)
- China blocked Meta's acquisition of Manus — cross-border AI M&A now a geopolitical tool
- 4TB voice data breach at Mercor (40K AI contractors) — training-data supply-chain risk materialized

**Decisions Made:**
- None (this was an intelligence digest, not a working session)

**Lessons Learned:**
- **Agentic coding shift:** OpenAI open-sourced Symphony (agent-per-issue orchestrator), GitHub moved Copilot to consumption-based pricing, Fig founder left AWS for Cognition — the agentic coding landscape is consolidating fast
- **On-device AI agents arriving:** Gemma 4 E2B runs as a fully local browser agent via WebGPU — no server, no API keys
- **Frontend agent technique:** specs → GPT-Image-2 mockup → code outperforms direct code generation
- **RL-trained "Conductor" model** automates prompt engineering across a pool of LLMs — step toward self-optimizing multi-agent systems
- **Xiaomi MiMo-V2.5** (MIT license) optimized for 1000+ tool-call sequences — new option for long-horizon agentic tasks
- **Anthropic:** Opus now gated behind extra-usage toggle on Pro plans; published election safeguards update
- **Microsoft released VibeVoice** — open-source voice-to-text coding tool (Simon Willison says it's actually usable)

**Action Items:**
- Ingest Microsoft/OpenAI deal restructuring → update [[openai]] and [[microsoft]] wiki pages
- Create or update wiki page for Ineffable Intelligence (David Silver)
- Track Manus acquisition block → relevant to [[china-ai-policy]] or geopolitics page
- Evaluate Symphony for low-stakes repo testing
- Note Copilot pricing shift — end of flat-rate AI coding tools