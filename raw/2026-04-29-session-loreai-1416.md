# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a blog post about CLAUDE.md vs Claude Memory — when to use each system for Claude Code context management.

**Key Exchanges:**
- CLAUDE.md = deterministic, version-controlled, team-shared layer (build commands, coding standards, architecture constraints)
- Memory = adaptive, personal, automatic layer (user profile, feedback corrections, transient project status)
- Rule: "If everyone on the team needs it → CLAUDE.md. If only you need it → Memory."

**Decisions Made:**
- Both systems are complementary, not alternatives — use both
- CLAUDE.md is the "floor" (shared foundation); Memory is the "ceiling" (personalized intelligence)
- Memory should NOT be checked into version control
- Configuration priority order: Global CLAUDE.md → Project CLAUDE.md → Subdirectory CLAUDE.md → Memory files → Conversation context

**Lessons Learned:**
- Anti-pattern: Dumping everything into CLAUDE.md (grows unwieldy, contains noise irrelevant to most team members)
- Anti-pattern: Ignoring Memory (missing personalization; repeating same corrections across sessions = signal Memory should capture it)
- Anti-pattern: Duplicating content across both systems (maintenance burden + conflicts)
- Anti-pattern: Never cleaning up Memory (stale project status entries become actively misleading)
- Memory files live at `~/.claude/projects/` as plain markdown with frontmatter — manually editable
- Memory doesn't override CLAUDE.md rules; it personalizes *within* those constraints

**Action Items:**
- Potential wiki page: `claude-code-context-management.md` covering CLAUDE.md vs Memory distinction
- Could cross-reference with existing Claude Code / builder tools pages
- Monthly memory cleanup cadence recommended for stale entries