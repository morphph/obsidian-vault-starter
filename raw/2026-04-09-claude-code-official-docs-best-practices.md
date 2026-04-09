# Claude Code Official Docs — Best Practices Feature Reference

**Source:** Official Anthropic documentation at code.claude.com/docs/en/
**Compiled:** 2026-04-09
**Purpose:** Cross-reference for Boris Cherny's best practices threads — official docs for every feature he mentions

---

## Documentation URLs Index

| Feature | Official URL |
|---------|-------------|
| CLAUDE.md / Memory | https://code.claude.com/docs/en/memory |
| Plan Mode / Permission Modes | https://code.claude.com/docs/en/permission-modes |
| Skills (includes slash commands) | https://code.claude.com/docs/en/skills |
| Hooks | https://code.claude.com/docs/en/hooks |
| Settings | https://code.claude.com/docs/en/settings |
| Sub-agents | https://code.claude.com/docs/en/sub-agents |
| MCP | https://code.claude.com/docs/en/mcp |
| Chrome Extension | https://code.claude.com/docs/en/chrome |
| Worktrees | https://code.claude.com/docs/en/common-workflows |
| Permissions | https://code.claude.com/docs/en/permissions |
| Model Config | https://code.claude.com/docs/en/model-config |
| Output Styles | https://code.claude.com/docs/en/output-styles |
| Statusline | https://code.claude.com/docs/en/statusline |
| Voice Dictation | https://code.claude.com/docs/en/voice-dictation |
| Remote Control | https://code.claude.com/docs/en/remote-control |
| Teleport | https://code.claude.com/docs/en/claude-code-on-the-web |
| Scheduled Tasks (local) | https://code.claude.com/docs/en/scheduled-tasks |
| Scheduled Tasks (cloud) | https://code.claude.com/docs/en/web-scheduled-tasks |
| --bare mode | https://code.claude.com/docs/en/headless#start-faster-with-bare-mode |
| /batch | https://code.claude.com/docs/en/skills#bundled-skills |
| Commands reference | https://code.claude.com/docs/en/commands |
| CLI reference | https://code.claude.com/docs/en/cli-reference |
| Interactive mode | https://code.claude.com/docs/en/interactive-mode |
| Desktop / Dispatch | https://code.claude.com/docs/en/desktop#sessions-from-dispatch |

---

## Feature Details

### CLAUDE.md
- Loaded every API call, 2-5K tokens fixed
- Scope hierarchy: managed > project > user > local
- `.claude/rules/` for path-scoped rules with glob frontmatter
- Import syntax: `@path/to/file` (max 5 hops)
- Target under 200 lines per file
- Auto memory: `~/.claude/projects/<project>/memory/MEMORY.md` (first 200 lines / 25KB)
- `/init` generates starter; `/memory` browses loaded files

### Plan Mode
- Permission mode: read-only exploration, no file edits
- Activate: Shift+Tab (cycle modes), `--permission-mode plan`, or `/plan` prefix
- After planning: approve → auto mode, accept edits, review each, keep planning, or Ultraplan
- 6 permission modes total: default, acceptEdits, plan, auto, dontAsk, bypassPermissions

### Skills (successor to Commands)
- `.claude/skills/<name>/SKILL.md` replaces `.claude/commands/<name>.md`
- Old commands still work; skills add: directory for supporting files, frontmatter, auto-discovery, path-scoping
- Scopes: enterprise (managed) > personal (~/.claude/skills/) > project (.claude/skills/) > plugin
- Frontmatter: name, description, argument-hint, disable-model-invocation, allowed-tools, model, effort, context (fork), hooks, paths
- String substitutions: $ARGUMENTS, $N, ${CLAUDE_SESSION_ID}, ${CLAUDE_SKILL_DIR}
- Dynamic context: `` !`command` `` runs shell before injection
- Bundled: /batch, /claude-api, /debug, /loop, /simplify

### Hooks
- 22 event types: SessionStart, InstructionsLoaded, UserPromptSubmit, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, Notification, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure, TeammateIdle, CwdChanged, FileChanged, PreCompact, PostCompact, ConfigChange, Elicitation, ElicitationResult, WorktreeCreate, WorktreeRemove, SessionEnd
- 4 handler types: command, http, prompt, agent
- Exit codes: 0=success, 2=blocking error, 1=non-blocking error
- JSON output can control: continue, stopReason, permissionDecision, updatedInput, additionalContext
- Matcher patterns for tool-specific hooks

### Sub-agents
- Built-in: Explore (Haiku, read-only), Plan (inherits, read-only), General-purpose (inherits, all tools)
- Custom: `.claude/agents/<name>.md` with YAML frontmatter
- Frontmatter: name, description, tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory, background, effort, isolation, color, initialPrompt
- Invocation: automatic (description match), @mention, --agent flag, natural language
- Cannot spawn sub-sub-agents (no nesting)
- CLI-defined: `--agents '{json}'` for ephemeral agents
- `/agents` command for interactive management

