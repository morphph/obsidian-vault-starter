# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Claude Code vs OpenAI Codex as AI coding tools (for loreai.dev blog).

**Key Exchanges:**
- Article covers architecture, workflow, extensibility, pricing, and use-case fit for both tools
- Claude Code = local, interactive, terminal-native, deep context, extensible (hooks/MCP/skills/agent teams)
- Codex = cloud-sandboxed, async fire-and-forget, PR-review model, parallelizable, ChatGPT ecosystem

**Decisions Made:**
- Framing: "not interchangeable — designed for different working styles" rather than a winner/loser comparison
- Verdict recommends both tools complementarily: Claude Code for architect-level interactive work, Codex for backlog parallelization
- Pricing angle: Claude Pro ($20/mo) vs ChatGPT Pro ($200/mo) as key solo-dev differentiator

**Lessons Learned:**
- Real-time interaction vs async review is the #1 workflow differentiator — should drive tool choice more than feature tables
- CLAUDE.md multi-layer config (CLAUDE.md → SKILL.md → hooks → MCP) is a competitive moat vs Codex's single AGENTS.md
- Codex sandbox model = zero local risk but no mid-task steering; tradeoff is wasted cycles on misunderstood tasks
- Cost predictability (Codex flat-rate) vs pay-per-use (Claude Code API) matters differently by usage volume

**Action Items:**
- Article references several internal links (`/blog/claude-code-seven-programmable-layers`, `/blog/claude-code-hooks-mastery`, `/compare/claude-code-vs-cursor`, etc.) — verify these exist or are planned
- Contains pricing data (mid-2026 framing) — will need periodic updates as both platforms evolve
- Could be ingested into wiki as a comparison page (e.g., `wiki/claude-code-vs-codex.md`) once published