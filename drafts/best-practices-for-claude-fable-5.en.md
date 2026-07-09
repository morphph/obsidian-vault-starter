---
status: draft
take: waived            # Author explicitly waived the take (WF3 TAKE_OPTIONAL, 2026-07-09); the thesis below is an editorial working stance, not an authored take
lang: en
sources:
  - raw/2026-07-08-fable-finding-your-unknowns.md
external-refs:          # Load-bearing claims lean on official sources not yet ingested — see "Sourcing & TODO" at the end
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - https://www.anthropic.com/news/claude-fable-5-mythos-5
  - https://www.anthropic.com/news/redeploying-fable-5
  - https://simonwillison.net/2026/Jun/9/claude-fable-5/
  - https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026
  - https://x.com/trq212/status/2073100352921215386
research: research/best-practices-for-claude-fable-5/
platform: blog
created: 2026-07-09
last-updated: 2026-07-09
tags: [draft]
---

# Claude Fable 5 Best Practices: The Opus-to-Fable Migration Checklist

X is flooded right now with "10 prompt tips for Fable 5." Almost all of them teach Fable as if it were a beefier Opus — reword the prompt, stack a few more few-shots, phrase your instructions harder.

But if you actually route production traffic to it, the first thing that bites you isn't prompt wording. It's your client timing out after a six-minute request, a well-meaning security-audit task getting refused while still returning HTTP 200, or your carefully written old skill quietly making the output *worse*.

**This isn't another "how to prompt Fable" list. It's a migration checklist — "you used Opus like this; with Fable, change these specific things" — and every item traces to an official source.**

## Who this is for · The one-line value

**Definition first:** Claude Fable 5 (`claude-fable-5`, GA 2026-06-09) is Anthropic's flagship model for the **hardest long-horizon tasks** — 1M context, up to 128k output tokens per request, priced at $10/M input and $50/M output, adaptive-thinking-only, and its raw chain-of-thought is never returned ([official intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)).

Its best practices run **opposite** to the previous generation. Where older models wanted **steps and checklists**, Fable wants **goals and reasons** — then it figures out the "how" itself ([official prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)).

**This article's working thesis (an editorial stance):** the popular explainer threads put the migration cost in the wrong place — in *how you word the prompt*. The real cost is in three pieces of infrastructure: **① the harness contract (timeouts / async progress / progress UI), ② fallback logic (refusal → Opus 4.8), and ③ skill slimming (prune the old prescriptive instructions)**. Leave those three unchanged and switching to Fable just makes things worse, more expensive, and more likely to break in production.

**Role-based entry points — find yourself:**
- **Solo builder:** start with §1 (prune old skills) and §2 (treat effort as the master dial). Both are zero-cost and pay off immediately.
- **Content creator / anyone running long agent jobs:** focus on §3 (the harness contract) and §5 (memory + send_to_user) — they decide whether your long runs survive to the end.
- **Team lead / integrator:** §4 (refusal fallback) and §6 (routing economics) are your two pre-launch gates. Don't skip them.

---

## 1. The mental shift: from "give steps" to "give goals + give reasons"

Older, weaker models needed hand-holding — exact steps, every edge case enumerated, prescriptive skill files. **On Fable, that habit is a shackle.**

Fable is built to **absorb ambiguity and supply the "how" itself**. The very first rule in the official prompting guide: give goals, not checklists — over-specification actually lowers output quality ([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)). So step one of migration isn't writing a new prompt — it's **auditing and pruning your old skills**. Those detailed "do A then B, and if C then…" instructions written for weaker models are mostly a liability now.

> This is one more proof that assumptions expire: the constraints you wrote for the last generation become shackles on the next. Every model upgrade is worth a fresh skill audit.

**Give reasons, not just instructions.** Fable judges better when it has context. Use this template:

> "I'm working on [big task] for [who]. They need [what the output enables]. With that in mind: [specific request]."

