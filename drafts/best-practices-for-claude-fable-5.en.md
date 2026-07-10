---
status: draft
sources:
  - raw/2026-07-08-fable-finding-your-unknowns.md
external-refs:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  - https://simonwillison.net/2026/Jun/9/claude-fable-5/
research: research/best-practices-for-claude-fable-5/
platform: blog
lang: en
created: 2026-07-10
last-updated: 2026-07-10
tags: [draft]
description: "With Claude Fable 5 the bottleneck isn't how you word your prompt — it's whether you can clarify your own unknowns. This maps Thariq's (Anthropic Claude Code) four-quadrant unknowns framework onto four copy-paste Fable moves: the goal template, the reverse interview, prototype-plus-source-reference, and the blindspot pass, plus a full before/during/after workflow."
keywords: [claude fable 5, unknowns, four quadrants, finding your unknowns, thariq, give goals not steps, blindspot pass, agentic coding, prompting, implementation notes]
category: techniques
related_blog: loop-engineering-guide
related_glossary: [claude-code, claude]
---

# Give Goals, Not Steps: Using Thariq's Four Quadrants of Unknowns to Drive Claude Fable 5

On July 4, 2026, Thariq (@trq212) from Anthropic's [Claude Code](/en/glossary/claude-code) team published an X article titled *Finding Your Unknowns*. By the time of writing it had accumulated **3.35M views and 20,168 bookmarks** — the only piece in this topic area with measured engagement numbers (every other Fable explainer's stats are eyeballed estimates). And it was bookmarked more than it was liked (8,885 likes). When bookmarks outrun likes, it usually means one thing: readers aren't there for entertainment, they're saving it to act on it.

The line that keeps getting quoted is his diagnosis:

> "Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns."

That sentence moves the bottleneck. For two years the ceiling on agentic coding was model capability: the stronger the model, the more you could do. Thariq is pointing at something else — **at the Fable tier, what caps your output is no longer that the model isn't smart enough, it's that you haven't articulated what you don't know.** For the first time, the real work sits *outside* the prompt.

## The official principle is missing half a sentence

Anthropic's official prompting guide for Fable distills best practice into one counter-intuitive rule: **give goals, not steps.** Fable is built to absorb ambiguity and figure out the *how* itself, so the harder you pin down the steps, the more you drag it down — the prescriptive skills you wrote for a slightly-weaker intelligence become shackles in Fable's hands.

The rule is right. But it's missing half a sentence: **what if the goal itself is wrong?**

Hand over a goal without excavating your unknowns first, and the goal you shipped may have been crooked from the start. Nearly every Fable tutorial on X is teaching you how to *word your prompt more nicely* — but Fable is the first model where the bottleneck isn't prompt wording, it's whether you can clarify your own unknowns. Thariq's four quadrants are, right now, the only framework that breaks that bottleneck down to something you can act on, and it dovetails precisely with the official "give goals, not steps" rule: **each quadrant of unknowns maps to one concrete Fable move.** Put differently — before you upgrade to Fable, upgrade how you ask questions. The most expensive bug tends to hide in the one sentence you never wrote down.

Thariq frames it with an older idea: *the map is not the territory.* The map is what you hand Claude — prompts, skills, context. The territory is where the work actually happens — the codebase, the real world, its actual constraints. **The gap between the map and the territory is what he calls unknowns.** Every time Claude hits an unknown, it has to decide based on its best guess of what you want; the more work in flight, the more unknowns it runs into.

So how do you find those unknowns systematically? **The four quadrants of unknowns is a self-audit framework Thariq borrows from Rumsfeld's known/unknown matrix: it splits your grasp of a task along two axes — whether you know a thing, and whether you know whether you know it — into four cells: known knowns, known unknowns, unknown knowns, unknown unknowns.** The map below runs through the whole piece: one copy-paste Fable move per cell.

