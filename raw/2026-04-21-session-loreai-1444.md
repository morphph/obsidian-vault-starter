# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article content comparing OpenAI Codex (2025 agentic tool) vs ChatGPT for software engineering workflows — likely ingested as a raw source or being drafted into the wiki.

**Key Exchanges:**
- No interactive exchanges occurred; this was a structured article read/ingest session.

**Decisions Made:**
- N/A (no interactive decisions logged)

**Lessons Learned:**
- **Codex (2025) ≠ original Codex API (2021):** The old Codex was a deprecated GPT-3 fine-tune powering early Copilot. The new Codex is a fully autonomous cloud coding agent. Critical disambiguation for the wiki.
- **Codex = async, repo-aware, self-verifying:** Clones repo, installs deps, runs your actual test suite, produces PRs. No human in the loop required.
- **ChatGPT = sync, conversational, no persistent repo context:** Better for ambiguous/exploratory work; starts from zero each session.
- **Pricing gate:** Codex requires Pro ($200/mo), Team ($25/user/mo), or Enterprise. No standalone plan. Students and OSS maintainers get free credits.
- **Combined workflow:** ChatGPT for thinking/design → Codex for queued execution → ChatGPT for interactive debugging → Codex PR review cycle.

**Action Items:**
- Consider creating or updating a `wiki/openai-codex.md` page with the async-agent model, pricing, and disambiguation from the legacy API.
- Cross-reference with any existing `wiki/` pages on coding agents, Claude Code, or agentic workflows.