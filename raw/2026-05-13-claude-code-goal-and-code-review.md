# Claude Code — Two New Features: `/goal` and Code Review

Captured 2026-05-13 from official Anthropic docs + announcement blog.

Sources:
- `/goal` reference: https://code.claude.com/docs/en/goal
- Code Review reference: https://code.claude.com/docs/en/code-review
- Announcement blog (HTTP 405 on direct fetch, summarized via InfoQ): https://claude.com/blog/code-review
- InfoQ writeup: https://www.infoq.com/news/2026/04/claude-code-review/

Both features are about **closing the human-in-the-loop gap**: `/goal` removes per-turn prompting inside a session; Code Review removes per-PR human review on GitHub. They're complementary primitives in the same direction — let the model run longer between human checkpoints, but with a verifier in the loop.

---

## Feature 1: `/goal` — Keep Claude working toward a goal

> "The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds. If not, Claude starts another turn instead of returning control to you. The goal clears automatically once the condition is met."

### Mechanics

- One goal per session. Setting a new goal replaces the old one.
- Setting a goal **starts a turn immediately** with the condition as the directive — no separate prompt needed.
- After every turn, the evaluator (a small fast model — Haiku by default) reads the conversation and returns yes/no + a short reason.
  - `no` → Claude does another turn, with the reason injected as guidance.
  - `yes` → goal clears, achievement entry recorded in the transcript.
