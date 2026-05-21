# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage batch (signals 21–32) for Claude Code content pipeline — routing new events to wiki/blog/FAQ pages.

**Decisions Made:**
- **Signal 28 (claude-code-setup plugin)** flagged as highest-priority: official Anthropic plugin that auto-configures hooks, skills, MCP, subagents. Touches 5 subtopics. Action: refresh install FAQ + plugin manifest FAQ, create new tutorial targeting "how to use claude-code-setup plugin anthropic."
- **Signal 31 (Mini Shai-Hulud malware)** flagged as high-severity security signal: supply-chain attack abusing Claude Code hooks for C2 persistence via stolen npm tokens. Action: refresh security blog, create new blog targeting "malware targeting claude code hooks supply chain attack."
- **Signal 22 (Engram identity layer)** introduced a new concept — persistent identity context vs. session memory. Action: refresh memory blog, create new FAQ targeting "persistent identity layer for claude code."
- **Signals 21, 25, 27, 30** routed as refreshes only: hydrology teaching repo (non-technical use cases), manga pipeline (Skills showcase), 6-hour orchestration tutorial (sub-agents + MCP), claude-api skill sandbox onboarding update.
- **Signals 23, 24, 26, 29, 32** correctly ignored (marketing hype, novelty app, philosophy, duplicate, generic crowd-source).

**Action Items:**
- Create tutorial: `claude-code-setup` plugin walkthrough (from signal 28)
- Create blog: malware targeting Claude Code hooks (from signal 31)
- Create FAQ: persistent identity/memory tools for Claude Code (from signal 22)
- Refresh existing pages: `blog/claude-code-is-not-a-coding-tool` (add hydrology example), `faq/claude-code-skills` (add manga pipeline + sandbox onboarding), `blog/claude-code-subagents-examples` + `blog/claude-code-mcp-setup` (cite 6-hour tutorial), `blog/claude-code-security-vulnerability-scanning` (add Shai-Hulud reference)