# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comparative article on Claude Code vs OpenAI Codex for the wiki knowledge base.

**Key Exchanges:**
- Source document is a detailed comparison article contrasting Claude Code (interactive, local, terminal-based) vs OpenAI Codex (async, cloud-sandboxed, PR-based)

**Decisions Made:**
- N/A (no interactive decisions in this session — context is article content only)

**Lessons Learned:**
- Codex runs in isolated cloud containers with **no internet access** — cannot fetch packages or call APIs during execution; changes only land when PR is explicitly merged
- Claude Code = pair programming model (real-time, interactive, local env access); Codex = delegation model (async, batch, review-after)
- Claude Code has persistent project context via CLAUDE.md + memory system; Codex has no cross-task memory — rediscovers conventions each task
- Codex enables true parallelism (multiple simultaneous tasks in separate containers); Claude Code is one session at a time (though agent teams add sub-agent parallelism)
- Pricing: Claude Code via Anthropic Max ($100–$200/mo) or API usage-based; Codex bundled in ChatGPT Pro/Team/Enterprise ($20–$200/mo)
- Privacy difference: Claude Code code stays local; Codex uploads repo to OpenAI cloud per task

**Action Items:**
- Consider ingesting this article as a raw source (`raw/`) and creating a `wiki/claude-code-vs-codex.md` page covering the tool comparison, decision rules, and pricing summary