# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese comparison article (draft) for LoreAI: Codex Subagents vs Claude Code Subagents.

**Key Exchanges:**
- Produced a full `/zh/compare/` article with slug `use-subagents-and-custom-agents-in-codex`, covering architecture differences, custom agent capabilities, and workflow recommendations

**Decisions Made:**
- Framed the comparison as **cloud async (Codex)** vs **local real-time orchestration (Claude Code)** — not direct competitors but different paradigms
- Codex = task queue model (independent sandboxes, no inter-task communication); Claude Code = recursive orchestration model (dynamic subagent spawning, context sharing, custom agent types)
- Verdict: no universal winner — Codex for batch independent tasks, Claude Code for complex cross-module work requiring context awareness

**Lessons Learned:**
- Codex "multi-agent" is really multi-task parallelism, not true agent orchestration — important distinction for accurate positioning
- Claude Code's `codex:codex-rescue` subagent type enables hybrid workflows (call Codex from within Claude Code), a growing pattern worth tracking
- Custom agent granularity: Codex uses a single `AGENTS.md` (instruction injection), Claude Code uses per-agent `.md` files with frontmatter (tool sets, model selection, role constraints) — structurally more mature

**Action Items:**
- Article references several internal links (`codex-complete-guide`, `claude-code-subagents-examples`, `agent-harnesses-2026`, `claude-code-agent-teams`) — verify these exist or are planned
- Slug references a French path (`con-u-pour-des-workflows-multi-agents`) that looks like a localization artifact — should be corrected