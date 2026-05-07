# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparative analysis article on OpenAI Codex vs Claude Code multi-agent architectures.

**Key Exchanges:**
- Detailed architectural comparison between Codex's task-based isolation model and Claude Code's in-process subagent model
- Analysis of custom agent creation capabilities (Codex has none; Claude Code has formal agent definition system)
- Parallel execution patterns: Codex = independent N tasks, Claude Code = orchestrated fan-out/fan-in, pipelines, conditional branching

**Decisions Made:**
- Framework for choosing between platforms: **independent tasks → Codex; interdependent tasks → Claude Code**
- Codex strengths: batch processing, strict isolation, GUI workflows, open-source cost advantage
- Claude Code strengths: coordinated refactoring, custom agent ecosystems, interactive exploration, local-first dev
- Both can be used together: Claude Code for exploration/coordination locally, Codex for well-scoped parallel cloud tasks

**Lessons Learned:**
- Codex's isolation is both its strength (safety) and weakness (no inter-agent coordination); the human becomes the orchestration layer
- Claude Code's worktree isolation is a middle ground — file-level isolation without losing parent communication
- Custom agent definitions traveling with the repo solve team onboarding/standardization problems that prompt libraries can't
- Practical subagent limit: 2-5 focused subagents per task recommended due to context window and token costs
- Codex lacks equivalent to CLAUDE.md context propagation — project instructions don't auto-inform task behavior

**Action Items:**
- Consider ingesting this as a wiki page (e.g., `wiki/codex-vs-claude-code-multi-agent.md`) covering the architectural comparison
- Cross-reference with existing wiki pages on Claude Code skills, subagents, and extension stack if they exist