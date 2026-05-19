# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Claude Code subagents vs OpenAI Codex for multi-agent coding workflows (likely for LoreAI blog).

**Key Exchanges:**
- Detailed comparison of two multi-agent coding paradigms: Claude Code's parent-child orchestration model vs Codex's container-per-task isolation model
- Three workflow patterns analyzed: large refactoring, bug investigation, test generation

**Decisions Made:**
- **Claude Code wins for coordinated workflows**: Typed agents (Explore, Plan), CLAUDE.md/SKILL.md layered customization, and parent-child orchestration make it better for tasks requiring cross-module awareness and real-time feedback loops
- **Codex wins for parallel/async workloads**: Container isolation, horizontal scaling, fire-and-forget execution model suits independent batch tasks
- **Verdict framing**: Not "which is better" but "which execution model matches your workflow pattern" — productive teams use both

**Lessons Learned:**
- Claude Code customization is layered: CLAUDE.md (project context) → SKILL.md (task patterns) → Agent type definitions (tool access scoping) → Hooks (deterministic automation). This travels with the repo, not in personal prompt templates.
- Codex has no formal subagent API — multi-agent behavior emerges from task-level parallelism with independent containers
- Codex's safety model (sandboxed containers, no network) is stronger by default; Claude Code relies on typed agent tool scoping + optional worktree isolation
- Cost models differ fundamentally: Codex flat-rate via ChatGPT Pro ($200/mo) vs Claude Code per-token API billing — each favors different usage patterns

**Action Items:**
- Article references several internal links (`/blog/9-principles-writing-claude-code-skills...`, `/blog/claude-code-hooks...`, `/blog/codex-for-open-source`, `/subscribe`) — ensure these exist or are created before publishing
- Consider ingesting this as a wiki page covering Claude Code agent architecture and Codex comparison for future reference