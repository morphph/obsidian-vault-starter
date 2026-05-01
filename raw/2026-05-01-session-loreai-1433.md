# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/source article comparing OpenAI Codex vs ChatGPT for coding tasks — likely content for LoreAI blog or wiki ingestion.

**Key Exchanges:**
- Detailed competitive analysis of OpenAI Codex (agentic, async, repo-aware, $200/mo Pro tier) vs ChatGPT (conversational, sync, no repo access, $20/mo Plus)
- Codex pricing gate: requires Pro/Team/Enterprise — not available on Free or Plus tiers
- Codex sandbox has **no internet access** — only dependencies in your lock file work; adding new libraries requires a separate step

**Decisions Made:**
- Article positions Codex and ChatGPT as **complements, not competitors** — "Codex handles execution, ChatGPT handles thinking"
- Recommended workflow: reason through approach in ChatGPT → hand off implementation to Codex
- Default recommendation: ChatGPT is the safer default; Codex justified for professional devs on large codebases

**Lessons Learned:**
- Codex's self-verification loop (run tests → read errors → fix → re-run) is its key differentiator over ChatGPT for multi-file tasks
- OpenAI has a fragmented editor story: Codex (agentic tasks) + Copilot (inline suggestions) + ChatGPT (conversational) = three separate products/subscriptions
- For teams already on ChatGPT Enterprise, Codex adoption cost is effectively zero — fastest adoption vector
- Codex works best for senior devs who can write precise task specs; beginners are better served by ChatGPT

**Action Items:**
- This content should be ingested into the wiki via `/ingest` — covers OpenAI Codex capabilities, pricing, and positioning (relevant to `wiki/` AI models/products knowledge)
- Could generate or update wiki pages for: `openai-codex.md`, `chatgpt.md`, `agentic-coding.md`