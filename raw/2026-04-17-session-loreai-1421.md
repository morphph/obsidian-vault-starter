# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reading an article about Claude Memory vs CLAUDE.md — when to use each, team dynamics, and common misuse patterns.

**Key Exchanges:**
- Article from LoreAI/similar source explaining the boundary between CLAUDE.md (shared project config) and Claude Memory (personal/temporal context)

**Decisions Made:**
- N/A (passive reading session, no decisions made in this repo)

**Lessons Learned:**
- **CLAUDE.md = project constitution**: version-controlled, team-wide, deterministic. Use for build commands, quality gates, architecture rules, naming conventions.
- **Claude Memory = personal notebook**: private, auto-maintained, per-developer. Use for personal preferences, temporal info (deadlines, project status), corrective feedback from past sessions.
- **The rule of thumb**: if removing it would break another team member's workflow → CLAUDE.md. If only affects your experience → Memory.
- CLAUDE.md consumes context window on every session — keep under 150–200 lines; move task-specific instructions to skill files.
- Memory is scoped per-project (`~/.claude/projects/<hash>/memory/`); user-type memories (role, style) carry across projects.
- Common anti-pattern: duplicating the same rule in both systems → when one gets updated, the other goes stale and causes contradictions.
- Memory entries can go stale (e.g. "merge freeze April 5" is wrong on April 15) — verify against current state before acting.
- CLAUDE.md must be **manually maintained** — treat updates as part of definition of done, same PR as the change it documents.

**Action Items:**
- Consider ingesting this article into `raw/` and creating a wiki page on `claude-code-memory-vs-claudemd.md` covering the mental model, use cases, and anti-patterns.