# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: "Codex CLI vs Claude Code" for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison covering architecture (async cloud sandbox vs interactive local agent), extension stacks, security models, pricing, IDE integration, and model capabilities.

**Decisions Made:**
- Framed Codex CLI as "async task runner / junior dev" and Claude Code as "pair programmer / collaborator" — two complementary tools, not direct competitors.
- Positioned Claude Code as the stronger choice for most professional developers due to extensibility, while Codex CLI fills a niche for batching well-scoped tasks.
- Avoided head-to-head model quality comparisons (too volatile), focused on architectural and workflow differences instead.

**Lessons Learned:**
- Codex CLI's key differentiator is cloud sandbox isolation (zero-trust by default) — appeals to security-first orgs adopting AI coding tools for the first time.
- Claude Code's differentiator is the programmable extension stack (CLAUDE.md → SKILL.md → Hooks → MCP → Agent Teams) — no equivalent in Codex CLI's current architecture.
- Security tradeoff: "secure by default" (Codex sandbox) vs "secure by policy" (Claude Code permissions) — neither strictly better, depends on threat model.
- Pricing comparison is usage-pattern dependent: bundled subscription (Codex) vs pay-per-token (Claude Code API) or included with Max subscription.

**Action Items:**
- Article references internal links (`/blog/claude-code-agent-teams`, `/blog/codex-vscode`, `/faq/is-codex-cli-safe-to-use`, etc.) — ensure these exist or are created.
- Consider ingesting this article into `raw/` and updating wiki pages for [[claude-code]], [[codex-cli]], and potentially a new [[ai-coding-tools-comparison]] page.
- Pricing section notes "as of mid-2026, pricing continues to evolve" — will need periodic refresh.