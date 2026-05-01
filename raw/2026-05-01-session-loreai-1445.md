# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a detailed article comparing Codex subagents vs custom agents for multi-agent coding workflows.

**Key Exchanges:**
- Article covers the full spectrum of multi-agent orchestration: automatic subagents (zero-config, system-decides decomposition) vs custom agents (user-configured, deterministic pipelines)
- Typical custom agent pipeline: Planner → Implementer → Test → Reviewer → Committer
- Claude Code's model sits between the two: explicit subagent spawning with structured agent types (Explore, code-reviewer, general-purpose) + SKILL.md files as persistent behavioral config

**Decisions Made:**
- Recommended migration path: subagents-first → identify patterns → custom agents for high-frequency tasks → hybrid approach
- Sweet spot for custom agents: 3-5 per team (reviewer, test writer, doc updater, 1-2 domain-specific)
- More than 8-10 custom agents signals over-specialization

**Lessons Learned:**
- Subagents are opaque to debug; custom agents are transparent and traceable — gap widens with complexity
- Custom agents can reduce token costs 30-40% vs ad-hoc subagents for recurring workflows (50 tasks/week benchmark)
- Subagents inherit parent tool permissions by default; custom agents can have individually scoped access
- Parent agent handles subagent file conflicts via merge-like resolution
- Custom agent instructions are mostly portable across platforms; orchestration/tool config is not

**Action Items:**
- Consider creating wiki pages for: `codex-multi-agent.md` (subagents vs custom agents), `agent-pipeline-patterns.md` (the 5-stage pipeline pattern)
- Cross-reference with existing wiki content on Claude Code subagents, SKILL.md, and agentic coding