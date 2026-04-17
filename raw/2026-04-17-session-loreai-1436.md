# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing article content comparing OpenAI Codex (agentic coding tool) vs ChatGPT for coding tasks

**Key Exchanges:**
- No actual user exchanges — context contains an article/blog post about Codex vs ChatGPT comparison

**Decisions Made:**
- N/A (no active session decisions)

**Lessons Learned:**
- OpenAI Codex (2025) ≠ old Codex API (code-davinci-002, deprecated 2023) — same name, completely different products
- Codex: full cloud container, GitHub PR integration, full repo context, multi-file ops, runs actual test suites; network access disabled during code execution
- ChatGPT Code Interpreter: Python-only Jupyter kernel, no arbitrary package installs, no Node/Rust/Go execution
- Codex access: Pro ($200/mo), Team, Enterprise only — NOT free or Plus tier; free access for open-source maintainers + $100 credits for students
- Practical combined workflow: ChatGPT for architecture discussion → Codex for implementation → ChatGPT for PR review → Codex for iteration

**Action Items:**
- Consider ingesting this article as a raw source for wiki pages on `openai-codex.md` or `coding-agents.md` — content aligns with domain focus (AI tools, builder workflows)