# 你不知道的 Claude Code：架构、治理与工程实践

**Source:** https://x.com/HiTw93/status/2032091246588518683
**Author:** Tw93 (@HiTw93) — Creator of Kaku, Mole, Pake, MiaoYan
**Published:** 2026-03-12 (edited)
**Engagement:** 191 replies, 2,191 reposts, 8,531 likes, 17,242 bookmarks, 2.8M views
**Fetch method:** Playwright MCP (accessibility tree, focus mode)

---

## 0. 太长不读

This article comes from 6 months of deep Claude Code usage (two accounts, $40/month each). Initially treated it as ChatBot, quickly realized problems: context gets messy, more tools = worse results, longer rules = less compliance. The issue isn't prompts — it's understanding how the system is designed.

The article covers: how Claude Code works underneath, why context gets messy and how to govern it, Skills and Hooks design, Subagents usage, Prompt Caching architecture impact, and how to write a truly useful CLAUDE.md.

Key insight: Claude Code should be viewed as 6 layers. Strengthening only one layer causes imbalance.

## 1. 底层运行机制

Core loop: 收集上下文 → 采取行动 → 验证结果 → [完成 or 回到收集]

The bottleneck is almost never model intelligence — it's wrong context or inability to verify/rollback.

Five key dimensions to watch: context loading order (not the model) for unstable results; control layer design for runaway automation; context pollution from intermediate artifacts for quality degradation in long sessions.

## 2. 概念边界：MCP / Plugin / Tools / Skills / Hooks / Subagents

Simple memory: give Claude new action capabilities → Tool/MCP; give it a work methodology → Skill; need isolated execution → Subagent; need deterministic constraints and auditing → Hook; cross-project distribution → Plugin.

## 3. 上下文工程：最重要的系统约束

Context is not a "capacity problem" — it's a "noise problem." Useful info gets drowned by irrelevant content.

### Real context cost breakdown

200K total context:
- Fixed overhead (~15-20K): System instructions ~2K, Skill descriptors ~1-5K, MCP Server tool definitions ~10-20K (biggest hidden killer), LSP state ~2-5K
- Semi-fixed (~5-10K): CLAUDE.md ~2-5K, Memory ~1-2K
- Dynamic available (~160-180K): conversation history, file content, tool call results

A typical MCP Server (e.g. GitHub) has 20-30 tool definitions, ~200 tokens each = 4,000-6,000 tokens. Connect 5 servers = 25,000 tokens (12.5%) just in fixed overhead. "I was shocked when I first calculated this."

### Recommended context layering
- Always resident → CLAUDE.md: project contract / build commands / prohibitions
- Path-loaded → rules: language / directory / file-type specific rules
- On-demand → Skills: workflows / domain knowledge
- Isolated → Subagents: large explorations / parallel research
- Not in context → Hooks: deterministic scripts / audit / blocking

### Context best practices
- Keep CLAUDE.md short, hard, executable. Anthropic's own CLAUDE.md is only ~2.5K tokens
- Put large reference docs into Skills supporting files, not SKILL.md body
- Use .claude/rules/ for path/language rules instead of bloating root CLAUDE.md
- In long sessions, proactively use /context to check consumption — don't wait for auto-compaction
- Task switching: prefer /clear; same task new phase: use /compact
- Write Compact Instructions in CLAUDE.md — you control what gets preserved during compression, not the algorithm

### Tool Output noise — another hidden context killer
Tool outputs (cargo test, git log, find, grep) can easily fill context with thousands of lines. RTK (Rust Token Killer) auto-filters command output before it reaches Claude — e.g., cargo test: 262 tests → "✓ cargo test: 262 passed (1 suite, 0.08s)". Open source: https://github.com/rtk-ai/rtk

### Compaction trap
Default compression algorithm prioritizes deleting "re-readable" content (tool outputs, file content) but also discards architecture decisions and constraint reasoning. Two hours later, the agent doesn't remember what was decided earlier.

