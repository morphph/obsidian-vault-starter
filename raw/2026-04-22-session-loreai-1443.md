# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article comparing OpenAI Codex vs ChatGPT for coding tasks — likely ingested or queued for ingest into the wiki.

**Key Exchanges:**
- No interactive Q&A — the context is a standalone article, not a conversation.

**Decisions Made:**
- (None recorded — no user decisions visible in this session)

**Lessons Learned:**
- **Codex is async + agentic**: spins up cloud containers, clones repo at current commit, runs real test suites, produces PRs — not chat messages
- **ChatGPT is synchronous + conversational**: no repo awareness, no test execution, user must manually apply generated code
- **Codex access**: Pro ($200/mo), Team, Enterprise only — NOT free or Plus tiers; students can get $100 credits
- **Codex limitations**: sandboxed (no internet during execution), can't steer mid-task, best for bounded/testable tasks
- **Codex competitors named**: Claude Code (local terminal), Cursor (IDE-integrated), GitHub Copilot Workspace
- **Recommended mental model**: ChatGPT = thinking partner (real-time), Codex = async workhorse (execution + verification)
- **Sweet spot for Codex**: bug fixes, test coverage, multi-file refactoring, PR-ready changes — tasks you'd write as a GitHub issue

**Action Items:**
- Consider ingesting this article as `raw/` source and creating/updating a `wiki/openai-codex.md` page — it has factual claims about Codex capabilities, pricing, and positioning vs Claude Code worth tracking