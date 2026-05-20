# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing an article comparing CLAUDE.md vs Claude Memory for the LoreAI blog/wiki.

**Key Exchanges:**
- Detailed breakdown of CLAUDE.md (declarative project rules, team-shared, git-tracked) vs Memory (accumulated personal context, local, auto-maintained)
- Analysis of team collaboration patterns: CLAUDE.md = shared "what," Memory = personal "who"
- Maintenance models differ: stale CLAUDE.md causes wrong behavior; stale Memory causes slightly off context — CLAUDE.md accuracy matters more

**Decisions Made:**
- **Combined approach is the recommendation:** CLAUDE.md for project layer (build/test/lint, style rules, architecture, workflows, skills/hooks), Memory for personal layer (role, preferences, feedback, sprint context, external system refs)
- **Practical test for placement:** "If you delete it, would another team member need it?" → CLAUDE.md. Personal workflow? → Memory.
- **Memory should NOT be checked into git** — mixing personal preferences with team config causes conflicts
- **CLAUDE.md has ~80% behavioral impact** (mandatory rules), Memory fine-tunes ~20% (tone, depth, approach)

**Lessons Learned:**
- Memory doesn't sync across machines — critical context needed everywhere should go in CLAUDE.md
- CLAUDE.md serves as the integration point for the extension stack (skills, hooks, MCP) — Memory doesn't play this role
- Best teams treat CLAUDE.md updates as part of the PR process: change the build system → update CLAUDE.md in the same commit
- Memory is better for frequently-changing info (sprint goals, incident status) since it updates conversationally vs requiring file edit + commit

**Action Items:**
- Article references `/blog/claude-code-memory` and `/blog/5-claude-code-skills-i-use-every-single-day` — ensure wiki pages exist for cross-linking
- Consider creating a wiki page on Claude Code configuration best practices synthesizing this analysis
- FAQ section could seed a standalone wiki page on CLAUDE.md vs Memory