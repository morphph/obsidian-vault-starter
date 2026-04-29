# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a LoreAI article comparing OpenAI Codex vs ChatGPT for coding use cases.

**Key Exchanges:**
- Article establishes that Codex and ChatGPT are architecturally different products (async sandbox agent vs. chat interface), not just branding variations
- Verdict recommends "use both" for professional developers — ChatGPT for exploration, Codex for defined implementation tasks

**Decisions Made:**
- Codex positioning: async agent that executes in a sandbox, not a conversational tool. Key differentiator is autonomous execution + codebase context, not code quality per se
- Pricing gate: Codex requires Pro ($200/mo), Team ($25/user/mo), or Enterprise. Free access exists for students and open-source maintainers via separate programs
- Target audience split: professionals → Codex; learners/occasional users → ChatGPT

**Lessons Learned:**
- ChatGPT's limitation is **integration**, not generation — it writes good code but lacks project context
- Codex validates output against test suites, which is its structural advantage over conversational code gen
- ChatGPT's Advanced Data Analysis runs Python only; Codex runs any language/toolchain in a full Linux sandbox

**Action Items:**
- Article references internal links (`/glossary/what-does-codex-mean`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/subscribe`) — ensure these destination pages exist on LoreAI
- Consider ingesting this as a raw source and creating/updating wiki pages for `openai-codex.md` and related entries