# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a blog post comparing CLAUDE.md vs Claude Memory as context mechanisms in Claude Code.

**Key Exchanges:**
- Article provides a comprehensive framework for deciding where to put AI context: CLAUDE.md (shared rules) vs Claude Memory (personal context)

**Decisions Made:**
- **CLAUDE.md = constitution; Memory = institutional knowledge.** CLAUDE.md is for deterministic, team-wide directives. Memory is for personal preferences, corrections, and ephemeral state.
- **Priority hierarchy:** CLAUDE.md always overrides Memory when they conflict. CLAUDE.md itself has three levels (Global → Project → Directory), Memory has two (Global → Project).
- **Decision rule:** If info must be consistent across all developers → CLAUDE.md. If personal, evolving, or too granular → Memory. When in doubt, start with Memory and promote to CLAUDE.md if repeated.

**Lessons Learned:**
- Memory can go stale; Claude Code treats memories as hints and verifies against current state before acting. CLAUDE.md entries are treated as absolute directives — no verification needed.
- Memory files (`.claude/projects/`) should never be committed to the repo — they're per-user personal context.
- Memory serves as a "staging area" for patterns that might deserve promotion to team-wide CLAUDE.md rules.
- Skills files sit as a third layer between CLAUDE.md (project-wide) and Memory (personal), providing task-specific instructions.

**Action Items:**
- Consider ingesting this article into `raw/` and creating/updating wiki pages on Claude Code workflows, CLAUDE.md best practices, and Claude Memory system
- Cross-reference with existing wiki content on Claude Code's seven programmable layers and skills authoring