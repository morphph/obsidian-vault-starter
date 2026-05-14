# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a blog article comparing Claude Memory vs CLAUDE.md — their roles, priority hierarchy, and when to use each.

**Key Exchanges:**
- Article defines a clean mental model: **CLAUDE.md is imperative** (rules, commands, constraints — "contributing guide" material); **Memory is declarative** (facts, preferences, situational context — "what you'd tell a new pair-programming partner")
- Claude Code context stack priority order: System prompt → Global CLAUDE.md → Project CLAUDE.md → Subdirectory CLAUDE.md → Memory index → Individual memory files → Conversation context
- CLAUDE.md wins all conflicts with Memory — it's authoritative; Memory is supplementary

**Decisions Made:**
- **CLAUDE.md = version-controlled, shared, deterministic**; Memory = local, personal, accumulated. Neither replaces the other.
- Start with CLAUDE.md if forced to prioritize — gives 80% of needed context with zero warm-up. Memory fills the remaining 20%.
- Personal cross-project preferences go in global `~/.claude/CLAUDE.md`; project-specific preferences that benefit all contributors go in project CLAUDE.md; personal/temporal context goes in Memory.

**Lessons Learned:**
- Memory doesn't sync across machines — each device builds independent memory. CLAUDE.md syncs via git.
- Stale memories can cause unexpected Claude behavior — review every few weeks.
- Teams that skip CLAUDE.md and rely only on Memory end up repeating the same corrections every session, and those corrections never propagate to teammates.
- When debugging unexpected Claude behavior: check CLAUDE.md first (forgotten rule?), then Memory (stale correction?).

**Action Items:**
- Article references several internal links (`/blog/claude-code-memory`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/5-claude-code-skills-i-use-every-single-day`) — potential candidates for future `/ingest` if not already in wiki.