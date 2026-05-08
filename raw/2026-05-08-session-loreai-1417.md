# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing a blog article about CLAUDE.md vs Claude Memory — when to use each system in Claude Code.

**Key Exchanges:**
- Article defines the boundary: CLAUDE.md = shared, deterministic project rules; Claude Memory = personal, temporal, adaptive context
- The decision test: "If removing it would make Claude worse for **everyone**, CLAUDE.md. If only for **you**, memory."
- Memory files live at `~/.claude/projects/*/memory/` with frontmatter metadata (name, description, type) — file-per-memory design for independent updates
- MEMORY.md index has ~200 line practical limit before truncation
- Memory explicitly excludes: code patterns, architecture details, file paths, git history, debugging solutions derivable from project state

**Decisions Made:**
- CLAUDE.md takes precedence over Memory when they conflict (Memory cannot override CLAUDE.md rules)
- Memory is local-only (`~/.claude/projects/`), not synced across machines — CLAUDE.md syncs via git
- Subdirectory CLAUDE.md files (e.g., `packages/api/CLAUDE.md`) recommended for module-specific rules in larger projects

**Lessons Learned:**
- Start CLAUDE.md minimal (commands, rules, gotchas) — grow organically from real mistakes, not anticipated ones
- Teams using only CLAUDE.md get bloated files with conflicting personal preferences; teams using only Memory get inconsistent conventions
- Best memory types: feedback corrections and reference pointers (prevent repeating yourself across sessions)
- Historical architectural decisions (e.g., "chose Postgres over DynamoDB") belong in CLAUDE.md only if still load-bearing; otherwise Memory

**Action Items:**
- This content is relevant to wiki pages on [[Claude Code]] tooling and workflows — consider ingesting if not already captured