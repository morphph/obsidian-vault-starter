# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a blog article comparing Claude Code vs OpenAI Codex for potential wiki ingestion.

**Key Exchanges:**
- The content is a full-length article (likely from LoreAI blog) titled something like "Claude Code vs Codex: When to Use Each"
- Covers architecture, workflow, context handling, parallelism, pricing, extensibility, security, and decision framework

**Decisions Made:**
- No explicit decisions recorded — this appears to be a pre-session flush with no prior tool activity or user interaction captured

**Lessons Learned:**
- Codex runs in cloud sandbox (no internet during execution), Claude Code runs locally with full env access
- Claude Code = synchronous pair programmer; Codex = async task queue
- Codex parallelism is cloud-native (multiple tasks, no local resource cost); Claude Code parallelism is sub-agent-based within one session
- Codex tasks are fully isolated — cannot coordinate across concurrent tasks
- Claude Code has deep config system (CLAUDE.md, SKILL.md, hooks, MCP); Codex only has a setup script
- Pricing: Claude Code on Pro/Max ($20–200/mo); Codex included with ChatGPT Pro ($200/mo) / Team ($30/user)
- Security: Codex sandboxed (no exfiltration risk); Claude Code requires permission approval discipline

**Action Items:**
- Consider ingesting this article as a raw source → wiki page on `claude-code-vs-codex.md` or updating existing `claude-code.md` with a Codex comparison section
- Source appears to be a LoreAI blog post — worth archiving to `raw/` if not already there