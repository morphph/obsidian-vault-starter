# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a blog article on CLAUDE.md vs Claude Memory persistence layers in Claude Code.

**Key Exchanges:**
- Comprehensive framework for deciding what goes in CLAUDE.md (team rules, build commands, architecture constraints) vs Memory (personal preferences, temporal context, feedback corrections)
- Three-question test for placement: Would a new team member need this? Is it about me or the project? Does it expire?

**Decisions Made:**
- CLAUDE.md is the **team rulebook** (deterministic, shared, version-controlled); Memory is **personal context** (automatic, individual, adaptive)
- CLAUDE.md wins over Memory when they conflict — team rules take precedence over personal preferences
- Memory files should NOT be checked into git; `.claude/` is gitignored by design
- CLAUDE.md should stay under 200 lines — link to separate docs for extensive content

**Lessons Learned:**
- CLAUDE.md staleness = low-risk but high-impact (wrong instructions applied deterministically to all devs). Fix: treat CLAUDE.md updates as part of code change process
- Memory staleness = high-risk but low-impact (stale context degrades quality gradually). Fix: periodic review of MEMORY.md index
- Anti-patterns: duplicating CLAUDE.md rules in memory, putting ephemeral task context in CLAUDE.md, ignoring Memory entirely, overloading CLAUDE.md with background context
- Session startup loads: global `~/.claude/CLAUDE.md` → project `CLAUDE.md` → relevant memories — this layering is how team rules + personal context compose

**Action Items:**
- Article references other posts: "5 Claude Code Skills I Use Every Single Day", "how to effectively prompt Claude Code", "what's so special about Claude Code" — ensure wiki cross-links exist
- Article ends with `/subscribe` CTA for LoreAI — confirms this is publication-ready draft content