# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Codex CLI vs Claude Code.

**Key Exchanges:**
- Detailed breakdown of two AI coding philosophies: **delegation** (Codex CLI) vs **collaboration** (Claude Code)
- Codex CLI = async task queue with sandbox isolation, uses OpenAI o3, included in ChatGPT Pro ($200/mo)
- Claude Code = interactive pair programming with full env access, usage-based API billing

**Decisions Made:**
- Framing: not "which is better" but "which workflow matches yours" — delegation vs collaboration
- Verdict: use both if possible — Codex for backlog volume, Claude Code for complex focused sessions
- Safety framing: Codex = security-by-isolation (sandbox), Claude Code = security-by-oversight (approval + hooks)
- Junior dev safety: Codex CLI wins due to narrower blast radius

**Lessons Learned:**
- Codex CLI sandbox trades safety for capability — can't install packages, call APIs, or run full CI
- Claude Code's extensibility (MCP, hooks, SKILL.md) is significantly deeper than Codex CLI's current offering
- Model choice rarely the bottleneck; context, tooling, and workflow integration matter more
- Cost crossover: heavy users favor Codex's flat rate; light users favor Claude Code's pay-per-token
- Combined workflow overhead is low since both tools read the repo directly — code is shared context

**Action Items:**
- Article references internal links (`/blog/claude-code-hooks-mastery`, `/blog/codex-for-students`, etc.) — ensure those exist before publishing
- Pricing info marked as "subject to change" — will need periodic updates
- Could become a wiki page (e.g., `wiki/codex-cli-vs-claude-code.md`) for the knowledge base