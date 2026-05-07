# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing a detailed comparison article on OpenAI Codex vs Claude Code multi-agent architectures, likely for wiki ingestion or draft creation.

**Key Exchanges:**
- Article covers subagent systems across both platforms: Codex uses cloud-sandboxed containers (fire-and-forget, async); Claude Code uses local orchestration with typed agents, worktree isolation, and parent-child coordination
- Parallel execution: Codex scales horizontally with compute budget (container per task); Claude Code practical limit is 3-8 background subagents before context management becomes a bottleneck

**Decisions Made:**
- **Codex best for**: bulk independent tasks (migrations, batch bug fixes), async/overnight workflows, CI/CD PR-based flows, resource-constrained local machines
- **Claude Code best for**: orchestrated context-dependent workflows (complex refactoring, codebase investigation, custom review pipelines, iterative dev with feedback loops, team-specific workflows via SKILL.md + Agent SDK)
- **Verdict**: Many teams will use both — Codex for bulk/independent, Claude Code for complex/coordinated

**Lessons Learned:**
- Codex tasks cannot communicate mid-execution; sequential orchestration must be manual
- Claude Code's `SendMessage` enables resuming subagents with additional context — useful for iterative debugging
- Cost model difference matters: Codex = compute credits (infra + tokens, scales with task count); Claude Code = API tokens only (local compute is free). Many short parallel tasks → Codex gets expensive. Fewer complex sessions → Claude Code cheaper
- Codex has stronger security isolation (sandboxed containers, no local access); Claude Code runs with user permissions (more power, less isolation)
- Custom agent types (typed agents via Agent SDK) are a Claude Code differentiator — Codex only has one general-purpose agent type customized via `AGENTS.md`
- Worktree isolation in Claude Code enables parallel code changes without conflicts, though less scalable than Codex's container model

**Action Items:**
- This content should be ingested into the wiki — touches topics: [[Claude Code]], [[OpenAI Codex]], multi-agent orchestration, subagent patterns, cost comparison
- Could update or create wiki pages for: `codex-vs-claude-code.md`, `multi-agent-patterns.md`, `claude-code-agent-sdk.md`