Solution: Write Compact Instructions in CLAUDE.md:
```markdown
## Compact Instructions
When compressing, preserve in priority order:
1. Architecture decisions (NEVER summarize)
2. Modified files and their key changes
3. Current verification status (pass/fail)
4. Open TODOs and rollback notes
5. Tool outputs (can delete, keep pass/fail only)
```

Also: before starting new sessions, have Claude write a HANDOFF.md with current progress, what was tried, what worked, what didn't, next steps. The next Claude instance reads only this file.

### Plan Mode engineering value
Plan Mode separates exploration from execution. Explore read-only, confirm approach, then execute. "For complex refactors, migrations, cross-module changes, this is much better than rushing to code." Advanced: one Claude writes plan, another (Codex) reviews as "senior engineer" — AI reviewing AI works great.

## 4. Skills 设计

A good Skill should:
- Description tells model "when to use me" (not "what I do")
- Has complete steps, inputs, outputs, and stop conditions
- Body contains only navigation and core constraints; large docs go to supporting files
- Side-effect Skills must set disable-model-invocation: true

### Three Skill types (from Kaku project):
1. **Checklist type** (quality gate): pre-release checks
2. **Workflow type** (standardized operations): config migration with built-in rollback
3. **Domain expert type** (decision framework): runtime diagnosis with evidence collection + decision matrix

### Skill descriptor optimization
Every enabled Skill's descriptor is always in context:
- Inefficient (~45 tokens): long multi-sentence description
- Efficient (~9 tokens): "Use for PR reviews with focus on correctness."

### Auto-invoke strategy:
- High-freq (>1/session) → keep auto-invoke, optimize descriptor
- Low-freq (<1/session) → disable-auto-invoke, manual trigger
- Very low-freq (<1/month) → remove Skill, move to docs

## 5. 工具设计：怎么让 Claude 少选错

Good tools for agents ≠ good APIs for humans. For agents, the priority is making tools easy to use correctly.

Design principles:
- Prefix names by system/resource: github_pr_*, jira_issue_*
- Support response_format: concise / detailed for large responses
- Error responses should teach the model how to fix, not just throw opaque codes
- Merge into high-level task tools when possible; avoid exposing low-level fragments

### Internal tool evolution lessons:
**AskUserQuestion evolution:**
- v1: Added question parameter to existing tools → model usually ignored it
- v2: Required specific markdown format in output → model often "forgot"
- v3: Independent AskUserQuestion tool → explicit call = pause, no ambiguity, much more reliable

Lesson: if you need Claude to stop and ask, give it a dedicated tool. Flags and format conventions get skipped.

**Todo tool evolution:** Early TodoWrite tool + periodic reminders → model got stronger → tool became a constraint rather than help. "Interesting lesson: the limitations added because the model was weak became shackles when it got stronger."

**Search tool evolution:** Started with RAG vector DB → fast but needed indexing, fragile across environments, and "Claude didn't like using it." Switched to Grep tool for self-directed search → much better. Bonus: Claude reads Skill files → Skill references other files → model recursively reads → discovers info on demand. This became "progressive disclosure."

## 6. Hooks

Hooks = taking things that can't be left to Claude's improvisation back into deterministic flow.

### Suitable vs unsuitable for Hooks:
- Suitable: block editing protected files, auto-format after Edit, inject dynamic context at SessionStart, push notifications on completion
- Not suitable: complex semantic judgments needing lots of context, long-running business processes, multi-step reasoning decisions → use Skill or Subagent

### CLAUDE.md + Skills + Hooks three-layer stack:
- CLAUDE.md: declares "must pass tests and lint before commit"
- Skill: tells Claude testing order, how to read failures, how to fix
- Hook: hard validation on critical paths, blocking when needed
"All three together is the stable setup. Any one missing creates gaps."

