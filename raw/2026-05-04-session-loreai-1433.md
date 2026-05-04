# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: OpenAI Codex vs ChatGPT for coding workflows (likely for LoreAI blog).

**Key Exchanges:**
- Full article produced covering Codex (async coding agent) vs ChatGPT (sync conversational AI) across multiple dimensions: workflow model, repo integration, output verification, use cases, pricing, limitations

**Decisions Made:**
- Article structure: async vs sync → repo access → verification → use cases → pricing → limitations → when to choose each → using both together → verdict → FAQ
- Verdict framing: not either/or — Codex for defined multi-file tasks, ChatGPT for exploration/learning/quick questions; most devs use both

**Lessons Learned:**
- **Codex key facts (as of early 2026):** async cloud agent, clones full repo into sandbox, runs tests to self-verify, outputs PRs, uses `AGENTS.md` for project config, no internet during execution, GitHub-only, has VS Code extension
- **Pricing:** Codex bundled with Pro ($200/mo), Team ($30/user/mo), Enterprise only — not on Free or Plus ($20/mo). Student program offers $100 free credits.
- **Codex sweet spot:** clearly defined tasks, multi-file changes, codebases with good test coverage
- **ChatGPT sweet spot:** exploration, learning, quick syntax, architecture discussion, non-code work, budget-conscious users
- **Complementary workflow pattern:** Explore in ChatGPT → Execute in Codex → Review in ChatGPT → Iterate in Codex

**Action Items:**
- Article contains internal links (`/blog/codex-for-students`, `/blog/codex-vscode`, `/blog/codex-complete-guide`, `/subscribe`) — ensure these destination pages exist or are planned
- Consider ingesting this into wiki as an OpenAI Codex page and/or ChatGPT page if not already covered
- Pricing and feature access may shift — flag for periodic review