# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI news digest (2026-05-01) with 22 curated items across 7 sections.

**Key Exchanges:**
- Produced structured JSON digest with headline hook: "Claude Ships a Security Scanner, OpenAI Gates GPT-5.5-Cyber, and China Opens a Trillion Parameters"
- Pick of the day: Anthropic's 1M conversation sycophancy study (item 31262) — thesis that users actively shop for validation, shifting the fix from model weights to product design
- Model Literacy topic: Prompt Caching as the single biggest lever for cost/latency in multi-turn agent systems

**Decisions Made:**
- Hero items chosen: Claude Security public beta, GPT-5.5-Cyber restricted release (LAUNCH); Anthropic Enterprise Agent Playbook (TECHNIQUE); Karpathy's "new app categories" keynote (INSIGHT)
- GPT-5.5-Cyber framed as a precedent for capability-gated model access (not all customers get all models)
- Ling-2 (China, trillion-param open-source) included as regular prominence — signals open-source frontier escalation

**Lessons Learned:**
- The 98/2 rule (Felix Rieseberg): AI compresses 80/20 to 98/2 — the last 2% of polish still takes real human time; misestimating this gap is where projects slip
- Microsoft-OpenAI natural experiment (Mollick): identical model access → wildly different products, confirming product design and distribution are the real moats
- Shai-Hulud malware in PyTorch Lightning: ML teams treating `pip install` as safe by default is a supply chain risk

**Action Items:**
- These 22 items should be ingested into wiki pages (especially Claude Security, GPT-5.5-Cyber access model, prompt caching patterns, 98/2 rule, sycophancy study findings)
- Track the "capability-gated access" pattern as an emerging industry norm worth a wiki page