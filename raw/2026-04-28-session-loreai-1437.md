# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a draft article comparing OpenAI Codex vs ChatGPT for the LoreAI blog.

**Key Exchanges:**
- Article covers five comparison dimensions: workflow model, pricing, integration/ecosystem, use-case fit, and FAQs
- Codex = autonomous agent (delegate & review PRs); ChatGPT = interactive pair programmer (real-time collaboration)

**Decisions Made:**
- Framed the core tradeoff as "writing code" (Codex) vs "understanding/planning code" (ChatGPT)
- Included a combined workflow pattern (ChatGPT for design → Codex for execution) as the recommended approach
- Pricing positioned as the key practical differentiator for most developers

**Lessons Learned:**
- Codex requires Pro ($200/mo), no free tier — exceptions: open-source maintainers (free) and students ($100 credits)
- ChatGPT free tier or Plus ($20/mo) covers substantial coding help — 10x price gap means Codex must save meaningful hours to justify
- Codex ecosystem still young: GitHub only, no GitLab/Bitbucket/self-hosted Git
- Codex supports OpenAI Agents SDK for custom orchestration workflows
- Codex has a VS Code extension for triggering tasks from editor
- ChatGPT has no native Git integration — manual copy-paste remains the workflow

**Action Items:**
- Article references several internal links (`/blog/codex-complete-guide`, `/blog/agent-harnesses-2026`, `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/blog/codex-vscode`) — ensure these exist or are planned
- Pricing note flagged as "as of April 2026" — will need periodic freshness checks
- Consider ingesting this content into wiki under an OpenAI Codex page if not already tracked