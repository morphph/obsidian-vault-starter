# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User reviewed an article comparing OpenAI Codex vs ChatGPT for potential ingestion into the LoreAI knowledge base.

**Key Exchanges:**
- The article is a comparison piece covering execution model, use cases, pricing, and workflow integration between OpenAI Codex and ChatGPT.

**Decisions Made:**
- No tools were used; this appears to be a flush/summary pass over ingested or reviewed source content.

**Lessons Learned:**
- **Codex vs ChatGPT mental model:** Codex = task executor (repo-aware, async, sandboxed, runs tests, produces PRs); ChatGPT = thinking partner (conversational, instant, general-purpose, no repo access)
- **Codex execution model:** Clones repo into sandboxed container, installs deps, runs test suite, self-corrects, produces a diff/PR — not a chat response
- **Key limitation of ChatGPT for code:** Cannot verify output; no access to cross-file context, imports, or your test suite
- **Pricing gate:** Codex requires Pro ($200/mo), Team ($25/user/mo), or Enterprise. Free/Plus tiers excluded. Student ($100 credits) and open-source maintainer (free Pro) exceptions exist.
- **They are always bundled:** At tiers where Codex is available, ChatGPT is always included — the choice is which to reach for, not which to buy
- **Use Codex when:** Well-defined task, multi-file, GitHub-hosted, test suite exists, async is acceptable
- **Use ChatGPT when:** Interactive debugging, learning, design exploration, non-code work, no GitHub repo

**Action Items:**
- Consider ingesting this article into the wiki under a page like `openai-codex.md` or `agentic-coding-tools.md` — good source for the "Builder tools and workflows" domain focus