# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Review of a comparative article on Claude Code vs Codex CLI (likely for wiki ingestion or draft creation)

**Key Exchanges:**
- Article covers: execution model, project context system, security/safety, developer experience, pricing, and use-case recommendations for both tools

**Decisions Made:**
- No explicit decisions recorded in this session

**Lessons Learned:**
- **Execution model**: Claude Code = synchronous + local; Codex CLI = async + cloud-sandboxed. Key tradeoff is control vs. throughput
- **Context system**: Claude Code has mature CLAUDE.md/SKILL.md/hooks layering; Codex CLI has no equivalent persistent context config
- **Security posture**: Codex CLI = max isolation by default (no network/filesystem); Claude Code = full local access with user approval. Interesting note: Claude Code's local execution is actually *more* compliant for data sovereignty (code never leaves your network)
- **Pricing**: Codex CLI = subscription-based (ChatGPT Pro/Team/Enterprise); Claude Code = API token billing or Max ($100–200/mo). Codex CLI has free tier for OSS maintainers and students ($100 credits)
- **Recommended combo**: Claude Code for interactive/exploratory work; Codex CLI for batch task delegation in parallel

**Action Items:**
- Consider ingesting this article as a raw source → wiki page comparing the two tools (e.g., `claude-code-vs-codex-cli.md`)
- Article ends with a LoreAI subscribe CTA — likely a draft/publish candidate for loreai.dev