# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting an article comparing OpenAI Codex (2025 agent) vs ChatGPT for professional coding workflows.

**Key Exchanges:**
- Article covers: interaction model, code quality/verification, repo context, pricing, IDE integration, and when to use each tool

**Decisions Made:**
- N/A (no decisions made in this session — content was presented, not discussed)

**Lessons Learned:**
- **Codex (2025) ≠ original Codex API (2021)**: Original was a GPT-3 fine-tune powering Copilot autocomplete, deprecated March 2023. Current Codex is an agentic coding platform built on `codex-1` (fine-tuned from o3), working in isolated cloud sandboxes and delivering results as PRs.
- **Key architectural difference**: Codex = delegated agent (async, repo-aware, runs tests); ChatGPT = pair programmer (sync, context-limited, no test execution).
- **Codex value prop depends on test coverage**: Without tests, Codex loses its verification advantage.
- **Pricing**: Codex requires Pro ($200/mo) or Team ($25/user/mo). Free access exists for students and open-source maintainers.
- **Recommended workflow**: Use ChatGPT for exploration/design → Codex for well-defined execution → ChatGPT to review generated code.

**Action Items:**
- Consider ingesting this as a wiki page (`openai-codex-vs-chatgpt.md`) under the AI/LLM tools category, cross-linking to any existing Codex or OpenAI pages.