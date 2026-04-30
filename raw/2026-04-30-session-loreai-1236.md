# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal routing/triage for OpenAI Codex content pipeline — 9 signals from Twitter, RSS, and GitHub releases evaluated for content action.

**Key Exchanges:**
- 4 of 9 signals deemed actionable; 5 ignored (empty RTs, off-topic Anthropic courses, personal anecdotes)

**Decisions Made:**
- **Signal 3 → refresh_and_create (tutorial):** Codex masterclass on subagents and parallel tasks. Keyword target: "how to use codex subagents parallel tasks." Updates `topics/codex` hub + new tutorial for multi-agent workflows.
- **Signal 5 → create (FAQ):** MCP vs Agent Skills distinction — fills a common misconception gap. Keyword: "codex mcp vs agent skills difference."
- **Signal 7 → refresh_and_create (blog):** Simon Willison extracted Codex's internal `base_instructions` system prompt. High-signal for `codex-agents-md` and `codex-prompting`. Updates `faq/codex` + new blog analyzing Codex defaults. Keyword: "openai codex base instructions system prompt."
- **Signal 8 → create (tutorial):** Next.js v16.3.0-canary.3 auto-generates `AGENTS.md` and `CLAUDE.md` in `next dev` — ecosystem validation of AGENTS.md as a standard. Keyword: "agents.md next.js codex configuration."

**Lessons Learned:**
- Duplicate RT signals (signals 1, 2, 4) should be collapsed early — only the substantive source tweet (signal 3) carried routing value.
- Cross-product signals (Anthropic courses appearing in Codex monitoring) need domain filtering before triage.

**Action Items:**
- Create tutorial: Codex subagents + parallel task delegation
- Create FAQ: MCP vs Agent Skills in Codex context
- Create blog post: Codex base_instructions analysis (from Willison source)
- Create tutorial: AGENTS.md + Next.js configuration guide
- Refresh `topics/codex` and `faq/codex` hub pages with new subtopics