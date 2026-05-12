# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a reference article on Claude Code's two persistence layers — CLAUDE.md vs Claude Memory — and when to use each.

**Key Exchanges:**
- Article explains the precedence hierarchy: CLAUDE.md (project rules) always overrides Memory (personal preferences) when they conflict
- Memory files live in `.claude/projects/<hash>/memory/`, are local-only, not synced across devices, and should NOT be committed to git
- CLAUDE.md supports nested directory-level overrides (e.g., `packages/api/CLAUDE.md`)

**Decisions Made:**
- **Durability heuristic:** If removing it breaks the build or violates team standards → CLAUDE.md. If removing it just makes Claude Code less helpful for you → Memory.
- **Temporal vs structural:** Durable architectural facts go in CLAUDE.md; time-sensitive context (sprint goals, deadlines, incident status) goes in Memory.
- **Starting from zero:** Write CLAUDE.md first; Memory builds itself from conversation corrections over time.

**Lessons Learned:**
- Memory index (`MEMORY.md`) truncates after 200 lines — quality over quantity; 20 focused memories beat 100 stale ones
- Common mistake: teams putting personal preferences in CLAUDE.md (creates friction) or project-critical instructions in Memory (doesn't propagate to teammates)
- Memory entries should be periodically pruned; stale project memories waste context and can mislead
- Periodically review Memory and migrate team-relevant patterns into CLAUDE.md via PR, then delete the Memory entry to avoid duplication

**Action Items:**
- Consider ingesting this as a wiki page under Claude Code tooling/workflow knowledge (relates to [[claude-code]] builder tools domain)
- Cross-reference with any existing wiki pages on Claude Code's programmable layers or extension stack