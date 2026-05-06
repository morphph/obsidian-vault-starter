# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: OpenAI Codex vs ChatGPT for developers.

**Key Exchanges:**
- Article covers architecture differences (Codex = autonomous agent with full repo clone + sandbox; ChatGPT = real-time conversational collaborator with manual context)
- Detailed task-type breakdown: Codex wins for multi-file implementation, test coverage, migrations; ChatGPT wins for debugging, learning, architecture discussions
- Pricing analysis: Codex is bundled into ChatGPT Pro ($200/mo), not a separate product; economic sense only at 10+ delegable coding hours/month

**Decisions Made:**
- Core thesis: "Use Codex for implementation, use ChatGPT for thinking" — complementary, not competitive
- Recommended workflow: think in ChatGPT → scope clearly → submit to Codex → review PR
- Budget recommendation: ChatGPT Plus ($20/mo) covers most developers; Pro only if heavy autonomous coding delegation

**Lessons Learned:**
- Codex cannot steer mid-execution — misunderstandings discovered only after completion (key tradeoff of async model)
- Codex is GitHub-only; no GitLab/Bitbucket/local support
- Codex sandbox cannot access external services (DBs, APIs, cloud resources)
- ChatGPT's lack of repo context means developer becomes "the integration layer" for multi-file changes
- Full-repo context (Codex) produces dramatically better first-pass output on established codebases with consistent patterns

**Action Items:**
- Article references CTA link `/subscribe` for LoreAI — ensure this is wired up
- Article positions against Claude Code as an alternative ("terminal-based agent") — could be worth a separate wiki page or cross-reference on competitive landscape
- OpenAI's Codex for open source program and student credits are noted as access paths — worth tracking if covering OpenAI's GTM strategy