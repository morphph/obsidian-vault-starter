# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/source article comparing Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison between Claude Code (Anthropic) and OpenAI Codex across six dimensions: execution model, extensibility, workflow style, context/project understanding, IDE options, and team/enterprise considerations.

**Decisions Made:**
- **Claude Code positioned as the power tool**: Best for interactive workflows, deep extensibility (7 programmable layers), persistent project context (CLAUDE.md/SKILL.md), and local environment access. Strongest for senior devs and teams investing in AI tooling configuration.
- **Codex positioned for async/isolation**: Best for fire-and-forget workflows, sandboxed cloud execution, task parallelism, and teams already on OpenAI's platform. Lower setup overhead.
- **Not mutually exclusive**: Article frames them as complementary — Claude Code for interactive dev sessions, Codex for batch/parallel task processing.

**Lessons Learned:**
- Local execution (Claude Code) trades security perimeter access for richer context; cloud sandbox (Codex) trades context for isolation — neither universally better.
- Persistent project context (CLAUDE.md) is a compounding advantage for large codebases with established conventions.
- Codex tasks start fresh each time — project conventions must be repeated per task unless encoded in the prompt.
- Enterprise adopters of Claude Code include Ramp, Shopify, Spotify.

**Action Items:**
- Article references several internal links (`/blog/...`, `/compare/...`) — ensure corresponding wiki pages exist or are created for cross-referenced concepts (agent teams, hooks, CLAUDE.md memory, enterprise adoption).
- If this is a raw source, it should be ingested into `raw/` and fanned out to relevant wiki pages (e.g., `claude-code.md`, `openai-codex.md`, `ai-coding-tools-comparison.md`).