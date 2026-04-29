# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Codex CLI vs Claude Code for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature-by-feature comparison completed across 7 dimensions: context/memory, workflow model, extensibility, safety, model capabilities, pricing, and use-case fit.

**Decisions Made:**
- **Overall verdict:** Claude Code recommended as default for most individual developers; Codex CLI better for sandboxed/batch/CI-CD/open-source-required scenarios. Not mutually exclusive — some teams use both.
- **Context system:** Claude Code's layered system (CLAUDE.md → skills → hooks → auto-memory) rated materially more sophisticated than Codex CLI's `codex.md` + `AGENTS.md`.
- **Workflow framing:** Codex CLI = async (submit → wait → review diffs); Claude Code = interactive (steer in real-time, runs real environment). Each has clear sweet spots.
- **Safety framing:** Codex CLI's sandbox = stronger isolation guarantees (physically can't access); Claude Code's permission model = more flexible but relies on user judgment.
- **Extensibility framing:** Codex CLI wins on transparency (open source, auditable); Claude Code wins on practical extensibility (MCP, hooks, skills, agent teams, slash commands).
- **Pricing:** Rated as roughly equivalent — both charge for API tokens, no meaningful tool-level cost difference.

**Lessons Learned:**
- Claude Code's agent teams enable coordinated parallel work in monorepos; Codex CLI can parallelize but tasks don't coordinate with each other.
- Codex CLI's sandbox means it can't run real test suites, connect to local DBs, or interact with running services — a significant limitation for integration-heavy work.
- Claude Code's CLAUDE.md + hooks system creates compounding returns across sessions and team members — conventions ship with the repo.
- Codex CLI's mid-task course correction gap: wrong direction isn't discovered until execution completes.

**Action Items:**
- Article appears ready for publication at `drafts/` — needs final human polish pass.
- Consider ingesting this into wiki as a standalone page (e.g., `wiki/codex-cli-vs-claude-code.md`) since it contains durable reference knowledge about both tools' architectures and trade-offs.