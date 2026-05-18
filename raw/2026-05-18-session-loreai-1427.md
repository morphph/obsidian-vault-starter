# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/review of a blog article comparing OpenAI Codex vs ChatGPT for coding workflows (likely for LoreAI blog).

**Key Exchanges:**
- Comprehensive comparison of Codex (agentic task executor) vs ChatGPT (conversational coding partner) — two distinct paradigms within the same platform
- Codex uses codex-1 model (fine-tuned from o3), runs in sandboxed cloud env with full repo access, outputs PRs
- ChatGPT remains request-response; human is the execution engine

**Decisions Made:**
- Article positions the tools as complementary, not competitive — "different tools in the same toolbox"
- Verdict: Pro plan ($200/mo) with both tools is optimal for professional devs; Plus ($20/mo) better for learners

**Lessons Learned:**
- Codex limitations worth tracking: GitHub-only (no GitLab/Bitbucket), no internet during execution, can't fetch packages outside lock file, async-only (no pair programming)
- Codex pricing: Pro $200/mo or Team $25/user/mo — no access on Free or Plus plans
- OpenAI has free Codex programs for open source maintainers and students
- The "combined workflow" pattern: ChatGPT for planning/spec → Codex for execution/testing → ChatGPT for review questions → Codex for iteration
- Codex's closed-loop test verification (runs your test suite, iterates on failures) is the key differentiator over conversational coding

**Action Items:**
- Article references several internal links (`/glossary/agentic-coding`, `/blog/codex-for-students`, `/blog/codex-vscode`, `/blog/codex-for-open-source`, `/blog/con-u-pour-des-workflows-multi-agents`) — ensure these pages exist or are drafted
- Consider ingesting this as a raw source and updating wiki pages for `openai-codex`, `chatgpt`, and pricing/model pages
- Pricing info is time-sensitive (as of mid-2026) — flag for staleness checks in future `/lint` runs