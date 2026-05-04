# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article on OpenAI Codex vs ChatGPT for coding tasks (likely raw source content for wiki ingestion).

**Key Exchanges:**
- Comprehensive breakdown of Codex (agentic, async, repo-integrated, $200/mo Pro or $25/user Team) vs ChatGPT (conversational, sync, no repo access, $0-20/mo)
- Codex uses codex-1 model (fine-tuned from o3), runs in sandboxed cloud containers with network disabled during execution
- Claude Code positioned as Anthropic's competitor — runs locally in terminal vs Codex's cloud-based async execution

**Decisions Made:**
- Decision framework established: Codex for well-scoped, delegatable tasks against real codebases; ChatGPT for exploration, learning, quick snippets, multi-project work
- Optimal workflow: Explore in ChatGPT → Delegate to Codex → Review PR → Iterate in ChatGPT
- Budget threshold: under $25/mo → ChatGPT Plus; Team plan already includes Codex → use it

**Lessons Learned:**
- Codex's async model means no mid-task steering — misunderstandings discovered only at review time; best for tasks with clear acceptance criteria
- Codex requires GitHub repos — non-GitHub projects can't use it
- Security model difference: Codex disables network during execution (prevents exfiltration); ChatGPT Free/Plus data may be used for training unless opted out
- Special programs exist: Codex for Students (free credits), Codex for Open Source (free Pro access)

**Action Items:**
- This content should be ingested into wiki as a raw source, with relevant updates to pages like `openai.md`, any existing Codex or ChatGPT pages, and potentially a new `codex-vs-chatgpt.md` wiki page
- Cross-reference with existing Claude Code wiki content for competitive landscape context