# What I Learned Pointing a Ralph Loop at My Product for a Week

**Source:** https://amplitude.com/blog/ralph-loop
**Author:** Amplitude (AI Week experiment researcher)
**Fetch method:** WebFetch
**Fetched:** 2026-05-17

## Setup

- **Agent:** Claude Code with browser use enabled
- **Orchestration:** Amplitude's Opportunity Finder (experimental — "AI PM" feature)
- **Application:** Backcountry route planning app for ski trips
- **Goal definition:** Examine competitors and optimize for fun planning experiences
- **Duration:** One week

## Results

- **102 features shipped** in 7 days
- Every PR included a browser-recorded GIF validating end-to-end functionality
- Agent self-proposed unexpected feature categories (physics-based avalanche runout simulation, mushroom foraging predictor, slope-angle overlays, weather/resort/biking/kayaking tabs)

## Architecture: The Three-Cycle Loop

```
1. Build next opportunity (from ranked queue)
2. Verify in browser (record GIF)
3. Generate more opportunities from new product state
```

The loop wasn't blind — the **Opportunity Finder is the dispatcher** that ranks tasks by:
- Analytics signals
- Session replays
- Customer feedback
- Agent traces
- Competitive gaps

Drafts structured specs (problem statement + proposed solution + behavioral evidence) for each opportunity.

## What Worked

### 1. Self-Instrumentation
The agent wired up its OWN telemetry: Amplitude events, session replay, metric definitions. Every feature reports on itself immediately. This created feedback loops preventing mode collapse — next cycle works from behavioral evidence, not prior assumptions.

### 2. Browser Verification
Claude Code clicked through every new feature, recording GIFs. Synthetic traffic revealed bugs unit tests miss: misaligned handlers, incorrect form submissions, unresolved state updates.

### 3. Structured Opportunity Queue
Instead of "what should I build next?", the loop drew from a ranked input tied to actual product goals. Queue refreshed each cycle with newly generated opportunities. This is fundamentally different from Ralph's original "while true; do agent; done" — the queue IS the intelligence.

## Three Core Lessons

### Lesson 1: The loop itself is secondary
The dispatcher (Opportunity Finder) and the verification gate matter most. Any loop requires honest outcome signals and clearly defined objective functions to progress toward value. "While true" with no scorer is noise.

### Lesson 2: Self-instrumentation enables compounding
Without telemetry, each cycle operates from identical priors. With it, the loop identifies which outputs actually worked and begins favoring specific opportunity shapes over time. Telemetry = memory across iterations.

### Lesson 3: Execution becomes abundant
When 102 features ship per week, **taste, prioritization, and opportunity selection become the bottleneck**. Human role transitions from building to judging:
- Which opportunities deserve pursuit
- Which shipped features move metrics

## Auto-Merge Policy

Manual merge control retained for most PRs. Narrow categories with clear success metrics (small UI additions) auto-merge without review. Data-touching work always gated.

## What's Missing from the Article

- No concrete code/prompts shown (architectural patterns only)
- No cost figures
- Specific GIF artifact format not detailed

## Connection to This Wiki

- Maps to existing [[ralph-wiggum]] but adds **dispatcher pattern** (Opportunity Finder)
- Validates [[verification-loops]] — GIF-as-proof is verification at the right level
- Reinforces [[silent-fallback-antipattern]] — skipped/false-success is the failure mode
- New concept: **abundance shifts the bottleneck** — when execution is cheap, taste becomes scarce
