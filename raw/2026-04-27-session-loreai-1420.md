# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reading/reviewing a blog article explaining Claude Memory vs CLAUDE.md — how each system works, precedence rules, and when to use which.

**Key Exchanges:**
- Article explains CLAUDE.md is loaded once at session start as authoritative project-level instructions; Memory is selective — only relevant memories surface per task
- CLAUDE.md is version-controlled, shared across team via git; Memory is local, per-user, not synced
- Precedence order: System instructions → CLAUDE.md → Skill files → Memory → Conversation context
- Memory has a built-in freshness check (Claude verifies claims against current code state before acting); CLAUDE.md is trusted directly with no verification step
- Global `~/.claude/CLAUDE.md` exists as per-user personal CLAUDE.md with project-level authority — sits above Memory but scoped to the individual

**Decisions Made:**
- N/A (article review, no decisions made in session)

**Lessons Learned:**
- Common mistake: treating Memory and CLAUDE.md as alternatives rather than complementary layers
- CLAUDE.md for: build commands, quality gates, architecture rules, team conventions — anything deterministic and team-wide
- Memory for: role/expertise, communication preferences, corrections, personal workflow, external system references (Linear, Slack, Grafana)
- Memory index (`MEMORY.md`) is truncated after 200 lines — keep it lean, prune regularly
- If something is in CLAUDE.md, don't duplicate it in Memory and vice versa

**Action Items:**
- Consider ingesting this article into `raw/` and creating a wiki page on `claude-code-context-systems.md` covering CLAUDE.md vs Memory distinction — highly relevant to the builder tools domain