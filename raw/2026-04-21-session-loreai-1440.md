# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting an article comparing OpenAI Codex (2025) vs ChatGPT for coding workflows.

**Key Exchanges:**
- Article content covers Codex vs ChatGPT across: async/sync execution model, repo context, code quality, GitHub integration, pricing, and capability scope

**Decisions Made:**
- N/A (no interactive decisions in this context — content was presented for review)

**Lessons Learned:**
- **Codex (2025) ≠ old Codex API**: Original Codex API deprecated March 2023; current Codex (May 2025) is a cloud coding agent fine-tuned on o3. Different product entirely.
- **Core distinction**: Codex = async delegation (clone repo, run unattended, return PR); ChatGPT = synchronous interactive loop
- **Codex strengths**: Multi-file repo changes, test writing, refactoring — tasks with clear upfront spec and existing tests to validate
- **ChatGPT strengths**: Exploratory/explanatory work, debugging, mixed-domain tasks (code + docs + data), no-repo snippets
- **Codex limitation**: No internet access, no external API calls in sandbox — intentional isolation
- **Pricing gate**: Codex requires Pro ($200/mo), Team ($30/user/mo), or Enterprise. Not on Free or Plus. Open source maintainers may get free access.
- **Hybrid workflow pattern**: ChatGPT to design → Codex to implement → ChatGPT to review issues → Codex to fix

**Action Items:**
- Consider ingesting this article into wiki as a page on OpenAI Codex or agentic coding tool comparison (if not already done)