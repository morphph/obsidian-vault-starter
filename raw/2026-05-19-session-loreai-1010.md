# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily AI newsletter digest for May 19, 2026 — curating and formatting AI industry news.

**Key Exchanges:**
- Newsletter covered Anthropic acquiring Stainless (SDK/MCP platform), Google I/O preview, Claude Design token limit increases, and new cache diagnostics API
- Model Literacy section explained prompt cache prefix matching mechanics

**Decisions Made:**
- Pick of the Day: Anthropic/Stainless acquisition framed as "owning the developer surface area" — the moat thesis is SDK stickiness, not model weights
- Newsletter structure: Lead story + 3 numbered items + Quick Hits + Model Literacy + Pick of the Day

**Lessons Learned:**
- **Prompt cache prefix matching**: Cache works character-by-character from the start; any change early in the prompt invalidates everything downstream. Static content (system prompt, tools, few-shot) goes at the front; variable content (user messages, dynamic context) goes at the end. Anthropic's new `cache_miss_reason` diagnostic makes this visible.
- **"Implementation Notes" prompt pattern**: Ask coding agents to maintain a running `implementation-notes.html` logging every decision not in the spec — turns implicit tradeoffs into auditable artifacts with no slowdown.
- **AI output revision leakage**: Models expose iteration history in outputs (e.g., "better version" footers). Add "check for leaked revision context" to review checklists.

**Action Items:**
- Ingest Anthropic/Stainless acquisition into wiki (strategic move re: SDK ownership, MCP integration)
- Ingest cache diagnostics feature (`diagnostics.previous_message_id` → `cache_miss_reason`)
- Track Google I/O outcomes tomorrow (Gemini 3.2 expected)
- Track PaddleOCR 3.5 (dropped PaddlePaddle dependency, now runs on Transformers/HuggingFace)
- Track Open Agent Leaderboard (IBM + HuggingFace standardized agent benchmarks)
- Track MaxSim kernel for ColBERT/late-interaction retrieval performance gains