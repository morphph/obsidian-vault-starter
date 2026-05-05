# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog post or draft comparing Codex CLI vs Claude Code as agentic coding tools.

**Key Exchanges:**
- Detailed feature comparison across 8 dimensions: workflow, context/understanding, customization, safety, pricing, IDE support, and use-case fit

**Decisions Made:**
- Framing: Codex = async cloud task runner (GitHub-native), Claude Code = real-time local pair programmer (terminal-native)
- Not positioned as competitors but complements: "one is your async task queue, the other is your real-time pair programmer"
- Claude Code's 7 programmable layers (CLAUDE.md, Skills, Hooks, Agent teams, MCP, slash commands, permissions) positioned as key differentiator
- Safety philosophy distinction: Codex = isolation-by-default (sandboxed, no network), Claude Code = transparency + permission-gating
- Pricing: Codex bundled with ChatGPT Pro ($200/mo flat), Claude Code usage-based per-token

**Lessons Learned:**
- Codex strengths: well-defined self-contained tasks, async batch workflows, GitHub issue→PR pipeline, predictable cost, cross-platform access
- Claude Code strengths: complex multi-file refactors, projects with non-obvious conventions, exploratory work, local context (uncommitted changes, running services, env configs), deep customization
- Codex requires ChatGPT Pro/Team/Enterprise subscription; offers free tiers for open-source maintainers and students
- Claude Code requires macOS/Linux (Windows via WSL only) — barrier for some users
- Both handle large codebases; Claude Code via CLAUDE.md + agent teams, Codex via full repo clone into sandbox

**Action Items:**
- This content should be ingested into wiki as a comparison page (e.g., `wiki/codex-cli-vs-claude-code.md`) — covers competitive landscape relevant to the AI builder domain
- Internal links reference several other blog posts (`/blog/claude-code-hooks-mastery`, `/blog/codex-vscode`, etc.) and glossary entries — these could seed future wiki pages or raw sources