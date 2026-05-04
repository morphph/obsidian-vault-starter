# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a detailed article about Claude Memory vs CLAUDE.md — the two persistence mechanisms in Claude Code and when to use each.

**Key Exchanges:**
- Claude Code has a **three-layer persistence stack**: CLAUDE.md (always-on project rules), SKILL.md (task-specific, on-demand), and Memory (personal/temporal, index + detail files)
- Memory uses a two-tier structure: `MEMORY.md` index (≤200 lines, loaded every session) → individual `.md` files read on demand
- Memory types: user, feedback, project, reference
- CLAUDE.md hierarchy: global `~/.claude/CLAUDE.md` → project-level `CLAUDE.md` (project overrides global)

**Decisions Made:**
- **CLAUDE.md for team-wide, stable rules** (build commands, coding standards, architecture, quality gates) — version controlled, loaded every session
- **Memory for personal/temporal context** (role, preferences, corrections, deadlines, external refs) — local only, not synced across machines
- **SKILL.md for task-specific instructions** — version controlled but only loaded when invoked
- CLAUDE.md takes precedence over Memory when they conflict

**Lessons Learned:**
- CLAUDE.md bloat is a real problem — consumes context window every session; move task-specific stuff to SKILL.md
- Memory files live in `~/.claude/projects/`, are NOT synced between machines (unlike CLAUDE.md via git)
- Don't store code-derivable info in Memory (file structure, function signatures) — Claude can read the code
- Don't put personal preferences in shared CLAUDE.md
- Ignoring Memory entirely means repeating corrections every session
- Stable memories should be promoted to CLAUDE.md entries over time

**Action Items:**
- Potential wiki pages: `claude-code-memory-system.md`, update `claude-code.md` if it exists with persistence stack details
- Key reference links from article: `/blog/claude-code-memory`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/9-principles-writing-claude-code-skills`