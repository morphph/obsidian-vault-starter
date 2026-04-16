# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing a detailed article comparing OpenAI Codex vs ChatGPT for coding tasks — likely for LoreAI content or wiki ingestion.

**Key Exchanges:**
- Article covers: architecture differences, code verification, workflow integration, pricing, use cases, FAQs
- Codex is agentic: spins up cloud containers, clones GitHub repos, installs deps, runs tests, produces PRs
- ChatGPT is conversational: generates code as text, no execution in user's environment, faster but unverified
- Codex integrates with GitHub and has a VS Code extension

**Decisions Made:**
- Article framing: Codex and ChatGPT are complementary, not either/or — use ChatGPT for exploration/quick tasks, Codex for delegated multi-file implementation

**Lessons Learned:**
- Codex pricing gate: only available on Pro ($200/mo), Team ($30/user/mo), Enterprise — **not** Free or Plus
- Codex loses verification advantage when projects lack test suites
- Open-source maintainers may qualify for free Codex access via OpenAI program
- Original Codex API (deprecated) ≠ current Codex product — naming history worth tracking
- Write-run-fix loop is Codex's core value: real signals vs model confidence

**Action Items:**
- Consider ingesting this as `raw/` source → wiki page on `openai-codex.md` or `codex-vs-chatgpt.md`
- Could cross-reference with existing [[agentic coding]] concepts if that page exists