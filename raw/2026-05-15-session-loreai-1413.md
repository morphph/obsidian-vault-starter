# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Researching/drafting content comparing Claude Memory vs CLAUDE.md persistence systems in Claude Code.

**Key Exchanges:**
- Detailed architectural comparison: CLAUDE.md is loaded unconditionally as instructions; Memory is loaded conditionally as context
- CLAUDE.md loading is deterministic and hierarchical (home → parent dirs → project root → .claude/), with more specific files taking precedence
- Memory uses index-based selective loading — MEMORY.md index always loaded (~200 lines cap), individual files loaded only when judged relevant

**Decisions Made:**
- **"If removing it would break the team, it's CLAUDE.md. If only you, it's memory."** — core decision heuristic
- CLAUDE.md should stay under 500 lines; overflow goes to skill files loaded on-demand
- Memory files should NOT be git-tracked (personal, would conflict across team members)
- Treat CLAUDE.md like production code — update in same PR that changes the convention it documents

**Lessons Learned:**
- CLAUDE.md staleness is high-risk because stale rules are still followed; stale memory is low-risk because it's treated as context and may be ignored
- Common mistake: putting personal preferences in CLAUDE.md (e.g., "explain changes before making them") — annoys teammates, belongs in memory
- Common mistake: putting critical team rules only in memory — gets forgotten, belongs in CLAUDE.md
- Memory has four types with different lifespans: `user` and `feedback` (long-lived), `project` (decays), `reference` (pointers)
- Memory cannot override CLAUDE.md — CLAUDE.md always takes precedence on conflicts
- Memory does NOT sync across devices; CLAUDE.md syncs via git

**Action Items:**
- Consider quarterly CLAUDE.md audits and monthly memory reviews as maintenance hygiene
- Pattern: promote recurring feedback memories to CLAUDE.md rules when they apply team-wide, then delete the memory to avoid duplication