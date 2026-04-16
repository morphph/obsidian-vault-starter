# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal processing run for the Claude Code knowledge base — 20 incoming signals routed across subtopics and pages (2026-04-15 to 2026-04-16).

**Key Exchanges:**
- No direct Q&A; this was an automated signal triage output.

**Decisions Made:**
- **Signal 1 / 2 / 4 / 5 / 7:** Claude Code desktop app fully rebuilt for parallel sessions → route to `topics/claude-code`, create new blog (keyword: "claude code desktop app parallel sessions")
- **Signal 3:** Claude Code Routines (scheduled + API-triggered + event-triggered cloud agents) → update `topics/claude-code` + `blog/claude-code-remote-sessions-phone`, create new blog (keyword: "claude code routines scheduled agents")
- **Signal 11:** `codeburn` tool reveals 56% of Claude Code spend is conversation overhead, 21% is actual coding → update `faq/claude-code-pricing`, create blog (keyword: "claude code token cost breakdown")
- **Signal 12:** Viral CLAUDE.md template framed as "self-reinforcing AI engineering infrastructure" → refresh `blog/claude-code-memory` + `faq/claude-code-skills` with this angle
- **Signal 13:** New tool drastically simplifies custom MCP server creation → refresh `blog/claude-code-mcp-setup`, create tutorial (keyword: "how to build a custom MCP server for Claude Code")
- **Signal 14:** Claude Code 2.1.108 — claude-api skill routing rewritten, new built-in Skills added (init, statusline, PR review, security-review) → refresh `faq/claude-code-skills`
- **Signal 18:** `claude-code-best-practice` repo (19.7K ⭐) distills Boris Cherny's guidance → refresh `topics/claude-code` + `blog/claude-code-hooks-mastery`, create blog (keyword: "claude code best practices tips")
- **Signal 20:** Claude API/Code criticized for ~99% uptime vs Codex's 99.99% — enterprise reliability concern → refresh `compare/claude-code-vs-codex` with reliability section

**Lessons Learned:**
- Duplicate signals (RTs, same-event coverage) should be collapsed to a single routing action on first occurrence; subsequent duplicates are ignored even if from high-authority accounts (e.g., bcherny)
- "Conversation overhead" (56%) vs "actual coding" (21%) is a highly shareable, concrete cost insight — strong blog angle
- Routines framing ("no laptop needed, runs on our infrastructure") is distinct enough from existing remote-control content to warrant a separate blog rather than just a refresh

**Action Items:**
- Create blog: Claude Code desktop app parallel sessions
- Create blog: Claude Code Routines scheduled agents
- Create blog: Claude Code token cost breakdown (codeburn)
- Create tutorial: How to build a custom MCP server for Claude Code
- Create blog: Claude Code best practices (synthesizing the 19.7K-star repo)
- Refresh: `faq/claude-code-pricing`, `faq/claude-code-skills`, `blog/claude-code-memory`, `blog/claude-code-mcp-setup`, `blog/claude-code-remote-sessions-phone`, `blog/claude-code-hooks-mastery`, `topics/claude-code`, `compare/claude-code-vs-codex`