# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a detailed comparison article: Claude Code vs OpenAI Codex — covering architecture, workflow, pricing, and use cases.

**Key Exchanges:**
- Claude Code = local execution, interactive/synchronous, full environment access, CLAUDE.md context system
- OpenAI Codex = cloud microVM sandbox, async/batch, no network access, AGENTS.md context system
- Codex uses **codex-1** model (based on o3 architecture), fine-tuned for SWE tasks
- Claude Code uses Sonnet (speed) / Opus (reasoning), switchable per task

**Decisions Made:**
- Article positions the tools as complementary, not competing — "many teams will benefit from using both"
- Claude Code recommended for: complex refactoring, local env access, iterative exploration, solo devs, security-sensitive codebases
- Codex recommended for: well-defined batch tasks, parallel execution, strict sandbox requirements, non-terminal users

**Lessons Learned:**
- Codex sandbox = no network, no local service access, no dynamic discovery — security strength but capability constraint
- Claude Code's hooks + MCP + CLAUDE.md create a "programmable development environment" — more mature context pipeline than AGENTS.md
- Pricing roughly equivalent at heavy use ($100-200/mo range); Claude Code wins for light/occasional use via pay-per-token API billing
- Codex's async model adds latency for ambiguous tasks (review → reject → re-describe → wait loop)
- OpenAI offers free Codex for open-source maintainers + $100 student credits — no equivalent Claude Code program mentioned

**Action Items:**
- This content should be ingested into wiki as a comparison page (e.g., `wiki/claude-code-vs-codex.md`)
- Could cross-reference existing wiki pages: [[anthropic]], [[claude-code]], any OpenAI/Codex pages
- Pricing details will go stale — worth flagging with a `> [!warning]` for periodic review
- The article references `/compare/claude-code-vs-cursor` and `/blog/claude-code-agent-teams` — check if those are in raw/ or wiki/ already