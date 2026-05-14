# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a Claude Code vs OpenAI Codex comparison article for the LoreAI blog.

**Key Exchanges:**
- Detailed feature-by-feature comparison covering: execution model (sync vs async), context/config systems, code quality validation, pricing, IDE integration, and extensibility
- Claude Code = real-time pair programming (terminal-native, local env access, 7 programmable layers)
- Codex = async task delegation ("assigning tickets to a junior dev", cloud sandbox, fire-and-forget)

**Decisions Made:**
- Verdict: Neither tool is universally better — they optimize for different workflows (control vs delegation spectrum)
- Recommended hybrid approach: Claude Code for interactive sessions (debugging, architecture, multi-service work); Codex for well-defined parallelizable tasks (tests, boilerplate, validation)
- Article structure follows comparison pattern: shared sections → "When to Choose X" → verdict → FAQ

**Lessons Learned:**
- Codex's sandbox has no internet access during execution — strong isolation but can't verify against real external services
- Claude Code's extensibility advantage compounds over time (skills, hooks, MCP encode team standards once); Codex trades configurability for simplicity
- codex-1 was trained with RL on real coding tasks using test outcomes as reward signals — specialized for code that passes tests
- Codex pricing bundled into ChatGPT Pro ($200/mo); Claude Code via API credits or Pro/Max subscriptions — cost comparison is usage-volume dependent
- Codex now has VS Code extension + mobile task submission; Claude Code has terminal + VS Code + JetBrains + web + desktop

**Action Items:**
- Article references related pages that should exist in wiki: Claude Code complete guide, Codex complete guide, Claude Code vs Cursor comparison, coding agents reshaping EPD
- Cross-link opportunities: [[Claude Code]], [[OpenAI Codex]], [[CLAUDE.md]], [[MCP]], [[agent teams]], [[Claude Code hooks]]
- Consider ingesting this as a raw source → wiki pages for both tools + a comparison page