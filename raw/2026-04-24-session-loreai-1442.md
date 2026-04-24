# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article comparing OpenAI Codex (agentic coding tool) vs ChatGPT for developer workflows.

**Key Exchanges:**
- Article distinguishes Codex as an **async execution engine** (clones repo, runs tests, creates PRs) vs ChatGPT as a **real-time thinking partner** (conversational, no repo context)
- Codex uses a specialized model called **codex-1**, fine-tuned from o-series reasoning models for software engineering tasks
- ChatGPT uses GPT-4o / GPT-4.1 / o-series depending on plan

**Decisions Made:**
- Recommended workflow: think through approach with ChatGPT → hand implementation to Codex → use ChatGPT to review anything unclear
- Codex only justifies cost when delegating enough multi-file implementation tasks to recoup time savings

**Lessons Learned:**
- Codex's closed-loop value multiplies with strong test suites — without tests, you're reviewing code blindly
- Codex optimizes for "make tests pass," which can produce architecturally questionable shortcuts
- Async overhead means Codex only pays off for tasks larger than ~30 seconds of manual coding
- Codex limitations: no internet in sandbox, GitHub-only, no mid-task redirection, $200/mo Pro required
- ChatGPT limitations: no repo context, hallucination risk on API signatures, manual copy-paste burden

**Action Items:**
- Consider ingesting this as a raw source → wiki page on `openai-codex.md` or expanding existing Codex/ChatGPT wiki entries
- Cross-reference with any existing wiki content on coding agents or OpenAI tools