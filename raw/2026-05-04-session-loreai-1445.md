# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/review of a comparison article: "Codex vs Claude Code" focusing on subagent workflows and custom agent capabilities for the LoreAI blog.

**Key Exchanges:**
- Article covers multi-agent architecture differences: Codex = no intra-task subagents (parallel only at task level via API), Claude Code = native subagent orchestration (parallel, sequential, worktree isolation)
- Customization depth comparison: Codex (natural language instructions + setup scripts, not version-controlled) vs Claude Code (SKILL.md + CLAUDE.md + hooks, composable, version-controlled)

**Decisions Made:**
- Framing: platforms don't compete — they serve different points on the complexity spectrum
- Recommended pattern: use both together (Claude Code for complex orchestration, Codex for fire-and-forget independent tasks)
- Cost rule of thumb: Codex linearly expensive for parallel tasks (container overhead); Claude Code cheaper for many small coordination steps (token-based, lightweight ops cheap)

**Lessons Learned:**
- Codex's zero-setup advantage is compelling for teams evaluating tools but trades off customization depth
- Claude Code's investment in configuration compounds over time (skills, hooks, CLAUDE.md refinements)
- Worktree isolation pattern in Claude Code solves the real problem of agents stepping on each other's changes during large refactors
- Codex sequential dependency limitation requires external orchestration (CI pipeline or manual sequencing)

**Action Items:**
- Consider ingesting this as a wiki page (e.g., `wiki/codex-vs-claude-code.md`) covering the architectural differences and decision framework
- Cross-references to create: links to existing wiki pages on Claude Code, MCP, skills/hooks if they exist
- Article references internal links (`/blog/claude-code-hooks-a-complete-guide...`, `/blog/9-principles-writing-claude-code-skills`, etc.) — verify these exist or are planned