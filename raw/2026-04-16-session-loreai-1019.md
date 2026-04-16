# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an AI newsletter digest (April 16, 2026) for knowledge base capture.

**Key Exchanges:**
- No Q&A — this was a solo newsletter review session.

**Decisions Made:**
- None recorded.

**Lessons Learned:**
- **Event-driven agents are the new paradigm**: Both Claude Code Routines and OpenAI Agents SDK launched on the same day with the same architectural bet — agents fire on events (cron, GitHub webhooks, API calls), not human prompts. This is the microservices pattern applied to AI.
- **VAKRA benchmark finding**: IBM Research found agents fail more on tool selection and parameter formatting than on reasoning itself — important signal for anyone building agent evals.
- **MCP gap is large**: The delta between "using Claude bare" vs "Claude wired via MCP" is described as enormous — persistent memory, database reads, API calls across sessions.

**Action Items:**
- Ingest Claude Code Routines launch into wiki — significant enough to warrant its own page or update to `claude-code.md`
- Ingest OpenAI Agents SDK sandbox update — production-grade agent isolation is now a shipping feature
- Note Baidu ERNIE-Image on Hugging Face as signal of Chinese labs entering global open-source ecosystem
- Consider capturing the $0 production stack (Ollama + Gemma 4 + LangGraph + ChromaDB + MCP + Next.js + SQLite + Langfuse) as a reference architecture page
- Notion's 5-rebuild story (Latent Space) is worth ingesting — concrete lessons on shipping AI-native products with 100+ MCP/CLI tools