With the *why* in hand, when your instruction collides with what Fable finds on the ground, it knows which way to veer instead of mechanically following a directive that no longer fits. Thariq (Claude Code @ Anthropic, a first-party Fable driver) puts it sharpest: too specific and Claude clings to your words even when a pivot is better; too vague and it fills gaps with industry defaults that may not fit your task ([Thariq, "Finding Your Unknowns"](https://x.com/trq212/status/2073100352921215386)). Giving reasons hands it a ruler for *when* to veer.

**Action items:**
- [ ] Open your current skills / system prompts, delete the step-by-step prescriptions written for weaker models, keep only goals and constraints.
- [ ] Rewrite key requests into the four-part shape: big task + audience + output value + request.
- [ ] Add one line to curb overreach: "do the simplest thing that works well — don't over-refactor, add abstractions, or handle impossible cases beyond what's asked." High-effort Fable tends to over-engineer; one sentence reins it in.

---

## 2. Effort is the new master dial

Older models had you tune a thinking budget. Fable collapses that into a single dial: **effort**, four levels `low / medium / high / xhigh`, defaulting to `high` ([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)).

Know this too: Fable has **only adaptive thinking** — no way to disable thinking, no extended-thinking budget, and its **raw chain-of-thought is never returned**; you get a `summarized` or (by default) `omitted` thinking block ([official intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)). So "tuning thinking" now simply means "tuning effort."

| Effort level | When to use | Cost / caveat |
|-----------|-----------|------------|
| `low` / `medium` | Everyday tasks, batch work, cost-sensitive paths | Official line: even dialed down, everyday quality beats the previous generation's xhigh. Start low, raise only if needed |
| `high` (default) | The starting point for most real work | A single request at `high` can run for **minutes** — fix your client timeout first (see §3) |
| `xhigh` | Critical tasks where **first-shot correctness** matters more than speed | Slowest and most expensive; don't default to it. Reserve it for "re-running is costly, must be right the first time" |

**Migration move:** don't blindly crank everything to max. Default to `high`; escalate to `xhigh` only when the value of getting it right the first time clearly outweighs latency and cost; drop everyday and batch work confidently to `medium/low`. This inherits Opus 4.7's effort framework, but on Fable effort becomes the **primary** dial — weighted more heavily than before.

---

## 3. The harness contract changed: "long" = minutes to hours

This is the piece explainer threads most often miss, and the one most likely to bite you in production.

Fable's "long-horizon" is literal: **a single request at high effort can run for minutes, and autonomous runs can extend for hours or even days** ([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)). The client you wrote for Opus — 30-second timeout, synchronous wait, a spinner in the frontend — will just break.

**Fix the harness *before* migrating. This is a prerequisite, not an optimization:**

1. **Extend client timeouts.** Reset them in minutes-to-hours, not seconds. Blocking synchronously on a request that may run for minutes is suicide.
2. **Move to async progress polling.** Don't block on the return; fire the task, then poll / stream for status.
3. **Don't show a "remaining tokens / context" countdown.** Counterintuitive but critical: if the UI exposes "how much context is left" to the model, Fable will **wrap up early** or proactively suggest "we should start a new session" — a long task that could have continued gets choked off by your own progress bar.

> This echoes the context-anxiety pattern we've tracked: shown a "running low on space" signal, the model rushes its ending like a person against a deadline. **The fix is to not feed it the countdown.**

Simon Willison's independent hands-on confirms the magnitude: he called Fable "a beast — slow, expensive," burning **$110** in a day, but finishing "several days' worth of work" in one go, and tested human-in-the-loop pause/resume ([Simon Willison, "Initial impressions"](https://simonwillison.net/2026/Jun/9/claude-fable-5/)). Slow and expensive are features, not bugs — but your harness has to survive the "slow" first.

---

## 4. Refusals will bite you: safety classifiers + Opus 4.8 fallback

If you change one thing from this article, change this.

Fable runs safety classifiers over three domains: **offensive cybersecurity, biological / life sciences, and reasoning-extraction (attempts to pull out the summarized thinking)** ([official intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)). Its behavior on trigger has three traps, each able to break an unprepared integration:

1. **A refusal returns HTTP 200, not an error.** The body carries a *successful* `stop_reason: "refusal"` and names the classifier that fired. Error handling written as "non-200 = failure" will **silently miss** it.
2. **Well-meaning tasks trip false positives.** A legitimate security-audit script or a bioinformatics analysis can be refused. Anthropic explicitly acknowledges these false positives exist.
3. **False-positive rates went *up* after redeploy.** Fable was **pulled on 2026-06-12** (US export controls + an Amazon-reported jailbreak that bypassed safety measures) and **fully redeployed 2026-07-01**; the improved classifier now blocks that jailbreak in >99% of cases — **at the cost of more false positives** ([redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)). In other words, over-refusal isn't a temporary artifact that fades with time — it's a **known cost** of this safety fix.

The good news: Anthropic paved the fallback path. **Safeguards trigger in <5% of sessions on average; a refusal (occurring before any output) isn't billed; the fallback refunds the prompt-cache switch cost**; and Anthropic directly recommends a **server- or client-side fallback to Opus 4.8** ([official intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)).

**So fallback is not optional.** Minimal implementation:

```python
# Pseudocode: fall back to Opus 4.8 on refusal
resp = call_model("claude-fable-5", request)

# Trap: a refusal is a successful HTTP 200, not an error — you must check stop_reason explicitly
if resp.stop_reason == "refusal":
    log.warn(f"Fable refused via classifier: {resp.refusal_classifier}")
    # Official recommendation: fall back to Opus 4.8; the refusal produced no output and isn't billed
    resp = call_model("claude-opus-4-8", request)

return resp
```

**One more trap: don't make Fable recite or verbatim-dump its reasoning** — that trips the reasoning_extraction classifier and drives up refusals. If you need to see what it's thinking, read the `summarized` thinking block; don't ask it to print its chain-of-thought in the prompt ([official intro](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)).

---

## 5. Let it run autonomously: memory / subagents / verifier / send_to_user

Fable's headline is **autonomous long runs** — it dispatches and sustains parallel subagents more aggressively and stays goal-directed over longer horizons ([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)). To actually use that, set up four things:

**① Build a memory system (Markdown).** One lesson per file, a one-line summary at the top, and record both the corrections you've made and the approaches you've confirmed work. Have Fable review the old sessions' memory to bootstrap before starting a new task — its own past experience becomes the next run's starting point.

**② Use parallel subagents freely, async-first.** Orchestrate non-blocking so multiple subagents run concurrently; long-lived subagents stay cheap via cache reads.

**③ Use a fresh-context verifier, not self-critique.** Anthropic recommends a verifier subagent with a **fresh context** to check the output, rather than having the original model grade itself. This confirms what we've long said: self-evaluation carries a self-evaluation bias, and a verifier uncontaminated by the original task context is more reliable.

**④ Build a `send_to_user` tool + a matching system reminder.** A long async agent needs a dedicated tool to **deliver verbatim output / progress to the user without ending the turn** (tool input is never summarized, so nothing is lost). Two accompanying disciplines:
- Explicitly instruct it in the system prompt to use this tool, or the model rarely calls it on its own.
- Add a system reminder to autonomous pipelines: **"You're running autonomously; the user isn't watching."** This stops it from halting to ask permission, or ending with a promise like "I'll now run X" without actually calling the tool.

**Pair this with a grounding discipline:** require Fable to verify every progress claim against actual tool results. This nearly eliminates the most annoying long-run failure — false status reports where it claims to have done something it didn't ([prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)).

**Checkpoint only on three conditions:** destructive / irreversible actions, genuine scope changes, and inputs only a human can provide. Don't enumerate every possible case — Fable's instruction-following is strong enough that one concise boundary rule beats an exhaustive list.

---

## 6. Cost & routing: don't send all traffic to Fable

$10/$50 pricing makes "everything on Fable" economically indefensible. The community's settled routing consensus (⚠️ unofficial, from [DigitalApplied](https://www.digitalapplied.com/blog/claude-sonnet-5-opus-4-8-fable-5-when-to-use-which-2026)'s family comparison): **keep 80–90% of traffic on the cheaper Sonnet 5 / Opus 4.8, and upgrade only the hardest long-horizon tasks to Fable.**

A useful mental model is the family tiering: **Sonnet 5 for execution, Opus 4.8 for judgment, Fable 5 for the hardest long-horizon upgrades** (⚠️ community-synthesized phrasing — consistent across sources but not official wording).

**A counterintuitive but important rule — aim high, not low.** To honestly evaluate whether Fable is worth it, hand it your **hardest unsolved problem** and let it scope it and ask you clarifying questions; test it with easy tasks and you'll only underrate it. Thariq calls Fable the first model where "the quality of the work is bottlenecked by my ability to clarify its unknowns" ([Thariq, "Finding Your Unknowns"](https://x.com/trq212/status/2073100352921215386)) — meaning the bottleneck has moved from *model capability* to *your ability to state the problem clearly*. Easy tasks never reach that bottleneck, so you never see its ceiling.

> ⚠️ **Pricing caveat:** only Fable's **$10/$50** is officially confirmed. Secondary sources contradict each other on Sonnet 5 ($2/$10 vs $3/$15); when doing family cost comparisons, treat Sonnet/Opus prices as "unverified."

---

## Before / after migration checklist

<!-- CTA: [placeholder for closing call-to-action] -->

The whole article compressed into one scannable table — this is your migration action list:

| Dimension | How you did it for Opus | Change to, for Fable |
|------|---------------------|----------------|
| **skill / prompt** | Detailed steps, enumerated edge cases | Prune prescriptive steps; give goals + give reasons |
| **effort** | Tune thinking budget | Default `high`, `xhigh` for critical tasks, drop everyday to `medium/low` |
| **client timeout** | Seconds | Minutes to hours |
| **progress query** | Synchronous blocking wait | Async / streaming polling |
| **progress UI** | Show token countdown | **Don't show** the countdown (or it wraps up early) |
| **error handling** | Non-200 only | Explicitly check `stop_reason: "refusal"` (it returns 200) |
| **fallback** | None / retry | refusal → **Opus 4.8 fallback** (mandatory) |
| **reasoning output** | Let it think out loud freely | Don't ask it to recite CoT (trips reasoning_extraction refusals) |
| **verifier** | Model grades itself | Fresh-context verifier subagent |
| **memory** | None | Markdown memory, one lesson per file, bootstrap by review |
| **routing** | Single model | 80–90% on Sonnet/Opus, upgrade only the hardest long-horizon work |

**Three-sentence close:** when you switch to Fable, don't rush to reword prompts first. Fix three pieces of infrastructure — **a harness that survives long runs, an integration that catches refusals, and old skills slimmed down**. Get those right and Fable does what Anthropic promises: several days' work in one pass. Get them wrong and it's just more expensive and more likely to break in production.

---

## Sourcing & TODO (before finalizing)

> ⚠️ **Load-bearing claims lack raw/ backing (WF3 headless self-check):** most of this article's load-bearing claims (the effort dial, refusal behavior, harness contract, routing economics) rest on **official sources not yet ingested into `raw/`** — they currently live only in `external-refs`. Per the project rule that "load-bearing claims must be backed by a raw/ source," **strongly recommend `/ingest`-ing these official sources before finalizing:**
> - `prompting-claude-fable-5` (the original source for nearly every best practice)
> - `introducing-claude-fable-5-and-claude-mythos-5` (the fact skeleton: pricing / refusal / adaptive-thinking)
> - `redeploying-fable-5` (the pull → redeploy event + false-positive cost)
>
> The only source already in `raw/` is Thariq's "Finding Your Unknowns," used here only as color / conceptual backing, not to carry core facts.
>
> Also: knowledge cutoff is 2026-01 and Fable 5 shipped 2026-06 — **all of §1's facts depend on external first-party sources**; verify each official URL at ingest time.
