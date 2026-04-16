# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User shared a long-form article comparing Claude Code vs OpenAI Codex (likely for ingestion or reference)

**Key Exchanges:**
- Article covers: persistent context (CLAUDE.md advantage), real-time vs async workflows, multi-agent parallelism, security/privacy, pricing, and when to use each tool

**Decisions Made:**
- No decisions made — this was a passive context review with no tool calls or user interaction

**Lessons Learned:**
- Claude Code advantage: `CLAUDE.md` accumulates project-specific knowledge over time; Codex has no equivalent persistent config — context must be re-provided per task
- Codex runs code in OpenAI cloud (code leaves local machine); Claude Code keeps code local — critical for compliance/privacy requirements
- Codex pricing: bundled in ChatGPT Pro ($200/mo) / Team ($25/user/mo); Claude Code: API usage-based or Claude Max flat rate
- Recommended combined pattern: Claude Code for active dev sessions + debugging; Codex for backlog clearing (parallel independent tasks overnight)
- Codex (2025) ≠ original Codex model (2021) — completely different product built on codex-1/o3

**Action Items:**
- Consider ingesting this article as a raw source if it's meant to be added to the wiki (e.g., `raw/claude-code-vs-codex.md`) — it covers Claude Code, Codex/OpenAI, and builder tools which fall squarely in the domain focus