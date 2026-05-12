# Session Capture: loreai

**Date:** 2026-05-12
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft or published comparison article: Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison covering: execution model (sync vs async), context/config systems, security models, pricing, developer experience, and ecosystem
- Claude Code: terminal-native, real-time, local execution, multi-layer config (CLAUDE.md → skills → hooks → MCP), permission-based security
- Codex: browser-based, async task delegation, simpler config (AGENTS.md), sandbox-isolated security with network disabled by default

**Decisions Made:**
- Verdict favors Claude Code for individual devs/small teams (interactivity, local access, extensibility)
- Codex positioned as better for enterprise/security-sensitive orgs and large task backlogs
- Recommended hybrid approach: Claude Code for interactive sessions, Codex for batch processing well-defined issues
- Pricing comparison: both start at $20/mo; heavy use tiers are CC Max $100-200/mo vs Codex Pro $200/mo

**Lessons Learned:**
- Sync vs async is the fundamental architectural split — affects everything downstream
- Codex's sandbox model eliminates compliance concerns but limits capability (no local services, no real infra access)
- Claude Code's agent teams enable parallelized sub-agents for monorepo/cross-cutting work — no Codex equivalent
- Codex struggles with ambiguous tasks requiring iteration (submit-wait-review cycle adds latency)
- Claude Code's learning curve is steeper but payoff compounds as config/skills accumulate

**Action Items:**
- Article references a companion piece: Claude Code vs Cursor comparison (`/compare/claude-code-vs-cursor`) — ensure that exists or is planned
- Consider ingesting this into wiki as a page on AI coding tools landscape (covers pricing, architecture patterns, competitive positioning)