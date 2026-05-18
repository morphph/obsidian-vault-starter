# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Claude Code subagents vs Codex custom agents for the LoreAI blog.

**Key Exchanges:**
- Comprehensive comparison of two AI coding agent paradigms: Claude Code subagents (interactive, local, skill-based) vs OpenAI Codex custom agents (async, cloud-sandboxed, GUI-driven)

**Decisions Made:**
- Framing: not a "which is better" but "which fits which workflow" — interactive orchestration vs asynchronous delegation
- Verdict: use both — Claude Code for complex high-context work, Codex for routine batch tasks
- Article includes internal links to other LoreAI content (skills guide, subagent examples, Codex VS Code, glossary terms)

**Lessons Learned:**
- **Isolation trade-off:** Codex sandbox = stronger security but no network/MCP access; Claude Code worktrees = weaker isolation but full local tooling
- **Skill files vs agent configs:** Skills live in repo (version-controlled, code-reviewed, evolve with codebase); Codex configs live in platform (portable but can drift from project conventions)
- **Cost model difference:** Claude Code = token-based (variable); Codex = subscription via ChatGPT Pro $200/mo (predictable). Budget implications vary by usage volume
- **Claude Code subagents inherit CLAUDE.md + SKILL.md context** — this is the key differentiation for deep project understanding
- **Practical parallelism:** Teams commonly run 3-7 Claude Code subagents in parallel; each in its own git worktree
- **Codex agents cannot use MCP servers** due to sandbox network restrictions — significant capability gap for tool-heavy workflows

**Action Items:**
- Article appears ready for final review and publication to drafts/
- Pricing section notes mid-2026 data — will need periodic updates
- Could be ingested into wiki as a page on agent orchestration patterns (covers Claude Code, Codex, subagent architecture)