# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comparison article on OpenAI Codex vs ChatGPT for coding workflows.

**Key Exchanges:**
- Article compares Codex (agentic, autonomous coding agent with repo access) vs ChatGPT (conversational, no persistent project context)
- Codex: connects to GitHub, reads full codebase, creates PRs, runs tests in sandbox, consumption-based pricing
- ChatGPT: standalone chat interface, unverified output, subscription pricing ($20/mo Plus), better for exploration/debugging

**Decisions Made:**
- Recommended workflow is a 4-phase combo: Understand (ChatGPT) → Specify (Human) → Execute (Codex) → Review (Human+ChatGPT)
- Codex best for: well-defined scope, multi-file changes, repeatable patterns, async-friendly tasks
- ChatGPT best for: exploratory/debugging, learning, quick snippets, architectural decisions

**Lessons Learned:**
- Codex's autonomy is double-edged: when wrong, propagates errors across multiple files at scale
- Critical calculation is tool cost vs developer time saved, not tool cost alone
- Codex's closed-loop execution (write → test → iterate) catches errors before presenting results
- ChatGPT's conversational nature gives more correction opportunities before code is written
- Teams should treat Codex as a sprint team member for well-defined tickets

**Action Items:**
- This content is a LoreAI blog draft (has internal links like `/blog/codex-complete-guide`, `/subscribe`) — likely needs wiki pages for: OpenAI Codex capabilities, Codex vs ChatGPT positioning, agentic coding workflow patterns
- Pricing note: Students get $100 free Codex credits; open source maintainers get dedicated free access