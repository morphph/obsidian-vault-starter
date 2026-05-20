# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing/reviewing a detailed comparison article on OpenAI Codex vs ChatGPT for coding workflows — likely raw source material for wiki ingestion.

**Key Exchanges:**
- Article explains the fundamental distinction: ChatGPT = conversational code assistant (you paste code, get answers); Codex = autonomous coding agent (clones repo, makes changes, runs tests, opens PRs)
- Codex launched in 2025, completely unrelated to the deprecated Codex API (March 2023) that powered early GitHub Copilot

**Decisions Made:**
- None explicitly — this is source content, not a working session

**Lessons Learned:**
- **Codex pricing gateway:** Requires ChatGPT Pro ($200/mo), Team ($25-30/user/mo), or Enterprise. Free Codex access exists for open-source maintainers and discounted for students (as of mid-2026)
- **Codex sweet spot:** Well-defined tasks a junior dev would take 30min–2hr on — bug fixes, test coverage, dependency updates, multi-file refactors
- **Recommended combo pattern:** "ChatGPT for thinking, Codex for doing" — design approach conversationally, then delegate implementation to Codex
- **Codex vs Claude Code positioning:** Codex = cloud-based, GitHub-native, web UI; Claude Code = terminal-first, local execution, git-native
- **Codex limitations:** Less effective on greenfield projects without test suites, open-ended architectural tasks, or quick one-off questions

**Action Items:**
- This article is raw source material — should be ingested via `/ingest` to update wiki pages on: OpenAI Codex, ChatGPT, agentic coding landscape, and competitive positioning vs Claude Code
- Pricing data is freshness-sensitive (article notes this explicitly) — wiki page should flag staleness risk