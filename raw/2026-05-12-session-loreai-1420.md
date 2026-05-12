# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a detailed article comparing Claude Memory vs CLAUDE.md — the two context systems in Claude Code.

**Key Exchanges:**
- Article explains the three-layer context architecture: CLAUDE.md (project rules, team-shared, version-controlled), Claude Memory (personal, agent-authored, private), and SKILL.md (task-specific, shared)
- CLAUDE.md is human-authored, concise (<100 lines), opinionated, and actionable. Stale instructions actively harm output.
- Claude Memory is agent-authored, accumulates naturally through corrections and conversations, stored in `~/.claude/projects/` as markdown with YAML frontmatter.

**Decisions Made:**
- The framing "choose one or the other" is wrong — they're complementary layers. The right question: "Does this belong to the project or to me?"
- CLAUDE.md takes precedence over Memory for project rules. Memory cannot override CLAUDE.md instructions.
- Common anti-pattern: teams trying to use Memory as shared knowledge base by telling each member to "remember" the same facts. Doesn't scale — use CLAUDE.md instead.

**Lessons Learned:**
- Three-layer model: CLAUDE.md defines the playing field, Skills define specific plays, Memory knows the player
- Decision test for placement: "Would a new team member need this on day one?" → Yes = CLAUDE.md, No = Memory
- Memory types: personal preferences, learned corrections, ephemeral project context (sprint goals, freezes), external system references
- CLAUDE.md types: project rules, error-preventing constraints, architectural decisions, workflow requirements, known gotchas
- Stale CLAUDE.md is actively harmful (e.g., "use Jest" when migrated to Vitest → Claude generates wrong tests)
- Memory files are just markdown — can be read, edited, deleted directly in `~/.claude/projects/`

**Action Items:**
- Consider creating/updating wiki pages: `claude-code.md` (context architecture), `claude-memory.md`, `skill-files.md`
- Source references several related articles worth ingesting: "Claude Code Complete Guide", "Claude Code Extension Stack", "5 Claude Code Skills", "How to Effectively Prompt Claude Code", "What's So Special About Claude Code"