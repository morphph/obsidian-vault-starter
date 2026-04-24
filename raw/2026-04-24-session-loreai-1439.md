# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article comparing OpenAI Codex vs ChatGPT for coding workflows — likely a raw source candidate for the wiki.

**Key Exchanges:**
- No interactive conversation occurred; the context is a standalone article comparing Codex and ChatGPT

**Decisions Made:**
- (None — no decisions were made in this session)

**Lessons Learned:**
- **Codex vs ChatGPT structural differences**: Codex connects directly to GitHub repos, runs real test suites in sandbox, produces PRs asynchronously. ChatGPT is interactive, no repo connection, no test execution.
- **Codex pricing gate**: Requires Pro ($200/mo), Team, or Enterprise. Not available on Free or Plus. Students may qualify for credits programs.
- **Use case split**: Codex = well-defined multi-file execution tasks (refactors, test gen, migrations). ChatGPT = exploratory thinking, debugging, architecture, quick snippets, non-code work.
- **Combined workflow pattern**: ChatGPT for fuzzy exploration → write precise spec → hand to Codex for execution → review diff + test results → iterate.
- **Codex limitations**: GitHub-only (no GitLab/Bitbucket), async latency bad for quick fixes, sandbox may not match prod environment, vague prompts produce vague output.
- **Team adoption**: Codex integrates naturally into PR review workflows; ChatGPT usage is harder to standardize across teams.

**Action Items:**
- This article is a strong `/ingest` candidate — would map to a new wiki page (e.g., `openai-codex-vs-chatgpt.md`) and enrich existing pages on [[agentic coding]], [[agent harnesses]], and OpenAI tooling.