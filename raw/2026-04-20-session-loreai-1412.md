# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Created a Chinese comparison article draft: Claude Code vs Codex — terminal agent vs cloud agent

**Key Exchanges:**
- Article produced: `claude-code-vs-codex.md` (zh, compare category), covering architecture, workflow, pricing, and use-case fit

**Decisions Made:**
- Framing: Claude Code = synchronous pair-programmer (local, interactive); Codex = async task dispatcher (cloud sandbox, batch)
- Two tools are positioned as complementary, not mutually exclusive: Claude Code for deep-context refactors, Codex for parallelizable peripheral tasks
- Pricing decision rule: if already on ChatGPT Pro, Codex marginal cost = $0; otherwise Claude Code's per-token billing is the cost to accept

**Lessons Learned:**
- Key differentiator is control vs. autonomy: Claude Code gives real-time intervention (Hooks, Skills, CLAUDE.md); Codex gives fire-and-forget async execution
- Codex's AGENTS.md is the rough equivalent of Claude Code's CLAUDE.md — worth noting when explaining either tool to new users
- Codex for Open Source program exists (free credits) — relevant when advising OSS maintainers

**Action Items:**
- None explicitly stated; draft is complete and ready for human polish before publication