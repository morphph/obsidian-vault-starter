# Session Capture: loreai

**Date:** 2026-04-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comparative article on Claude Code vs OpenAI Codex for the LoreAI knowledge base.

**Key Exchanges:**
- Article covers Claude Code vs Codex across 7 dimensions: context systems, dev experience, security, pricing, IDE integration, decision criteria, and FAQ

**Decisions Made:**
- N/A (no interactive decisions recorded — this appears to be a content review/ingest session)

**Lessons Learned:**
- **Codex context system**: Uses `AGENTS.md` + setup script (ephemeral, no cross-session memory); Claude Code uses multi-file CLAUDE.md system with persistent memory
- **Workflow model**: Claude Code = interactive pair programming (real-time, tight loop); Codex = async task delegation (PR-based, batch review)
- **Security model**: Claude Code = local permissions, approval-based; Codex = isolated cloud sandbox, no network access during execution
- **Pricing (early 2026)**: Claude Code entry at $20/month (Pro); Codex requires ChatGPT Pro at $200/month (with free tier for open-source)
- **Decision rule summary**: Claude Code for hands-on devs needing local access + real-time iteration; Codex for teams with well-specced backlogs + async workflows
- **Complementary use**: Claude Code for active dev + review; Codex for parallel batch tasks + well-defined tickets

**Action Items:**
- Consider ingesting this article as a raw source (`raw/`) and creating a wiki page comparing `claude-code` vs `codex` under builder tools domain