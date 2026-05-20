# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article — Codex custom agents vs Claude Code subagents.

**Key Exchanges:**
- Full feature comparison between Codex custom agents (cloud, sandboxed, fire-and-forget) and Claude Code subagents (local, typed, orchestrated)
- Execution model analysis: Codex = async cloud containers with no internet; Claude Code = local terminal with full environment access
- Multi-agent coordination: Codex agents are isolated (no inter-agent communication); Claude Code supports parent-session orchestration with parallel spawning and `SendMessage` continuation

**Decisions Made:**
- Article verdict: recommend **using both** — Codex for batch/well-defined tasks, Claude Code for interactive/complex orchestration. They're complementary, not competing.
- Framing around "autonomy-vs-control spectrum" as the organizing principle

**Lessons Learned:**
- Codex custom agents: strength is simplicity (define once, delegate many); limitation is rigidity (static templates, no mid-run adaptation, no sub-task spawning)
- Claude Code subagents: strength is orchestration (typed agents, SKILL.md inheritance, parallel spawning, session context); limitation is upfront investment in writing good SKILL.md files
- Claude Code's `run_in_background: true` can approximate Codex's async model, but session must stay active
- Practical parallel agent sweet spot: 2–5 concurrent agents before coordination overhead outweighs gains
- Codex = flat-rate (ChatGPT Pro/Team); Claude Code = usage-based API billing. Cost winner depends on volume.
- Claude Code subagents inherit MCP server config, hooks, and memory from parent session automatically

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — verify these exist or are planned
- Consider ingesting this article into `raw/` and creating/updating wiki pages for `codex.md`, `claude-code-subagents.md`, and possibly `agentic-coding.md`