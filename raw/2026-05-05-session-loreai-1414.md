# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/reference content about CLAUDE.md vs Claude Memory in Claude Code — how the two context systems differ and complement each other.

**Key Exchanges:**
- Complete feature comparison between CLAUDE.md (deterministic, version-controlled, team-shared) and Memory (adaptive, personal, emergent)
- Claude Code's context loading order: System prompt → User CLAUDE.md → Project CLAUDE.md → Memory index → Individual memory files

**Decisions Made:**
- CLAUDE.md = "constitution" (hard rules); Memory = "institutional knowledge" (soft context)
- CLAUDE.md takes priority when it conflicts with Memory
- Memory is gitignored by default; lives at `.claude/projects/<id>/memory/`
- Three-layer approach recommended: project CLAUDE.md + Memory + user-level `~/.claude/CLAUDE.md`

**Lessons Learned:**
- Don't put personal preferences in project CLAUDE.md (forces them on team)
- Don't put project rules in Memory (not shared with new members)
- Don't use Memory for code patterns discoverable from the codebase itself
- Memory should store things that **can't be derived** from current code: decisions, preferences, external refs, rationale
- Update CLAUDE.md in the same PR that introduces the change it documents
- Memory doesn't sync across devices (local filesystem only)

**Action Items:**
- This content maps to a wiki page (e.g., `wiki/claude-md-vs-memory.md`) covering Claude Code's dual context system
- Cross-references needed: links to Claude Code page, possibly MCP/skills/hooks pages
- The article references several internal blog links (`/blog/claude-code-seven-programmable-layers`, `/blog/claude-code-memory`, etc.) — these represent potential future wiki pages or raw sources to ingest