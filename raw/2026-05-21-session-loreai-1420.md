# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting an article comparing Claude Memory vs CLAUDE.md — two context systems in Claude Code.

**Key Exchanges:**
- Article covers the full taxonomy: CLAUDE.md (project-scoped, version-controlled, shared), Claude Memory (user-scoped, auto-saved, personal)
- Claude Code's extension stack layering: **hooks for hard rules, CLAUDE.md for project guidance, memory for personal tuning, skills for task-specific instructions**

**Decisions Made:**
- Decision rule for where context belongs: "Does this apply to every developer, or just me?" Everyone → CLAUDE.md. Just you → Memory.
- CLAUDE.md takes precedence over Memory when they conflict (project config > personal context)
- Claude Memory is local-only (`~/.claude/projects/`), does NOT sync across machines
- Recommended adoption order for teams: CLAUDE.md first (higher leverage), then let memory accumulate

**Lessons Learned:**
- CLAUDE.md hierarchy merges automatically: global (`~/.claude/CLAUDE.md`) → project root → subdirectory — no need to repeat global rules
- Memory auto-save is useful but requires periodic curation (monthly MEMORY.md review recommended)
- Redundancy between layers creates confusion, not reinforcement — pick one authoritative layer per piece of context
- Hooks are independent of both systems — they execute deterministically regardless of CLAUDE.md or memory content
- Skills interact with CLAUDE.md (inherit project constraints), Memory interacts with conversational behavior (adjusts communication style)

**Action Items:**
- Potential `/ingest` candidate: this article covers Claude Code architecture patterns relevant to the wiki's "Builder tools and workflows" domain (Claude Code, MCP, pipelines)
- Wiki pages that could be created/updated: `claude-code-context-systems.md`, updates to existing `claude-code.md` if it exists