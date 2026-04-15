# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reading/ingesting an article about CLAUDE.md vs Claude Memory in Claude Code — when to use each system.

**Key Exchanges:**
- Article explains the split: CLAUDE.md = objective, team-wide, deterministic instructions ("what" and "how"); Claude Memory = personal, subjective, time-bound context ("who" and "when")
- Key table: CLAUDE.md holds build commands, test rules, framework versions, coding standards; Memory holds user preferences, skill level, merge freezes, ephemeral project state
- Memory is local (`.claude/projects/`), not git-tracked; CLAUDE.md is committed and shared across team and CI/CD

**Decisions Made:**
- If forgetting an instruction causes bugs/broken builds → CLAUDE.md (always loaded, authoritative)
- If an instruction is time-bound or personal → Memory
- CLAUDE.md does NOT get overridden by Memory; CLAUDE.md takes precedence on conflicts
- No duplication: choose one home per rule

**Lessons Learned:**
- Common mistakes: personal prefs in CLAUDE.md, relying on memory for critical rules, stale CLAUDE.md (worse than none), duplicating across both systems, putting ephemeral context in CLAUDE.md
- CLAUDE.md recommended limit: under 200 lines — longer files waste context window
- Memory doesn't persist in CI/CD (clean filesystem); CLAUDE.md does since it's repo-tracked
- Signal to move to CLAUDE.md: repeating same instructions across sessions; signal to use Memory: Claude keeps forgetting a personal correction

**Action Items:**
- Article source appears to be from LoreAI blog (`/blog/claude-code-memory`) — worth ingesting as `raw/` source if not already done
- Review current CLAUDE.md against the "common mistakes" checklist (e.g., check for ephemeral context, personal prefs, stale commands)