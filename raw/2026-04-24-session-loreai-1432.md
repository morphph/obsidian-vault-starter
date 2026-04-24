# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article comparing Claude Code vs Codex CLI across workflow, architecture, safety, and pricing dimensions.

**Key Exchanges:**
- Article covers Claude Code vs Codex CLI across: configuration depth, sync/async workflow, multi-agent execution, safety models, pricing, and IDE integration.

**Decisions Made:**
- No decisions were made — this was a passive review of article content, not an active working session.

**Lessons Learned:**
- **Claude Code config stack**: CLAUDE.md + SKILL.md + hooks + MCP = programmable platform. Codex CLI config is simpler/instructional only (agents.md or codex.md).
- **Sync vs async**: Claude Code = real-time pair programming with interruption; Codex = fire-and-forget async, submit + review PR later.
- **Multi-agent**: Claude Code spawns coordinated sub-agents sharing local env + git worktrees; Codex tasks are independent sandboxes, cannot coordinate.
- **Safety**: Codex safe by isolation (cloud sandbox, no local access); Claude Code safe by layered permissions (configurable, requires setup).
- **Pricing**: Codex bundled with ChatGPT Plus/Pro ($20/$200/mo); Claude Code is usage-based API tokens (pay per use, no subscription).
- **Practical combo**: Claude Code for active current task; Codex for backlog batch tasks running in parallel.

**Action Items:**
- Consider ingesting this comparison article into `raw/` as a source for a `claude-code-vs-codex.md` wiki page covering the tool comparison landscape.