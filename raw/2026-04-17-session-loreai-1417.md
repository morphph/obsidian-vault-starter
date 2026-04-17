# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing article content about CLAUDE.md vs Claude Memory — comparing the two persistence mechanisms in Claude Code.

**Key Exchanges:**
- Article covers: CLAUDE.md (stable, team-shared, version-controlled rules) vs Claude Memory (personal, contextual, auto-accumulating)
- CLAUDE.md has fixed token cost (loaded every turn); Memory has variable cost (index always loaded, detail files loaded on demand)
- Core decision rule: **if it's a rule → CLAUDE.md; if it's context → Memory**

**Decisions Made:**
- CLAUDE.md acts as authoritative source; memory yields to it when they conflict
- Keep project-level CLAUDE.md under 100 lines of actionable instructions
- Memory → CLAUDE.md promotion signal: telling multiple team members the same thing
- CLAUDE.md → Memory demotion signal: file growing past 100 lines with quarter-specific context

**Lessons Learned:**
- CLAUDE.md staleness is *visible* (readable file); Memory staleness is *hidden* (only individual user encounters it)
- SKILL.md files are a third tier — loaded on demand, sit between always-loaded CLAUDE.md and contextually-loaded memory
- Claude Memory is local only (`.claude/projects/`) — not synced across machines; CLAUDE.md follows the repo
- Hooks enforce CLAUDE.md rules deterministically; memory influences behavior subtly

**Action Items:**
- This article appears to be a candidate for ingestion into the wiki (topic: Claude Code memory systems / CLAUDE.md architecture)
- Possible wiki page: `claude-code-memory-vs-claudemd.md` under builder tools domain