# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the daily Anthropic/AI news digest (`/ingest-anthropic-daily`) for 2026-05-19.

**Key Exchanges:**
- Selected 22 items across LAUNCH, TOOL, TECHNIQUE, RESEARCH, INSIGHT, and BUILD categories from Twitter, platform docs, HuggingFace blog, Hacker News, GitHub releases, and MIT Tech Review

**Decisions Made:**
- **Anthropic acquires Stainless** (score 95) — vertical integration of the SDK/MCP server layer. Signals Anthropic controlling the full developer tooling stack.
- **Claude Design doubles token limits** (score 93) — all plans, 10K+ likes. Meaningful capacity expansion.
- **Cache diagnostics public beta** (score 92) — API now reports `cache_miss_reason` with `diagnostics.previous_message_id`. Eliminates cache debugging guesswork.
- **Web search tool gets SEC filing data** (score 90) — structured financial data for research agents.
- **llama.cpp adds MTP for Qwen3.6** (score 89) — multi-token prediction on consumer hardware; major local inference speedup.
- **Google I/O imminent** (score 88) — Gemini 3.2 expected; MIT Tech Review frames Google as "clear third place" in foundation models.
- **Sam Altman endorses latest ChatGPT update** (score 86) — likely tied to GPT-5.5 fixes.

**Lessons Learned:**
- **Prompt technique (trq212, score 91):** Ask agents to maintain a running `implementation-notes.html` of decisions not in the spec. Turns implicit coding decisions into auditable artifacts.
- **AI output hygiene (Mollick):** Models leak revision history into outputs (e.g., slide footers saying "better version"). Add this to content QA checklists.
- **Git `--author` flag** as lightweight defense against AI-generated spam PRs in open-source repos.
- **MaxSim kernel** solves the ColBERT/late-interaction retrieval bottleneck — relevant for RAG pipelines.
- **PaddleOCR 3.5** now runs on standard Transformers backend, removing the PaddlePaddle framework dependency.

**Action Items:**
- Ingest Stainless acquisition into wiki (impacts [[anthropic]], SDK tooling pages)
- Update wiki with cache diagnostics feature and SEC filing tool enhancement
- Track Google I/O announcements tomorrow for competitive landscape updates
- Consider adding implementation-notes.html technique to agent prompt templates
- Open Agent Leaderboard (IBM + HuggingFace) worth a wiki page if it gains traction as a standard benchmark