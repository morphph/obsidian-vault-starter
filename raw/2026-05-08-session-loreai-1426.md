# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article comparing OpenAI Codex CLI vs Claude Code — a detailed feature/architecture comparison piece for LoreAI.

**Key Exchanges:**
- Comprehensive comparison across 6 dimensions: architecture, extensibility, security, pricing, developer experience, and use-case fit
- Codex CLI = cloud-sandboxed, async task delegation (o3/o4-mini models); Claude Code = local execution, interactive pair programming (Opus/Sonnet/Haiku models)

**Decisions Made:**
- Verdict favors Claude Code for "most professional developers" due to depth/flexibility, but acknowledges Codex's sandbox model as genuinely valuable for security-sensitive environments
- Framing: "not interchangeable — designed for different working styles" (delegation vs pair programming)
- Pricing comparison left nuanced: subscription (Codex) vs usage-based (Claude Code), neither clearly cheaper — depends on usage pattern

**Lessons Learned:**
- Codex extensibility is limited — no CLAUDE.md equivalent, no hooks, no MCP, no agent teams. Interaction is prompt-only
- Security tradeoff: architectural constraints (sandbox) vs operational constraints (permissions + review) — neither universally better, depends on threat model
- "Agent matters more than model" — execution model, context system, and extensibility determine outcomes more than raw model benchmarks
- Codex offers free tiers for open source maintainers and students ($100 credits) — relevant competitive positioning
- Common hybrid pattern: Claude Code for interactive dev, Codex for batch tasks (tests, docs, issue backlog)

**Action Items:**
- Article references multiple internal links (`/blog/claude-code-*`, `/blog/codex-*`) — ensure those destination pages exist in wiki or drafts
- Consider ingesting this as a wiki page on competitive landscape (e.g., `wiki/codex-vs-claude-code.md`)