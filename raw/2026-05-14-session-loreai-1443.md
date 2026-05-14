# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on OpenAI Codex vs ChatGPT for the LoreAI blog.

**Key Exchanges:**
- Detailed breakdown of ChatGPT tiers (Free/Plus $20/Pro $200) vs Codex access (Pro/Team $25·user/Enterprise only)
- Codex uses `codex-1`, a code-specialized fine-tuned model with a closed feedback loop (clones repo, runs tests, iterates)
- ChatGPT generates code without execution feedback (except Python via Code Interpreter) — verification burden falls on the user

**Decisions Made:**
- Article positions Codex and ChatGPT as **complementary, not competing** — different points in the dev workflow
- Use-case split: Codex for repo-aware autonomous tasks (multi-file features, refactoring, test generation); ChatGPT for interactive/breadth tasks (learning, snippets, architecture discussions, non-coding)
- Codex best suited for senior engineers comfortable reviewing PRs; ChatGPT better for newcomers and mixed workflows

**Lessons Learned:**
- Codex has no standalone subscription — it's bundled into ChatGPT Pro/Team/Enterprise tiers
- OpenAI offers free Codex access via student and open-source maintainer programs (worth noting for wiki)
- Quality gap between the two scales with task complexity: comparable for single functions, Codex wins on multi-file work due to test validation loop
- Codex's async workflow (assign morning, review after lunch) fits naturally into team dev processes

**Action Items:**
- Consider ingesting this article's facts into wiki pages: `openai-codex.md`, `chatgpt.md`, and possibly `openai-pricing.md`
- Verify pricing/tier info is current (data may shift — Pro $200/mo, Team $25/user/mo as of article date)