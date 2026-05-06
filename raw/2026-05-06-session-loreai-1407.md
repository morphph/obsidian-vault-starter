# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft or raw article comparing Claude Code vs OpenAI Codex as AI coding tools.

**Key Exchanges:**
- Comprehensive feature comparison: Claude Code (local, terminal-native, extensible) vs Codex (cloud sandbox, async, managed)
- Security model analysis: permission-based (Claude Code) vs isolation-based (Codex) — neither universally more secure, depends on threat model
- Pricing breakdown: Claude Pro $20/mo vs ChatGPT Pro $200/mo; Team tier comparable at $25/user/mo

**Decisions Made:**
- Framing: "not direct competitors — different tools for different workflows"
- Recommended split: Claude Code for senior engineers doing complex/interactive work; Codex for well-scoped async delegation
- Both can coexist on the same project without conflict

**Lessons Learned:**
- Claude Code's extensibility stack (CLAUDE.md → skills → hooks → MCP → agent teams) is its key differentiator — no Codex equivalent
- Codex's sandbox tradeoff: strong isolation but environment fidelity suffers for projects with complex local dependencies
- Claude Code's ROI scales with configuration investment; Codex is simpler but less optimizable
- Codex has free tiers for open-source maintainers and students ($100 credits) — Claude Code doesn't match this

**Action Items:**
- This content should be ingested into the wiki — touches multiple wiki-relevant topics: [[Claude Code]], Codex, AI coding tools pricing, agent security models
- Could inform wiki pages on: Claude Code extensibility layers, AI coding tool landscape, MCP ecosystem