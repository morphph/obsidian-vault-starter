# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a comparative article on Claude Code vs OpenAI Codex for potential wiki ingestion.

**Key Exchanges:**
- The conversation context is an editorial article (likely from LoreAI blog) comparing Claude Code and OpenAI Codex across six dimensions: execution model, customization, multi-agent support, security, pricing, and developer experience.

**Decisions Made:**
- No explicit decisions recorded — this appears to be a passive review/flush pass with no user interaction.

**Lessons Learned:**
- Claude Code = interactive pair programmer; Codex = async task worker / PR machine
- Claude Code's customization stack (CLAUDE.md → SKILL.md → hooks → MCP) is significantly deeper than Codex's AGENTS.md-only approach
- Claude Code keeps code local (compliance-friendly); Codex clones repo into OpenAI cloud sandbox (ephemeral, not used for training)
- Codex is free for ChatGPT Pro/Team subscribers — zero marginal cost if already in OpenAI ecosystem
- Claude Code suits: real-time control, deep project customization, regulated industries, multi-file/monorepo changes
- Codex suits: well-defined async tasks, GitHub-centric PR workflows, minimal setup, non-terminal users
- Many teams use both: Claude Code for hard/exploratory problems, Codex for backlog of clear tasks

**Action Items:**
- Consider ingesting this article as a raw source (`/ingest`) to create or update a `claude-code-vs-codex.md` wiki page under the "Builder tools and workflows" category.