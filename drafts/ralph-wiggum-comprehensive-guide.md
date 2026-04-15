---
status: draft
sources:
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
  - raw/2026-04-15-ghuntley-ralph-wiggum-original.md
  - raw/2026-04-15-anthropic-ralph-wiggum-plugin.md
  - raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md
  - raw/2026-04-15-anthropic-claude-code-sandboxing.md
  - raw/2026-04-15-humanlayer-brief-history-of-ralph.md
  - raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md
  - raw/2026-04-15-aihero-getting-started-with-ralph.md
  - raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md
  - raw/2026-04-15-repo-ralph-orchestrator.md
platform: blog
created: 2026-04-15
last-updated: 2026-04-15
tags: [draft]
---

<!-- HOOK: A $50,000 contract delivered for $297 in API costs. An entire programming language built while its creator slept. This is what happens when you put an AI coding agent in a while loop and walk away. -->

# The Ralph Wiggum Guide: Autonomous AI Coding From First Loop to Production

A $50,000 contract delivered for $297 in API costs. A programming language — compiler, standard library, LLVM integration — built over three months of autonomous iteration. Six repositories shipped overnight during a Y Combinator hackathon. Test coverage taken from 16% to 100% while the developer did something else.

This is the Ralph Wiggum technique. Named after the Simpsons character who never stops trying, it's the simplest and most powerful pattern in autonomous AI coding: put your agent in a loop, define what "done" looks like, and walk away.

This guide covers everything — from your first loop to production-grade orchestration. Whether you're running Claude Code, Codex, Gemini, or any other AI coding CLI, the pattern is the same.

---

## What Is Ralph?

AI coding has evolved through four distinct phases:

1. **Vibe coding** — let the AI write code without checking it. Fast, but the quality suffers.
2. **Planning** — ask the AI to plan before it codes. Better quality, but limited to one context window.
3. **Multi-phase plans** — break large features into phases, each with a separate prompt. Scales better, but requires constant human involvement to write each prompt.
4. **Ralph** — run the same prompt in a loop. The agent chooses the task. You define the end state.

At its simplest, Ralph is one line of bash:

```bash
while :; do cat PROMPT.md | claude-code ; done
```

That's it. Every iteration reads a plan, picks a task, implements it, runs tests, commits, and reports progress. When everything is done, it stops.

The key shift: **the agent chooses the task, not you.** With multi-phase plans, a human writes a new prompt at the start of each phase. With Ralph, the agent picks what to work on next from your PRD. You define the end state. Ralph gets there.

Geoffrey Huntley, who created the technique in mid-2025, puts it this way: **"The loop is the hero, not the model."** Don't wait for smarter models. Build persistent systems that iterate until they succeed.

---

## Getting Started: Your First Ralph Loop

### Prerequisites

- An AI coding CLI (Claude Code, Codex, OpenCode, Copilot CLI, etc.)
- Docker Desktop 4.50+ (for safe AFK execution)

### Step 1: Install Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Run `claude` to authenticate.

### Step 2: Set Up Docker Sandbox

Docker provides an isolated environment where the agent can execute commands safely:

```bash
docker sandbox run claude
```

This mounts only your current directory. The agent can edit project files and commit — but can't touch your home directory, SSH keys, or system files. This matters a lot when you walk away.

### Step 3: Create Your PRD

Use Claude's plan mode (`shift-tab`) to develop your PRD iteratively. Save it as `PRD.md`. Format doesn't matter — markdown checklists, JSON, plain text — as long as individual tasks are extractable.

