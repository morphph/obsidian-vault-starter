# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: OpenAI Codex subagents vs Claude Code subagents for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Codex = cloud sandbox, serverless-function model (each task = independent container); Claude Code = local, hierarchical subagent system with typed agents (Explore, Plan, codex-rescue, general-purpose)
- Feature matrix covering execution environment, specialization, parallelism, context sharing, isolation, configuration, and cost

**Decisions Made:**
- **Verdict framing**: Codex wins for batch/async/independent tasks; Claude Code wins for orchestrated/context-rich/multi-step workflows. Recommended using both together (Claude Code as orchestrator, Codex for delegated batch work)
- **Key differentiators identified**: Codex's container isolation vs Claude Code's cooperative permission model; Codex's GitHub-native PR output vs Claude Code's conversational result return; Claude Code's typed agent system + hooks + skills as programmable orchestration layer

**Lessons Learned:**
- `codex:codex-rescue` agent type bridges both platforms — Claude Code can delegate to Codex, making them complementary rather than purely competitive
- Codex's network-disabled sandbox is stronger for security isolation; Claude Code's local execution is necessary when agents need access to local services (dev servers, databases)
- Claude Code's `worktree` isolation is opt-in and weaker than container isolation but enables local environment interaction
- Codex bundled pricing (ChatGPT Pro/Team) favors high-volume batch; Claude Code per-token API billing favors targeted sessions

**Action Items:**
- Wiki pages to consider creating/updating: `codex-subagents.md`, `claude-code-subagents.md`, or a unified `multi-agent-comparison.md`
- Cross-references worth tracking: Claude Code Agent Teams, Claude Code extension stack (skills/hooks/agents/MCP), Claude Code Hooks guide
- Article links to internal blog posts (claude-code-complete-guide, claude-code-agent-teams, claude-code-hooks, codex-for-open-source, codex-for-students) — verify these exist and are accurate