# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a blog article comparing OpenAI Codex vs Claude Code for subagent and custom agent workflows.

**Key Exchanges:**
- Detailed comparison of two multi-agent paradigms: Codex (async, containerized, isolated) vs Claude Code (synchronous, orchestrated, interactive)
- Practical example: "Add input validation to all API endpoints" — Codex requires decomposed independent tasks; Claude Code handles as single coordinated instruction

**Decisions Made:**
- Article framing: complementary tools, not competitive — "use both" is the recommended verdict
- Codex = independent parallelizable tasks (batch tests, docs, lint fixes); Claude Code = interconnected coordinated work (cross-cutting refactors, schema changes cascading across layers)
- Cost model distinction: Codex flat-rate ($200/mo Pro); Claude Code per-token API billing

**Lessons Learned:**
- Codex agents cannot communicate during execution — no inter-task coordination, parent must manually sequence dependent work
- Claude Code's layered customization stack: SKILL.md (task instructions) → agent types (tool constraints) → hooks (deterministic automation) — significantly more granular control
- Claude Code error recovery is more powerful (parent can retry, adjust, spawn investigation agents) but more opaque (reasoning in conversation context vs clear execution logs)
- Key tradeoff: Codex's simplicity/isolation vs Claude Code's coordination/complexity

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/blog/codex-complete-guide`, etc.) — ensure these exist or are queued for publication
- Article could be ingested to wiki as a reference on multi-agent workflow patterns and tool selection criteria