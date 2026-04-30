# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: OpenAI Codex vs ChatGPT for coding tasks (likely for LoreAI blog).

**Key Exchanges:**
- Codex (2025) is NOT the same as the deprecated Codex API (2021) — completely different product, now a cloud-based coding agent on codex-1 model
- Codex is bundled into ChatGPT, not a separate product — requires Pro ($200/mo), Team ($30/seat/mo), or Enterprise
- Core distinction: Codex = async execution agent with GitHub integration; ChatGPT = interactive conversational coding

**Decisions Made:**
- Article frames the tools as complementary, not competitive: "think in ChatGPT, execute in Codex"
- Task suitability matrix: Codex wins on well-defined delegatable tasks (bug fixes, test coverage, refactoring); ChatGPT wins on exploratory/ambiguous tasks (debugging unclear issues, architecture design, learning)

**Lessons Learned:**
- Codex sandbox has no internet access — can't fetch packages not in lockfile
- Codex is limited to GitHub-hosted repos only
- The combined workflow loop (explore → delegate → review → debug → fix) is the recommended pattern for power users
- Entry-level pricing gap: Plus ($20) → Pro ($200) is a big jump solely for Codex access; Team tier ($30/seat) is more accessible for orgs

**Action Items:**
- Article references several internal links that need to exist: `/blog/codex-for-students`, `/blog/codex-complete-guide`, `/blog/codex-for-open-source`, `/glossary/agentic-coding`, `/glossary/what-does-codex-mean`
- Consider ingesting this into wiki as an OpenAI Codex page covering pricing, capabilities, and positioning vs ChatGPT