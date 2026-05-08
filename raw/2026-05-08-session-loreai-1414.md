# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting an article about CLAUDE.md vs Claude Memory — when to use each persistence layer in Claude Code.

**Key Exchanges:**
- CLAUDE.md is a **shared team resource** — version-controlled, goes through code review, inherited by every developer who clones the repo
- Memory is a **personal resource** — local to `~/.claude/projects/`, stores individual expertise, preferences, corrections, and working context
- Decision rule: "If removing the info would hurt a teammate's Claude Code experience → CLAUDE.md. If it only affects yours → Memory."

**Decisions Made:**
- CLAUDE.md ideal size: 50–150 lines of actionable instructions; split into directory-level files if >200 lines
- CLAUDE.md takes precedence over Memory when they conflict (e.g., CLAUDE.md says Jest, Memory says Vitest → Jest wins)
- Memory does NOT sync across machines; CLAUDE.md syncs via git
- Stable recurring Memory corrections should be **promoted** to CLAUDE.md

**Lessons Learned:**
- Common mistake: putting personal preferences in CLAUDE.md, or putting critical team rules only in Memory
- Don't duplicate info across both systems — Memory is designed to skip what's already in CLAUDE.md
- Don't pre-populate Memory; let it grow organically from real conversations and corrections
- Stale memories cause outdated context application — periodic review needed
- SKILL.md files are a third mechanism: reusable task-specific instructions (distinct from project-wide CLAUDE.md rules)

**Action Items:**
- Consider ingesting this as a wiki page (e.g., `wiki/claude-code-persistence-layers.md`) — it documents a core workflow pattern for Claude Code usage
- Cross-reference with existing wiki pages on [[Claude Code]] if they exist