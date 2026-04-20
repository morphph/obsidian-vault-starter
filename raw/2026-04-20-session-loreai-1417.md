# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Content piece about CLAUDE.md vs Claude Memory — explaining their distinct roles in Claude Code setups.

**Key Exchanges:**
- Article distinguishes CLAUDE.md (project operating manual: deterministic, shared, version-controlled) from Claude Memory (personal context layer: learned preferences, auto-managed, not git-tracked)
- Key analogy: "CLAUDE.md is the constitution, Memory is case law"

**Decisions Made:**
- CLAUDE.md takes precedence over Memory when they conflict — Memory cannot override explicit project rules
- Memory files belong in `.claude/` (gitignored), never checked into git; CLAUDE.md is the team-shared file

**Lessons Learned:**
- Claude Memory is fully automatic — no manual setup required; Claude creates and updates it from conversation
- For teams, CLAUDE.md is non-negotiable for consistent AI behavior across developers
- SKILL.md files are task-specific workflows ("how we do this type of task"), distinct from CLAUDE.md ("how we work on this project") — both are git-tracked and shared
- If memory conflicts with CLAUDE.md, Claude should follow CLAUDE.md and discard the stale memory

**Action Items:**
- Consider ingesting this as a raw source on Claude Code architecture (CLAUDE.md vs Memory distinction) — useful reference for the wiki's "Builder tools and workflows" domain