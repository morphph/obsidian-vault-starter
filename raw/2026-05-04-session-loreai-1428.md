# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Codex CLI vs Claude Code (for LoreAI blog).

**Key Exchanges:**
- Detailed feature-by-feature breakdown of two AI coding agents: OpenAI's Codex CLI (open-source, container-sandboxed) vs Anthropic's Claude Code (permission-based, deeply configurable)

**Decisions Made:**
- Article structure follows: Security → Context/Memory → Extensibility → Models → Workflow → Pricing → When-to-choose → Verdict → FAQ
- Verdict framing: not "X is better" but axis-based recommendation (safety-first → Codex CLI; configurable platform → Claude Code; practical tiebreaker = model preference on your codebase)
- Positioned Claude Code's value as compounding over time (CLAUDE.md, skills, hooks, memory) vs Codex CLI's value as immediate simplicity

**Lessons Learned:**
- Codex CLI sandbox: OS-level enforcement (no writes outside project dir, no network) — stronger default isolation but less flexibility
- Claude Code hooks + permissions: more configurable but relies on correct setup — `settings.json` auto-approve patterns, pre/post hooks for validation
- Codex CLI has no cross-session memory; Claude Code has layered context (CLAUDE.md → skills → auto-memory)
- Codex CLI extensibility = fork the source; Claude Code extensibility = MCP servers, hooks, agent teams, skills (7 programmable layers)
- Pricing: both usage-based API; Claude Code also has Max subscription ($100 Sonnet / $200 Opus) for predictable costs; Codex CLI = pure per-token
- Key quote for wiki: "the wrapper around the model increasingly matters more than the model itself" (agent harness thesis)

**Action Items:**
- Consider ingesting this article into wiki as a source (`raw/`) covering: Codex CLI capabilities, Claude Code vs competitors, agent harness landscape
- May warrant wiki pages: `codex-cli.md`, `agent-harness-comparison.md`, or updates to existing Claude Code / agent tooling pages
- Article references several internal links (`/blog/claude-code-hooks...`, `/blog/claude-code-memory`, etc.) — verify these exist on loreai.dev before publishing