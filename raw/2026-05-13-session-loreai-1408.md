# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting content about Claude Code's CLAUDE.md vs Memory system — best practices for when to use each.

**Key Exchanges:**
- Content explains the two-layer system: CLAUDE.md (project governance, deterministic, team-shared) vs Memory (personal adaptation, accumulated context)
- Decision rule: **project-intrinsic → CLAUDE.md; personal/state → Memory**

**Decisions Made:**
- CLAUDE.md takes strict precedence over Memory in all conflict cases — Memory cannot override CLAUDE.md rules
- For teams, CLAUDE.md is non-negotiable; for individuals, Memory alone can suffice; for serious use, both together is optimal
- Migration path: review MEMORY.md, move project-intrinsic entries (build commands, standards, gotchas, architecture) to CLAUDE.md, keep personal preferences in Memory, delete duplicates

**Lessons Learned:**
- Stuffing personal preferences into CLAUDE.md clutters the team instruction set
- Encoding build commands into Memory is fragile and unauditable
- Memory entries are created automatically from conversations — explicit "remember this" is rarely needed
- CLAUDE.md is Claude Code–specific; other AI tools don't read it, but the practice of a project instruction file is broadly useful
- Only repo-root CLAUDE.md is shared via git; `~/.claude/CLAUDE.md` and `.claude/CLAUDE.md` are private

**Action Items:**
- This content is relevant to the wiki under Claude Code / builder tools — could update or create a wiki page on Claude Code configuration best practices if not already covered