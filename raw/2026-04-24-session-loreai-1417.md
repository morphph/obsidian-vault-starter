# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article about Claude Code's two-layer context system (CLAUDE.md vs Memory) for potential wiki ingestion.

**Key Exchanges:**
- Article explains the CLAUDE.md vs Memory distinction: CLAUDE.md = project-scoped, team-shared, version-controlled; Memory = personal, evolving, conversation-derived
- Rule of thumb for the gray zone: "if you'd put it in a team wiki → CLAUDE.md; if you'd keep it in personal notes → Memory"
- Memory stored at `~/.claude/projects/<path>/memory/`; not synced across devices, not git-tracked by default
- Full context hierarchy: CLAUDE.md (project rules) → Memory (personal context) → SKILL.md (task-specific instructions)

**Decisions Made:**
- None — this was a read-only content review, no actions taken

**Lessons Learned:**
- CLAUDE.md consumes context window at session start; keep it focused on rules/constraints, not documentation. Past a few hundred lines, split into directory-level files or skill files
- Memory auto-save handles most persistence; periodic manual cleanup of `~/.claude/projects/<path>/memory/` prevents drift
- Memory entries accumulating the same correction across multiple devs = signal to promote the rule to CLAUDE.md (Memory as canary for missing project-level instructions)
- CLAUDE.md conflicts with Memory: CLAUDE.md wins (treated as authoritative project rules)

**Action Items:**
- Consider ingesting this article as a raw source (`/ingest`) to build or enrich a `claude-code-context-system.md` wiki page covering the CLAUDE.md ↔ Memory mental model