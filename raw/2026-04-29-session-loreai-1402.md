# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a Claude Code vs OpenAI Codex comparison article for LoreAI blog.

**Key Exchanges:**
- Detailed feature-by-feature comparison covering: interaction model (sync vs async), context systems, extensibility, pricing, security/sandboxing, and use-case fit

**Decisions Made:**
- **Claude Code positioned as the more powerful/flexible tool** for interactive, complex, ambiguous tasks with deep local environment integration
- **Codex positioned as more accessible/frictionless** for async task delegation and parallelized well-defined work
- **Recommendation framework:** "Pick Claude Code if terminal + real environment. Pick Codex if task queue + review later."
- **Both tools framed as complementary**, not competing — mirrors sync vs async work modes teams already use

**Lessons Learned:**
- Claude Code's layered context system (CLAUDE.md → rules → skills) is a meaningful differentiator — Codex has no equivalent persistent hierarchical context
- Codex sandbox trades environment fidelity for security isolation; Claude Code trades isolation for real-environment access
- MCP servers, hooks, agent teams, and skills give Claude Code a significant extensibility gap over Codex
- Pricing models fundamentally differ: Claude Code = per-token (scales with usage), Codex = per-seat subscription (predictable but potentially costlier for small heavy-use teams)
- Codex cannot access private registries or internal APIs by default — important limitation for enterprise use

**Action Items:**
- Article references `/subscribe`, `/blog/` and `/compare/` URLs — ensure these routes exist on loreai.dev
- Article is LoreAI-branded content with CTA — should be tracked in drafts/ once finalized
- Consider creating wiki pages for: [[claude-code]], [[openai-codex]], [[agentic-coding-tools-landscape]] to back-reference from this article