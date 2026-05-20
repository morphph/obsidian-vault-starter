# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Claude Code vs OpenAI Codex — a detailed feature-by-feature comparison for the LoreAI blog.

**Key Exchanges:**
- Comprehensive comparison across 7 dimensions: configuration, developer experience, task parallelism, safety/sandboxing, pricing, and use-case fit
- Claude Code = interactive terminal-native agent with deep customization (CLAUDE.md, hooks, MCP); Codex = async cloud-sandboxed task runner via ChatGPT

**Decisions Made:**
- Framing: "not interchangeable — they serve different workflows" rather than picking a winner
- Verdict positions Claude Code for complex interactive work, Codex for parallelized well-defined tasks
- Acknowledged complementary use: "many teams will find value in using both"

**Lessons Learned:**
- Claude Code parallelism is *within* a task (sub-agents); Codex parallelism is *across* tasks (independent containers) — fundamentally different models
- Codex sandbox (no network) is architecturally stronger for security but prevents interaction with local services/APIs
- Pricing crossover: Claude Code Max at $100/mo is cheaper than ChatGPT Pro at $200/mo required for Codex, but Codex is "free" if already on Pro
- Configuration investment compounds: teams with extensive CLAUDE.md/hooks/MCP get increasing returns from Claude Code; teams wanting zero-config benefit from Codex's simplicity
- Codex's ChatGPT integration is double-edged: low barrier to entry but forces context-switching for terminal-native devs

**Action Items:**
- Article references internal links (`/blog/codex-vscode`, `/blog/codex-complete-guide`, `/compare/claude-code-vs-cursor`, `/blog/codex-for-open-source`, `/blog/codex-for-students`) — verify these exist or create them
- Pricing info tagged "as of mid-2026" — will need periodic updates
- Consider ingesting this into wiki as a page on Claude Code vs Codex competitive positioning