# Session Capture: loreai

**Date:** 2026-05-10
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Produced the 2026-05-10 daily AI newsletter (Chinese-language digest format).

**Key Exchanges:**
- Newsletter successfully generated covering: Baidu Ernie-5.1 launch, Anthropic alignment research, Antirez's ds4 local inference engine, Altman crowdsourcing GPT next-gen priorities, and developer tooling updates.

**Decisions Made:**
- 今日精选 (Editor's Pick) went to Anthropic's "Teaching Claude Why" research — framing alignment as a trainable reasoning skill rather than bolted-on guardrails. Rationale: highest engagement (4,519 likes), deepest strategic implications.
- 模型小课堂 (Model Explainer) covered weight quantization — tied directly to Antirez's ds4 story, making the concept immediately relevant.

**Lessons Learned:**
- Claude Code token consumption breakdown worth noting for our own setup: 14% consumed by CLAUDE.md before any code is written, 13% re-reading conversation history, 73% total "invisible" consumption. Actionable: audit our own CLAUDE.md size.
- GitHub Copilot dropping Grok Code Fast 1 on May 15 — hard deadline, not a deprecation warning. Migration path: GPT-5 mini or Claude Haiku 4.5.

**Action Items:**
- Track Ernie-5.1 independent benchmarks when available (current claims are self-reported only)
- Track Anthropic Claude Certified Architect certification — signals AI engineering professionalizing beyond "can call an API"
- Monitor Antirez ds4 project — 2-bit quantized frontier models on 128GB Macs could shift local-vs-cloud economics
- Altman's crowdsourced feedback thread is live market signal — revisit high-voted replies for pain point analysis