# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Created a Chinese-language draft article comparing Claude Memory vs CLAUDE.md for the LoreAI blog.

**Key Exchanges:**
- Draft produced: `claude-memory-vs-claude-md.md` — a bilingual-friendly zh article covering two-layer memory architecture in Claude Code

**Decisions Made:**
- Article framing: Memory = personal private notebook (user-scoped, auto-maintained); CLAUDE.md = team rulebook (repo-scoped, manually maintained) — not either/or, but complementary layers
- Core decision rule surfaced: "换一个人来，这条信息还有用吗？" (Would this info be useful to someone else?) → yes = CLAUDE.md, no = Memory
- Article links out to related blog posts: `claude-code-memory`, `claude-code-seven-programmable-layers`, `claude-code-extension-stack-skills-hooks-agents-mcp`

**Lessons Learned:**
- Memory has a 200-line limit on MEMORY.md index — worth noting in any wiki page about Claude Memory
- CLAUDE.md takes priority over Memory when they conflict — Claude may auto-update/delete stale Memory entries
- `project`-type memories expire fastest (date-bound states); need periodic pruning

**Action Items:**
- Draft file needs to be placed in `drafts/` and human-polished before publishing
- Consider creating/updating a wiki page on `claude-code-memory.md` to capture the Memory system details (four types: user, feedback, project, reference; storage path `~/.claude/projects/`)