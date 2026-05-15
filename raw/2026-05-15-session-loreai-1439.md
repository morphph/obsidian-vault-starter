# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing/reviewing a draft article comparing OpenAI Codex (agentic coding tool) vs ChatGPT (conversational assistant) for the LoreAI blog.

**Key Exchanges:**
- Codex = **agent** (autonomous, clones repo, runs tests, produces PRs). ChatGPT = **assistant** (interactive, human-in-the-loop, no project access).
- Core distinction maps to **execution vs exploration**: know what to do → Codex; figuring out what to do → ChatGPT.
- Codex's killer advantage: direct repository integration eliminates the "context gap" of pasting code into chat.
- Codex self-verifies by running tests; ChatGPT code is unverified by default.

**Decisions Made:**
- Article positions the two as **complementary, not competing** — this is the editorial thesis.
- Recommended workflow: explore in ChatGPT → assign to Codex → review PR → debug in ChatGPT → iterate with Codex.
- Pricing framing: Pro at $200/mo is "expensive for individuals, cheap vs developer time."

**Lessons Learned:**
- ChatGPT Code Canvas is a scratchpad, not a dev environment — cannot run project tests or install project deps.
- Codex is overkill for ambiguous tasks needing iterative refinement — re-assigning costs more than just chatting.
- ChatGPT is better for learning (interactive explanation) vs Codex (produces finished code without teaching).
- Free tier ChatGPT still covers casual code Q&A; Codex requires paid plan (Plus gets limited, Pro gets full).

**Action Items:**
- This content should be ingested into wiki as knowledge about OpenAI's product lineup (Codex positioning, pricing tiers, ChatGPT capabilities).
- Relevant wiki pages to update/create: OpenAI Codex, agentic coding patterns, AI coding tools comparison.
- Article contains internal links (`/blog/codex-complete-guide`, `/blog/codex-for-students`, `/glossary/agentic-coding`) — these are LoreAI site links, worth tracking as content inventory.