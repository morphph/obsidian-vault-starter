# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on OpenAI Codex vs ChatGPT for the LoreAI blog.

**Key Exchanges:**
- Detailed breakdown of ChatGPT pricing tiers: Free, Plus ($20/mo), Pro ($200/mo), Team ($25/user/mo), Enterprise (custom)
- Codex access is bundled into Pro, Team, and Enterprise — no separate Codex subscription exists
- Codex uses **codex-1**, a specialized model fine-tuned from OpenAI's reasoning model family, distinct from GPT-4o used by ChatGPT
- OpenAI offers free Codex for students and open-source maintainers

**Decisions Made:**
- Framing: Codex and ChatGPT are complementary, not competitors (coding agent vs conversational assistant)
- Codex wins for autonomous implementation (bug fixes, test coverage, refactoring, dependency upgrades, scaffolding)
- ChatGPT wins for conversational/exploratory tasks (design discussions, code explanation, quick snippets, learning)
- Recommended hybrid workflow: ChatGPT for planning → Codex for implementation → ChatGPT for review → Codex for iteration

**Lessons Learned:**
- Codex limitations: no real-time interaction, sandbox constraints, GitHub-only, $200/mo minimum for individuals, requires well-scoped tasks
- ChatGPT limitations: no codebase awareness, no execution against real code, copy-paste friction, no cross-session persistence, hallucination risk without execution verification
- Decision heuristic: if you'd assign Codex multiple tasks/day, Pro plan justified; if coding questions a few times/week, Plus suffices
- For teams already on ChatGPT Team/Enterprise, Codex is included — natural evolution, not a new purchase

**Action Items:**
- Article references internal links (`/blog/codex-complete-guide`, `/blog/coding-agents-reshaping-epd`, `/glossary/agentic-coding`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/faq/codex-download`) — ensure these pages exist or are created
- Consider ingesting this into wiki as an OpenAI pricing/product page covering Codex and ChatGPT positioning