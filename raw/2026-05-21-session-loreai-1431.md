# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs Codex CLI for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code runs locally (terminal-native, interactive), Codex CLI runs in cloud sandboxes (async, task-queue model)
- Context systems differ fundamentally: Claude Code has layered persistent context (CLAUDE.md → SKILL.md → auto-memory → MCP), Codex CLI relies on repo snapshot + per-task instructions with no persistent convention encoding
- Security posture tradeoff: Codex CLI sandboxed by default (no network, no local access), Claude Code local execution with permission gates

**Decisions Made:**
- Framing: "no universal winner" — position as workflow-dependent choice, not feature-checklist comparison
- Recommendation pattern: Codex CLI for parallelizable/well-defined batch work (migrations, test backfill); Claude Code for interactive/context-heavy work (debugging, architecture, full-stack dev)
- Both tools together is the recommended approach for many teams

**Lessons Learned:**
- Codex CLI's per-task pricing favors many small tasks; Claude Code's per-token billing favors fewer complex sessions — cost comparison is usage-pattern dependent
- Codex CLI's sandboxing satisfies compliance/regulated environments more easily
- Claude Code's CLAUDE.md + skills system is a significant advantage for team convention enforcement
- Key tradeoff articulation: **throughput (Codex) vs quality-per-task (Claude Code)**
- Code quality depends more on usage discipline than tool choice

**Action Items:**
- Article references several internal links (`/blog/...`, `/faq/...`) — verify all exist before publishing
- Pricing section notes "as of early 2026" and "verify current details" — flag for freshness review
- Could become a wiki page on `codex-cli-vs-claude-code.md` for the knowledge base