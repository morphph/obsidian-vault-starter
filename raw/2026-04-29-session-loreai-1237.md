# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage run for OpenAI Codex topic cluster — 8 signals from Twitter, RSS, and GitHub evaluated for content routing.

**Key Exchanges:**
- 8 signals scored; 3 actionable refreshes, 2 new content opportunities, 4 ignored with rationale

**Decisions Made:**
- **Signal 1 (ChatGPT Pro 2x Codex rate limits through May 31):** Refresh pricing FAQ — time-sensitive promo, expires May 31
- **Signal 2 (Codex = best coding model roundup):** Refresh comparison pages with community social proof
- **Signal 5 (Simon Willison on Codex base_instructions):** Refresh + create blog post — high-signal reverse-engineering of Codex system prompt reveals prompting strategy insights
- **Signal 6 (Next.js v16.3.0-canary.3 auto-generates AGENTS.md):** Refresh + create tutorial — major ecosystem integration, Next.js `next dev` now auto-generates AGENTS.md/CLAUDE.md
- **Ignored:** Sam Altman rate-limit abuse RT (redundant with Signal 1), Anthropic free courses (off-topic), Yuan astrology skill (novelty), custom CLI fork anecdote (niche/private)

**Action Items:**
- [ ] Write blog post: "What Codex's base instructions reveal about how to prompt it" (from Signal 5, keyword: `OpenAI Codex base instructions system prompt`)
- [ ] Write tutorial: "Using Codex with Next.js AGENTS.md auto-generation" (from Signal 6, keyword: `Next.js AGENTS.md auto-generate Codex`)
- [ ] Update `faq/codex-pricing` with Pro 2x rate limit promo (deadline: before May 31 expiry)
- [ ] Update comparison pages (`compare/codex-vs-claude-code`, `compare/codex-chatgpt`) with coding model roundup citation