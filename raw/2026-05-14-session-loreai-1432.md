# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working with a blog post comparing Codex CLI (OpenAI) vs Claude Code (Anthropic) as AI coding agents.

**Key Exchanges:**
- Detailed architectural comparison: Codex runs in cloud sandbox (isolated container, repo snapshot), Claude Code runs locally (full environment access, real-time)
- Workflow model difference: Codex is async-first (fire-and-forget task queue), Claude Code is sync-first (interactive pair programming)
- Security model: Codex = hard boundary (sandbox isolation), Claude Code = soft boundary (permission system)

**Decisions Made:**
- The "hybrid verdict": Claude Code for hard problems needing pair programming + deep context; Codex for task queue needing throughput — they complement, not compete
- Claude Code's value compounds over time with investment in CLAUDE.md, SKILL.md, hooks; Codex's value is more immediate/tactical

**Lessons Learned:**
- Codex cannot access local env vars, running services, databases, or local filesystem — only the repo snapshot. This is both its security advantage and its limitation
- Claude Code's seven programmable layers (user prefs → system hooks) create a customization stack that Codex lacks
- Pricing models differ fundamentally: cloud compute (Codex) vs local compute + API tokens (Claude Code) — they scale differently at volume
- Context quality determines output quality: Claude Code wins on context depth (CLAUDE.md + SKILL.md + hooks + MCP), Codex relies on repo-level context only (AGENTS.md)
- "When to use which" decision framework: task parallelism + security isolation → Codex; deep context + local access + iteration → Claude Code

**Action Items:**
- This content should be ingested into wiki as a reference page on AI coding agent comparison (Codex CLI vs Claude Code)
- Could inform wiki pages on: [[Claude Code]], builder tools taxonomy, and competitive landscape tracking