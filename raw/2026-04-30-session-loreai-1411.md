# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting an article about Claude Memory vs CLAUDE.md — two complementary context systems in Claude Code.

**Key Exchanges:**
- Article explains the architectural difference: CLAUDE.md = shared, version-controlled, deterministic rules (always loaded). Memory = personal, adaptive, contextual preferences (selectively loaded).
- Decision framework for what goes where: build commands, quality gates, coding standards, architecture constraints → CLAUDE.md. Role/expertise, communication preferences, ephemeral project state, workflow feedback → Memory.

**Decisions Made:**
- CLAUDE.md takes priority when it conflicts with Memory (hard constraint vs soft guidance)
- Memory files (`.claude/projects/*/memory/`) should NOT be checked into version control
- Gray area test: "Would a new team member benefit from seeing this on day one?" → yes = CLAUDE.md, no = Memory

**Lessons Learned:**
- Most common mistake: putting team rules in Memory (invisible to teammates) or personal preferences in CLAUDE.md (affects whole team)
- Project-state memories (merge freezes, sprint priorities) go stale fastest — review every few weeks
- Memory works in per-project scopes, so Claude adapts behavior per codebase without managing multiple config files
- In CI/CD (ephemeral contexts), CLAUDE.md works standalone without Memory

**Action Items:**
- Potential wiki page: `claude-code-context-systems.md` covering Memory vs CLAUDE.md architecture, or update existing `claude-code.md` if it exists
- Content references "seven programmable layers" of Claude Code context — worth tracking as a concept