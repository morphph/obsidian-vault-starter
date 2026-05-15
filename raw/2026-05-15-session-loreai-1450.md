# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Claude Code vs OpenAI Codex subagent and custom agent workflows for LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code uses native parent-child subagent spawning with parallel execution; Codex uses one-agent-per-task cloud sandbox model
- Claude Code's four-layer customization: CLAUDE.md → SKILL.md → Agent definitions → MCP servers
- Codex customization is prompt-only — no equivalent to CLAUDE.md inheritance or typed agent roles
- Isolation models differ: Codex = cloud containers (stronger security, higher latency); Claude Code = git worktrees (lighter weight, local execution)

**Decisions Made:**
- Article verdict: Claude Code is stronger for multi-agent orchestration; Codex is stronger for single-agent isolated tasks
- Pragmatic recommendation: use both — Codex for independent fire-and-forget tasks, Claude Code for complex parallel workflows
- Three workflow patterns chosen as illustrative examples: large refactoring, multi-concern code review, test generation

**Lessons Learned:**
- Claude Code subagent parallelism means total time ≈ slowest agent; Codex sequential tasks = sum of all tasks
- Claude Code's `isolation: "worktree"` auto-cleans if agent makes no changes — useful detail for wiki
- Codex's flat pricing (ChatGPT Pro/Team) vs Claude Code's per-token billing creates different cost profiles depending on workflow complexity
- Claude Code's permission modes (`plan`, `acceptEdits`) for subagents have no Codex equivalent — relevant for security-sensitive workflows
- CLAUDE.md + SKILL.md travel with the repo, giving team-wide AI behavior standardization on day one — this is a key differentiator for enterprise adoption

**Action Items:**
- Article references internal links (`/blog/claude-code-subagents-examples`, `/blog/claude-code-agent-teams`, `/glossary/agentic-coding`) — ensure these wiki pages exist or are created
- Article includes CTA to `/subscribe` — verify this route works on loreai.dev
- Consider ingesting this as a raw source and fanning out wiki updates to pages on: Claude Code, Codex, multi-agent coding patterns, agentic coding tools comparison