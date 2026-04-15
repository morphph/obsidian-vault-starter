# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a source article comparing OpenAI Codex vs ChatGPT for coding workflows.

**Key Exchanges:**
- The article covers: async vs sync workflow, repo access, task type fit, pricing tiers, quality/reliability differences, and workflow integration patterns.

**Decisions Made:**
- N/A (this appears to be a passive review of source content, not an interactive session with decisions)

**Lessons Learned:**
- **Codex = async execution agent**: spins up sandbox, clones full repo, runs tests, opens PRs. Best for multi-file, well-defined, delegatable tasks.
- **ChatGPT = sync conversation**: no repo context, zero friction, best for exploration, debugging, quick snippets, architecture discussion.
- **Decision rule**: "If you can write it as a ticket a competent dev could pick up without clarification → Codex. If you need to explore → ChatGPT."
- **Pricing**: Codex requires paid plan (Plus $20/mo minimum); consumes compute credits per task. Free tier = ChatGPT only.
- **Combined workflow**: Plan with ChatGPT → implement with Codex → debug issues with ChatGPT → refine with Codex.
- Codex has self-verification loop (runs tests before delivering); ChatGPT output is unverified against actual project.

**Action Items:**
- Consider ingesting this article as a raw source if it's from LoreAI's content pipeline (source appears to be a blog article, possibly from loreai.dev or an external site being tracked).