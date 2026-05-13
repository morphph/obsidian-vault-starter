# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex vs Claude Code subagent orchestration models for the blog.

**Key Exchanges:**
- Detailed architectural comparison of two multi-agent paradigms: Codex's async task parallelism (container-isolated, PR-output) vs Claude Code's synchronous hierarchical agent teams (session-level, real-time)
- Claude Code Agent tool types documented: `Explore` (read-only search), `Plan` (architecture), `code-reviewer`, `general-purpose` — each with enforced tool restrictions
- Codex model: each task gets its own sandboxed container with repo clone; tasks cannot communicate; output = PRs
- Claude Code model: parent spawns typed subagents, waits or backgrounds them, synthesizes results; worktree isolation available for Codex-like sandboxing per subtask

**Decisions Made:**
- Framework: "batch vs compositional" as the core decision axis — Codex optimizes for independent parallel tasks, Claude Code for multi-step coordinated workflows
- Both can coexist on same project (`AGENTS.md` + `CLAUDE.md` are independent)
- Article structured as a balanced comparison with clear "when to choose" sections rather than declaring a winner

**Lessons Learned:**
- Codex tasks can't negotiate conflicts mid-execution; conflicts resolve at PR review/merge time
- Claude Code's worktree isolation bridges the gap — provides container-like safety while keeping in-session communication
- `AGENTS.md` (Codex) and `CLAUDE.md` (Claude Code) serve analogous roles but are platform-specific; neither reads the other
- For monorepos >1GB, Claude Code's local execution avoids clone overhead that Codex containers incur
- Claude Code's power comes with complexity tradeoff: "spawn agents, compose results, make decisions" requires understanding the agent system

**Action Items:**
- Article references several internal links (`/blog/claude-code-agent-teams`, `/blog/codex-complete-guide`, etc.) — ensure these exist or are planned before publishing
- Consider ingesting this as a wiki source once published — covers Claude Code architecture, Codex capabilities, and multi-agent patterns comprehensively