The JSON format with a `passes` field works especially well (inspired by Anthropic's research on long-running agents):

```json
[
  {
    "category": "functional",
    "description": "New chat button creates a fresh conversation",
    "steps": [
      "Click the 'New Chat' button",
      "Verify a new conversation is created",
      "Check that chat area shows welcome state"
    ],
    "passes": false
  }
]
```

Ralph marks `passes` to `true` when complete. The PRD becomes both scope definition and progress tracker.

Also create a progress file:

```bash
touch progress.txt
```

### Step 4: Run Your First HITL Loop

Start with a single-iteration, human-in-the-loop script. Watch everything the agent does:

```bash
#!/bin/bash
# ralph-once.sh

claude --permission-mode acceptEdits "@PRD.md @progress.txt \
1. Read the PRD and progress file. \
2. Find the next incomplete task and implement it. \
3. Commit your changes. \
4. Update progress.txt with what you did. \
ONLY DO ONE TASK AT A TIME."
```

Run it, watch, intervene when needed. This is how you learn Ralph and refine your prompt.

### Step 5: Go AFK

Once your prompt is solid, wrap it in a loop with a cap:

```bash
#!/bin/bash
# afk-ralph.sh
set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <iterations>"
  exit 1
fi

for ((i=1; i<=$1; i++)); do
  result=$(docker sandbox run claude --permission-mode acceptEdits -p \
  "@PRD.md @progress.txt \
  1. Find the highest-priority task and implement it. \
  2. Run your tests and type checks. \
  3. Update the PRD with what was done. \
  4. Append your progress to progress.txt. \
  5. Commit your changes. \
  ONLY WORK ON A SINGLE TASK. \
  If the PRD is complete, output <promise>COMPLETE</promise>.")

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "PRD complete after $i iterations."
    exit 0
  fi
done
```

Run it:

```bash
./afk-ralph.sh 20
```

Then do something else. Come back when it's done.

---

## The Methodology: How to Structure Work for Ralph

### Huntley's Three Phases

Geoffrey Huntley's official playbook breaks work into three phases with two prompts:

1. **Requirements Definition** — Human and LLM collaborate on Jobs-to-Be-Done (JTBD). Break them into discrete topics. Generate specification files in `specs/`.

2. **Planning Mode** — Claude analyzes specs versus existing code and produces `IMPLEMENTATION_PLAN.md` with prioritized tasks. This plan is **disposable** — regeneration costs one planning loop. Never fight to save a plan.

3. **Building Mode** — Claude implements tasks from the plan, runs tests, commits changes, and updates the plan. One task per loop.

Key files in this system:

| File | Purpose |
|------|---------|
| `PROMPT_plan.md` | Planning mode instructions |
| `PROMPT_build.md` | Building mode instructions |
| `AGENTS.md` | Operational guide: build/test commands (~60 lines) |
| `IMPLEMENTATION_PLAN.md` | Disposable task list, updated by Claude |
| `specs/*` | Topic-specific requirement documents |

### Progress Tracking

Every Ralph loop should emit a `progress.txt` file, committed directly to the repo. AI agents forget everything between context windows. Without a progress file, Ralph must explore the entire repo to understand current state.

A progress file short-circuits that exploration. Keep it concise:

- Tasks completed in this session
- Decisions made and why
- Blockers encountered
- Files changed

Use the verb "append" in your prompt to make sure Ralph doesn't overwrite previous entries.

### Scope Definition — The Make-or-Break

Vague tasks are dangerous. Ralph might loop forever finding endless improvements, or take shortcuts and declare victory prematurely.

Real example: Running Ralph to increase test coverage on a CLI. After three iterations, Ralph reported "Done with all user-facing commands" — but it had skipped internal commands entirely, deciding they weren't user-facing.

What to specify:

| What to Specify | Why It Prevents Shortcuts |
|-----------------|---------------------------|
| Files to include | Ralph won't ignore "edge case" files |
| Stop condition | Ralph knows when "complete" actually means complete |
| Edge cases | Ralph won't decide certain things don't count |

You can adjust scope mid-flight. Set `passes` back to `false`, add notes, add new PRD items. Ralph adapts.

---

## The Principles: What Makes Ralph Work

### 1. One Thing Per Loop

Each iteration addresses exactly one feature. This conserves the ~170K token context window and prevents the agent from diverging. It's tempting to bundle tasks for efficiency, but context rot — where LLM output quality degrades as context fills — punishes you for it.

Bias small. Especially for AFK runs, where you're not watching.

### 2. Feedback Loops Are Non-Negotiable

Ralph's success depends entirely on feedback loops. The more you give it, the higher quality code it produces.

| Feedback Loop | What It Catches |
|---------------|-----------------|
| TypeScript types | Type mismatches, missing props |
| Unit tests | Broken logic, regressions |
| Playwright MCP | UI bugs, broken interactions |
| ESLint / linting | Code style, potential bugs |
| Pre-commit hooks | Blocks bad commits entirely |

The best setup blocks commits unless everything passes. Ralph can't declare victory if the tests are red.

For subjective criteria (tone, aesthetics, UX quality), use **LLM-as-judge** — a separate evaluation with binary pass/fail. "Is this UX good?" becomes a testable gate.

As Matt Pocock puts it: "These aren't AI-specific techniques. They're just good engineering. Ralph makes them non-negotiable."

### 3. Backpressure Over Prescription

Don't tell the agent *how* to do things. Create gates that reject bad work.

Instead of: "First write tests, then implement the function, then run the linter..."
Write: "Run tests, typecheck, and lint before committing. Do NOT commit if any feedback loop fails."

The agent figures out the how. You define the what.

### 4. Prioritize Risky Tasks First

Without explicit guidance, Ralph picks easy wins. Seasoned engineers know you should nail down the hard stuff first.

| Task Type | Priority | Why |
|-----------|----------|-----|
| Architectural work | High | Decisions cascade through entire codebase |
| Integration points | High | Reveals incompatibilities early |
| Unknown unknowns | High | Better to fail fast than fail late |
| UI polish | Low | Can be parallelized later |
| Quick wins | Low | Easy to slot in anytime |

Use HITL for risky tasks — architectural decisions stay forever. Save AFK for when the foundation is solid.

### 5. The Repo Wins

Your instructions compete with your codebase. The prompt is a few lines. The codebase is thousands of lines of evidence. When they conflict, agents follow the codebase.

You can write "never use `any` types" in your prompt. But if Ralph sees `any` throughout your existing code, it will follow the codebase, not your instructions.

**Agents amplify what they see.** Poor code leads to poorer code. A human commits once or twice a day. Ralph can pile dozens of commits in hours. If those commits are low quality, software entropy compounds fast.

Before letting Ralph loose:
- Keep your codebase clean
- Use feedback loops (linting, types, tests) to enforce standards
- Make quality expectations explicit: "Production code. Must be maintainable." or "Prototype. Speed over perfection."

### 6. Prompt Language Matters

Huntley discovered specific phrasings that Claude responds to better:

- **"study"** (not "read") — implies deeper analysis
- **"don't assume not implemented"** — forces codebase search before creating something new
- **"using parallel subagents"** — triggers parallelization for expensive operations
- **"capture the why"** — documents reasoning, not just actions
- **"DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS"** — prevents the lazy shortcut

The agent also benefits from self-learning. Include instructions for it to update `AGENTS.md` when it discovers better build/execution approaches.

---

## Security: Sandboxing for AFK Loops

When you walk away, the sandbox is the **only security boundary**. With `--dangerously-skip-permissions` or `--permission-mode acceptEdits`, nothing else stops the agent.

### Docker Sandboxes (Recommended for AFK)

```bash
docker sandbox run claude
```

This runs Claude Code inside a container. Your current directory is mounted, but nothing else. Ralph can edit project files and commit — but can't touch your home directory, SSH keys, or system files.

Tradeoff: your global `AGENTS.md` and user skills won't be loaded. For most Ralph loops, this is fine.

### Native Sandboxing (Alternative)

Claude Code's built-in sandboxing uses OS-level primitives:
- **macOS**: Seatbelt — works out of the box
- **Linux/WSL2**: bubblewrap — `sudo apt-get install bubblewrap socat`

Enable with `/sandbox`. In auto-allow mode, sandboxed commands run without permission prompts. Internally, Anthropic reports a **84% reduction in permission prompts**.

Both filesystem and network isolation are enforced. Without network isolation, a compromised agent could exfiltrate SSH keys. Without filesystem isolation, it could backdoor system resources.

The sandbox runtime is open-sourced: `npx @anthropic-ai/sandbox-runtime <command>` — can sandbox any program, not just Claude Code.

**Rule of thumb:** HITL sandboxes are optional. AFK sandboxes are essential. Overnight sandboxes are non-negotiable.

---

## The Official Plugin vs The Bash Loop

There are two ways to run Ralph, and the community is split on which is better.

### The Bash Loop (Original)

```bash
while :; do cat PROMPT.md | claude-code ; done
```

Each iteration starts with a **fresh context**. The agent re-reads specs, plan, and code every cycle. Huntley designed this intentionally — fresh context means no accumulated confusion, no context rot.

### The Anthropic Plugin (Official)

Anthropic shipped an official Ralph Wiggum plugin in December 2025, formalized by Boris Cherny (head of Claude Code):

```bash
/ralph-loop "Build a REST API for todos. Output <promise>COMPLETE</promise> when done." \
  --completion-promise "COMPLETE" \
  --max-iterations 50
```

The plugin uses a **Stop hook** that intercepts Claude's exit attempts. The agent works, tries to exit, the hook blocks exit and feeds the same prompt back. The loop happens inside your current session.

Commands:
- `/ralph-loop` — start the loop
- `/cancel-ralph` — stop it

### Which One?

| | Bash Loop | Plugin |
|---|-----------|--------|
| Context | Fresh each iteration | Accumulates |
| Setup | Script file needed | Built-in command |
| Context rot risk | None | Grows with iterations |
| Creator preference | Huntley, Horthy | Anthropic |

Dex Horthy (HumanLayer), who's been using Ralph since the early days, still prefers "5-line bash loops" over the official plugin. The plugin "dies in cryptic ways unless you have `--dangerously-skip-permissions`."

Huntley's core argument: fresh context is reliability. The "smart zone" is 40-60% of the ~176K usable tokens. Beyond that, quality degrades.

For most users starting out: **use the bash loop.** It's simpler to reason about, easier to debug, and follows the original design intent. Use the plugin when you want convenience and are running short, well-scoped tasks.

---

## Scaling Up: Ralph Orchestrator

For production-grade Ralph, there's Ralph Orchestrator — a 2,702-star Rust framework by Mikey O'Brien that extends the basic loop into a full orchestration system.

### Installation

```bash
npm install -g @ralph-orchestrator/ralph-cli
```

### Key Features

**Multi-backend support** — Not just Claude Code. Ralph Orchestrator works with Gemini CLI, Codex, Kiro, Amp, Copilot CLI, OpenCode, and Roo.

```bash
ralph init --backend claude
ralph plan "Add user authentication with JWT"
ralph run -p "Implement the feature in specs/user-authentication/"
```

**Hat System** — Specialized agent personas coordinating through an event bus. Think of hats as lightweight multi-agent architecture without separate processes. A "reviewer" hat triggers on `review.file` events, a "synthesizer" hat aggregates results.

**Agent Waves** — Intra-loop parallelism. A hat with `concurrency > 1` spawns multiple parallel workers within one iteration. Scatter-gather pattern: agent emits wave events → N parallel workers → results merged back. Breaks the "one thing per loop" limitation for reviewable, parallelizable work.

**Parallel Loops** — Multiple orchestration loops on the same repo using `git worktree`. The primary loop holds `.ralph/loop.lock` and manages a merge queue. Worktree loops have isolated filesystems with symlinked memories and specs.

**RObot (Telegram HITL)** — A third mode between pure HITL and pure AFK. Agents emit questions via Telegram and block until answered. Humans can send proactive guidance from their phone at any time. No need to sit at the keyboard.

```yaml
RObot:
  enabled: true
  telegram:
    bot_token: "your-token"
```

**Web Dashboard** — React + Vite frontend with Rust RPC API. Monitor and manage loops visually.

**MCP Server** — `ralph mcp serve` for integration with MCP-compatible clients.

### The Six Ralph Tenets

Ralph Orchestrator codifies the philosophy:

1. **Fresh Context Is Reliability** — Each iteration clears context. Optimize for the "smart zone" (40-60% of ~176K tokens).
2. **Backpressure Over Prescription** — Don't prescribe how; create gates that reject bad work.
3. **The Plan Is Disposable** — Regeneration costs one planning loop. Cheap.
4. **Disk Is State, Git Is Memory** — Memories and tasks are the handoff mechanisms.
5. **Steer With Signals, Not Scripts** — The codebase is the instruction manual.
6. **Let Ralph Ralph** — Sit *on* the loop, not *in* it. Tune like a guitar, don't conduct like an orchestra.

---

## Alternative Loop Types

Ralph isn't just for feature backlogs. Any task describable as "look at repo, improve something, report findings" fits the pattern:

**Test Coverage Loop:**
```
Find uncovered lines in the coverage report.
Write tests for the most critical uncovered code paths.
Run coverage again. Target: 80% minimum.
```

**Linting Loop:**
```
Run: npm run lint
Fix ONE linting error at a time.
Run lint again to verify the fix.
Repeat until no errors remain.
```

**Entropy Loop:**
```
Scan for code smells: unused exports, dead code, inconsistent patterns.
Fix ONE issue per iteration.
Document what you changed in progress.txt.
```

**Duplication Loop:** Hook Ralph up to `jscpd` to find duplicate code. Ralph identifies clones, refactors into shared utilities, and reports what changed.

---

## Limitations: When Not to Use Ralph

Be honest about what Ralph can and can't do:

- **Greenfield only** — Huntley is explicit: Ralph works best for new projects. Retrofitting existing codebases is problematic.
- **The overbaking phenomenon** — Leave Ralph running too long and it produces unexpected emergent behaviors. Like post-quantum cryptography support nobody asked for.
- **Senior oversight required** — Ralph amplifies skilled guidance but doesn't replace it. The operator's skill in prompt engineering and specification writing is the critical success factor.
- **Context compaction risk** — In long sessions, context compaction can cause drift. Huntley warns: "Compaction is the devil."
- **~90% completion, not 100%** — Expect to review and polish the last mile yourself.
- **Codebase garbage** — Until production release, expect temporary files and "unspecified latent behaviours." This is normal.

---

## The Economics

Ralph is configurable to any budget. You don't need to run massive AFK loops to benefit.

| Approach | Effort Per Phase | Best For |
|----------|------------------|----------|
| Multi-phase plans | Write new prompt each time | One-off large tasks |
| HITL Ralph | Rerun same prompt | Learning, refinement |
| AFK Ralph | Set and forget | Bulk work, automation |

Even if you never go AFK, HITL Ralph has big advantages over multi-phase planning. Running the same prompt over and over is simpler than writing a different prompt for each phase.

Local/open-source models aren't good enough for Ralph yet. You have to pay to play. But we're in a golden age: AI does magical things faster than humans, yet the market still pays human wages. The gap won't last.

---

## Timeline: How Ralph Got Here

| Date | Milestone |
|------|-----------|
| June 2025 | Geoffrey Huntley presents Ralph at a Twitter agentic coding meetup |
| July 2025 | Official blog launch: `while :; do cat PROMPT.md \| amp ; done` |
| Aug 2025 | 6 repos shipped overnight; "specification quality = output quality" proven |
| Sep 2025 | CURSED programming language launched (compiled to Zig via LLVM) |
| Oct 2025 | Conference presentations accelerate community adoption |
| Dec 2025 | Anthropic ships official Ralph Wiggum plugin for Claude Code |
| Jan 2026 | Matt Pocock's viral X thread (204K views, 4.8K bookmarks); bash vs plugin showdown |
| 2026+ | Mainstream adoption — workshops, awesome-ralph (849 stars), Ralph Orchestrator (2,702 stars) |

---

## What's Next

The Ralph ecosystem is growing fast. Two concepts point to where it's heading:

**Gas Town** (Steve Yegge concept): "Kubernetes for agents." Not just one loop, but orchestrated swarms of loops working on decomposed tasks. Distributed coordination at scale.

**MEOW** (Molecular Expression of Work): Granular task definitions that enable parallel agent coordination. The smallest unit of work an agent can meaningfully complete.

The pattern is clear: from one bash loop to orchestrated agent systems. The simplicity of Ralph — its elegant minimalism — is both its greatest strength and the foundation everything else builds on.

Start with a loop. Define what done looks like. Walk away.

<!-- CTA: Try your first Ralph loop today. Start HITL, go AFK when you're ready. The code ships while you sleep. -->

---

*Sources: Geoffrey Huntley (ghuntley.com/ralph, how-to-ralph-wiggum), Anthropic (Claude Code plugin, sandboxing docs), Matt Pocock (AI Hero — 11 Tips, Getting Started), Dex Horthy (HumanLayer — Brief History of Ralph), Dev Interrupted (Huntley interview), Ralph Orchestrator (mikeyobrien/ralph-orchestrator).*
