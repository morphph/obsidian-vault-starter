# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a comparative article on Claude Code vs Codex CLI — likely raw source material for the wiki.

**Key Exchanges:**
- No interactive exchanges occurred. The context is a standalone article comparing Claude Code and Codex CLI across: configuration systems, safety models, IDE integration, multi-agent parallelism, pricing, and model capabilities.

**Decisions Made:**
- None recorded in this session.

**Lessons Learned:**
- **Claude Code vs Codex CLI — key differentiators worth tracking in wiki:**
  - Claude Code: local execution, `CLAUDE.md` persistent config, interactive/synchronous, agent teams for interdependent tasks, permission-approval safety model, terminal-native
  - Codex CLI: cloud containers, fire-and-forget, network-isolated sandbox, parallel independent tasks, no persistent config — each task starts fresh
  - Pricing parity at $200/month tier; Codex CLI cheaper for teams already on ChatGPT ($30/user/month)
  - Models: Codex uses GPT-4.1 + o-series; Claude Code uses Claude Haiku/Sonnet/Opus with extended thinking
  - Complementary use case: Claude Code for interactive/complex work, Codex CLI for batch/backlog dispatch
  - Article source appears to be LoreAI content (ends with LoreAI subscribe CTA) — candidate for `raw/` ingest

**Action Items:**
- Consider ingesting this article as a raw source → wiki page on `claude-code-vs-codex-cli.md`