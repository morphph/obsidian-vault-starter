# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese comparison article for the LoreAI blog: "Claude Memory vs CLAUDE.md：两套记忆系统到底怎么选？"

**Key Exchanges:**
- Article covers the two persistence mechanisms in Claude Code: CLAUDE.md (project-level, Git-tracked, team-shared, human-maintained) vs Claude Memory (personal, auto-maintained by Claude, local only, not version-controlled)

**Decisions Made:**
- Article framing: the two systems are **complementary, not competing** — CLAUDE.md manages project rules, Memory manages personal context
- Core principle stated: "CLAUDE.md 管规则，Memory 管上下文"
- Article cross-links to: `claude-code-memory`, `claude-code-seven-programmable-layers`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `9-principles-writing-claude-code-skills`

**Lessons Learned:**
- Memory reliability requires discounting: auto-recorded info can go stale; CLAUDE.md should be treated as source of truth for project rules
- Mixing the two causes problems: project rules in Memory → not shared; personal preferences in CLAUDE.md → forced on team
- Memory files are plain Markdown under `~/.claude/projects/<project>/memory/` — manually editable

**Action Items:**
- Draft was generated but not saved to `drafts/` — needs to be written to file and logged in `wiki/log.md` if this was a `/draft` command invocation
- Check whether related wiki pages (`claude-code.md`, `claude-md.md`) need cross-reference updates