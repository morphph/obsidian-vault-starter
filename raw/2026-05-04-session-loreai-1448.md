# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Claude Code subagents vs Codex custom agents for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code uses orchestrated parent-child agent model (real-time coordination, shared state); Codex uses task-queue model (isolated containers, async execution)
- Customization paths differ: Claude Code agents live in `.claude/agents/` directory (travel with codebase), Codex agents configured through UI (simpler, no schema needed)
- Claude Code agents compose (spawn sub-agents, chain outputs); Codex agents are standalone task executors

**Decisions Made:**
- Article framing: not "which is better" but "match tool to workflow pattern"
- Verdict recommends using both: Claude Code for interactive coordination-heavy sessions, Codex for batch/parallel independent tasks
- Target audience: AI builders evaluating orchestration approaches

**Lessons Learned:**
- Claude Code subagents excel at: complex refactoring, architecture exploration, iterative development, monorepo coordination
- Codex custom agents excel at: batch processing, speculative exploration, security-sensitive environments, async workflows, team onboarding
- Key tradeoff: coordination capability (Claude Code) vs isolation guarantees (Codex)
- Codex containers have no inter-task communication — you are the orchestrator
- Claude Code worktree isolation is a middle ground between shared-state and full container isolation
- Cost model: Claude Code subagents share billing account, each uses own context window (token usage scales linearly with agent count)

**Action Items:**
- Article appears ready for `/draft` finalization or publish to LoreAI blog
- Consider creating wiki pages for: `codex-custom-agents.md`, `claude-code-subagents.md` if not already existing
- Cross-reference with existing wiki entries on Claude Code extension stack, hooks, skills