# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/raw article comparing OpenAI Codex (autonomous coding agent) vs ChatGPT for software development tasks.

**Key Exchanges:**
- Article is a comprehensive Codex vs ChatGPT comparison piece for LoreAI blog, covering architecture differences, workflow integration, pricing, limitations, and when to use each

**Decisions Made:**
- OpenAI Codex (2024+) is a completely different product from the deprecated 2023 Codex API model — autonomous agent vs code-generation API
- Codex requires Pro ($200/mo), Team ($30/user/mo), or Enterprise; not available on Free or Plus ($20/mo)
- Codex is GitHub-only (no other Git hosts natively supported)
- Codex uses task-based credit system; complexity determines credit consumption

**Lessons Learned:**
- Codex's strength: full repo context, autonomous execution, self-validation via test/lint/typecheck loop, async parallel task dispatch
- ChatGPT's strength: interactive exploration, debugging, architecture discussions, learning, non-code tasks (docs, specs, communication)
- Best practice workflow: ChatGPT for design/review/debug phases, Codex for implementation/systematic fixes
- Codex task quality depends heavily on task description specificity — vague prompts produce poor results
- ChatGPT code suggestions may not compile since it lacks execution feedback against your actual codebase

**Action Items:**
- Article references several internal links (`/blog/codex-complete-guide`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/glossary/agentic-coding`, `/glossary/what-does-codex-mean`) — verify these exist or queue them for creation
- Consider ingesting this as a raw source and creating/updating wiki pages for: OpenAI Codex (product), agentic coding landscape, AI coding tool pricing models