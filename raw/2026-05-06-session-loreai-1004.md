# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI digest (2026-05-06) covering 23 items across industry news.

**Key Exchanges:**
- Produced structured JSON digest with sections: LAUNCH, TOOL, RESEARCH, TECHNIQUE, INSIGHT, BUILD, QUICK_LINKS
- Pick of the day: Strategic sandbagging research (models learning to hide capabilities from evaluations)

**Decisions Made:**
- Headline hook combined Anthropic/Blackstone enterprise push with GPT-5.5 Instant rollout as dual heroes
- Model Literacy concept: Multi-Token Prediction (Speculative Decoding) — tied to both Gemma 4 speedup and Ollama MTP support appearing same day
- Prominence assignments: 3 heroes (Blackstone partnership, GPT-5.5 Instant, sandbagging research), rest regular/quick

**Lessons Learned:**
- "You Are an Expert" prompt prefix no longer helps on frontier models (item 33670) — prompting technique now dead weight, worth auditing system prompts
- Strategic sandbagging implies evaluation paradigm needs to shift from measuring outputs to understanding internal representations
- Anthropic's enterprise strategy is evolving from API-only → full-stack managed AI services (Blackstone JV + financial templates + deployment playbook = coordinated vertical push)

**Action Items:**
- Ingest key items into wiki: Anthropic enterprise services pivot, GPT-5.5 Instant, sandbagging research, MTP technique
- Update [[anthropic.md]] with Blackstone partnership and financial services vertical push
- Consider wiki page for strategic sandbagging / alignment evaluation limitations
- Note: Bun potentially porting Zig→Rust using AI agents (PORTING.md designed for coding agents) — relevant to builder tools tracking