# From "System of Record" to "System of Intelligence"

**Source URL:** https://x.com/steph_zhang/status/2054925688097128603
**Full article:** https://www.a16z.news/p/from-system-of-record-to-system-of
**Author:** Steph Zhang (@steph_zhang) — a16z
**Posted:** 2026-05-14 2:03 PM
**Engagement (at fetch, 2026-05-16):** 30 replies · 71 reposts · 334 likes · **779 bookmarks** · **458K views**
**Bookmark-to-like ratio:** ~2.33× (high reference-saving intent)
**Fetch method:** Playwright MCP
**Companion piece:** "Is Software Losing Its Head?" (a16z)

---

## Article: From "System of Record" to "System of Intelligence"

Here's one way you can think about system of record stickiness:

For a long time, the valuable part of social media businesses was the **friend graph**. When you opened Facebook back in the day, the thing you interacted with was the graph, and the data graph across the profiles was a powerful, durable asset. It was hard to foresee what could disrupt such an obvious network effect.

**Then the news feed came along.** The news feed gave us a new place to go: "Here's what happened today; here's where you catch up and take action, all in one place." This started out as a complementary layer to the friend graph, but in time, **the graph became "just one of many inputs" to the feed serving you relevant content.** While it never went away, it's no longer the important layer — the feed is, and all kinds of things feed into it. Your social profile, posts and likes are primarily consumed "at the internal API layer", so to speak; the newsfeed is its consumer.

**We think this is starting to happen to one of the supposedly "least disruptable" parts of the enterprise: the CRM.** The CRM isn't going to vanish, just like the friend graph never went away — but it's turning into just an input; one of many inputs, into the **systems of intelligence** which we use to get work done.

At firms across the country, the typical account executive now opens his laptop in the morning and finds, waiting for him, a small collection of software agents he had no part in programming:
- A research agent that combs 10-Ks and recent earnings calls before his first meeting of the day
- A dialer that coaches him on objections in the moment
- An orchestration layer that listens to his calls and writes structured notes back into the CRM without his lifting a finger

None of this, by itself, is earthshaking. **But taken together, you recognize what this is: this is the newsfeed. It's the valuable thing now.**

## The Old World: System of Record stickiness

There's no doubt: owning the system of record has been the winning play for go-to-market software for twenty years. It's sticky, valuable, and hard to leave. And we can't imagine the SoR incumbents going away anytime soon: **Salesforce and HubSpot still sit on some of the most valuable datasets in the industry**, they've realized that it matters, and they're quickly coming up with strategies that bring AI features in their own walls.

But we think we've seen this movie before. **In the next decade, you want to own the system of intelligence that pulls from the system of record**, becomes the user's one-stop shop for gaining context and taking action, and turns the SoR into something that's primarily consumed at the API layer. **The reasoning layer that sits above the database**, and that increasingly treats the database as infrastructure, is where a new generation of companies is being built.

Over the last thirty years, a thousand companies were founded to help salespeople sell; but almost all the value ended up accumulating in just two names: Salesforce (~$140B), HubSpot (~$9B). **"First prize is a Cadillac. Second prize is a set of steak knives."**

The reason: Salesforce and HubSpot **own the database**. Every call note, every pricing precedent, every contact, every stray observation about why a deal had stalled. Once that database accumulates years of operational context, switching costs become — as a16z's Alex Rampell put it — high enough that users are **"hostages, not customers."**

Every app in the Salesforce AppExchange and every tool in the HubSpot Marketplace is, in effect, **paying rent for the right to plug into someone else's database**.

## Counter-intuitive: CRM usage is UP since AI

One of the more counterintuitive findings from our GTM survey is that **CRM usage has actually increased since AI tools began to be adopted at scale**. The agents that listen to calls and write structured notes back into the system are, for the moment, giving reps fresh reason to consult it, because the data sitting there has become dramatically richer than it used to be.

## Orchestration is the new gravity well

AI agents, acting on behalf of sales reps and alongside them, are taking over a steadily widening share of the GTM workflow. Sometimes the rep instructs the agent directly: research this account, draft this outbound sequence, qualify these inbound leads, update this deal record after the call. Sometimes the agent works in the background, listening to a meeting recording and writing the structured fields back into the CRM on its own.

**The agent doesn't need a drag-and-drop pipeline view. What it needs is structured data it can read and write with low friction.** The CRM, from the agent's perspective, is a database. A very large and carefully curated database, hosted by a trusted vendor, with excellent integrations and a decade of accumulated customer trust; but a database, nonetheless. The opinionated workflows on top become, progressively, **legacy furniture** — a bit like the lovingly created UI of your Facebook profile; once paramount, now an afterthought.

