# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/reference article comparing OpenAI's Codex CLI vs Anthropic's Claude Code for AI-assisted coding workflows.

**Key Exchanges:**
- Codex CLI = async task delegation ("assign and review" pattern); Claude Code = live interactive pairing ("pair programming" pattern)
- Codex uses container-based sandbox isolation (no network by default); Claude Code uses permission-based approach on local machine
- Claude Code has structured context hierarchy (CLAUDE.md → SKILL.md → auto-memory); Codex starts fresh per task with optional AGENTS.md
- Claude Code agent teams enable coordinated parallel sub-agents sharing parent context; Codex parallelizes independent isolated tasks

**Decisions Made:**
- Framing: tools are complementary, not competing — "they compete for your budget and ecosystem commitment, not the same moment in your workflow"
- Codex best for: batch well-specified tickets, safety-critical envs, teams already on ChatGPT Pro ($0 marginal cost)
- Claude Code best for: exploratory debugging, complex refactoring, full-stack verification, architecture decisions, long sessions with accumulating context

**Lessons Learned:**
- Codex sandbox trades execution fidelity for safety (can't run tests needing external services)
- Claude Code's CLAUDE.md/SKILL.md system gives it an edge for team consistency on longer projects
- Pricing models differ fundamentally: Codex bundled with ChatGPT subscription (caps vary by tier); Claude Code is per-token API billing (no hard caps)
- Codex for open-source maintainers (free Pro access) and students ($100 credits) signals aggressive ecosystem capture by OpenAI

**Action Items:**
- Article references several internal links (`/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/codex-for-open-source`, etc.) — ensure these exist or are created before publishing
- Article is positioned for LoreAI blog (`/subscribe` CTA at bottom) — ready for `/draft` polish pass when publishing