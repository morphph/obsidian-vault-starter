# Session Capture: loreai

**Date:** 2026-05-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated the daily AI newsletter digest for 2026-05-17.

**Key Exchanges:**
- Produced a complete newsletter covering: GPT-5.5 Codex 48-hour regression, Stingning 30B-A3B MoE model achieving olympiad gold, CTF scene dying due to frontier AI, and other developments.

**Decisions Made:**
- Led with the Codex regression story as the most actionable item for readers (your code from past 48 hours may be affected)
- Featured CTF death as 今日精选 — framed it as first domino for all human-vs-AI competition domains, not just a security niche story
- Included 模型小课堂 explaining MoE/active parameters to connect the Stingning story to reader understanding

**Lessons Learned:**
- GPT-5.5 model versions are not static in production — capability regressions can happen silently for ~48 hours before detection/fix. Critical workflows should not blindly trust a single model provider.
- MoE architecture now proven: 30B total / 3B active achieves olympiad gold on consumer GPU — parameter count labels are increasingly misleading
- Test-time compute scaling (second scaling law) shows no diminishing returns yet across math, science, hacking, even crosswords

**Action Items:**
- Wiki updates needed: Anthropic Mythos (250 vulns vs 22), PrimeIntellect autonomous research with Claude Code Opus 4.7, Cerebras $60B IPO, River AI ($1B raise no product), NVIDIA SANA-WM open source world model
- Track: Gemini Pro pricing rumor ($12/M output tokens vs GPT-5.5) — verify when announced
- Track: Claude API grey market exploitation (Oxford researchers, 10% of official price via promo credits)
- Track: Energy-Based Models (EBM) resurgence as alternative to autoregressive generation