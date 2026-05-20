# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparative analysis article on Claude Code subagents vs Codex multi-agent workflows.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code uses composable in-session sub-agents (markdown files in `.claude/agents/`), Codex uses independent cloud sandbox task-dispatch model
- Parallel execution semantics differ: Claude Code spawns concurrent agents within a single conversation turn with shared context; Codex dispatches independent sandboxed tasks that return PRs

**Decisions Made:**
- Verdict: Claude Code wins for multi-agent orchestration (coordination, context sharing, model-per-agent flexibility); Codex wins for independent batch dispatch (isolation, simplicity, cloud compute)
- Many teams should use both — Claude Code for interactive orchestrated sessions, Codex for fire-and-forget batch tasks
- The `codex-rescue` agent type bridges both platforms (spawn Codex from within Claude Code)

**Lessons Learned:**
- Claude Code custom agents are version-controlled markdown files → composable building blocks; Codex custom configs are environment-based task templates → independent units
- Cost optimization lever: use cheaper models (Haiku) for simple sub-agents, reserve Opus for complex reasoning
- Codex struggles with conditional orchestration (sequential tasks with data dependencies); Claude Code handles this natively via parent-agent context passing
- Neither platform is categorically cheaper — Claude Code better for shared-context workflows, Codex better for independent batch tasks where container isolation prevents cascading failures

**Action Items:**
- Consider ingesting this article into wiki as a page (e.g., `wiki/claude-code-vs-codex-agents.md`) covering multi-agent workflow patterns
- Cross-link with existing wiki pages on Claude Code, Codex, and AI builder tools