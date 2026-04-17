# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language AI daily digest newsletter (April 17, 2026) covering major model releases and industry developments.

**Key Exchanges:**
- Assistant produced a full bilingual-style newsletter covering: Opus 4.7 launch, OpenAI GPT Rosalind (biology vertical), Qwen3.6-35B-A3B open-source MoE model, Codex expansion, and assorted quick news items.

**Decisions Made:**
- Newsletter lead angle: "open-source laptop model beats flagship APIs" — Qwen3.6 framed as the most important signal of the day over Opus 4.7 itself.
- Included a "模型小课堂" (Model Primer) section explaining MoE / sparse activation for readers unfamiliar with the architecture.

**Lessons Learned:**
- Qwen3.6-35B-A3B: 35B total / 3B active params, Apache 2.0, runs via Ollama GGUF. Beat Opus 4.7 on Simon Willison's pelican test. Key data point: open-source MoE is eroding frontier API moat from below.
- Opus 4.7: Cursor benchmark 58% → 70%, Notion +14% with fewer tool calls. Prompting patterns differ from 4.6 (per Boris Cherny). Ethan Mollick flagged adaptive effort routing as a UX gap — no manual override unlike ChatGPT.
- GPT Rosalind: OpenAI's first vertical-domain frontier model. Signal: vertical specialization as strategy post-general-model ceiling.
- Claude Mythos: First model to pass AISI cybersecurity benchmark (independent third-party, not Anthropic self-reported).
- Gas Town controversy: tool accused of consuming users' API credits to train its own model — trust issue worth tracking.

**Action Items:**
- None explicitly stated. Newsletter appears complete and ready for publication.