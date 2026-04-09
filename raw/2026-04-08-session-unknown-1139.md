# Session Capture: unknown

**Date:** 2026-04-08
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Configuring MCP servers (Playwright, Computer Use) at user level for all Claude Code sessions

**Key Exchanges:**
- Playwright MCP successfully fetched a full tweet from X/Twitter without login — accessibility tree captured complete article text
- Discussed whether Claude for Chrome extension could be chained with Claude Code — concluded they're isolated runtimes with no shared API

**Decisions Made:**
- Moved Playwright MCP config from project-level (`blog2video/.mcp.json`) to user-level (`~/.claude/.mcp.json`) — removed project-level duplicate
- Added `@github/computer-use-mcp` (v0.1.16, by GitHub) alongside Playwright at user level
- Decided against pursuing Claude for Chrome integration — Playwright MCP with `--browser chrome` already provides authenticated browsing via real Chrome cookies

**Lessons Learned:**
- Playwright MCP with `--browser chrome` can fetch X/Twitter content without login — accessibility tree gives full text including stats
- MCP servers and skills are different mechanisms — MCPs provide tools, skills use them
- MCP config only read at session startup — restart required for changes
- User-level MCP config lives at `~/.claude/.mcp.json`, merges with project-level

**Action Items:**
- Source fetch fallback chain could be updated: Playwright MCP → WebFetch → Ask user to paste (not yet implemented)