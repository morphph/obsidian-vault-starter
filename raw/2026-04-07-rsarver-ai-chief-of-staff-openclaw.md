# How I built a chief of staff on OpenClaw that's better than any human I've hired

**Source:** https://x.com/rsarver/status/2041148425366843500
**Author:** Ryan Sarver (@rsarver)
**Published:** 9:38 pm · 6 Apr 2026
**Fetch method:** Playwright MCP (x.com JS-heavy site)
**Engagement:** 33 replies, 56 reposts, 615 likes, 2,691 bookmarks, 217.7K views

## Context

Ryan Sarver is a VC in the middle of a fundraise, sitting on boards, helping portfolio companies, and angel investing on the side. He's worked with great human EAs and chiefs of staff over the years. When the first AI APIs came out, he tried to build an AI version as a product and couldn't make it work. When OpenClaw launched he went deep immediately.

@ryancarson's post about how he built his OpenClaw assistant was also great to see, and the response to it convinced Sarver to write up what he's been building.

> What I have now is more capable than any human chief of staff I've ever worked with. It never forgets a commitment, it handles the small stuff without being asked, flags the important stuff without being told, and it gets better every week. Plus it never sleeps and it never tires.

Her name is Stella.

## Memory: the foundation

Session memory is a lie. Any assistant that treats conversation history as its working context will fail you at the most frustrating moments.

Two layers:

1. **Daily notes**: one markdown file per day (`memory/YYYY-MM-DD.md`) serving as a raw log of everything that happened. Meetings attended, decisions made, tasks added and completed, context that came up in conversation. A script pulls from sessions throughout the day and writes these automatically.

2. **Long-term memory** in `MEMORY.md`, curated by Stella herself. Key people, active projects, lessons learned, decisions made. She periodically synthesizes this from the daily notes, and it's what she reads on startup to orient herself on what matters right now.

Every meeting processed, every email triaged, and every task tracked feeds back into this picture continuously. Without this layer you have a capable assistant with amnesia. With it you have something closer to a person who's been working alongside you for months and never forgets anything.

All of this lives in flat **markdown files rather than a database**. Can open any memory file, read it, edit it if something's wrong, and understand exactly what the assistant knows. Can back the whole thing up to git and restore anything instantly. No abstraction layer between user and the assistant's understanding.

### Example: Fundraise pipeline

Managing a fundraise involving 100+ LP contacts across multiple countries. Stella tracks the full pipeline, keeps context on each LP and contact, and knows where every relationship stands. For first meetings: researches the fund, recent content from partners, preps with tailored talking points. For ongoing relationships: knows pipeline stage, prior discussions, commitments made.

## Kaizen: the system improves itself

Every Friday, a cron job runs research. Stella scans the OpenClaw community, checks for new patterns, looks at what other builders are doing, and saves findings to `memory/kaizen-research-YYYY-MM-DD.md`. On Sunday morning they review it together — summarizes the week's research, surfaces top ideas worth trying, discuss what to actually change.

Also learns from daily interactions. If user keeps correcting something, or if a feature creates more friction than value, that gets captured in memory and surfaces as a suggestion to fix it.

> This is something a human chief of staff genuinely cannot do at scale. They can absolutely learn from working with you, but they can't simultaneously scan what hundreds of other builders are doing and cross-reference it against your system every week.

The Kaizen loop also drives continuous refactoring of the system itself. First versions are always too complicated, too noisy, or solving the wrong part of the problem. A smaller system you trust will always beat a bigger one you route around.

## Meeting prep and follow-through

60 minutes before any external meeting, a brief arrives via WhatsApp. Pulls prior meeting notes from memory, checks recent email threads, finds open action items. For LP meetings: pipeline stage, deck version seen, prior questions, commitments made.

Post-meeting: processes every meeting through the **Granola API** (or any note taker with an API). Fetches notes, deduplicates, extracts action items. User's tasks go to **Todoist** with proper projects and due dates. Other people's commitments tracked in per-person markdown files.

Everything feeds back into memory — next meeting cycle starts with richer picture.

## Task and priority management

Stella keeps comprehensive task picture in structured markdown (source of truth). Important near-term items synced to **Todoist** (focused app view). LLMs handle judgment; dedicated tools handle focused views.

Every evening: task sweep. What's due, overdue, sitting too long, coming this week. Flags patterns (rolled forward 5 days), high-stakes meetings with incomplete prep. If nothing needs attention, silence.

## Stakeholder and relationship context

Maintains persistent, structured context on every person, company, and project. Relationship history, last touchpoint, open commitments, what they care about. Every meeting/email/task feeds back in. This is memory applied to relationships — the piece that compounds the most visibly over time.

## Information filtering

Email and calendar triage across personal and work Gmail. Auto-pulls expense receipts, generates travel itineraries from booking confirmations, drafts follow-up emails in user's voice and queues for review.

## Operational rhythm

- Morning brief at 9am via WhatsApp: top priorities, overdue tasks, today's calendar, attention items
- Evening wrap at 6pm: what happened, what stalled, what to prep for tomorrow
- If nothing to say, silence

> This is the piece that makes it feel like working with a chief of staff rather than using a tool.

## Research and intelligence

Weekly curated digest of X accounts tracked and newsletters subscribed to. Organized into tiers (AI researchers, VCs, founders, operators), scored by engagement, filtered for relevance. Turns 45 minutes of scrolling into a few minutes of high value reading.

## Judgement vs predictability

**Key design rule:** LLMs handle judgment, and scripts handle everything else. Anything deterministic (reading files, calling APIs, sending messages, comparing timestamps) lives in Python. LLM layer handles synthesis, prioritization, drafting, and reasoning.

> When you push deterministic work through an LLM, things break in unpredictable ways and you stop trusting the system.

## Where this is going

> I didn't get the best assistant I've ever had by asking better questions. I got it by giving the system a better operating model.
