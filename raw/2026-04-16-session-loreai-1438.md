# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewed a detailed comparison article between OpenAI Codex (agent) and ChatGPT for coding tasks.

**Key Exchanges:**
- Article covers Codex vs ChatGPT across: execution model, GitHub integration, pricing, model differences, security, and use case fit

**Decisions Made:**
- This content is worth ingesting into the wiki — it covers AI tool capabilities, pricing, and workflows, squarely within domain focus

**Lessons Learned:**
- OpenAI Codex (May 2025) ≠ old Codex model (deprecated March 2023). New Codex is a cloud-based coding **agent**, not a code-generation API
- Codex uses **codex-1** (fine-tuned from o3); ChatGPT defaults to GPT-4o
- Codex is **async + container-based**: clones repo, runs tests, opens PRs. ChatGPT code interpreter is **sync + sandboxed Python only** — no repo access
- Codex requires **ChatGPT Pro ($200/mo)**. Free access: open-source maintainers + students ($100 credits). No general free tier
- Codex reads GitHub Issues natively; ChatGPT has zero GitHub integration
- Strongest workflow: ChatGPT for design/exploration → Codex for implementation/PRs

**Action Items:**
- Consider `/ingest`-ing this article as a raw source and creating a `openai-codex-agent.md` wiki page covering: capabilities, pricing, codex-1 model, GitHub integration, comparison with ChatGPT