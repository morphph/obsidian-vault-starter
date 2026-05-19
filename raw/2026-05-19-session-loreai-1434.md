# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article draft/source comparing OpenAI Codex (autonomous coding agent) vs ChatGPT (conversational coding assistant).

**Key Exchanges:**
- Codex = autonomous agent: clones repo, writes code, runs tests, returns diff. Best for well-defined, testable tasks.
- ChatGPT = conversational partner: interactive debugging, architecture discussions, learning. You are the feedback loop.
- Codex quality scales with test coverage; ChatGPT quality scales with how well you describe the problem.

**Decisions Made:**
- Codex requires Pro tier ($200/mo); ChatGPT Plus ($20/mo) covers most individual dev needs. No middle ground — 10x jump from chat to agent.
- Recommended workflow: **think with ChatGPT, execute with Codex**. Use ChatGPT to explore problem space → hand well-specified task to Codex.

**Lessons Learned:**
- Codex has deep/narrow context (sees full repo, no conversation history); ChatGPT has shallow/wide context (sees conversation, not full repo). Tradeoff matters for task selection.
- Codex wins: bug fixes with repro steps, boilerplate, multi-file refactoring, test writing, dependency updates.
- ChatGPT wins: architecture discussions, debugging unfamiliar code, code review, learning, quick one-offs.
- Codex's self-correction loop (write → test → iterate) is its core advantage — loses value in repos with minimal tests.
- Codex VS Code extension bridges the gap between agent capabilities and editor-centric workflows.

**Action Items:**
- This content should be ingested as a raw source and fanned out to wiki pages on: OpenAI Codex, AI coding agents comparison, agentic vs conversational AI tools, and pricing models for AI dev tools.