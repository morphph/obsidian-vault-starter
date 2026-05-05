# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex vs ChatGPT for coding tasks (likely for LoreAI blog)

**Key Exchanges:**
- Article establishes Codex as autonomous agent (clones repo, writes code, runs tests, delivers PRs) vs ChatGPT as interactive assistant (conversational, no filesystem/GitHub access)
- Codex uses `codex-1` model in sandboxed cloud environment
- Core tradeoff: Codex saves time on scoped tasks but can't be steered mid-task; ChatGPT catches misunderstandings immediately via interactive loop

**Decisions Made:**
- Verdict: "not competitors — complementary tools on the autonomy spectrum"
- Recommended workflow: ChatGPT for exploration/design → hand scoped tasks to Codex → review PRs
- Budget pick: ChatGPT Plus ($20/mo) covers most developers; Codex justified for devs with queue of well-defined tickets

**Lessons Learned:**
- Codex pricing (May 2026): Pro $200/mo, Team $25/user/mo, Enterprise custom. Plus access announced but not yet live
- Codex for Open Source program: free Pro for qualifying maintainers
- Student program: $100 API credits
- Codex accessed via ChatGPT interface or VS Code extension
- Task scoping is the practical key: clear self-contained descriptions → Codex; exploratory/ambiguous → ChatGPT

**Action Items:**
- Article references internal links (`/blog/codex-for-students`, `/blog/codex-for-open-source`, `/blog/codex-vscode`, `/glossary/agentic-coding`, `/glossary/what-does-codex-mean`) — these pages need to exist or be created
- Wiki pages to update/create: OpenAI Codex (product), codex-1 (model), agentic coding patterns
- Pricing may need periodic refresh — article notes "OpenAI updates plans frequently"