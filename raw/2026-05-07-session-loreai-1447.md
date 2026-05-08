# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article: Codex Subagents vs Claude Code Agent Teams

**Key Exchanges:**
- Generated a complete `/zh/blog/` comparison post (`use-subagents-and-custom-agents-in-codex`) covering multi-agent coding approaches from both OpenAI and Anthropic

**Decisions Made:**
- Core framing: Codex = "分发-收集" (dispatch-collect) pattern; Claude Code = "协作-协调" (collaborate-coordinate) pattern — this is the central mental model for choosing between them
- Codex strengths: cloud sandbox isolation, horizontal parallelism, batch-independent tasks, fire-and-forget workflows
- Claude Code strengths: shared context via CLAUDE.md/SKILL.md, local environment access, interactive iteration, deep project understanding
- Practical recommendation: use both — Codex for batchable independent tasks (test gen, formatting, dependency upgrades), Claude Code for coordination-heavy tasks (architecture refactors, cross-module features)

**Lessons Learned:**
- Subagent vs Custom Agent distinction worth noting: Subagent = temporary workers auto-created during task decomposition; Custom Agent = pre-defined specialist agents with fixed prompts/tools — "临时工 vs 专职员工"
- Claude Code Agent Teams practical limit is ~3-5 parallel sub-agents due to local resource constraints and token cost

**Action Items:**
- Article references several related posts (`codex-complete-guide`, `claude-code-agent-teams`, `claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — verify these all exist and cross-link correctly
- Wiki pages to consider creating/updating: one on multi-agent coding patterns consolidating the dispatch-collect vs collaborate-coordinate framework