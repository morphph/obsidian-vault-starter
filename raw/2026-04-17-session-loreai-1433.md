# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article content comparing ChatGPT vs OpenAI Codex — likely for LoreAI blog or draft ingestion.

**Key Exchanges:**
- No user-AI dialogue present; content is a standalone comparison article.

**Decisions Made:**
- N/A

**Lessons Learned:**
- Codex runs on **codex-1**, fine-tuned from o3 specifically for software engineering (not the same as ChatGPT's model suite)
- Codex requires **ChatGPT Pro ($200/mo)** minimum — not available on free or Plus tiers
- Codex key differentiator: runs in isolated cloud containers, clones repo, executes tasks async, delivers output as GitHub PRs with full audit log
- ChatGPT differentiator: interactive, immediate, no repo connection, works for non-coding tasks, available from $0–$20/mo
- Dividing line: **single-step → ChatGPT; multi-file/multi-step → Codex**
- Codex has network access **disabled by default** during task execution (security property worth noting)
- ChatGPT conversations may be used for model training unless opted out (Team/Enterprise disables this)

**Action Items:**
- This article content may be a candidate for `/ingest` into the wiki as a source on OpenAI Codex or for a draft page on `chatgpt-vs-codex.md` or `openai-codex.md`