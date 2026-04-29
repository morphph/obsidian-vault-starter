# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User working on/reviewing a blog article comparing CLAUDE.md vs Claude Memory in Claude Code's configuration architecture.

**Key Exchanges:**
- Article establishes a clear two-layer model: CLAUDE.md = project layer (shared, version-controlled, team-wide); Memory = user layer (personal, adaptive, individual)
- Trust hierarchy defined: CLAUDE.md wins over Memory when they conflict, because CLAUDE.md goes through code review
- "Memory-to-CLAUDE.md promotion" pattern identified as healthiest interaction between the two systems

**Decisions Made:**
- Decision framework codified: project rules → CLAUDE.md, personal preferences → Memory, derivable-from-code → neither
- CLAUDE.md should describe *what* and *why*, not exhaustive *how* — detailed patterns belong in skills files or code itself
- MEMORY.md index should stay under 200 lines to avoid truncation

**Lessons Learned:**
- Top 5 pitfalls: using CLAUDE.md as personal notepad; ignoring Memory entirely; duplicating project rules in Memory; never updating CLAUDE.md; overloading CLAUDE.md with implementation details
- Memory is local to `.claude/projects/` per working directory — does NOT sync across devices (unlike CLAUDE.md which syncs via git)
- Claude Code verifies Memory records against current reality before acting; CLAUDE.md content is trusted more directly
- Even a 20-line CLAUDE.md listing build commands and key gotchas makes a measurable difference

**Action Items:**
- Article references several internal links (`/blog/claude-code-seven-programmable-layers`, `/blog/9-principles-writing-claude-code-skills`, etc.) — ensure these are published or scheduled before this post goes live
- This content is relevant for wiki pages on [[Claude Code]] tooling and workflows