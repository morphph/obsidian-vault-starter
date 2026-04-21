# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a compare-page draft article on Claude Memory vs CLAUDE.md for LoreAI.

**Key Exchanges:**
- Draft produced: `claude-memory-vs-claude-md` (zh, category: compare/tools)
- Core positioning established: CLAUDE.md = project rules (team-shared, git-versioned, explicit); Memory = personal context (individual, auto-accumulated, implicit)

**Decisions Made:**
- Decision framework for info placement: "Would removing this cause a teammate to make a mistake?" → Yes = CLAUDE.md, No = Memory
- Conflict resolution rule documented: CLAUDE.md always wins over Memory when they contradict

**Lessons Learned:**
- CLAUDE.md and Memory are complementary layers, not substitutes — CLAUDE.md is static context injection, Memory is dynamic context accumulation
- Memory should not be pre-filled; let it grow naturally through corrections and expressed preferences, then prune monthly
- Bloated CLAUDE.md (thousands of lines) degrades Claude's attention allocation — keep it lean and focused

**Action Items:**
- Draft at `drafts/claude-memory-vs-claude-md.md` needs human review and polish before publish
- Related posts wired in frontmatter: `claude-code-memory`, `claude-code-seven-programmable-layers`, `anthropic-claude-memory-upgrades-importing`, `agentic-coding`