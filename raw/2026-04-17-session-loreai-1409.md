# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Content from a comparative article on Claude Code vs Codex (OpenAI) — likely a raw source or draft being reviewed for the wiki.

**Key Exchanges:**
- No interactive Q&A occurred. The session context is the article body itself, not a conversation.

**Decisions Made:**
- *(none visible)*

**Lessons Learned:**
- **Claude Code strengths**: Interactive/exploratory work, complex multi-file refactors, environment-sensitive tasks, real-time steering, local code execution (data stays on-machine), deep customization via hooks/skills/CLAUDE.md.
- **Codex strengths**: Async batch tasks, parallel independent tickets, web-based (no local setup), cloud sandbox, included in ChatGPT Pro subscription, good for teams optimizing throughput.
- **Model context difference**: Claude Code loads full project context via CLAUDE.md + local filesystem; Codex works from a repo snapshot (misses local-only config, uncommitted changes).
- **Security distinction**: Claude Code keeps code local (only snippets sent to API); Codex clones full repo into OpenAI's cloud sandbox — relevant for enterprise/proprietary code.
- **Practical combined workflow**: Claude Code for active dev / hard problems; Codex for backlog clearing / well-scoped tickets.
- **Cost note**: Codex bundled with ChatGPT Pro (predictable flat cost); Claude Code API-based (scales with token usage — heavier for large codebases).

**Action Items:**
- This article is a strong candidate for `/ingest` into the wiki under builder tools — covers [[Claude Code]] vs Codex comparison, security models, and workflow patterns relevant to the domain.