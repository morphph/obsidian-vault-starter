# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/draft comparing Claude Code subagent architecture vs Codex custom agent architecture for the LoreAI blog.

**Key Exchanges:**
- Claude Code uses **hierarchical, synchronous** agent orchestration (parent spawns typed subagents, synthesizes results)
- Codex uses **flat, asynchronous** agent architecture (independent agents, no built-in parent-child coordination)
- Claude Code subagent types have enforced tool restrictions (Explore = read-only, Plan = no edits, etc.)
- Codex agents run in isolated cloud sandboxes with broad access within the container but no per-directory restrictions
- Claude Code agent configs are repo-level (versioned in git); Codex agent configs are org-level (platform UI/API)

**Decisions Made:**
- Positioning: Claude Code for interactive/tightly-coupled tasks; Codex for async/loosely-coupled tasks — "not which is better, but which execution model fits each task"
- Hybrid workflow recommended: Claude Code for active dev sessions, Codex for background/fire-and-forget tasks
- Sweet spot for parallel Claude Code subagents: 2-4 concurrent before context management gets complex
- Cost guidance: Claude Code cheaper for <5 devs / <20 agent tasks per week; Codex may win at higher volumes

**Lessons Learned:**
- Typed subagents eliminate an entire error class — an Explore agent physically cannot edit files
- Codex flat architecture advantage: no orchestration logic to debug, no parent-child comms to manage
- Codex tradeoff: agents sometimes go down wrong path with no mid-task correction, wasting full execution cycles
- Claude Code subagents share local filesystem = no clone/build/setup overhead per task (speed advantage)

**Action Items:**
- Article references several internal links that need to exist: `/blog/agent-harnesses-2026`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/claude-code-agent-teams`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`
- Wiki pages worth creating/updating: [[claude-code]], [[codex]], [[agent-sdk]], [[agent-architectures]]
- The comparison table (Configuration Aspect) and decision framework are high-value reference material for the wiki