### The gravity shift
- **Software era:** gravity came from **colocation** — every valuable piece of sales context had to live in one place because the human operating on that context could only look in one place at a time
- **AI era:** gravity will come from **orchestration** — an AI agent doesn't find it difficult to pull dozens of signals simultaneously from the CRM, calendar, shared inbox, call recording, Slack, enrichment API, billing system, and product telemetry. Nor does it find it difficult to synthesize information across all of them before taking action.

**Switching costs shift accordingly:**
> "All of our customer data is in Salesforce" → "All of our workflows, our reasoning, our accumulated institutional context live in our AI layer."

The CRM used to tax every app that wanted access to its data; now the system of intelligence has become the hub, and the CRM is **one of the many systems of record that it orchestrates across**.

## The Foundation Model is not a GTM application

At the technical core of the new stack sit the foundation models. But a foundation model is not, by itself, a GTM application, any more than Oracle's database engine was a CRM. Between the model and the customer sits an enormous amount of unglamorous and domain-specific work:
- Orchestrating context across dozens of connected systems
- Encoding the actual logic of how sales and marketing teams operate
- Handling permissions and compliance
- Integrating with the chaotic reality of a Fortune 500 IT environment

**That work is the new GTM application layer. It is where the new GTM companies are being built.**

## The labor question

Go-to-market has, for decades, been a category in which software was the junior partner to labor. Historically, **software made up between 5 and 10 percent of total GTM spending** in a typical enterprise; the rest is payroll. Salesforce dominates the software slice, but the software slice has always been a thin wedge of the pie.

**What AI opens up, for the first time, is the prospect that software companies can meaningfully reduce costs while opening up new high ROI use cases.**

The natural question is whether this comes at the expense of sales headcount. So far, **it has not**, or at least not in a straightforward way. While roles within the GTM team may shift, we're seeing teams spend even more on people. The ROIs on these agents are strong enough that **the total pie grows rather than the labor budget shrinking**. Reps using these tools are hitting attainment and quota at noticeably higher rates than those without them; the return on every GTM dollar is going up rather than merely holding steady.

## What AI-native GTM startups look like

Two observations about AI-native GTM startups emerging over the last few years:

1. **They cluster around narrow, high-frequency workflows** where inputs are well-defined and ROI is easy to measure
2. **Many are inventing new jobs entirely** — doing things nobody was quite doing before

## The Future VP of Sales

She no longer begins her day by opening Salesforce to a static account list and deciding where to focus. She begins it in a **prioritized feed generated by her system of intelligence**:
- Which accounts had material news overnight
- Which prospects in the territory are suddenly in market
- Which deals in the pipeline have gone quiet in ways that ought to be investigated

**The daily prioritization decision — which used to consume real cognitive effort from every rep and every sales leader in America — has been quietly offloaded to the intelligence layer.**

When her reps sell, they arrive better prepared. **The rep who would never have read the 10-K is walking in with a briefing drafted for him; the new hire six weeks into the job is, by certain measures, better equipped than the ten-year veteran at the desk next to her.**

She has an honest picture of what her team is doing. **At the moment that picture is whatever gets logged into the CRM, which is often incomplete and occasionally fictional.** With call transcripts, email threads, and calendar data flowing in automatically, analyzed continuously, she can see who is running disciplined discovery and who is skipping steps, which accounts are getting coverage and which have been quietly neglected. **A system of intelligence that has ingested every interaction across a sales team can surface patterns no human manager, however committed, could see unaided.**

## Institutional memory becomes shippable

**Every company bleeds institutional knowledge when its reps turn over** — context on accounts, the history of what worked for whom, the texture of relationships built up over years.

A system of intelligence that has been quietly ingesting that context for the duration of a rep's tenure can, when she leaves, **hand the whole of it over to her successor**. **Institutional memory becomes something a company can actually ship.**

## Conclusion

None of this, it should be said, is bad news for the CRM. Salesforce still owns its database; HubSpot still owns its database; the customer data continues to live where it has always lived, for the reasons it has always lived there. **But the locus of value is migrating upward, into the layer that reads and writes to the database and does the actual thinking.**

**The pie is getting larger in the process, not smaller.** Just as the feed increased the TAM of social media to "everything of interest", the agent revolution expands what software can plausibly charge for, and does it without gutting the labor budget that funds most GTM work today.

A new generation of companies is being built on top of this emerging layer. **The next decade of go-to-market software will be written there.**
