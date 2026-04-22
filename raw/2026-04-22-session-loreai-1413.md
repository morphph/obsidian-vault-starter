# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewed a detailed article comparing Claude Code's CLAUDE.md vs Claude Memory systems — likely for potential wiki ingestion.

**Key Exchanges:**
- Article covers how CLAUDE.md (project-level, git-tracked) and Claude Memory (local, personal, conversation-derived) serve different but complementary roles in Claude Code sessions
- CLAUDE.md loads first as hard rules/constraints; Memory supplements but never overrides it
- Memory stored at `~/.claude/projects/<project>/memory/` — local only, does not sync across devices or team members

**Decisions Made:**
- Clear decision rule from article: *"If you'd put it in a README, put it in CLAUDE.md. If you'd tell a colleague verbally, let memory handle it."*
- CLAUDE.md wins on conflicts with Memory — it's authoritative

**Lessons Learned:**
- CLAUDE.md = shared, deterministic, rule-based (build commands, coding standards, architecture constraints, known gotchas)
- Claude Memory = personal, adaptive, conversation-derived (preferences, role context, feedback accumulation, ephemeral project state)
- Anti-pattern: duplicating info across both systems
- Stale memories can waste context window; audit when something feels off
- Practical CLAUDE.md size: 20–200+ lines; every line costs tokens at session start
- To promote memory → CLAUDE.md: copy rule, delete memory file + MEMORY.md entry

**Action Items:**
- Article ends with a CTA to LoreAI (`/subscribe`) — potential ingest candidate if raw source not already in `raw/`
- Consider ingesting this article as a raw source for a wiki page on `claude-code-memory-vs-claudemd.md`