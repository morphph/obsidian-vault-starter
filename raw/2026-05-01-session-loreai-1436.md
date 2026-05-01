# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing/reviewing a detailed comparison article: OpenAI Codex vs ChatGPT for coding tasks (likely for LoreAI blog or wiki ingest).

**Key Exchanges:**
- Comprehensive product comparison between OpenAI Codex (autonomous coding agent) and ChatGPT (conversational AI assistant)
- Article positions them as **different categories of tool**, not competitors — "like comparing a CI pipeline to a pair-programming session"

**Decisions Made:**
- Codex uses dedicated model `codex-1` optimized for agentic coding, not the same GPT-4o/o3 models ChatGPT uses
- Codex requires GitHub integration — no GitLab/Bitbucket/self-hosted support as of early 2026
- Codex works via sandboxed cloud containers: clones repo → executes → outputs PR/diff (batch/async model)

**Lessons Learned:**
- **Pricing structure (as of article date):** Codex entry point is $200/mo (Pro) for individuals, $25/user/mo (Team) for orgs. ChatGPT free tier exists; Plus at $20/mo. Pro includes both tools.
- **Codex strengths:** Multi-file refactoring, bug fixes with test verification, codebase-wide migrations, CI fixes — anything requiring full repo context
- **ChatGPT strengths:** Learning/explanation, quick snippets, code review discussion, prototyping, non-code work, platform-agnostic
- **Key Codex limitation:** Async-only execution means no mid-task steering; cloud sandbox can't handle env-specific tasks (DB connections, hardware, proprietary SDKs)
- Student and open-source maintainer programs exist for free Codex credits

**Action Items:**
- This content should be ingested into wiki as raw source — covers OpenAI Codex product details, pricing, and competitive positioning vs ChatGPT
- Relevant wiki pages to create/update: `openai-codex.md`, potentially `agentic-coding.md`, update `chatgpt.md` if it exists