# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/review of a comparison article: "Codex CLI vs Claude Code" — a comprehensive guide for the LoreAI blog.

**Key Exchanges:**
- Article covers architecture differences (sandboxed cloud vs local terminal), workflow models (async delegation vs sync pair-programming), safety approaches (isolation vs permission gating), pricing, and IDE options
- Clarifies that Codex CLI ≠ the old OpenAI Codex model (GPT-3 based, now retired) — common source of confusion

**Decisions Made:**
- Framing: tools are **complementary, not competing** — choice depends on task shape, not which is "better"
- Codex CLI = task delegation tool ("junior dev in a clean room"); Claude Code = pair-programming partner ("sits at your desk")
- Hybrid approach recommended: Codex CLI for batch/independent tasks, Claude Code for exploratory/interactive work

**Lessons Learned:**
- Async (Codex CLI) works best when tasks are well-scoped with clear acceptance criteria; vague tasks produce vague results
- Claude Code's advantage grows with project complexity — multiple services, env-specific config, running databases, external APIs
- Codex CLI parallel tasks can't coordinate — merge conflicts discovered at PR time, not during execution
- Claude Code's agent teams (sub-agents) share local env so they can coordinate, but consume local resources
- For regulated/strict-security environments, Codex CLI sandboxing provides stronger default boundary
- CLAUDE.md + SKILL.md system is called out as a significant Claude Code advantage for teams with structured documentation

**Action Items:**
- Article references several internal links (`/blog/...`, `/subscribe`) — ensure these are valid before publishing
- Cross-links to related articles: Claude Code enterprise engineering (Ramp/Shopify/Spotify), Claude Code security guide, multi-agent workflows, 5 Claude Code skills, Codex for open-source/students
- Consider ingesting this as a wiki page (e.g., `wiki/codex-cli-vs-claude-code.md`) since it captures useful competitive intelligence on AI coding tools