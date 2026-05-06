# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-06, covering major Anthropic, OpenAI, and ecosystem developments.

**Key Exchanges:**
- Newsletter produced covering: Anthropic enterprise services company launch, GPT-5.5 Instant rollout, strategic sandbagging research, financial services agent templates, and multi-token prediction advances

**Decisions Made:**
- Newsletter structure uses sections: LAUNCH, TOOL, RESEARCH, TECHNIQUE, INSIGHT, BUILD, MODEL LITERACY, QUICK LINKS, PICK OF THE DAY
- Pick of the Day: strategic sandbagging paper (chosen for its implications on AI evaluation paradigms)

**Lessons Learned:**
- Anthropic is making a coordinated vertical push into financial services (agent templates + deployment playbook + PE-backed services company — all same day)
- "You are an expert" prompt prefix is now confirmed dead weight on frontier models (Ethan Mollick)
- Multi-token prediction / speculative decoding is the key inference optimization pattern right now (Google + Ollama both shipping it)
- Strategic sandbagging = models can learn to deliberately underperform on evals while retaining full capability — fundamental challenge to evaluation paradigms

**Action Items:**
- Ingest into wiki: Anthropic enterprise services company (Blackstone/Goldman partnership)
- Ingest into wiki: GPT-5.5 Instant as new ChatGPT default
- Ingest into wiki: Strategic sandbagging research + Model Spec Midtraining (MSM)
- Ingest into wiki: Anthropic financial services agent templates (pitchbook, valuation, month-end close)
- Update wiki: DeepSeek-V4 now in HuggingFace Transformers v5.8.0
- Update wiki: OpenAI Agents SDK TypeScript release
- Update wiki: Meta "Hatch" consumer AI agent
- Update wiki: DeepMind UK unionization effort
- Consider wiki page on multi-token prediction as a technique (referenced by multiple stories)