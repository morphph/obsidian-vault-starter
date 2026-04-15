# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article ingested or reviewed explaining CLAUDE.md vs Claude Memory — when to use each, how they interact.

**Key Exchanges:**
- Detailed breakdown of CLAUDE.md (static, team-shared, git-versioned) vs Claude Memory (dynamic, per-user, evolves conversationally)
- CLAUDE.md hierarchy: global (`~/.claude/CLAUDE.md`) → project root → subdirectory
- Memory types: User, Feedback, Project, Reference — each with different trigger conditions and shelf lives

**Decisions Made:**
- Clear heuristic: "If a new team member needs to know it → CLAUDE.md. If it's about how Claude should interact with *you* specifically → Memory."
- Memory files live in `.claude/projects/{hash}/memory/` — plain markdown, NOT committed to git
- CLAUDE.md belongs in repo root, IS committed

**Lessons Learned:**
- Memory capped at 200-line index in context; don't store code patterns/file paths in Memory — Claude reads codebase directly
- Memory doesn't sync across devices; CLAUDE.md does (via git)
- Common failure mode: putting personal preferences in project CLAUDE.md (affects all team members) or relying on Memory for team-critical rules (only affects your sessions)
- Project memories have shortest shelf life — verify against current state before acting

**Action Items:**
- If this article is from a raw source, consider ingesting it as a wiki page on `claude-code-memory-system.md` or similar, cross-linked with existing Claude Code tooling pages