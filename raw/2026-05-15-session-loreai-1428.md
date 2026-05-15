# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a comprehensive comparison article: Codex CLI vs Claude Code for AI-assisted coding workflows.

**Key Exchanges:**
- Detailed architectural comparison: Codex CLI = cloud sandbox batch delegation; Claude Code = local interactive agent
- Security models differ fundamentally: Codex = isolated containers (stronger default isolation); Claude Code = local machine permissions (more capable but requires trust)
- Parallel execution: Codex parallelizes across independent tasks (batch); Claude Code parallelizes within a single complex task (agent teams)

**Decisions Made:**
- Article positions them as **complementary, not competing** tools — different bottlenecks addressed
- Verdict: Claude Code more versatile for individuals; Codex CLI adds throughput for teams with well-scoped backlogs
- Strongest approach = use both: Codex for batch routine tasks, Claude Code for complex interactive work

**Lessons Learned:**
- Codex CLI cloud sandbox tradeoff: security isolation gained, but cannot access local services/DBs/env vars
- Claude Code's extensibility stack (CLAUDE.md → SKILL.md → Hooks → MCP → Agent teams) is a key differentiator — makes it a "programmable platform" vs just a coding tool
- Pricing crossover: Codex flat-rate ($200/mo ChatGPT Pro) favors heavy usage; Claude Code usage-based favors selective use — calculate expected token usage before committing
- Codex CLI beginner-unfriendly: requires clear upfront task specification; Claude Code's interactive model more forgiving for learning
- Large codebases: Claude Code's on-demand file reading typically faster for monorepos vs Codex's full repo clone

**Action Items:**
- This content should be ingested into wiki as a source comparing AI coding tools (Codex CLI vs Claude Code)
- Could inform wiki pages on: [[codex-cli]], [[claude-code]], [[ai-coding-tools-comparison]]
- Cross-references existing wiki topics: Claude Code extension stack, MCP servers, agent teams