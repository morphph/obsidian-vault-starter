# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User shared a long-form article comparing OpenAI Codex (2025 agentic tool) vs ChatGPT for developer workflows.

**Key Exchanges:**
- Article covers: async vs sync model, codebase awareness, task complexity thresholds, code quality/verification, pricing, and use case split between the two tools.

**Decisions Made:**
- (None — no tool calls or user decisions made this session; content was presented, not acted on)

**Lessons Learned:**
- **Critical naming confusion**: "Codex" refers to two different products — the deprecated 2021 GPT-3-based code completion API (sunset March 2023) and the 2025 cloud-based autonomous coding agent. Any pre-2024 references to "Codex" mean the old API.
- **Core distinction**: Codex = async, repo-connected, test-running agent that produces PRs. ChatGPT = sync, clipboard-limited, explanatory conversation partner.
- **Crossover threshold**: Tasks touching >2–3 files or requiring test-suite verification favor Codex. Below that, ChatGPT's immediacy wins.
- **Pricing gate**: Codex requires Pro ($200/mo) or Team/Enterprise. No free or Plus ($20/mo) access. Free tier exists only for open-source maintainers.
- **Hybrid workflow pattern**: Use ChatGPT to explore/design → write clear spec → hand to Codex for implementation → use ChatGPT to discuss PR review findings.

**Action Items:**
- Consider ingesting the article as a raw source and creating a `wiki/openai-codex.md` or `wiki/codex-vs-chatgpt.md` page capturing the async/sync distinction, pricing, and naming confusion.