# 11 Tips For AI Coding With Ralph Wiggum

**Source:** https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
**Author:** Matt Pocock (AI Hero)
**Fetch method:** User-provided markdown content

---

If you're using AI coding CLIs like [Claude Code](https://code.claude.com/docs/en/overview), [Copilot CLI](https://github.com/features/copilot/cli), [OpenCode](https://opencode.ai/), and [Codex](https://openai.com/codex/), this article is for you.

Most developers use these tools interactively. You give it a task, watch it work, and intervene when it goes off-track. This is "human-in-the-loop" (HITL) coding.

But there's a new approach called [Ralph Wiggum](https://ghuntley.com/ralph/). Ralph runs your AI coding CLI in a loop, letting it work autonomously on a list of tasks. You define what needs to be done. Ralph figures out how - and keeps going until it's finished. In other words, it's long-running, autonomous, and unsupervised AFK coding.

This is not a quickstart guide. If you want to get up and running fast, read [Getting Started With Ralph](https://www.aihero.dev/getting-started-with-ralph).

### The 11 Tips

| #   | Tip                                                                         | Summary                                  |
| --- | --------------------------------------------------------------------------- | ---------------------------------------- |
| 1   | Ralph Is A Loop                                       | What Ralph is and why it works           |
| 2   | Start With HITL, Then Go AFK              | The two modes of running Ralph           |
| 3   | Define The Scope                                     | How to specify what "done" looks like    |
| 4   | Track Ralph's Progress                          | Using progress files between iterations  |
| 5   | Use Feedback Loops                                 | Types, tests, and linting as guardrails  |
| 6   | Take Small Steps                                     | Why smaller tasks produce better code    |
| 7   | Prioritize Risky Tasks                                         | Tackle hard problems first               |
| 8   | Explicitly Define Software Quality | Don't let Ralph cut corners              |
| 9   | Use Docker Sandboxes                             | Isolate AFK Ralph for safety             |
| 10  | Pay To Play                                              | Cost considerations and tradeoffs        |
| 11  | Make It Your Own                                    | Alternative loop types and customization |

## 1. Ralph Is A Loop

AI coding has evolved through distinct phases in the last year or so. Let's briefly define them:

**Vibe coding** is where you let the AI write code without really checking it. You "vibe" with the AI, accepting its suggestions without scrutiny. It's fast, but the code quality suffers.

**Planning** is where you ask the AI to plan before it codes. In Claude Code, you can enter plan mode to have the AI explore your codebase and create a plan before writing code. This improves quality, but you're still limited to what fits in one context window.

**Multi-phase plans** break large features into phases, each handled in a separate context window. You write a different prompt for each phase: "Implement the database schema," then "Add the API endpoints," then "Build the UI." This scales better, but requires constant human involvement to write each prompt.

**Ralph** simplifies everything. Instead of writing a new prompt for each phase, you run the same prompt in a loop:

```bash
# ralph.sh
# Usage: ./ralph.sh <iterations>

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <iterations>"
  exit 1
fi

# For each iteration, run Claude Code with the following prompt.
for ((i=1; i<=$1; i++)); do
  result=$(docker sandbox run claude -p \
"@some-plan-file.md @progress.txt \
1. Decide which task to work on next. \
This should be the one YOU decide has the highest priority, \
- not necessarily the first in the list. \
2. Check any feedback loops, such as types and tests. \
3. Append your progress to the progress.txt file. \
4. Make a git commit of that feature. \
ONLY WORK ON A SINGLE FEATURE. \
If, while implementing the feature, you notice that all work \
is complete, output <promise>COMPLETE</promise>. \
")

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "PRD complete, exiting."
    exit 0
  fi
done
```

Each iteration:

1. Looks at a plan file to see what needs to be done
2. Looks at a progress file to see what has already been done
3. Decides what to do next
4. Explores the codebase
5. Implements the feature
6. Runs feedback loops (types, linting, tests)
7. Commits the code

The key improvement here is that **the agent chooses the task, not you**.

With multi-phase plans, a human writes a new prompt at the start of each phase. With Ralph, the agent picks what to work on next from your PRD. You define the end state. Ralph gets there.

## 2. Start With HITL, Then Go AFK

There are two ways to run Ralph:

| Mode                         | How It Works                      | Best For                    |
| ---------------------------- | --------------------------------- | --------------------------- |
| **HITL** (human-in-the-loop) | Run once, watch, intervene        | Learning, prompt refinement |
| **AFK** (away from keyboard) | Run in a loop with max iterations | Bulk work, low-risk tasks   |

For HITL Ralph, keep a `ralph-once.sh` that runs a single iteration. You watch everything it does and step in when needed.

For AFK Ralph, always cap your iterations. Infinite loops are dangerous with stochastic systems. I typically use 5-10 iterations for small tasks, or 30-50 for larger ones.

HITL Ralph resembles pair programming. You and the AI work together, reviewing code as it's created. You can steer, contribute, and share project understanding in real-time.

Once your prompt is solid, AFK Ralph unlocks real leverage. Set it running, do something else, come back when it's done.

The progression is simple:

1. Start with HITL to learn and refine
2. Go AFK once you trust your prompt
3. Review the commits when you return

## 3. Define The Scope

Before you let Ralph run, you need to define what "done" looks like. This is a shift from planning to requirements gathering. Instead of specifying each step, you describe the desired end state and let the agent figure out how to get there.

### Formats For Defining Scope

There are many ways to define scope for Ralph:

- A markdown list of user stories
- GitHub issues or Linear tasks
- Using beads

One approach from Anthropic's research on long-running agents: structure PRD items as JSON with a `passes` field:

```json
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
```

Ralph marks `passes` to `true` when complete. The PRD becomes both scope definition and progress tracker.

### Why Scope Matters

The vaguer the task, the greater the risk. Ralph might loop forever, finding endless improvements. Or it might take shortcuts, declaring victory before you'd consider the job done.

Example: Running Ralph to increase test coverage on AI Hero CLI. After three iterations, Ralph reported "Done with all user-facing commands" but had skipped internal commands entirely.

### Adjusting PRDs Mid-Flight

You can adjust while Ralph is running:
- Already implemented but wrong? Set `passes` back to `false`, add notes, rerun.
- Missing a feature? Add a new PRD item even mid-loop.

## 4. Track Ralph's Progress

Every Ralph loop emits a `progress.txt` file, committed directly to the repo. Inspired by Anthropic's article on long-running agent harnesses.

AI agents are like super-smart experts who forget everything between tasks. Each new context window starts fresh. Without a progress file, Ralph must explore the entire repo to understand the current state.

A progress file short-circuits that exploration. Ralph reads it, sees what's done, and jumps straight into the next task.

### What Goes In The Progress File

- Tasks completed in this session
- Decisions made and why
- Blockers encountered
- Files changed

Ralph should commit after each feature for clean git log, diff capability, and rollback points.

## 5. Use Feedback Loops

Ralph's success depends on feedback loops. The more loops you give it, the higher quality code it produces.

| Feedback Loop       | What It Catches                |
| ------------------- | ------------------------------ |
| TypeScript types    | Type mismatches, missing props |
| Unit tests          | Broken logic, regressions      |
| Playwright MCP      | UI bugs, broken interactions   |
| ESLint / linting    | Code style, potential bugs     |
| Pre-commit hooks    | Blocks bad commits entirely    |

The best setup blocks commits unless everything passes. Ralph can't declare victory if the tests are red.

Great programmers don't trust their own code. They build automations and checks to verify what they ship. The same applies to AI agents.

## 6. Take Small Steps

The rate at which you can get feedback is your speed limit. Never outrun your headlights.

Context windows are limited, and LLMs get worse as they fill up — called context rot. The longer you go, the stupider the output.

### The Tradeoff

Each Ralph iteration has startup costs. But:
- Larger tasks mean less frequent feedback
- More context means lower quality code
- Smaller tasks mean higher quality, but slower progress

For AFK Ralph, keep PRD items small. For HITL Ralph, slightly larger is okay. Bias small.

## 7. Prioritize Risky Tasks

Ralph chooses its own tasks. Without explicit guidance, it will often pick the easiest.

Focus on spikes — things you don't know how they'll turn out. Build features end-to-end rather than layer by layer. Integrate early.

| Task Type          | Priority | Why                                       |
| ------------------ | -------- | ----------------------------------------- |
| Architectural work | High     | Decisions cascade through entire codebase |
| Integration points | High     | Reveals incompatibilities early           |
| Unknown unknowns   | High     | Better to fail fast than fail late        |
| UI polish          | Low      | Can be parallelized later                 |
| Quick wins         | Low      | Easy to slot in anytime                   |

Use HITL Ralph for risky tasks. Save AFK Ralph for when the foundation is solid.

## 8. Explicitly Define Software Quality

The agent doesn't know if this is a throwaway prototype or production code. You need to tell it explicitly.

| Repo Type  | What To Say                                   | Expected Behavior                  |
| ---------- | --------------------------------------------- | ---------------------------------- |
| Prototype  | "This is a prototype. Speed over perfection." | Takes shortcuts, skips edge cases  |
| Production | "Production code. Must be maintainable."      | Follows best practices, adds tests |
| Library    | "Public API. Backward compatibility matters." | Careful about breaking changes     |

### The Repo Wins

Instructions compete with the codebase. When Ralph explores your repo, it sees two sources of truth: what you told it to do and what you actually did. If Ralph sees `any` types throughout existing code, it will follow the codebase, not your instructions.

Agents amplify what they see. Poor code leads to poorer code. This is software entropy — Ralph accelerates it. A human might commit once or twice a day. Ralph can pile dozens of commits in hours.

## 9. Use Docker Sandboxes

AFK Ralph needs permissions to edit files, run commands, and commit code. Docker sandboxes isolate it:

```bash
docker sandbox run claude
```

Your current directory is mounted, but nothing else. Ralph can edit project files and commit — but can't touch your home directory, SSH keys, or system files.

For HITL Ralph, sandboxes are optional. For AFK Ralph, especially overnight loops, they're essential.

## 10. Pay To Play

Ralph is completely configurable to how much you want to spend.

| Approach          | Effort Per Phase  | Best For              |
| ----------------- | ----------------- | --------------------- |
| Multi-phase plans | Write new prompt  | One-off large tasks   |
| HITL Ralph        | Rerun same prompt | Learning, refinement  |
| AFK Ralph         | Set and forget    | Bulk work, automation |

Open source models you can run on your laptop are not yet good enough for Ralph. In AI coding, you have to pay to play.

For the next couple of years, we're in a golden age where you can do magical things with AI faster than humans — but the market still pays human wages. The market hasn't adjusted yet.

## 11. Make It Your Own

Ralph is just a loop. That simplicity makes it infinitely configurable.

### Swap The Task Source

| Task Source    | How It Works                        |
| -------------- | ----------------------------------- |
| GitHub Issues  | Ralph picks an issue, implements it |
| Linear         | Ralph pulls from your sprint        |
| Beads          | Ralph works through a beadfile      |

### Change The Output

Instead of committing directly to main, each Ralph iteration could create a branch and open a PR, add comments to existing issues, or update a changelog.

### Alternative Loop Types

- **Test Coverage Loop**: Find uncovered lines, write tests, iterate until coverage hits target. Used to take AI Hero CLI from 16% to 100% coverage.
- **Duplication Loop**: Use `jscpd` to find duplicate code, refactor into shared utilities.
- **Linting Loop**: Fix linting errors one by one, running linter between iterations.
- **Entropy Loop**: Scan for code smells — unused exports, dead code, inconsistent patterns — and clean them up. Software entropy in reverse.

Any task that can be described as "look at repo, improve something, report findings" fits the Ralph pattern.