### Output length: always pipe through | head -30 to avoid Hook output polluting context. Or use RTK for systematic filtering.

## 7. Subagents

Subagent = independent Claude instance dispatched from main conversation, with own context window, specified tools only, reports results back.

The biggest value is not "parallelism" but **isolation**. Code scanning, test running, reviews — these produce huge output that crowds out useful context in the main thread. Give to Subagent → main thread gets only a summary.

Built-in: Explore (read-only, runs Haiku for cost savings), Plan (planning/research), General-purpose. Can customize.

Configuration constraints:
- tools / disallowedTools: limit tools (don't give same permissions as main thread)
- model: exploration → Haiku/Sonnet, important reviews → Opus
- maxTurns: prevent runaway
- isolation: worktree for file modifications

Anti-patterns:
- Subagent permissions as wide as main thread (defeats isolation purpose)
- Unfixed output format (main thread can't consume)
- Strong dependencies between subtasks requiring shared intermediate state

## 8. Prompt Caching

"Cache Rules Everything Around Me" — Claude Code's entire architecture is built around prompt caching. High hit rate saves money AND loosens rate limits. Anthropic runs alerts on hit rate — too low triggers a SEV.

### Prompt layout for caching:
1. System Prompt → static, locked
2. Tool Definitions → static, locked
3. Chat History → dynamic, comes later
4. Current user input → last

### Cache-breaking pitfalls:
- Timestamps in static system prompt (changes every time)
- Non-deterministically reordering tool definitions
- Adding/removing tools mid-session

Dynamic info (like current time) → put in user message with <system-reminder> tags, not system prompt.

### Don't switch models mid-session
Prompt cache is model-specific. Switching from Opus to Haiku after 100K tokens is actually MORE expensive because you rebuild the entire cache for Haiku. Use Subagent for handoff instead.

### defer_loading for tools
Claude Code has dozens of MCP tools. Including all every request is expensive, but removing mid-session breaks cache. Solution: send lightweight stubs (tool name only, marked defer_loading: true). Model discovers them via ToolSearch tool. Full schema loads only when model selects → cache prefix stays stable.

### Plan Mode cache preservation
Intuitively Plan Mode should switch to read-only tool set, but that breaks cache. Actual implementation: EnterPlanMode is a tool the model calls itself. Tool set doesn't change → cache unaffected.

## 9. 验证闭环

"Claude saying it's done" is useless. You need to know if it's correct, be able to rollback, and have an audit trail.

Verifier levels:
- Lowest: exit codes, lint, typecheck, unit test
- Middle: integration tests, screenshot comparison, contract tests, smoke tests
- Higher: production log verification, monitoring metrics, human review checklists

Key insight: "If you can't articulate 'what does done look like' for a task, it's probably not suitable for Claude to complete autonomously."

## 10-11. Commands + CLAUDE.md

Key commands for active context management: /context, /clear, /compact, /memory, /mcp, /hooks, /permissions, /sandbox, /model, /simplify, /rewind, /btw, /insight

CLAUDE.md is a collaboration contract, not team docs or knowledge base. Only put things that must be true every session.

What to include: build/test/run commands, key directory structure, coding conventions, non-obvious environment traps, NEVER list, Compact Instructions
What to exclude: long background intros, full API docs, vague principles like "write high quality code," info Claude can infer from reading the repo

"Start with nothing. When you find yourself repeating the same thing, add it."

## 12-13. Lessons from Kaku project + Anti-patterns

Environment transparency matters: add a `doctor` command for structured health reports. CLI with semantic subcommands (init, config, reset) works much better than Claude guessing config file layout.

## 14. /health check

Open-source Skill: tw93/claude-health — one-command check of your Claude Code configuration against these principles. Outputs priority report: fix now / structural issues / can do later.

## 15. Three stages of Claude Code usage
1. "How do I use this feature"
2. Learning features and patterns
3. "How do I make the agent run autonomously under constraints" — this is the real shift
