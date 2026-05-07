# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingested a detailed comparison article: Claude Code vs OpenAI Codex — architecture, developer experience, use cases, pricing.

**Key Exchanges:**
- Claude Code = interactive terminal pair programmer with full local environment access; Codex = async task delegator with cloud sandbox isolation
- Claude Code uses token-based API billing (also bundled in Claude Pro $20/mo, Max $100-200/mo); Codex bundled in ChatGPT Pro $200/mo, Team $25/user/mo
- Codex sandbox model: clones repo, reads docs, can run builds/unit tests, but no access to external services or production DBs
- Claude Code context advantage: CLAUDE.md, skills, hooks, MCP servers compound over time; Codex relies on repo contents + task description only

**Decisions Made:**
- Article positions the tools as complementary, not competing — Claude Code for hard interactive work, Codex for batch routine tasks
- Many teams use both: Claude Code for debugging/refactoring/complex tasks, Codex for parallel independent task batches

**Lessons Learned:**
- Codex's sandbox isolation is a feature for security-sensitive orgs, not just a limitation
- Neither model eliminates code review — difference is inline (Claude Code) vs after-the-fact PR review (Codex)
- Setup complexity tradeoff: Codex easier to start, Claude Code pays off more with investment in configuration
- Claude Code excels at: complex debugging, codebase-wide refactoring, workflow automation, knowledge-intensive tasks
- Codex excels at: batch task processing, team-scale delegation, onboarding/accessibility, security-sensitive environments
- Large codebase advantage goes to Claude Code due to CLAUDE.md context system and MCP integrations

**Action Items:**
- Wiki pages to create/update: `claude-code.md`, `openai-codex.md`, `ai-coding-tools-comparison.md`
- Cross-reference with existing wiki pages on Claude Code features (hooks, agent teams, MCP, skills)
- Pricing data is time-sensitive (as of mid-2026) — flag for periodic refresh