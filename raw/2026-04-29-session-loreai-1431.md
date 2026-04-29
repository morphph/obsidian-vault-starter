# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a blog article comparing OpenAI Codex vs ChatGPT for coding tasks, likely for LoreAI blog.

**Key Exchanges:**
- Comprehensive comparison article covering: async vs sync workflows, codebase context, code verification, pricing, IDE integration, and non-coding capabilities

**Decisions Made:**
- Article positions Codex and ChatGPT as **complementary tools, not competitors** — Codex for autonomous multi-file tasks, ChatGPT for interactive/exploratory work
- Pricing framed as the key deciding factor for individuals ($20/mo Plus vs $200/mo Pro for Codex access)

**Lessons Learned:**
- **codex-1** is a distinct model fine-tuned from **o3** specifically for software engineering (RL on real coding tasks, optimized for test-passing)
- Codex operates fully async — no mid-task interaction, outputs PR diffs not chat messages
- Codex available on Pro ($200/mo), Team ($25/user/mo), Enterprise only — not Plus or free tier
- Student program: $100 free credits; open-source maintainers may get free access
- Codex has VS Code extension and GitHub-native integration (branches + diffs)
- Codex self-verifies by running tests/linters in sandboxed containers — ChatGPT cannot run code against your actual project dependencies
- `AGENTS.md` is the Codex equivalent of `CLAUDE.md` for project-specific instructions

**Action Items:**
- Wiki candidates: update `wiki/` with Codex product page (new OpenAI product, codex-1 model details, pricing tiers)
- Cross-reference with existing OpenAI/ChatGPT wiki pages if any
- Article references internal links (`/blog/codex-complete-guide`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/faq/codex-download`) — ensure these exist or are planned in drafts/