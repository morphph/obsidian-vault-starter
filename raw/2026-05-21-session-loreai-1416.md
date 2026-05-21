# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/content about CLAUDE.md vs Claude Memory in Claude Code — comparing when to use each system.

**Key Exchanges:**
- CLAUDE.md = project-level, version-controlled, shared via git; Memory = personal, per-user, auto-accumulated
- Claude Code context loading order: Global CLAUDE.md → Project CLAUDE.md → Auto-memory → Subdirectory CLAUDE.md files
- CLAUDE.md takes priority over Memory when instructions conflict

**Decisions Made:**
- If forced to choose one: start with CLAUDE.md — shared project context prevents more errors than personal preferences optimize
- Decision framework: "everyone needs to know X" → CLAUDE.md; "Claude should treat me differently" → Memory; "never do X in this codebase" → CLAUDE.md; "ongoing sprint context" → Memory

**Lessons Learned:**
- Common mistake: putting personal preferences in project CLAUDE.md (affects whole team unnecessarily)
- Common mistake: relying on Memory for critical rules (it's per-user and clearable — not reliable for enforcement)
- Common mistake: duplicating instructions across both systems (creates drift)
- CLAUDE.md limitation: static file requiring manual maintenance; Memory limitation: personal/local, doesn't help new team members
- CLAUDE.md is Claude Code-specific — no effect in claude.ai web UI or raw API
- Memory files stored at `~/.claude/projects/<project-hash>/memory/` as markdown

**Action Items:**
- Potential wiki page: `claude-code-context-system.md` covering CLAUDE.md + Memory architecture, loading order, and best practices
- This content references several related blog posts (claude-code-complete-guide, claude-code-memory, claude-code-extension-stack, etc.) — worth ingesting if not already in wiki