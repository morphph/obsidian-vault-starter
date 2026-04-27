# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article draft comparing OpenAI Codex (2025 autonomous agent) vs ChatGPT for coding workflows — likely for LoreAI blog or wiki ingest.

**Key Exchanges:**
- The article establishes a clear decision rule: "if the task ends with a git commit, use Codex. If it ends with a decision or understanding, use ChatGPT."
- Codex (2025) is distinct from the original Codex API (released 2021, deprecated March 2023) — same name, entirely different product.
- Codex is NOT a separate product — it's a feature inside ChatGPT, accessed via paid tiers.

**Decisions Made:**
- Recommended workflow: reason with ChatGPT → execute with Codex → review everything
- Entry-point recommendation: ChatGPT Plus ($20/mo) for most devs; upgrade to Pro ($200/mo) if processing 15+ routine coding tasks/month

**Lessons Learned:**
- Codex quality depends on test coverage — without tests, its self-correction loop has no signal and output quality drops sharply
- Codex tradeoff: tested code with shallow review; ChatGPT tradeoff: untested code with deep reasoning
- Codex cannot do: ambiguous/creative tasks, architectural discussion, real-time debugging, non-coding work
- ChatGPT Code Interpreter ≠ Codex — cannot clone repos, install deps, or run full test suites

**Action Items:**
- Consider ingesting this as a raw source → wiki page on `openai-codex.md` or `codex-vs-chatgpt.md`
- Pricing table (Free/Plus/Pro/Team/Enterprise) should be flagged as time-sensitive — verify against openai.com/pricing regularly