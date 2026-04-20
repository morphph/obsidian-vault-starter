# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison article (draft) for LoreAI: "Codex vs ChatGPT" — targeting developers choosing between the two OpenAI tools.

**Key Exchanges:**
- Article created as a structured comparison piece with frontmatter metadata (slug: `codex-chatgpt`, category: `tools`, lang: `zh`)
- Core framing: Codex = agentic cloud coding executor; ChatGPT = general-purpose conversational AI. Not competitors — complementary tools.

**Decisions Made:**
- TL;DR verdict: Use Codex for multi-file engineering tasks + GitHub workflows; ChatGPT for learning, general coding Q&A, non-coding tasks
- Internal linking strategy: connects to `codex-complete-guide`, `codex-for-students`, `codex-vscode`, `what-does-codex-mean`, `agentic-coding`
- FAQ section included covering: same model?, pricing, learning use case, replacement question

**Action Items:**
- Draft file likely needs to be saved to `drafts/` directory (if not already done)
- Verify related pages exist: `/zh/blog/codex-for-open-source` is linked but not in `related_blog` frontmatter — may need reconciliation