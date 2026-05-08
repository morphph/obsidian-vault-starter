# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a LoreAI blog article comparing OpenAI Codex (2025 agent) vs ChatGPT for developers.

**Key Exchanges:**
- Detailed product comparison article covering code quality, pricing, workflow integration, use-case routing, and limitations

**Decisions Made:**
- Article positions Codex as stronger for repo-level engineering work, ChatGPT as better for learning/brainstorming/quick tasks, and recommends using both strategically
- Pricing breakdown included: Free → Plus ($20/mo) → Pro ($200/mo, required for Codex) → Team ($25-30/user/mo) → Enterprise

**Lessons Learned:**
- OpenAI Codex (2025) is entirely different from the original Codex API (2021, deprecated March 2023) — only shares the name
- Codex uses **codex-1** model, fine-tuned from o3 specifically for software engineering
- Codex is not a standalone product — it's a feature within the ChatGPT platform (Pro/Team/Enterprise only)
- Codex delivers diffs/PRs against actual repos; ChatGPT delivers copy-paste snippets — fundamentally different integration models
- OpenAI offers free Codex access for open-source maintainers and student credit programs

**Action Items:**
- Article references several internal links (`/blog/codex-complete-guide`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/blog/codex-vscode`, `/glossary/what-does-codex-mean`) — ensure these exist or are queued for creation
- Consider ingesting this article's key facts into wiki pages: `openai-codex.md`, `chatgpt.md`, `codex-1-model.md`