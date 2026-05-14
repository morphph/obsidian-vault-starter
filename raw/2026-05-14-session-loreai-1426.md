# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article content comparing Codex CLI vs Claude Code — likely being reviewed for ingestion into the wiki.

**Key Exchanges:**
- Detailed architectural comparison: Codex CLI runs in cloud sandboxes (safety through isolation), Claude Code runs locally (capability through access)
- Context systems differ: Claude Code has multi-layered programmability (CLAUDE.md → SKILL.md → Hooks → MCP), Codex CLI uses single-layer AGENTS.md
- Workflow models: Codex = batch/async task delegation, Claude Code = interactive pair programming

**Decisions Made:**
- The two tools are complementary, not competing — Codex for well-defined ticket backlog, Claude Code for complex context-heavy work
- Security tradeoff framed as **data residency** (Claude Code wins) vs **execution safety** (Codex wins)
- Pricing: Codex = flat subscription via ChatGPT plans; Claude Code = usage-based API billing (cheaper for light users, less predictable for heavy users)

**Lessons Learned:**
- Codex CLI's sandbox means no access to local DBs, staging servers, env vars, or custom build scripts — important constraint for task selection
- Claude Code's permission system is the risk mitigation layer for local execution (vs Codex's sandbox isolation)
- Neither tool works offline
- Claude Code handles large codebases better due to local execution (no repo clone overhead)
- Model quality difference (codex-1/o3 vs Claude Opus/Sonnet) matters less than how each tool provides project context

**Action Items:**
- This content is suitable for a wiki page (e.g., `wiki/codex-cli-vs-claude-code.md`) — covers a key builder-tools comparison
- Pricing details are time-sensitive (May 2026 snapshot) — worth noting staleness risk
- Cross-link opportunities: [[Claude Code]], [[MCP]], [[Codex CLI]], [[CLAUDE.md conventions]]