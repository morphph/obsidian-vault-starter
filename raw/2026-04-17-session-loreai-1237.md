# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Automated signal batch reviewing 4 Twitter/X signals about OpenAI Codex updates (2026-04-17), with triage decisions on which wiki pages to refresh or create.

**Key Exchanges:**
- Signal 1: OpenAI reframes Codex from "coding assistant" → "real workspace" — action: refresh `topics/codex` and `faq/codex`
- Signal 2: Developer frustration with "oh my codex" bulk-installing MCPs and modifying Custom Instructions without consent — reveals a content gap around manual MCP server setup for Codex
- Signal 3: Codex desktop app (macOS) adds native computer use, gpt-image-1.5, 90+ third-party plugins, persistent threads + scheduling — multi-subtopic update affecting topic hub, FAQ, and blog
- Signal 4: Anthropic releasing 13 free AI courses (Claude API, MCP, Claude Code) — **ignored** as irrelevant to Codex content

**Decisions Made:**
- Signal 1 → refresh only (no new page; not enough detail to justify creation)
- Signal 2 → create tutorial: "how to add MCP servers to Codex without modifying custom instructions"
- Signal 3 → refresh existing pages + create new blog post targeting "OpenAI Codex computer use macOS"
- Signal 4 → ignore (Claude/Anthropic content, not Codex)

**Action Items:**
- Update `topics/codex` and `faq/codex` to reflect workspace-first positioning
- Create tutorial page on manual MCP server installation for Codex (subtopics: codex-plugins, codex-mcp-servers, codex-agents-md)
- Refresh `topics/codex`, `faq/codex`, `blog/codex-vscode` with computer use + plugin + scheduling details
- Create new blog post on Codex computer use for macOS (gpt-image-1.5, 90+ plugins, scheduling)