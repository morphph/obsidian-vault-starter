# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese-language comparison article (Codex CLI vs Claude Code) for the blog.

**Key Exchanges:**
- Generated a full `codex-cli-vs-claude-code` comparison draft covering architecture, security models, context windows, ecosystem, configurability, pricing, and use-case recommendations

**Decisions Made:**
- Framed the comparison as "two design philosophies" rather than a winner/loser — Codex CLI as "controllable executor" (沙箱优先, open-source) vs Claude Code as "AI engineering system" (七层架构, deep integration)
- Recommended a coexistence strategy: Codex CLI for security-sensitive experiments, Claude Code for daily engineering workflows
- Cross-linked to existing blog posts: `codex-complete-guide`, `claude-code-seven-programmable-layers`, `claude-code-hooks-mastery`, `claude-code-enterprise-engineering-ramp-shopify-spotify`, `claude-code-agent-teams`, `codex-vscode`

**Lessons Learned:**
- Key differentiators worth tracking: Codex CLI's sandbox-first security (Docker/Seatbelt, network-off) vs Claude Code's trust-but-verify permission layers; Claude Code's 1M token context vs Codex CLI's ~128K; Claude Code's 7-layer programmability has no Codex CLI equivalent beyond `codex.md`/`AGENTS.md`

**Action Items:**
- Article needs to be saved to `drafts/` and indexed if not already done
- Related wiki pages (`codex-cli`, `claude-code`) should be checked for consistency with claims in this draft
- Pricing/model version numbers (Opus 4.6, Sonnet 4.6, GPT-4.1) are date-sensitive — flag for staleness on next lint pass