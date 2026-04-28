# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article draft comparing OpenAI Codex vs ChatGPT for developers — likely for LoreAI publication.

**Key Exchanges:**
- Codex is an **agentic coding tool** — clones repo, reads codebase, writes code, runs tests, opens PRs autonomously. Runs on `codex-1` model (fine-tuned from o3).
- ChatGPT is **conversational** — interactive, manual code extraction, no repo access.
- Codex requires **ChatGPT Pro ($200/mo)** or Team/Enterprise. No free tier. ChatGPT free tier available, Plus at $20/mo.
- Codex has a **VS Code extension** for in-editor task assignment.
- Codex is **limited to GitHub repos** as of early 2026.

**Decisions Made:**
- Article positioning: not "which is better" but "match the tool to the task"
- Three complementary usage patterns identified: (1) ChatGPT for design → Codex for implementation, (2) ChatGPT for learning → Codex for production, (3) ChatGPT for triage → Codex for execution

**Lessons Learned:**
- Codex's key differentiator is the **self-verification loop** (run tests → fix → rerun) — catches bugs ChatGPT cannot detect
- Codex is overkill for single-file/quick tasks due to spin-up time
- ChatGPT loses coherence on tasks spanning many files — context management is manual
- For teams, Codex's PR-based output creates an **audit trail**; ChatGPT output is invisible to the team
- OpenAI offers limited free Codex credits for students and open-source maintainers

**Action Items:**
- Article references internal links (`/blog/codex-complete-guide`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/glossary/agentic-coding`, `/blog/con-u-pour-des-workflows-multi-agents`) — verify these exist before publishing
- Consider ingesting this into wiki as a page on **OpenAI Codex** product positioning and pricing (updates existing knowledge about OpenAI's developer tools landscape)