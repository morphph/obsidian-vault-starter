# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/published article comparing Codex CLI vs Claude Code as AI coding agents (likely for LoreAI blog).

**Key Exchanges:**
- Comprehensive feature comparison between Codex CLI (OpenAI) and Claude Code (Anthropic) as of early 2026

**Decisions Made:**
- Article frames the tools as complementary rather than competing — optimized for different workflows
- Verdict: Codex CLI = async task engine; Claude Code = programmable pair-programming partner
- Many teams should use both: Codex for well-defined tickets, Claude Code for context-rich judgment work

**Lessons Learned:**
- **Codex CLI architecture**: Cloud sandbox model — clones repo, executes in isolated container, produces PR. Strong isolation but context-poor (no local state, no cross-task memory, no persistent project knowledge).
- **Claude Code architecture**: Local execution model — reads filesystem, runs shell commands in actual terminal, full env access. Rich context but requires trust/permission configuration.
- **Extension gap is widest differentiator**: Claude Code has CLAUDE.md → Skills → Hooks → MCP → Agent teams. Codex CLI has limited customization (task instructions + repo access only).
- **Async vs interactive**: Codex = dispatch 5 tasks before coffee, review PRs later. Claude Code = real-time pair programming with immediate feedback loops.
- **Safety tradeoffs**: Codex achieves safety through isolation (easier compliance). Claude Code achieves safety through graduated permissions + hooks (more flexible but requires config).
- **Pricing**: Codex included in ChatGPT Pro ($200/mo) + Team/Enterprise plans. Claude Code = usage-based API billing or capped Pro/Team tiers.
- **Original Codex (2021) vs Codex CLI (2025)**: Completely different products — old was GPT-3 fine-tune for autocomplete, new is cloud-based coding agent.
- **Monorepo handling**: Claude Code's agent teams coordinate better for interconnected changes; Codex tasks lack shared state between parallel executions.

**Action Items:**
- Consider ingesting this as a wiki source covering both tools' architectures and positioning
- Potential wiki pages: `codex-cli.md`, update `claude-code.md` with extension stack details if not already covered