- **If you mostly write code**, focus on "known unknowns → the reverse interview" and "unknown knowns → prototype + source reference" in the next section — those two cells are the ones that blow up mid-implementation.
- **If you run long-horizon agent tasks**, focus on the "Stitched into a workflow" section: laying the four moves across before/during/after is what keeps a multi-hour autonomous run from drifting.
- **If you lead a team**, the "Economics" and "Five moves" sections translate straight into team norms.

## The four quadrants, one Fable move per cell

Thariq has watched top agentic coders work (he names Boris and Jarred): what they share isn't fancy prompting, it's **very few unknowns** — they're deeply in sync with both the codebase and model behavior, and they know what they want in detail. But they also **budget for unknowns**. Reducing and planning for your unknowns *is* the craft of agentic coding. The good news: it's a skill you improve by working with Claude.

### Known knowns → the goal template (give reasons, not a checklist)

**Definition:** the stuff you explicitly write into your prompt — what you tell the agent you want.

**How to spot it:** you can state "what done looks like" in one sentence, and you're confident in that sentence. This cell looks the safest, which is exactly why it gets written too dry: a goal with no *why*.

**The move:** wrap the goal in a layer of reasons. What Thariq keeps stressing is to give Claude context about your starting point: tell it where you are in your thought process, disclose your experience with the problem and the codebase, let it work as a thought partner rather than an executor. The official guide crystallizes that into a copy-paste template:

> I'm working on [big task] for [who]. They need [what this output lets them do]. With that in mind: [the specific request].

With the "for whom / what they need" attached, when Fable hits an unknown you didn't write down, it has a basis to veer in the right direction — instead of defaulting to an "industry best practice" that may not fit your work at all.

### Known unknowns → let Fable interview you

**Definition:** the parts you haven't figured out yet but **know** you haven't.

