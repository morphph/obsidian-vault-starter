# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage run for Claude Code content pipeline — 20 detected events from Twitter/HackerNews reviewed for wiki/blog refresh and creation actions.

---

**Key Exchanges:**

- Signal triage classified 20 events: 7 ignored/retweets, 8 refresh-only, 5 refresh_and_create, 1 create-only
- Two major Claude Code product launches detected: **Desktop App redesign** (parallel sessions, new sidebar) and **Routines** (scheduled/API/event triggers, serverless)
- Version updates logged: **2.1.105** (37 CLI changes, stream abort fallback) and **2.1.108** (claude-api skill routing rewrite, new built-in Skills: init, PR review, security-review)

---

**Decisions Made:**

- GLM-5.1 vs Claude Code anecdotal tweet → ignored (no data)
- Pure retweets (signals 7, 8) → ignored
- Claude Code Desktop App redesign (signals 3, 4, 6) → refresh `topics/claude-code`, create desktop app launch blog
- Routines (signals 5, 18) → refresh topic hub, create blog + FAQ (two content types warranted)
- Houtini MCP 93% token savings claim → refresh pricing FAQ + MCP setup blog, create tutorial ("reduce Claude Code token costs MCP")
- claude-code-best-practice repo trending #1 on GitHub (19.7K stars) → refresh topic hub, create best-practices roundup blog
- Autonomous agent-optimizing-agent loop (Vercel AI SDK) → create tutorial on autonomous optimization loops

---

**Lessons Learned:**

- `CLAUDE_INVOKED_BY` env var is the recursion guard for Pipeline B — must be set when auto-compiling raw files
- `--dangerously-disable-streaming` flag noted as minor but concrete CLI reference item (terminal flicker fix)
- CLAUDE.md-as-AI-infrastructure pattern (mistake → rule, repetition → workflow, breakage → guardrail) is gaining viral traction — strong team adoption framing
- MCP is expanding beyond dev tooling: organizational knowledge layer for sales/marketing, Microsoft Power Apps official server, custom API scaffolding tools

---

**Action Items:**

| Priority | Content Type | Target Keyword |
|---|---|---|
| High | Blog | claude code desktop app parallel sessions 2026 |
| High | Blog + FAQ | claude code routines scheduled agents setup |
| High | Blog | claude code best practices guide 2026 |
| Medium | Tutorial | reduce claude code token costs MCP server |
| Medium | Tutorial | claude code autonomous agent optimization loop |
| Low | Refresh | CLI FAQ: v2.1.105 stream abort fallback, v2.1.108 skill routing |
| Low | Refresh | Comparison pages: claude-code-vs-cursor, claude-code-vs-codex (Epitaxy release context) |