### MCP
- 3 transports: HTTP (recommended), SSE (deprecated), stdio (local)
- 3 scopes: local (default, ~/.claude.json), project (.mcp.json, version controlled), user (~/.claude.json global)
- Commands: claude mcp add/list/get/remove, /mcp in-session
- OAuth 2.0 support, env var expansion in .mcp.json
- Popular servers: Sentry, GitHub, Notion, Stripe, Asana, Airtable
- MCP_TIMEOUT env var, MAX_MCP_OUTPUT_TOKENS (default warning 10K)

### Chrome Extension
- Beta. Requires Chrome/Edge + Claude in Chrome extension v1.0.36+ + Claude Code v2.0.73+
- Start: `claude --chrome` or `/chrome`
- Uses Chrome Native Messaging protocol
- Capabilities: live debugging, design verification, web app testing, authenticated apps, data extraction, task automation, session recording (GIF)
- Pauses for manual login/CAPTCHA intervention
- Not supported: Brave, Arc, WSL

### Worktrees
- `claude --worktree feature-auth` or `claude -w`
- Creates `.claude/worktrees/<name>/` with branch `worktree-<name>`
- Branches from origin/HEAD
- .worktreeinclude for auto-copying gitignored files (.env etc)
- Cleanup: auto-removed if no changes; prompted if changes exist
- Subagent worktrees: `isolation: worktree` in frontmatter
- /resume shows sessions across worktrees

### Model Config
- Aliases: default, best, sonnet, opus, haiku, sonnet[1m], opus[1m], opusplan
- Set via: /model, --model, ANTHROPIC_MODEL env, settings
- Extended thinking: Option+T toggle, effort levels low/medium/high/max
- "ultrathink" in prompt triggers high effort for single turn
- 1M context: append [1m] suffix

### /teleport
- Pulls cloud session into local terminal
- `/teleport` or `claude --teleport` or `claude --teleport <session-id>`
- One-way: cloud → terminal only
- Requirements: clean git state, correct repo, branch pushed, same account

### /remote-control
- Connects claude.ai/code or mobile app to local CLI session
- `claude --remote-control` or `/remote-control`
- Everything runs locally; web is just a window
- Supports --spawn for multiple concurrent sessions
- Auto-reconnects after sleep/network drops

### /loop
- Bundled skill. Syntax: `/loop [interval] <prompt>`
- Default: 10min. Supports s/m/h/d suffixes
- Can loop over other commands: `/loop 20m /review-pr 1234`
- Session-scoped. Max 50 tasks, 7-day expiry

### /schedule
- Cloud scheduled tasks on Anthropic infrastructure
- Create via web UI, Desktop, or /schedule in CLI
- Hourly/Daily/Weekdays/Weekly, minimum 1 hour
- Each run: new cloud session, clones repo from GitHub
- Can connect MCP connectors (Slack, Linear, etc)

### /branch
- `/branch [name]` — forks conversation at current point
- Alias: /fork (original name)
- Creates new session ID with conversation state to that point

### /btw
- `/btw <question>` — side question without adding to conversation
- Works during streaming (mid-response)
- Runs in separate context, doesn't pollute main conversation

### /batch
- Bundled skill. Orchestrates large-scale parallel changes
- Researches → decomposes into 5-30 units → presents plan → spawns agents in worktrees
- Each agent: implements, tests, opens PR

### /voice
- `/voice` toggles push-to-talk dictation
- Default key: Space (hold). Rebindable via keybindings.json
- Streams to Anthropic servers for transcription
- 20 languages. Tuned for coding vocabulary
- Requires claude.ai account (not API key)

### --bare
- Skips hooks, LSP, plugins, MCP, skills, auto memory, CLAUDE.md
- Only retains Bash, file read, file edit tools
- Must use ANTHROPIC_API_KEY (skips OAuth)
- Recommended for scripted/SDK calls
- Can manually load context via flags

### --add-dir
- `claude --add-dir ../apps ../lib`
- Grants file access but NOT config discovery
- Also available as `/add-dir` mid-session

### --agent
- `claude --agent my-custom-agent`
- Loads subagent definition as session's primary agent
- Same resolution order as subagent files

### Output Styles
- Built-in: Default, Explanatory, Learning
- Explanatory: educational insights between tasks
- Learning: collaborative, TODO(human) markers
- Custom: markdown files in ~/.claude/output-styles or .claude/output-styles
- Frontmatter: name, description, keep-coding-instructions (boolean)

### /statusline
- Customizable bottom bar running shell script
- Receives JSON: model, context usage, cost, workspace, rate limits, session info
- `/statusline <description>` auto-generates script
- Supports ANSI colors, multiple lines, clickable links

### /context
- Visualizes context usage as colored grid
- Shows optimization suggestions
- Flags: context-heavy tools, memory bloat, capacity warnings

### /clear and /compact
- `/clear` (aliases /reset, /new): clears history, frees context
- `/compact [instructions]`: compacts with optional focus
- Example: `/compact focus on the auth module changes`

### Cowork Dispatch
- In Desktop app's Cowork tab
- Message from mobile → Dispatch spawns Code session
- Push notification when done or needs approval
- Requires Pro or Max plan
- Distinct from Remote Control (RC connects to existing session; Dispatch creates new ones)
