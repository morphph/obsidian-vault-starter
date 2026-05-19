# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog post or draft comparing Codex CLI vs Claude Code as AI coding tools, likely for LoreAI publication.

**Key Exchanges:**
- Comprehensive feature-by-feature comparison: architecture (cloud sandbox vs local execution), context systems (AGENTS.md vs CLAUDE.md/SKILL.md stack), safety models (isolation vs permission layers), extensibility, pricing, DX
- Real workflow example: JWT auth refactoring task showing practical differences between the two tools

**Decisions Made:**
- **Claude Code wins for most professional developers** — local execution, CLAUDE.md/SKILL.md context system, hooks, MCP integrations, agent teams make it stronger for real projects with local dependencies
- **Codex CLI wins for security-sensitive environments** — sandbox isolation provides safety guarantees no permission system can match; also better for teams already in OpenAI ecosystem
- **Not mutually exclusive** — recommended pattern: Codex CLI for untrusted/exploratory tasks, Claude Code for deep integration work

**Lessons Learned:**
- Codex CLI's cloud sandbox means it can't run integration tests against local DBs, Docker, or local APIs — a hard limitation for many real workflows
- Claude Code's four extension layers (Skills, Hooks, MCP, Agent teams) compound in value for teams over time — this is the key differentiator for extensibility
- Codex CLI is "free" open source but requires paid OpenAI model access (ChatGPT Pro $200/mo); Claude Code has Max subscription ($100-$200/mo) or per-token API pricing
- Codex CLI's repo-snapshot approach has limitations with very large repositories (upload times, sandbox resource constraints)
- Code quality depends more on prompting and underlying model than on the tool wrapper

**Action Items:**
- This content should be ingested into wiki as a comparison page (e.g., `wiki/codex-cli-vs-claude-code.md`)
- Cross-link to existing wiki pages: [[Claude Code]], [[MCP]], [[Codex CLI]] if they exist
- Pricing info ($200/mo Pro, $100-$200/mo Max) is time-sensitive — mark with date for staleness tracking