# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a blog article comparing CLAUDE.md (instruction layer) vs Claude Memory (context layer) in Claude Code.

**Key Exchanges:**
- Article draws a clear architectural distinction: CLAUDE.md = declarative team-wide rules; Claude Memory = accumulated personal context
- Decision rule for gray zone: "If a new team member joining tomorrow needs to know it → CLAUDE.md. If only you need it → Memory."

**Decisions Made:**
- CLAUDE.md wins over Memory when there's a conflict — it is the authoritative instruction layer
- Teams should prioritize CLAUDE.md for consistency; solo devs can lean on Memory with minimal CLAUDE.md

**Lessons Learned:**
- CLAUDE.md failures are visible (wrong build command → build breaks); Memory failures are subtle (slightly miscalibrated behavior, stale assumptions)
- Memory does NOT sync across machines — stored locally under `.claude/projects/*/memory/MEMORY.md`
- Four memory types with different decay rates: *user* (months), *feedback*, *project* (sprint-scale), *reference*
- Neither system is appropriate for secrets — use env vars or secret managers
- Effective CLAUDE.md = specific + actionable (concrete commands, gotchas, API contracts); NOT project descriptions Claude can infer from the codebase
- Memory files are gitignored by default and should stay that way

**Action Items:**
- None noted — article is informational/reference content, likely candidate for ingestion into wiki under a "claude-code-memory-system" or "claude-code-architecture" page