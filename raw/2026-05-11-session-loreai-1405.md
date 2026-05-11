# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Claude Code vs OpenAI Codex — a detailed feature-by-feature comparison for the LoreAI blog.

**Key Exchanges:**
- Article covers architecture differences (local/sync vs remote/async), programmability, security models, pricing, IDE integration, and use-case recommendations
- Claude Code: terminal-native, local execution, real-time pair-programming, deep extension stack (CLAUDE.md, SKILL.md, hooks, MCP, agent teams)
- Codex: cloud sandbox, async PR-based delivery, parallel task execution, bundled into ChatGPT subscriptions

**Decisions Made:**
- Verdict framing: tools are **complementary, not competing** — different points on control-vs-delegation spectrum
- Claude Code wins on: control, customization, environmental access, complex tasks
- Codex wins on: async throughput, security isolation, batch well-scoped tasks, free tiers (OSS/students)
- Pricing comparison: Claude Code is token-based/Max ($100-200/mo heavy); Codex bundled in ChatGPT Pro ($200/mo)

**Lessons Learned:**
- Codex has **no equivalent to CLAUDE.md/SKILL.md programmability** — relies on repo context and prompts only
- Codex sandbox = no network access during execution → safer but can't reach local services/DBs
- Claude Code agent teams partially close the concurrency gap but remain interactive
- Quality depends more on task scoping than tool choice; ambiguous tasks favor Claude Code's interactive loop
- Many teams will pragmatically use both tools for different task types

**Action Items:**
- Article references several internal links (`/blog/claude-code-agent-teams`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/compare/claude-code-vs-cursor`, etc.) — verify these exist or create them
- Article references `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/blog/codex-vscode` — these may need wiki pages for the underlying facts
- Consider ingesting this into wiki as a page on `claude-code-vs-codex.md` once finalized
- Cross-reference with existing wiki pages on [[Claude Code]] and [[Codex]] if they exist