- A `◎ /goal active` indicator shows duration while running.
- `/goal` with no args = status (condition, time, turns evaluated, token spend, evaluator's last reason).
- `/goal clear` (aliases: stop / off / reset / none / cancel) to abort early. `/clear` also removes the goal.
- Up to 4,000 characters for the condition.
- Resumes with `--resume` / `--continue` (condition preserved, but turn count, timer, token baseline reset).
- Works in non-interactive mode: `claude -p "/goal CHANGELOG.md has an entry for every PR merged this week"`. Ctrl+C to stop.

### Implementation detail

`/goal` is a wrapper around a **session-scoped prompt-based Stop hook**. The evaluator is part of the hook system, so:
- It runs only in trusted workspaces (trust dialog accepted).
- Unavailable when `disableAllHooks` is set at any settings level, or when `allowManagedHooksOnly` is set in managed settings.
- The evaluator does NOT call tools — it can only judge what Claude has surfaced in the conversation.

### How to write an effective condition

The doc is explicit: the condition must be checkable from the **transcript**, because the evaluator can't run commands or read files independently. Three components of a good condition:

1. **One measurable end state** — test result, build exit code, file count, empty queue.
2. **A stated check** — how Claude should prove it. e.g., "`npm test` exits 0" or "`git status` is clean".
3. **Constraints that matter** — invariants that must not change on the way there. e.g., "no other test file is modified".

To bound runtime: add a turn or time clause, e.g., `... or stop after 20 turns`. Claude reports progress against the clause each turn.

### Recommended use cases (from the docs)

- Migrating a module to a new API until every call site compiles and tests pass.
- Implementing a design doc until all acceptance criteria hold.
- Splitting a large file into focused modules until each is under a size budget.
- Working through a labeled issue backlog until the queue is empty.

### Comparison with other autonomous workflows

| Approach     | Next turn starts when      | Stops when                                      |
| ------------ | -------------------------- | ----------------------------------------------- |
| `/goal`      | The previous turn finishes | A model confirms the condition is met           |
| `/loop`      | A time interval elapses    | You stop it, or Claude decides the work is done |
| Stop hook    | The previous turn finishes | Your own script or prompt decides               |
| Auto mode    | (per tool call, not turn)  | Claude judges work done                         |

`/goal` is a **session-scoped Stop hook with a model evaluator**. A custom Stop hook gives you deterministic checks; `/goal` gives you model-evaluated checks without writing config. Auto mode and `/goal` are complementary — auto mode removes per-tool prompts, `/goal` removes per-turn prompts. Combine them for unattended runs.

### Cost note

Evaluator tokens are billed on the small fast model (Haiku default) — "typically negligible compared to main-turn spend."

---

## Feature 2: Code Review — Multi-agent PR review as a managed service

> "Code Review analyzes your GitHub pull requests and posts findings as inline comments on the lines of code where it found issues. A fleet of specialized agents examine the code changes in the context of your full codebase, looking for logic errors, security vulnerabilities, broken edge cases, and subtle regressions."

### Mechanics

- Triggered when a PR opens, on every push, manually, or via `@claude review` / `@claude review once` PR comments — per-repo configurable.
- Multiple agents run in **parallel on Anthropic infrastructure**, each looking at a different class of issue.
- A **verification step** checks candidates against actual code behavior to filter false positives.
- Results are deduplicated, ranked by severity, and posted as inline diff comments + a summary in the PR review body.
- If nothing found: short confirmation comment.
- Average completion: ~20 minutes; cost scales with PR size.

### Severity model

| Marker | Severity | Meaning |
|--------|----------|---------|
| 🔴 | Important | A bug that should be fixed before merging |
| 🟡 | Nit | A minor issue, worth fixing but not blocking |
| 🟣 | Pre-existing | A bug that exists in the codebase but was not introduced by this PR |

Each finding includes a collapsible **extended reasoning** section explaining why Claude flagged it and how it verified the issue.

### Reported quality

From Anthropic's internal testing (cited in Code Review blog + InfoQ):
- **Large PRs (>1000 lines):** 84% receive findings, averaging 7.5 issues.
- **Small PRs (<50 lines):** 31% receive findings, averaging 0.5 issues.
- **False positive rate:** <1% of findings marked incorrect by engineers.
- Has caught critical bugs humans missed (one-line auth failure; pre-existing type mismatch corrupting encryption key cache).

### Feedback loop

Each review comment arrives with 👍/👎 pre-attached. Reactions are collected after PR merges, used to tune the reviewer. Reactions don't trigger re-review.

Replying inline does NOT prompt Claude to respond. To act: fix the code and push. Push-triggered reviews auto-resolve threads when issues are fixed.

### Check-run integration

A **Claude Code Review** check run lands alongside CI checks. The **Details** link shows a severity table of every finding. Each finding also appears as an annotation in the **Files changed** tab.

The check run **always completes with a neutral conclusion** so it never blocks merging via branch protection. To gate merges on findings, parse the machine-readable comment in the check run output:

```bash
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson'
```

Returns e.g., `{"normal": 2, "nit": 1, "pre_existing": 0}`. `normal` = Important count.

### Configuration via two repo files

#### `CLAUDE.md`
- Project-wide Claude Code instructions, hierarchical (every directory level).
- Code Review reads it as **project context**; newly introduced violations flagged as **nit-level** findings.
- Bidirectional: if the PR makes a `CLAUDE.md` statement outdated, Claude flags that the docs need updating too.

#### `REVIEW.md`
- Review-only instructions, **injected as highest priority** into every agent in the review pipeline.
- Plain markdown, NO `@` import syntax (referenced files not read).
- High-impact knobs (from the docs):
  - **Severity recalibration** — redefine what "Important" means for the repo (e.g., a docs repo or prototype needs a narrower bar).
  - **Nit volume cap** — e.g., "report at most five nits; mention the rest as a count in the summary."
  - **Skip rules** — paths/branches/categories where Claude should post nothing (generated code, lockfiles, vendored deps, lint/spellcheck already in CI).
  - **Repo-specific checks** — e.g., "new API routes must have an integration test." Lands more reliably than the same rule buried in a long `CLAUDE.md`.
  - **Verification bar** — "behavior claims need a `file:line` citation, not an inference from naming."
  - **Re-review convergence** — "after the first review, suppress new nits and post Important findings only" — stops a one-line fix from reaching round seven on style alone.
  - **Summary shape** — ask for a one-line tally like `2 factual, 4 style` at the top.

#### Example REVIEW.md (from docs)

```markdown
# Review instructions

## What Important means here

Reserve Important for findings that would break behavior, leak data,
or block a rollback: incorrect logic, unscoped database queries, PII
in logs or error messages, and migrations that aren't backward
compatible. Style, naming, and refactoring suggestions are Nit at
most.

## Cap the nits

Report at most five Nits per review. If you found more, say "plus N
similar items" in the summary instead of posting them inline. If
everything you found is a Nit, lead the summary with "No blocking
issues."

## Do not report

- Anything CI already enforces: lint, formatting, type errors
- Generated files under `src/gen/` and any `*.lock` file
- Test-only code that intentionally violates production rules

## Always check

- New API routes have an integration test
- Log lines don't include email addresses, user IDs, or request bodies
- Database queries are scoped to the caller's tenant
```

### Setup

1. Admin opens claude.ai/admin-settings/claude-code → Code Review section.
2. Install Claude GitHub App (perms: contents read+write, issues read+write, PRs read+write).
3. Select repositories.
4. Pick **Review Behavior** per repo:
   - **Once after PR creation** — review on open / ready-for-review.
   - **After every push** — review on every push, auto-resolves threads when fixed. Most expensive.
   - **Manual** — only on `@claude review` / `@claude review once` comment.

### Manual trigger commands

| Command | Effect |
|---------|--------|
| `@claude review` | Starts a review AND subscribes the PR to push-triggered reviews. |
| `@claude review once` | Single review, no subscription. |

Both work as **top-level PR comments** (not inline). Author must have owner/member/collaborator access. Both work on draft PRs (manual trigger = explicit intent).

### Availability + pricing

- **Research preview** for **Team and Enterprise** subscriptions only.
- **NOT available** with Zero Data Retention.
- **$15–25 per review** average, scaling with PR size and complexity.
- Billed via "extra usage", **separate from plan included usage**.
- Cost falls on Anthropic bill regardless of Bedrock/Vertex usage for other Claude Code features.
- Monthly **spend cap** at claude.ai/admin-settings/usage. When hit: skipped reviews post a comment explaining.
- Analytics dashboard: claude.ai/analytics/code-review (PRs reviewed, weekly cost, feedback resolutions, per-repo breakdown).

### Troubleshooting notes

- **Retrigger** failed/timed-out review: comment `@claude review once` (the GitHub Re-run button does NOT retrigger Code Review).
- **Spend cap hit**: skip comment posted; reviews resume next billing period or when admin raises cap.
- **Findings not appearing inline**: check the check-run Details, the Files changed annotations, and the "Additional findings" section in the review body (lines that no longer exist in current diff after a push during review).

### Related

- Plugins marketplace has a `code-review` plugin for running on-demand reviews **locally before pushing**.
- For self-hosted/CI: GitHub Actions, GitLab CI/CD, GitHub Enterprise Server.

---

## How they fit together

| Question | `/goal` | Code Review |
|----------|---------|-------------|
| Where does it run? | Inside your Claude Code session | On Anthropic infrastructure, triggered by GitHub PRs |
| What's the unit of autonomy? | A turn (until evaluator says done) | A PR review (one shot or per-push) |
| Who's the verifier? | A small fast model checking the transcript | A specialized verification agent checking against codebase |
| What it removes | Per-turn human prompting | Per-PR human reviewer round-trip |
| Plan tier | Anyone with Claude Code | Team / Enterprise only |
| Cost model | Negligible evaluator tokens | $15–25/review, separate bill |
| Customization surface | The condition string | `CLAUDE.md` (project) + `REVIEW.md` (review-only, highest priority) |

Both follow the same pattern: **agent + verifier in a loop**. `/goal` does it within one session at the turn boundary; Code Review does it across many agents at the PR boundary. This is the same architecture as Claude's own internal "manage by team" pattern — multiple specialized agents, one verifier checking outputs before they reach the human.
