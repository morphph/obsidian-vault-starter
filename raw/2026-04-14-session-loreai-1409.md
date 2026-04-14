# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewed a long-form comparison article: Claude Code vs OpenAI Codex (appears to be a loreai.dev blog post or source document).

**Key Exchanges:**
- No interactive exchanges — this was a document review, not a conversation.

**Decisions Made:**
- N/A (no decisions were made in this session)

**Lessons Learned:**
- **Claude Code vs Codex — core distinction:** Claude Code is interactive + persistent (terminal-based, local execution, memory across sessions); Codex is async + stateless (cloud sandbox, no memory, submit-and-review workflow)
- **Memory:** Claude Code has CLAUDE.md, Skills, auto-memory — compounds over time. Codex starts fresh every task with no equivalent.
- **Execution model:** Claude Code runs locally (code never leaves machine for execution, only API inference crosses network). Codex uploads repo to OpenAI cloud sandbox.
- **Extensibility:** Claude Code has Skills/Hooks/MCP/agent teams — deeply programmable. Codex customization is per-task prompt only.
- **Pricing:** Claude Code = usage-based API tokens (or Max plan flat fee). Codex = included in ChatGPT Pro ($200/mo), Team ($30/user), Enterprise.
- **Best-fit rules:** Claude Code for complex refactors, env-dependent work, unfamiliar codebases, long sessions. Codex for batching well-scoped tasks, teams already on ChatGPT plans, sandboxed execution guarantee.
- **Model note:** Current Codex (2025) ≠ original Codex API (2021, deprecated 2023). Powered by `codex-1` model optimized via RL on coding tasks.

**Action Items:**
- Consider ingesting the source article into `raw/` and creating a `wiki/claude-code-vs-codex.md` page — directly relevant to domain focus (builder tools and workflows).