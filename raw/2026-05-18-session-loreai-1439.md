# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a detailed comparison article: Codex vs Claude Code subagents and custom agents.

**Key Exchanges:**
- Codex uses **task-level parallelism** (isolated containers, no inter-task communication, horizontal scaling) — best for batch independent tasks
- Claude Code uses **session-level composition** (Agent tool with subagent_type, worktree isolation, SendMessage coordination, dynamic spawning) — best for interactive multi-agent orchestration
- Claude Code Agent tool params: `subagent_type` (Explore/Plan/code-reviewer/general-purpose), `isolation: "worktree"`, `run_in_background`, `name`
- Codex has no subagent concept — every task uses the same agent type, differentiation only via instructions/AGENTS.md
- Claude Code custom agents composed via subagent_type + detailed prompt + SKILL.md; Codex via AGENTS.md + task instructions

**Decisions Made:**
- Verdict: Claude Code is more capable for subagents/custom agents today; Codex wins on horizontal batch scale
- Recommended hybrid approach: Claude Code for interactive dev sessions, Codex for batch operations
- Pricing framing: Codex flat subscription (predictable) vs Claude Code per-token (cheaper for light use, scales with heavy multi-agent)

**Lessons Learned:**
- Codex tasks cannot pivot mid-task — scope is fixed at dispatch. Claude Code can spawn Explore agents dynamically based on runtime discoveries
- For dependent task chains in Codex, you must wait/merge/re-dispatch — fighting the architecture
- Claude Code practical limit ~10 parallel sub-agents before hitting resource/rate constraints; Codex has no such ceiling
- Agent SDK ≠ Agent tool — SDK is infrastructure for building custom agent platforms, Agent tool is a user-facing CC feature

**Action Items:**
- Article references internal links (`/blog/codex-vscode`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/glossary/agent-sdk`, etc.) — ensure these wiki pages exist or are created
- Consider ingesting this as a wiki page (e.g., `wiki/codex-vs-claude-code-agents.md`) for the AI tools comparison knowledge area