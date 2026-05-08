# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage of 20 Anthropic/Claude Code social + GitHub events from May 7–8, 2026, routing each to wiki pages, content actions, and blog angles.

**Key Exchanges:**
- Triaged 20 signals → 11 actionable (refresh/create), 9 ignored (duplicates, third-party noise, social endorsements without content)
- Strongest signals: Anthropic+SpaceX compute deal doubling usage limits (signals 3 & 8), Claude Code desktop app DOM/UI annotation preview (signal 9), Claude Code DDoS incident response story (signal 7)

**Decisions Made:**
- **Refresh-and-create** for 5 signals: SpaceX compute deal (pricing FAQ + blog), DDoS incident response (security blog angle), desktop DOM context (computer-use FAQ + blog), harness engineering concept (hooks blog + new blog), brand-to-ad Skills pipeline (skills FAQ + non-coding blog), auto-generated MCP servers from API docs (MCP blog + new blog)
- **Refresh-only** for 4 signals: doubled usage limits confirmation, GBrain MCP topology, Claude Code 2.1.132 changelog (SESSION_ID, DISABLE_ALTERNATE_SCREEN, risky-action policy), v2.1.129 changelog (--plugin-url, FORCE_SYNC_OUTPUT, auto-update env var)
- **Ignored** all "Code with Claude" event RTs (signals 1,2,4,5,6) — no actionable content in event announcements
- **Ignored** third-party wrappers (Gentle AI, Penguin Office, API Center) — out of scope

**Lessons Learned:**
- Duplicate detection across RT chains is critical — 5 of 20 signals were the same event announcement
- "Harness engineering" is emerging as a practitioner term for optimizing Claude Code's surrounding config (prompts, tools, skills, hooks) as a discipline — worth tracking as a concept
- Non-coding use cases (marketing pipelines via Skills) continue to surface as a content gap
- Salesforce releasing an official MCP server signals enterprise ecosystem maturity

**Action Items:**
- Update `faq/claude-code-pricing` with doubled 5-hour limits across Pro/Max/Team/Enterprise
- Update `faq/claude-code-cli` and hooks blogs with 2.1.132 + 2.1.129 changes
- Create blog: Claude Code for real-time security incident response (DDoS angle)
- Create blog: Claude Code desktop app visual context workflow (DOM + UI annotation)
- Create blog: Harness engineering — optimizing Claude Code's surrounding config
- Create blog: Claude Code Skills for non-technical content pipelines (DTC/agency angle)
- Reference Salesforce Data 360 and GBrain topologies in MCP setup blog refresh