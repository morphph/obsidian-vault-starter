# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal routing run for LoreAI content pipeline — evaluating 4 Twitter signals about OpenAI Codex and Claude on 2026-04-17.

**Key Exchanges:**
- Signal 3 (major): Codex desktop app released native macOS computer use, gpt-image-1.5, 90+ third-party plugins, persistent threads, and scheduling — framed as a shift from "coding assistant" to "real workspace"
- Signal 2: Chinese developer community frustration with "oh my codex" installing unwanted MCPs; demand for a curated, safe plugin workflow (analogous to Claude Code's Ralph Wiggum Plugin)

**Decisions Made:**
- Signal 3 → `refresh_and_create`: Update all compare pages (codex-vs-claude-code, codex-cli-vs-claude-code, codex-chatgpt) + new blog on "Codex computer use macOS"
- Signal 2 → `refresh_and_create`: New tutorial on "how to set up MCP servers in Codex" targeting safe plugin management
- Signal 1 (retweet, no content) → ignore; Signal 4 (Claude courses, off-topic) → ignore

**Lessons Learned:**
- MCP install safety is an emerging community pain point for Codex users — a real content gap with search demand
- Codex's "90+ plugins" milestone materially changes competitive comparisons; any compare page against Codex is likely stale after this release

**Action Items:**
- Create blog: "Codex computer use macOS" (keyword: `Codex computer use macOS`)
- Create tutorial: "How to set up MCP servers in Codex" (keyword: `how to set up MCP servers in Codex`)
- Refresh: `topics/codex`, `faq/codex`, `compare/codex-vs-claude-code`, `compare/codex-cli-vs-claude-code`, `compare/codex-chatgpt`, `blog/codex-vscode`