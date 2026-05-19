# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/working with a blog article draft comparing Codex CLI (OpenAI) vs Claude Code (Anthropic) as AI coding tools.

**Key Exchanges:**
- Detailed architectural comparison: Codex CLI uses cloud sandboxes (Docker containers), Claude Code runs locally on the developer's machine
- Codex CLI uses codex-1 model (based on o3 architecture); Claude Code uses Claude model family (Opus/Sonnet/Haiku)
- Codex = async "assign and review" workflow; Claude Code = interactive "pair programming" workflow

**Decisions Made:**
- Article verdict: Claude Code stronger for individual daily coding; Codex CLI better for parallel batch processing at scale
- Tools positioned as complementary, not mutually exclusive — use Claude Code interactively, queue well-scoped tickets to Codex overnight

**Lessons Learned:**
- Execution model matters more than raw model benchmarks — a weaker model with human guidance often outperforms a stronger model running blind
- Claude Code's customization stack (CLAUDE.md → SKILL.md → Hooks → MCP) is a meaningful differentiator for teams, less important for solo/small projects
- Codex pricing: included in ChatGPT Pro ($200/mo) and Team ($25/user/mo); Claude Code: Pro ($20/mo) or per-token API billing
- Security tradeoff: sandbox isolation (Codex) vs permission-based local access (Claude Code) — different fits for different compliance requirements
- Codex has VS Code extension, free credits for open-source maintainers, $100 credits for students
- Claude Code has voice mode, remote sessions (phone), agent teams for parallelization

**Action Items:**
- Consider ingesting this as a raw source → wiki pages on [[codex-cli]], [[claude-code-vs-codex]], [[ai-coding-tools-landscape]]
- Pricing and feature details are time-sensitive (article assumes current state as of mid-2026) — flag for staleness checks