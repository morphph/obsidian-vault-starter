# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comprehensive article on CLAUDE.md vs Claude Memory configuration patterns in Claude Code.

**Key Exchanges:**
- Article covers the two-system architecture: CLAUDE.md (shared, explicit, stable project rules) vs Memory (personal, learned, evolving context)
- Detailed breakdown of what belongs where, with anti-patterns for each

**Decisions Made:**
- CLAUDE.md: team-wide stable rules — build commands, quality gates, coding conventions, architectural constraints. Keep under 200 lines.
- Memory: personal evolving context — role, preferences, corrections, project status, current focus areas.
- Neither system should store info derivable from code itself (file paths, function signatures, git history).
- CLAUDE.md takes precedence when the two contradict.

**Lessons Learned:**
- Overloading CLAUDE.md (500+ lines) dilutes critical instructions — move task-specific instructions to Skill files
- Duplicating content across both systems creates maintenance risk when rules change
- Volatile info (sprint goals, blockers, deploy schedules) belongs in Memory, not CLAUDE.md
- If the same Memory correction keeps appearing across team members, migrate it to CLAUDE.md
- Solo devs still benefit from separation: CLAUDE.md for rules you'd want in 6 months, Memory for current context
- Skills handle task-scoped instructions ("when writing newsletters, use this tone"); Hooks enforce what CLAUDE.md can only request

**Action Items:**
- This content is suitable for a wiki page (e.g., `claude-code-memory-vs-claude-md.md`) covering Claude Code configuration best practices
- Could cross-reference with existing wiki pages on [[Claude Code]] tooling and workflows