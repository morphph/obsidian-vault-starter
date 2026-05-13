# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/source comparing OpenAI Codex CLI vs Anthropic Claude Code as AI coding agents (mid-2025 landscape).

**Key Exchanges:**
- Codex CLI = cloud sandbox, async task queue, included with ChatGPT Pro ($200/mo), uses codex-1/o3/o4-mini models
- Claude Code = local execution, interactive pair-programming, per-token API billing, uses Claude Opus/Sonnet/Haiku
- Codex safety is structural (network-isolated sandbox); Claude Code safety is permission-based (tiered approvals + hooks)
- Claude Code has richer extensibility: CLAUDE.md, SKILL.md, MCP servers, hooks, sub-agents in parallel worktrees
- Codex CLI has no equivalent to CLAUDE.md for persistent project instructions; sandbox is network-isolated
- Both tools can be used together — Claude Code for interactive/complex work, Codex for batched/lower-risk tasks

**Decisions Made:**
- Article verdict: Claude Code stronger for experienced devs on complex, context-heavy projects; Codex CLI wins for sandboxed safety, async workflows, or existing OpenAI ecosystem investment
- Complementary positioning — not either/or

**Lessons Learned:**
- Execution model (local vs cloud) matters more than underlying model differences for most workflows
- Codex CLI ≠ old OpenAI Codex model (2021) — completely different product, shared name causes confusion
- For large opinionated codebases with implicit conventions, lack of explicit context injection (Codex) is a real limitation
- Claude Code's CLAUDE.md + hooks system is a genuine workflow advantage with no Codex equivalent
- Neither tool has native Windows support as of mid-2025 (both use WSL)

**Action Items:**
- Consider ingesting this as a wiki source comparing coding agent tools (relevant to builder tools domain)
- Could inform wiki pages on: Claude Code, Codex CLI, AI coding agents landscape, pricing models for AI dev tools