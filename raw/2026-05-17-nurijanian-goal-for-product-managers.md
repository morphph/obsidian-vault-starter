# 🕹️ /goal for Product Managers

**Source URL:** https://x.com/nurijanian/status/2055927283991654775
**Author:** George (@nurijanian) — from prodmgmt.world (Verified account)
**Bio:** "Can I make everyone a great product manager? I will do my best | Get my AI PM OS ⬇️"
**Posted:** 4:23 pm · 17 May 2026
**Engagement (at fetch, 2026-05-18):** 2 replies · 18 reposts · 208 likes · **591 bookmarks** · **27.9K views**
**Bookmark-to-like ratio:** ~2.84× (high reference-saving intent)
**Fetch method:** Playwright MCP
**Format:** X Long-form Article

---

## Article

[Claude Code](https://code.claude.com/docs/en/goal) & [Codex's new /goal](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) command feel like a new era of agentic coding.

You give the agent a target, and it keeps working while a separate evaluator or long-running harness checks whether the target is satisfied. The agent plans, edits, runs tests, repairs failures, updates status, and keeps going until the goal is met or the loop hits a bound.

That sounds like autonomy, but I think it is better understood as **the Ralph Wiggum loop with product design around it**.

Ralph Wiggum loops were the rough version: put an agent in a bash loop, give it the same repo context every time, tell it to read the spec and implementation plan, pick the next unchecked task, complete it, write or run a test, mark the task done only if the test passes, then start again.

(Ref: https://www.youtube.com/watch?v=I7azCAgoUHc)

The useful part was not a smarter model. It was the fresh context at the start of each run.

Instead of trusting one bloated chat to remember everything through compaction, the loop reloaded durable files: the spec, the plan, the task list, the test suite, the status notes. The conversation could rot, but the source of truth stayed outside the conversation.

That is the core idea behind the native /goal. The loop is only as good as the plan it reloads, the tests, the acceptance criteria, and the evidence it leaves behind.

For product people, that changes the work in a very specific way.

Requirements start acting more like target states than prose.

That pushes PM work past "write enough detail that an engineer understands the intent" and toward "define done clearly enough that an agent can keep trying, a harness can inspect the evidence, and a human can tell whether the outcome is product-correct."

That is a much higher bar than a normal ticket.

## The further out of the loop you go, the more leverage you get.

But the more important your setup and planning becomes.

If you sit next to Claude and steer every turn, your plan can be loose because your attention fills the gaps. You notice when the agent misreads the intent. You catch the awkward implementation. You stop it before the wrong abstraction gets cemented into the repo.

When you step away, the spec has to do more of that work.

Ralph forces this because every iteration is a fresh agent instance. It does not carry the memory of your last correction. It does not remember the nuance buried 60,000 tokens ago. It reads the files you gave it, acts on them, and starts the next pass from the same durable source.

That makes the spec and plan **the product surface**.

A good Ralph loop usually has:
- a spec that explains the target behavior
- an implementation plan with ordered tasks
- acceptance criteria that can be checked
- tests or validation commands that prove progress
- a status file that records what changed, what passed, and what still looks risky

Claude Code /goal separates doing the work from judging whether the work is done. The working agent has to surface evidence in the conversation because the evaluator judges from what it can see there: test output, lint output, changed files, queue state, or some other observable proof.

Codex long-horizon examples point at the same structure. The loop depends on externalised intent: spec files, plan files, runbooks, validation commands, status logs, and periodic proof.

The loop needs a target it can inspect.

## The weak version of /goal

A bad goal reads like a wish.

> /goal improve onboarding

The agent can do *something* with that. It can rename buttons, add a checklist, change copy, simplify screens, create tests, or make a plausible-looking PR.

But the goal itself gives it no way to know whether onboarding improved.

So the agent starts optimising for whatever is easiest to prove. It may make the UI cleaner because screenshots look cleaner. It may add tests because tests pass. It may reduce steps because fewer steps sounds better. It may satisfy the evaluator because the transcript contains evidence that some work happened.

None of that means the product got better.

The same failure appears in PM requirements all the time:
> make activation easier
> reduce friction
> improve the dashboard
> clean up the settings experience
> make search smarter

Humans will rescue these tickets through conversation. Agents are worse at that when they run unattended because they will keep converting vagueness into implementation.

That is where long-running agents get dangerous.

**A one-shot mistake is annoying. A loop can spend 40 turns making the wrong thing more internally consistent.**

## The strong version of /goal

A stronger goal gives the loop a finish line, a proof method, and a boundary.

> /goal implement the new onboarding checklist from docs/onboarding-spec.md. All acceptance criteria in the spec must pass. npm test -- onboarding exits 0. npm run lint exits 0. No files outside app/onboarding, components/onboarding, or test/onboarding are changed. Stop after 20 turns with a status report if any criterion remains blocked.

That is not a perfect product requirement. It still depends on the quality of the spec. But it gives the agent something much closer to an evaluable condition.

You can make the product intent sharper inside the spec:

> The checklist is done when:
> - first-time users see three setup steps after account creation
> - each step has a visible complete/incomplete state
> - completing a step persists after refresh
> - users can skip the checklist and return to it later
> - existing users do not see the checklist unless they have no completed setup steps
> - analytics emits onboarding_checklist_viewed, onboarding_step_completed, and onboarding_checklist_dismissed
> - the empty state links to the checklist when no setup steps are complete

Then you pair those criteria with evidence:

> Validation evidence required:
> - unit tests for persisted step state
> - integration test for first-time user visibility
> - regression test for existing users
> - browser smoke test for completing, refreshing, and dismissing the checklist
> - screenshot or DOM evidence for the empty state link
> - event capture test or mocked analytics assertion for each event

Now /goal has something to work with.

The loop can run the tests, show the output, inspect the changed files, and report which criteria are still blocked. The evaluator can judge the transcript because the transcript contains proof instead of vibes.

**That is the difference PMs need to internalise. A prompt asks for effort, while a contract defines the condition where effort stops.**

## Watch the first loops

One of the best pieces of advice: **watch the first iterations.**

Do not write a giant spec, start the loop, close the laptop, and hope the robot does product development.

Start the loop and watch what it does with your instructions.

- If it misunderstands the target, stop it, edit the spec, and restart.
- If it writes a bad test that blesses the wrong behavior, stop it, fix the validation protocol, and restart.
- If it touches unrelated files, stop it, add scope boundaries, and restart.
- If it keeps asking the same question, stop it. The spec probably has an ambiguity that humans were silently resolving.

The first loops are calibration. They teach you how the agent interprets the plan.

This is the part that feels annoying because it looks like "not trusting the agent." But that is backwards. Watching the first iterations is how you make later unattended work less stupid.

**The loop becomes useful after the spec survives contact with the model.**

## Where /goal is genuinely good

I like /goal most when the target is concrete and the validation is cheap.

**Migration work is a natural fit:**
> /goal migrate all imports from legacyAuth to authClient in app/auth. No legacyAuth imports remain in app/auth. npm test -- auth exits 0. npm run typecheck exits 0. Stop after 15 turns if any usage is ambiguous.

**Backlog clearing is a natural fit:**
> /goal resolve every failing test marked @auth-regression. Each fix must include the smallest relevant production change. do not delete tests. After each fix, update docs/status-auth-regressions.md with cause, files changed, and validation output.

**File splitting is a natural fit:**
> /goal split app/components/AccountSettings.tsx into modules under 250 lines. Behavior must stay the same. existing tests must pass No new component should mix billing, profile, and notification concerns.

Brute-force testing is another good fit. Ralph is strong when the job is to keep trying attack vectors, checkout paths, login flows, search cases, forms, permissions, edge states, and unhappy paths until the queue is empty.

Exploration mode can work too, but the expectation should be different.

**For exploration, the goal should produce learning, not production code:**
> /goal explore three viable approaches for making project search faster. For each approach, create a short note with expected complexity, risks, files touched, and how we would validate it. Do not edit production code. stop after producing docs/search-speed-options.md

That version embraces what Ralph is good at. It spends tokens to search a space while keeping the output bounded.

**The dangerous version is asking an exploratory loop to silently become a production loop.**

## The PM implication

This is where product management gets interesting.

**Agentic coding does not remove product thinking. It punishes vague product thinking faster.**

The ticket is no longer enough on its own. The more useful artefact is an executable definition of done.

That means a PM has to get better at writing:
- observable behavior
- negative cases
- scope boundaries
- validation evidence
- stop conditions
- status-report expectations
- customer-facing success criteria

**A weak PM requirement says:**
> Users should be able to manage notifications more easily.

**A stronger agent-ready version says:**
> Users can turn product updates, billing alerts, and research reminders on or off independently. Each preference persists after refresh. The default state matches the existing notification behavior for current users. Users who turn off billing alerts see a warning explaining which emails cannot be disabled for legal or account-security reasons. The settings page passes existing accessibility checks. The work is done when the notification preferences tests pass, the browser smoke test shows persistence after refresh, and no billing email logic is modified outside the documented preference gate.

That is still product work.

That version decides what "manage notifications" means, names the billing-alert edge case, preserves backward compatibility for current users, names the proof, and blocks the agent from wandering into unrelated email logic.

But I would argue that this has always been important, we just got sloppy, and with AI, even sloppier; so now we need to get back to the basics.

## A practical goal template

When I write goals for long-running agents, I would use this shape:

---

```
/goal [specific target state]

Source of truth:
- read [spec file]
- follow [implementation plan]
- update [status file]

Acceptance criteria:
- [observable behavior 1]
- [observable behavior 2]
- [negative case]
- [non-regression condition]

Validation:
- [test command]
- [lint/typecheck/build command]
- [browser/visual/manual evidence if needed]

Boundaries:
- only edit [paths]
- do not change [systems]
- preserve [contract/data/API behavior]

Loop behavior:
- after each meaningful change, run the relevant validation
- update the status file with changed files, result, and remaining risk
- stop after [N turns/time] if blocked and report the blocker
```

---

**The status file is basically your epic in JIRA, reimagined.**

If the agent runs for a long time, you need a place that records what happened without relying on chat memory. The status file should say:
- what changed
- which checks passed
- which checks failed
- what decision the agent made
- what remains risky
- what a human should inspect next

That is the durable memory layer.

It is also how you avoid context rot. Every fresh turn can reload the spec and status instead of trying to reconstruct the project from a decaying conversation.

## What PMs should stop handing agents

There are a few instruction shapes I would stop using for unattended loops.

**Do not hand the agent adjectives:**
> make it better
> make it cleaner
> make it easier
> make it smarter

**Replace them with observable states:**
> Reduce the empty-state decision path from four visible actions to two. Keep "Import CSV" and "Create manually." Move advanced import settings behind the existing disclosure component. Add a regression test that the empty state still exposes both setup paths.

**Do not hand the agent vibes:**
> polish the onboarding flow

**Name the product behavior:**
> After signup, users should land on the setup checklist. They should see the first incomplete step expanded. Completing the workspace-profile step should mark it complete without a full-page refresh. If the API call fails, the step should return to incomplete and show the existing toast error pattern.

**Do not hand the agent an implementation preference disguised as a product goal:**
> Refactor settings into a cleaner architecture.

**Name the pain the refactor must relieve:**
> Split settings so billing, profile, and notification changes can be tested independently. Each module should own its form state, validation, and save action. Existing settings behavior must not change. The work is done when each module has its own test file and the current settings regression suite passes.

**This is the difference between delegating effort and delegating an outcome.**

## The part PM OS is trying to encode

PM OS exists because this kind of product judgment is hard to improvise every time.

Writing agent-ready acceptance criteria pulls together a lot of tacit PM work:
- what user behavior matters
- which edge cases are dangerous
- which constraints are fake and which are load-bearing
- what validation evidence should count
- when to stop an agent and ask for human judgment

You can learn that through years of painful product reps.

Or you can encode the patterns into reusable workflows so each new piece of work starts with a sharper definition of done.

That is where I think PM OS fits this moment.

It gives product work an operating layer: memory, context, workflows, assumptions, research, decisions, measurement, and review all structured so agents have something better than a vague ticket to chew on.

/goal is going to make that even more obvious.

Teams with good tests and crisp acceptance criteria will get more useful loops. Teams with mushy requirements will get longer, faster mush that burns their tokens.

The tool is new, but the standard is old.

**The operating rule is simple: define done, prove done, and keep the proof outside the chat.**

PM OS is built for that kind of product work.

---

## Author Context (Quoted Replies)

Referenced in the article's reply thread:

**George's earlier piece (2026-05-10):** "PM OS v2: The Memory Loop" — PM OS v1-1.8 helps a PM think and ship... [110 likes, 254 bookmarks, 24K views]

**George's writing-requirements thread (2026-05-16, 628 likes / 1,134 bookmarks / 46K views):** "my favorite ways to 'write requirements' with AI: 1. /grill-me by @mattpocockuk (github.com/mattpocock/skills) 2. /shaping by @rjs (github.com/rjs/shaping-skill)"

Both reinforce that this article ties into a broader PM-OS narrative: PM OS v2 launching soon with "improved memory, agents and skill workflows."

## Key Links Cited
- Claude Code /goal: https://code.claude.com/docs/en/goal
- Codex Using Goals: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- Ralph Wiggum (YouTube): https://www.youtube.com/watch?v=I7azCAgoUHc
- Matt Pocock skills: github.com/mattpocock/skills
- Ryan Singer shaping: github.com/rjs/shaping-skill
- PM OS product: prodmgmt.world/ai-pm-os
