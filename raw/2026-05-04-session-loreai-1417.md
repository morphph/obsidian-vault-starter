# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/content about CLAUDE.md vs Claude Memory — comparing Claude Code's two persistence mechanisms and when to use each.

**Key Exchanges:**
- CLAUDE.md is static, always-loaded, version-controlled project instructions; Claude Memory is a two-layer system (MEMORY.md index + on-demand memory files) that Claude self-maintains
- CLAUDE.md occupies context window every session; Memory only loads relevant files per session (more token-efficient at scale)
- Claude can create/update/delete Memory files but never writes to CLAUDE.md — by design

**Decisions Made:**
- **Use both together** as complementary layers: CLAUDE.md = shared constitution (the "what"), Memory = personal journal (the "who" and "how")
- **If forced to pick one:** CLAUDE.md for team projects (consistency), Memory for solo projects (zero-maintenance)
- **Antipattern to avoid:** duplicating instructions across both systems — creates conflicting versions when one gets updated

**Lessons Learned:**
- CLAUDE.md staleness is low-risk but high-impact (wrong instructions hit everyone); Memory staleness is higher-risk but lower-impact (individual sessions)
- Treat CLAUDE.md updates as part of the same PR that changes the underlying system (e.g., change test framework → update CLAUDE.md in same commit)
- Memory files live at `~/.claude/projects/<project-hash>/memory/` — plain markdown with YAML frontmatter, manually editable
- CLAUDE.md also serves as human-readable documentation; Memory files are useful only to Claude
- Promotion/demotion pattern: frequently-referenced memory that applies team-wide → promote to CLAUDE.md; personal-only CLAUDE.md rules → demote to memory

**Action Items:**
- Consider ingesting this into wiki as a page on Claude Code configuration best practices (covers CLAUDE.md, Claude Memory, team workflows)