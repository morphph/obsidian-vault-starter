# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article between Claude Code and OpenAI Codex (the 2025 agentic tool) for potential wiki ingestion.

**Key Exchanges:**
- No interactive Q&A — session consisted of a single document review request with no prior conversation turns.

**Decisions Made:**
- N/A (no decisions recorded in this session)

**Lessons Learned:**
- Claude Code vs Codex key differentiators worth preserving:
  - **Execution model:** Claude Code = local (accesses running services, DBs, files); Codex = cloud sandbox (isolated, safer)
  - **Customization depth:** Claude Code wins with CLAUDE.md + SKILL.md + hooks stack; Codex has no equivalent
  - **Workflow fit:** Claude Code = interactive/iterative pair-programming; Codex = async fire-and-forget task delegation
  - **Pricing:** Claude Code Pro = $20/mo; ChatGPT Pro (includes Codex) = $200/mo; Claude Code API = pay-per-token
  - **Codex free access:** qualifying open-source maintainers + $100 credits for students
  - **"New Codex" ≠ "2021 Codex"** — the 2025 Codex is a full agent using codex-1 model (RL-trained), not just a code-gen model
  - **Recommended combined workflow:** Claude Code for complex/exploratory 20%; Codex for well-defined delegatable 80%

**Action Items:**
- Consider running `/ingest` on this article if a raw source file exists — it contains useful structured knowledge about Claude Code capabilities, Codex positioning, and pricing that would extend the AI Builder knowledge base.