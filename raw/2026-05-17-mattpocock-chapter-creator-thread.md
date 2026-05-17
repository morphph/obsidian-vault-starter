# Matt Pocock's Chapter-Creator AFK Flow (Screenshot Capture)

**Source:** X / Twitter thread by @mattpocockuk (~2026-05-15, 2 days before fetch)
**Capture method:** Screenshot transcription (URL not preserved by user; X content not WebFetchable)
**Fetched:** 2026-05-17
**Engagement at time of capture:** 14 comments, 3 retweets, 182 likes, 16K views

## Full 6-Step Tweet (Verbatim)

> 1. I wanted to create an automatic chapter creator for my videos
> 2. I did /grill-with-docs with the agent to figure out what I wanted
> 3. I said 'let's prototype the prompt passed to the agent' not really knowing what to expect
> 4. It built an entire TUI (in @EffectTS_) for me, pointing at my live data
> 5. I iterated on the system prompt until it was awesome
> 6. AFK agent one-shotted it

## Decomposed Flow

**Phase 1 — Discovery (Step 1)**
Starts with an unrefined wish: "automatic chapter creator for my videos." No spec, no design. Just the idea.

**Phase 2 — Grilling (Step 2)**
Runs `/grill-with-docs` (his own skill). Agent interrogates him one question at a time until shared understanding reached. CONTEXT.md and any ADRs updated inline. By the end he KNOWS what he wants.

**Phase 3 — Prompt prototyping (Step 3)**
Says "let's prototype the prompt passed to the agent" — open-ended, doesn't know what to expect. Key phrase: "passed to the agent" — he's already designing for the AFK handoff in step 6, but doesn't realize what intermediate scaffolding the agent will build to help him get there.

**Phase 4 — Interactive live-data surface (Step 4)**
Agent goes beyond what was asked: builds an entire TUI in EffectTS pointing at his live (real, production) data. He can SEE the prompt running on real inputs and observe outputs. This is the "live-data prototype" — sibling to Thariq's throwaway-editors pattern but terminal-flavored.

**Phase 5 — System prompt iteration (Step 5)**
With the TUI running, he iterates on the system prompt. Tight feedback loop: edit prompt → see output on real data → adjust. Continues "until it was awesome" — implicit quality bar, no formal eval.

**Phase 6 — AFK handoff (Step 6)**
Once the prompt converges, hands off to an AFK agent which "one-shots it" — processes all videos autonomously, no babysitting. Production deployment.

## What Matt's Flow Shows About Idea-to-AFK Methodology

1. **You don't write the AFK agent first.** You prototype interactively, then promote.
2. **The TUI is scaffolding, not the product.** It's a feedback-loop accelerator built by the agent for the human.
3. **The same agent does discovery, prototype, and execution.** Different roles, same model.
4. **"Awesome" is the gate.** No formal eval; trusts his own judgment from watching real data.
5. **AFK is the reward, not the entry point.** Earned by getting the prompt right interactively first.

## Connection to His Skills Repo

Step 2 maps to `/grill-with-docs` (just confirmed in his repo).
Steps 3-5 map to `/prototype` skill ("runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route") — this is exactly what built the TUI.
Step 6 maps to Sandcastle's `sandcastle.run()` — the AFK agent primitive.

So the tweet is a worked example of his own published toolkit.

## Engagement Note

182 likes / 16K views — modest by his standards but suggests a self-contained vignette rather than a viral methodology drop. The flow is implicit; the audience that gets it deeply is small. Good seed for a longform unpacking.
