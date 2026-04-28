# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a compare-format blog draft: "Claude Memory vs CLAUDE.md: Which Context System Should You Use?"

**Key Exchanges:**
- Produced a full `/compare/` article distinguishing Claude Memory (personal, automatic, `~/.claude/projects/`) from CLAUDE.md (shared, version-controlled, deterministic)
- Article follows the site's compare template with frontmatter, TL;DR, feature table, use-case sections, verdict, and FAQ

**Decisions Made:**
- Framed as complementary tools, not competitors — verdict is "use both"
- CLAUDE.md takes precedence when the two conflict (explicit directive > implicit memory)
- Categorized: CLAUDE.md for shared/stable/prescriptive rules; Memory for personal/contextual/evolving preferences
- Internal linking to related posts: `claude-code-memory`, `claude-code-complete-guide`, `claude-code-seven-programmable-layers`, `claude-code-extension-stack`, `5-claude-code-skills-i-use-every-single-day`

**Lessons Learned:**
- Both systems drift differently: CLAUDE.md drifts when codebase changes but file isn't updated; Memory drifts when saved context no longer matches reality
- Memory files don't sync across machines; CLAUDE.md does via git
- Memory is user-scoped and lives in `~/.claude/projects/{project-hash}/memory/`

**Action Items:**
- Article needs human review/polish before publishing to `drafts/` or the blog
- Verify all internal links resolve (referenced blog slugs and glossary entries must exist)
- Consider adding related_compare entries once more compare articles exist in the series