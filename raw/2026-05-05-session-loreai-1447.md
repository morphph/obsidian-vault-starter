# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code subagents vs Codex custom agents for multi-agent coding workflows.

**Key Exchanges:**
- Detailed architectural comparison between Claude Code (hierarchical, synchronous parent-child orchestration) and Codex (queue-based, asynchronous container isolation)
- Analysis of context handling: Claude Code passes context through parent agent as broker; Codex tasks are isolated with no cross-task communication
- Safety model comparison: Claude Code uses permission-based + typed agent roles; Codex uses container sandboxing with proposed diffs

**Decisions Made:**
- Article verdict: coordination-heavy work → Claude Code; pure parallel execution → Codex
- Hybrid workflow recommended: Claude Code for exploration/architecture, Codex for well-defined parallel tasks, Claude Code again for integration
- Deciding factor framed as: "do your agents need to coordinate, or just execute in parallel?"

**Lessons Learned:**
- Claude Code's typed subagent system (Explore, Plan, etc.) enforces constraints at tool-access level, not just prompt level — structural guarantee vs best-effort
- Codex's simplicity advantage: easier to debug (just edit system prompt), no layered inheritance to untangle
- Claude Code's layered config (CLAUDE.md + SKILL.md + hooks) scales better for multi-repo orgs but adds complexity
- For 100K+ line codebases, Claude Code's selective context is more efficient than Codex's full repo clone per container
- Cross-agent coordination is the key architectural gap in Codex — requires manual bridging

**Action Items:**
- Article references internal links (`/blog/claude-code-subagents-examples`, `/blog/codex-complete-guide`, etc.) that need to exist or be created
- FAQ section mentions Codex concurrency limits are plan-tier dependent — may need updating as pricing changes