**How to spot it:** you've got a mental list of "TBD" items, you just haven't (or can't) spell them all out at once.

**The move:** don't stew on them — have Fable pull them out one at a time. Thariq's verbatim template:

> Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture.

One question at a time, and **lead with the ones where your answer would change the architecture** — spend the interview budget at the highest-leverage forks, not on cosmetic details.

### Unknown knowns → let a prototype surface implicit criteria; point references at source code

**Definition:** things so obvious you'd never write them down, but you'd recognize the instant you saw them. The classic case is visual taste: hard to describe, obvious on sight.

**How to spot it:** you catch yourself saying "I can't quite articulate it, build it and let me look."

**Move A — prototype:** before wiring up a backend or state, have Fable mock a throwaway HTML prototype with fake data so you can react to the layout. Thariq's usage:

> Before wiring anything up, make a single HTML file mocking the new editor toolbar with fake data. I want to react to the layout before you touch the real app.

Surfacing an implicit criterion at prototype stage is cheap; discovering it during implementation is not — a small change in spec can force a drastically different implementation in code, and reverting the agent's earlier changes is harder.

**Move B — reference:** sometimes you can't even describe what you want. The best reference isn't docs or a screenshot — **it's source code.** Point Fable straight at the folder that already implements the behavior you want, even if it's in another language:

> This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client.

It reads the underlying markup and structure, so it gets far richer detail than a screenshot ever gives.

### Unknown unknowns → the blindspot pass

**Definition:** things you haven't considered at all — you don't know that you don't know. Entering a new part of the codebase, or doing unfamiliar work (iterating on a design), this cell is usually the fullest.

**How to spot it:** you don't even know what questions to ask, what "good" looks like, or which potholes others already hit.

**The move:** ask Claude to find your blindspots and explain them to you. Thariq recommends using **the literal words "blindspot pass" and "unknown unknowns"**, and always giving it context on who you are and what you already know:

> I'm working on adding a new auth provider but I know nothing about the auth modules in this codebase. Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better.

Claude searches your codebase and the internet extremely fast, knows more than you about the average topic, and iterates from failure faster than you can — it's the lowest-effort tool for dragging unknowns up to the surface.

## Stitched into a workflow: before / during / after

Thariq describes working with Fable as "an iterative process of discovering my unknowns before, during, and after implementation." Lay the four cells' moves along a timeline and you get a full workflow:

**Before (five cheap probes):** blindspot pass → prototype / brainstorm → reverse interview → source reference → implementation plan. He's specific about the plan step: write it in HTML and **lead with the decisions you're most likely to change** — data model, type interfaces, anything user-facing; bury the mechanical refactoring at the bottom ("I trust you on that part").

**During (keep a ledger):** once you're happy with the plan, start a fresh session and feed in the artifacts — the spec, the prototype. But no amount of planning kills the lurking unknowns; the agent may need to change tack over an edge case it finds. So have it keep a temporary `implementation-notes.md`:

> Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under 'Deviations', and keep going.

Hit an edge case, forced to deviate: take the conservative option, log it under `Deviations`, keep moving — the next attempt learns from that ledger.

**After (buy-in + verification):** two things. First, pitches / explainers — package the prototype, spec, and notes into a single doc you can drop in Slack for buy-in, leading with the demo GIF; when reviewers start with the same unknowns you did, it accelerates both their understanding and their approval. Second, quizzes — after a long session Claude has often done more than you realized, and reading diffs only gives a shallow picture, so ask it for a context-rich report on the changes plus a quiz at the bottom, and **only merge after you pass it perfectly.**

The punchline: this isn't extra burden, it's **the four-quadrant moves spread across time.** In Thariq's words, every explainer, brainstorm, interview, prototype, and reference is "a cheap way to find out what you didn't know before it gets expensive to fix."

## Economics: the pricier the model, the bigger the leverage of finding unknowns

Why is this discipline worth more on Fable than on any prior model? Look at the bill.

On launch day, independent developer Simon Willison called Fable "a beast — slow, expensive" in his hands-on review: it burned **$110 in a day**, but did "several days' worth of work" in one go. Fable is priced at **$10 / M input and $50 / M output** — every run costs more than the prior generation; at high effort a single request runs for minutes, and an autonomous run can stretch for hours.

Stack those two facts: the pricier the model and the longer each run, the more expensive the rework from a single unclarified unknown. **cheap now < expensive later** stops being a proverb and becomes a number that literally shows up on the invoice. Each of those five cheap probes is buying down a possible tens-of-dollars re-run with a few cents of prototyping and interviewing. The stronger and pricier the model, the higher the leverage of finding unknowns first — which is exactly why "find unknowns first" graduates, in the Fable era, from good habit to cost discipline.

## Five moves to start today

1. **Make the first sentence of your next project "find my unknowns," not a task assignment.** Use the literal words "blindspot pass" and "unknown unknowns."
2. **When you give a goal, hand over the reason with it.** Use the "I'm working on … for … They need … With that in mind: …" template so it has a basis to veer the right way.
3. **For anything TBD, have it interview you one question at a time**, leading with architecture-changing questions.
4. **For anything you can't articulate, prototype first, then reference source code** — point Fable at the folder that already got it right.
5. **After a long session, pass the quiz before you merge**, and have it log plan deviations under `Deviations`.

Find the unknowns first, then design the loop — that ordering is the prerequisite homework for [loop engineering](/en/blog/loop-engineering-guide): you have to know *what* you're verifying before the loop means anything. We've also made a whiteboard deep-read video of the same Thariq piece (with the four-quadrant diagram as its spine). The two are two sides of one coin: this piece is *how to do it*, the video is *why to think this way*. Before you hand your hardest task to [Claude](/en/glossary/claude), spend ten minutes letting it find the part you don't yet know you don't know.

## References

- Thariq (@trq212), *A Field Guide to Fable: Finding Your Unknowns*, X Article, 2026-07-04 — <https://x.com/trq212/status/2073100352921215386> (companion example artifact: <https://thariqs.github.io/html-effectiveness/unknowns/>)
- Anthropic, *Prompting Claude Fable 5* (official prompting guide) — <https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5>
- Anthropic, *Introducing Claude Fable 5 and Claude Mythos 5* — <https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5>
- Simon Willison, *Claude Fable 5: initial impressions*, 2026-06-09 — <https://simonwillison.net/2026/Jun/9/claude-fable-5/>
