# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comparative article about OpenAI Codex (2025 agentic tool) vs ChatGPT for software development

**Key Exchanges:**
- Article covers architecture, pricing, use cases, and tradeoffs between the two tools
- Key distinction: Codex = async agentic executor (clones repo, runs tests, produces PRs); ChatGPT = sync conversational partner (no repo access, blind code generation)

**Decisions Made:**
- Recommended workflow: ChatGPT for exploration/design → Codex for implementation → ChatGPT for review → Codex for follow-up fixes

**Lessons Learned:**
- **Naming confusion is real**: Old Codex API (2021, deprecated Mar 2023) vs new Codex product (2025). Search results are noisy; only trust sources from 2025+
- Codex uses `codex-1`, a model fine-tuned from o3 specifically for agentic SE tasks
- Codex sandbox has **no internet access** — packages not in lock file and external API calls during tests will fail
- Codex only sees committed code — local uncommitted changes don't exist in its world
- Codex is NOT separately purchasable; requires Pro ($200/mo), Team ($25/user), or Enterprise

**Action Items:**
- Consider creating/updating a `wiki/openai-codex.md` page with these facts (pricing, architecture, codex-1 model, naming history)
- Cross-link to any existing [[ChatGPT]], [[agentic coding]], or [[OpenAI]] wiki pages
- Note: Students get $100 free Codex credits; open-source maintainers get free Pro access — worth tracking as program details may change