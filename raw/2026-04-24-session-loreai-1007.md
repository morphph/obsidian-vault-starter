# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language newsletter draft covering AI news from April 24, 2026 — primarily GPT-5.5 launch, Claude connectors expansion, and Anthropic's postmortem.

**Key Exchanges:**
- (No user Q&A — assistant produced a full newsletter draft in one output)

**Decisions Made:**
- Newsletter format: section headers with emoji, bilingual-friendly tone, concise bullets with engagement metrics and source links
- "Today's Pick" (今日精选) section anchors with a single analytical argument rather than summary

**Lessons Learned:**
- Anthropic postmortem revealed infrastructure config variance can exceed inter-model benchmark gaps — benchmark rankings may measure infra drift, not intelligence; Anthropic's recommendation: run evals in your own environment
- Claude Code v2.1.119 key features: persistent config, Agent worktrees, vim visual mode
- Claude Managed Agents memory API is now in public beta; Python SDK v0.97.0 and TS SDK v0.91.0 ship same-day support
- Claude connectors live: Resy, Tripadvisor, Booking.com, Instacart, Spotify, TurboTax
- Codex (GPT-5.5-powered) now has browser capabilities — can click, screenshot, iterate on live web apps
- Kimi 2.6 (Moonshot): first public case of a production workload migrated from closed-source to open-source model (Abacus AI)
- Simon Willison warning: prompt injection attack surface grows exponentially as agents gain real-world tool access
- DiLoCo (DeepMind): decoupled distributed training across data centers; tolerates network failures — key for next-gen frontier model training

**Action Items:**
- None explicitly mentioned