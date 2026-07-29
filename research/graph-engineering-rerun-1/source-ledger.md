# Source Ledger: Graph Engineering — X Evidence Rerun

> as_of: 2026-07-29 16:00 SGT
> channels searched: official docs, original essays, papers, public Web, X original post pages
> primary search languages: English, Chinese
> important access limits: no X MCP credentials; ChatGPT Chrome Extension absent; X native search
> requires login; public direct post pages worked; one X Article remained inaccessible

## Claim records

## C-001 — Graph Engineering is agent control-topology engineering

- **Claim:** In the 2026 agent discourse, Graph Engineering most usefully means designing nodes,
  edges, state, verification, authority, stopping, and recovery across multiple work units.
- **Kind:** definition
- **Status:** probable
- **Time sensitivity:** high
- **Primary source:** https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase
- **Supporting sources:** https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph,
  https://x.com/ericosiu/status/2079991948106957131
- **Counter-evidence:** https://x.com/PawelHuryn/status/2078755464754376719
- **Search boundary:** original definition, institutional response, direct sampled definitions
  and criticism through 2026-07-29
- **Used in report:** Executive Summary, §1
- **Notes:** There is no standards body or canonical specification.

## C-002 — The phrase has a direct 2024 semantic predecessor

- **Claim:** Itamar Friedman directly used `flow (/graph) engineering` for AI systems on
  2024-02-29.
- **Kind:** origin
- **Status:** verified
- **Time sensitivity:** low
- **Primary source:** https://x.com/itamar_mar/status/1763168555539812407
- **Supporting sources:** none required
- **Counter-evidence:** this is not the exact standalone phrase `Graph Engineering`
- **Search boundary:** direct original post plus earlier indexed phrase search
- **Used in report:** §2
- **Notes:** This establishes a semantic predecessor, not absolute priority.

## C-003 — Peter was an amplifier, not a definer

- **Claim:** Peter Steinberger's 2026-07-18 post was a major amplification event but contained
  only a question and no definition, implementation, or release.
- **Kind:** timeline
- **Status:** verified
- **Time sensitivity:** high for metrics
- **Primary source:** https://x.com/steipete/status/2078277297791189132
- **Supporting sources:** https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph
- **Counter-evidence:** none found that turns the post into a formal proposal
- **Search boundary:** original post and sampled replies observed 2026-07-29
- **Used in report:** Executive Summary, §2, §5
- **Notes:** Direct UI observation provides a first-party metric snapshot at the stated time.

## C-004 — A low-engagement pre-viral explicit use exists

- **Claim:** Mike wrote `next is: graph engineering` on 2026-07-11, one week before Peter.
- **Kind:** origin
- **Status:** verified
- **Time sensitivity:** low
- **Primary source:** https://x.com/michaelmasson55/status/2075913998449701170
- **Supporting sources:** none required
- **Counter-evidence:** the post gives no definition
- **Search boundary:** direct original post observation
- **Used in report:** §2
- **Notes:** Useful example of why reach cannot determine origin.

## C-005 — Paweł's criticism contains substantive design claims

- **Claim:** Paweł Huryn argues that graphs/state machines/evals are useful but old, and that
  objective, independent verification, autonomy boundaries, and stopping matter more than the
  new label.
- **Kind:** synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://x.com/PawelHuryn/status/2078755464754376719
- **Supporting sources:** visible sampled replies on the same page
- **Counter-evidence:** source does not show that every current graph practice is old in every
  operational detail
- **Search boundary:** original post and visible reply sample
- **Used in report:** §4
- **Notes:** This directly strengthens the critic lane.

## C-006 — A high-engagement post conflates two meanings

- **Claim:** Codez's post calls a knowledge-graph memory pipeline `Graph Engineering`, while the
  main agent discourse uses the term for execution/control topology.
- **Kind:** comparison
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://x.com/0xCodez/status/2080250266851463209
- **Supporting sources:** https://arxiv.org/abs/2307.06917
- **Counter-evidence:** knowledge graphs can be a state/memory component inside an execution graph
- **Search boundary:** direct original post, official-site searches, adjacent-field source
- **Used in report:** Executive Summary, §1, §4
- **Notes:** The two meanings can compose but are not interchangeable.

## C-007 — Codez makes an Anthropic affiliation claim

- **Claim:** Codez explicitly says a senior Anthropic engineer released the described 12-page PDF.
- **Kind:** synthesis
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://x.com/0xCodez/status/2080250266851463209
- **Supporting sources:** none required
- **Counter-evidence:** none needed to establish that the source makes the claim
- **Search boundary:** direct original post observation
- **Used in report:** Executive Summary, §4
- **Notes:** `verified` applies only to what Codez wrote, not whether the affiliation is true.

## C-008 — No Anthropic first-party source was found in the bounded search

- **Claim:** This bounded search did not find an Anthropic page, paper, or identifiable Anthropic
  author supporting Codez's affiliation claim.
- **Kind:** synthesis
- **Status:** probable
- **Time sensitivity:** high
- **Primary source:** none found
- **Supporting sources:** none; this is a bounded negative-search record
- **Counter-evidence:** a private, deleted, renamed, or poorly indexed source could exist
- **Search boundary:** direct post and linked X Article surface plus exact queries
  `"A senior Anthropic engineer just dropped 12-page PDF"`,
  `"Graph-Engineering-Athropic-Playbook.pdf"`,
  `"Extract Resolve Assemble Query Repeat" graph engineering Anthropic`, and
  `site:anthropic.com "Graph Engineering" knowledge graph`, through 2026-07-29
- **Used in report:** Executive Summary, §4
- **Notes:** The underlying affiliation remains unsupported, not disproven.

## C-009 — Graph-shaped workflows predate the July 2026 label

- **Claim:** General DAG workflows are older, while LangGraph documented nodes, edges, and shared
  graph state for multi-agent workflows on 2024-01-23 and Anthropic documented graph-shaped agent
  workflow patterns in 2024.
- **Kind:** origin
- **Status:** verified
- **Time sensitivity:** low
- **Primary source:** https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html
- **Supporting sources:** https://www.langchain.com/blog/langgraph-multi-agent-workflows,
  https://www.anthropic.com/engineering/building-effective-agents
- **Counter-evidence:** older workflow engines predate both sources
- **Search boundary:** dated first-party agent framework and engineering sources
- **Used in report:** §2, §3
- **Notes:** Establishes older practice, not the earliest graph-shaped software system.

## C-010 — Anthropic reports benefits and costs for multi-agent research

- **Claim:** Anthropic reports an internal multi-agent research improvement over its single-agent
  baseline while also reporting materially higher token cost and task-dependence.
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://www.anthropic.com/engineering/multi-agent-research-system
- **Supporting sources:** none required
- **Counter-evidence:** internal evaluation is not independent replication
- **Search boundary:** first-party engineering report
- **Used in report:** §6
- **Notes:** The report deliberately avoids generalizing the vendor result to all graph systems.

## C-011 — Multi-agent gains depend on task and coordination architecture

- **Claim:** Google's studied configurations show that multi-agent performance depends on task
  parallelizability, tool intensity, and coordination architecture.
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
- **Supporting sources:** linked paper from the first-party research summary
- **Counter-evidence:** the benchmark families do not represent every production task
- **Search boundary:** research summary and linked study
- **Used in report:** §6, §7
- **Notes:** Supports conditional adoption rather than a universal anti-multi-agent claim.

## C-012 — Parallel writers remain a known coordination risk

- **Claim:** Cognition argues that read-only specialist agents can help while parallel writers
  often fail because they lack shared context and make conflicting implicit decisions.
- **Kind:** synthesis
- **Status:** verified
- **Time sensitivity:** medium
- **Primary source:** https://cognition.com/blog/dont-build-multi-agents
- **Supporting sources:** https://cognition.com/blog/multi-agents-working
- **Counter-evidence:** stronger shared-state or ownership protocols may reduce the failure mode
- **Search boundary:** two first-party practitioner essays
- **Used in report:** §6, §8
- **Notes:** Verified as Cognition's production judgment, not a controlled universal result.

## C-013 — AutoGen GraphFlow is an implementation with an experimental status

- **Claim:** AutoGen GraphFlow supports sequential, parallel, conditional, and looping control
  flow and is documented as experimental.
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/graph-flow.html
- **Supporting sources:** none required
- **Counter-evidence:** status may change after the as-of date
- **Search boundary:** official dev documentation observed through 2026-07-29
- **Used in report:** §6
- **Notes:** Capability existence does not establish comparative effectiveness.

## C-014 — Loop and graph are related by scope, not replacement

- **Claim:** A loop focuses on iterative improvement within a work unit, while a graph coordinates
  multiple work units and can contain loops as nodes or cycles.
- **Kind:** comparison
- **Status:** probable
- **Time sensitivity:** medium
- **Primary source:** https://x.com/ericosiu/status/2079991948106957131
- **Supporting sources:** https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph,
  https://www.louisbouchard.ai/graph-engineering-explained/
- **Counter-evidence:** authors use both terms inconsistently and some loops have complex routing
- **Search boundary:** direct community definition, institutional response, independent analysis
- **Used in report:** Executive Summary, §3, §7
- **Notes:** This is the report's stable comparison dimension, not an official taxonomy.

## C-015 — The narrative expanded rapidly after Peter's post

- **Claim:** Carlos E. Perez published a same-day extended analysis, while multiple contemporary
  sources report Hamel Husain's X Article title and timing shortly after Peter's post.
- **Kind:** timeline
- **Status:** probable
- **Time sensitivity:** medium
- **Primary source:** https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c
- **Supporting sources:** https://www.turingpost.com/p/is-graph-engineering-real-why-everyone-is-talking-about-it,
  https://www.aibuilderclub.com/blog/loop-engineering-guide-2026,
  https://x.com/HamelHusain/article/2078346425621237935
- **Counter-evidence:** Hamel's Article body and direct timestamp were inaccessible in this run
- **Search boundary:** reachable same-week primary article plus two contemporary timelines
- **Used in report:** §2, §4
- **Notes:** Carlos's publication is directly readable; Hamel's timing remains proxy evidence.

## C-016 — Several factors probably explain the July resonance

- **Claim:** Stronger agent nodes, longer tasks, available orchestration frameworks, cheap
  parallel fan-out, and a shareable naming ladder together probably explain why the label
  resonated in July 2026.
- **Kind:** synthesis
- **Status:** probable
- **Time sensitivity:** high
- **Primary source:** none; this is researcher synthesis
- **Supporting sources:** https://www.anthropic.com/engineering/multi-agent-research-system,
  https://www.langchain.com/blog/langgraph-multi-agent-workflows,
  https://www.anthropic.com/engineering/building-effective-agents,
  https://x.com/michaelmasson55/status/2075913998449701170
- **Counter-evidence:** the timing may mostly reflect attention dynamics and rapid content
  production rather than a measured change in production bottlenecks
- **Search boundary:** production retrospectives, dated framework history, direct X naming posts,
  and sampled visible replies
- **Used in report:** §2 “为什么这句话会爆”
- **Notes:** The components are supported individually; the combined causal explanation is not
  independently identified.

## C-017 — Josh is the earliest reachable systematic standalone definition

- **Claim:** Josh C. Simmons's 2026-07-04 article is the earliest reachable source in this search
  that uses the standalone label `graph engineering` and gives it a systematic agent-control
  definition.
- **Kind:** origin
- **Status:** probable
- **Time sensitivity:** medium
- **Primary source:** https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase
- **Supporting sources:** https://x.com/itamar_mar/status/1763168555539812407,
  https://x.com/michaelmasson55/status/2075913998449701170
- **Counter-evidence:** Itamar's 2024 `flow (/graph) engineering` is a semantic predecessor; an
  earlier standalone use could exist in unindexed, deleted, private, or inaccessible X content
- **Search boundary:** exact phrase and dated Web searches before 2026-07-04 plus directly
  reachable known X URLs; no authenticated or full-archive X search
- **Used in report:** §2, §4
- **Notes:** This is explicitly not an absolute first-use or inventor claim.

## C-018 — Third-party pages repeat the PDF filename and attribution

- **Claim:** Third-party indexed pages reproduce Codez's Anthropic attribution and/or the
  `Graph-Engineering-Athropic-Playbook.pdf` filename.
- **Kind:** timeline
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://w.twstalker.com/DocQpj
- **Supporting sources:** https://sandrise.io/
- **Counter-evidence:** repetition does not establish provenance or truth
- **Search boundary:** exact-phrase and exact-filename Web queries observed 2026-07-29
- **Used in report:** §4
- **Notes:** These are propagation artifacts only.

## C-019 — LangGraph exposes graph runtime primitives

- **Claim:** LangGraph officially models workflows with state, nodes, and edges, and documents
  checkpointed persistence, interrupts, and dynamic routing.
- **Kind:** mechanism
- **Status:** verified
- **Time sensitivity:** high
- **Primary source:** https://docs.langchain.com/oss/python/langgraph/graph-api
- **Supporting sources:** https://docs.langchain.com/oss/python/langgraph/persistence,
  https://docs.langchain.com/oss/python/langgraph/overview
- **Counter-evidence:** available primitives do not establish that a graph is the best design for
  a specific workload
- **Search boundary:** official LangGraph docs observed through 2026-07-29
- **Used in report:** §6
- **Notes:** This is a capability claim, not a performance claim.

## Source records

## S-001 — We Are Entering the Graph Engineering Phase

- **URL:** https://www.drjoshcsimmons.com/writing/we-are-entering-the-graph-engineering-phase
- **Author / publisher:** Josh C. Simmons
- **Published / updated:** 2026-07-04
- **Role:** definer
- **Source class:** primary
- **Claims supported:** C-001
- **Limitations:** Does not establish absolute term priority or empirical superiority.

## S-002 — Itamar Friedman flow (/graph) engineering post

- **URL:** https://x.com/itamar_mar/status/1763168555539812407
- **Author / publisher:** Itamar Friedman / X
- **Published / updated:** 2024-02-29 11:45 UTC
- **Role:** semantic predecessor
- **Source class:** community
- **Claims supported:** C-002
- **Limitations:** Reply context; uses `flow (/graph) engineering`, not standalone title case.

## S-003 — Peter Steinberger loops-or-graphs post

- **URL:** https://x.com/steipete/status/2078277297791189132
- **Author / publisher:** Peter Steinberger / X
- **Published / updated:** 2026-07-18 00:34 UTC
- **Role:** amplifier
- **Source class:** community
- **Claims supported:** C-003
- **Limitations:** One-line question; sampled public replies are not representative opinion.

## S-004 — Mike naming-ladder post

- **URL:** https://x.com/michaelmasson55/status/2075913998449701170
- **Author / publisher:** Mike / X
- **Published / updated:** 2026-07-11 12:04 UTC
- **Role:** early predictor
- **Source class:** community
- **Claims supported:** C-004
- **Limitations:** No definition and very low reach.

## S-005 — Eric Siu graph-versus-loop post

- **URL:** https://x.com/ericosiu/status/2079991948106957131
- **Author / publisher:** Eric Siu / X
- **Published / updated:** 2026-07-22 18:08 UTC
- **Role:** definer / explainer
- **Source class:** community
- **Claims supported:** C-001
- **Limitations:** Analogy simplifies dynamic graph and complex loop behavior.

## S-006 — Paweł Huryn criticism

- **URL:** https://x.com/PawelHuryn/status/2078755464754376719
- **Author / publisher:** Paweł Huryn / X
- **Published / updated:** 2026-07-19 08:14 UTC
- **Role:** critic / practitioner
- **Source class:** community
- **Claims supported:** C-005
- **Limitations:** Experience-based position, not a controlled comparison.

## S-007 — Codez knowledge-graph post

- **URL:** https://x.com/0xCodez/status/2080250266851463209
- **Author / publisher:** Codez / X
- **Published / updated:** 2026-07-23 11:14 UTC
- **Role:** amplifier / conflated explainer
- **Source class:** community
- **Claims supported:** C-006, C-007
- **Limitations:** Anthropic affiliation has no first-party source found; post merges knowledge
  graph memory with agent control topology.

## S-008 — LLM-assisted Knowledge Graph Engineering

- **URL:** https://arxiv.org/abs/2307.06917
- **Author / publisher:** Lars-Peter Meyer et al. / arXiv
- **Published / updated:** 2023-07-13
- **Role:** adjacent-field primary source
- **Source class:** primary
- **Claims supported:** C-006
- **Limitations:** Not about agent execution topology.

## S-009 — 3 Years of Graph Engineering with LangGraph

- **URL:** https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph
- **Author / publisher:** Sydney Runkle, Harrison Chase / LangChain
- **Published / updated:** 2026-07-22
- **Role:** institutional adopter / critic
- **Source class:** first-party
- **Claims supported:** C-001, C-003
- **Limitations:** Retrospective product framing.

## S-010 — Building Effective Agents

- **URL:** https://www.anthropic.com/engineering/building-effective-agents
- **Author / publisher:** Anthropic
- **Published / updated:** 2024-12-19
- **Role:** official mechanism source
- **Source class:** first-party
- **Claims supported:** C-001, C-009
- **Limitations:** Engineering guidance, not a controlled benchmark.

## S-011 — LangGraph: Multi-Agent Workflows

- **URL:** https://www.langchain.com/blog/langgraph-multi-agent-workflows
- **Author / publisher:** LangChain
- **Published / updated:** 2024-01-23
- **Role:** official implementation history
- **Source class:** first-party
- **Claims supported:** C-009, C-014
- **Limitations:** Establishes mechanism and date, not comparative effectiveness.

## S-012 — How We Built Our Multi-Agent Research System

- **URL:** https://www.anthropic.com/engineering/multi-agent-research-system
- **Author / publisher:** Anthropic
- **Published / updated:** 2025-06-13
- **Role:** practitioner
- **Source class:** first-party
- **Claims supported:** C-010
- **Limitations:** Internal evaluation, model-specific architecture, no independent replication.

## S-013 — Towards a Science of Scaling Agent Systems

- **URL:** https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
- **Author / publisher:** Yubin Kim, Xin Liu / Google Research
- **Published / updated:** 2026-01-28
- **Role:** empirical researcher / critic
- **Source class:** first-party
- **Claims supported:** C-011
- **Limitations:** Studied benchmark families cannot represent every production workload.

## S-014 — Don't Build Multi-Agents

- **URL:** https://cognition.com/blog/dont-build-multi-agents
- **Author / publisher:** Walden Yan / Cognition
- **Published / updated:** 2025-06-12
- **Role:** practitioner / critic
- **Source class:** first-party
- **Claims supported:** C-012
- **Limitations:** Coding-agent experience rather than a controlled benchmark.

## S-015 — AutoGen GraphFlow

- **URL:** https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/graph-flow.html
- **Author / publisher:** Microsoft AutoGen
- **Published / updated:** current dev docs observed 2026-07-29
- **Role:** official implementation
- **Source class:** first-party
- **Claims supported:** C-013
- **Limitations:** Experimental API and time-sensitive dev documentation.

## S-016 — Graph Engineering Explained: What Actually Changed

- **URL:** https://www.louisbouchard.ai/graph-engineering-explained/
- **Author / publisher:** Louis-François Bouchard / What's AI
- **Published / updated:** 2026-07-22
- **Role:** independent explainer / critic
- **Source class:** independent analysis
- **Claims supported:** C-014
- **Limitations:** Commentary and teaching synthesis, not a primary technical result.

## S-017 — Third-party reproduction of the Codez attribution

- **URL:** https://w.twstalker.com/DocQpj
- **Author / publisher:** TwStalker mirror
- **Published / updated:** observed 2026-07-29
- **Role:** aggregator / propagation evidence
- **Source class:** aggregator
- **Claims supported:** C-018
- **Limitations:** No independent provenance; cannot verify the affiliation.
- **Retrieval handle:** Query `"A senior Anthropic engineer just dropped 12-page PDF"`; result
  title `QPJDoc @DocQpj - Twitter Profile | TwStalker`; exact Codez text was visible in the page.

## S-018 — Page indexing the PDF filename

- **URL:** https://sandrise.io/
- **Author / publisher:** Nick Sanders
- **Published / updated:** observed 2026-07-29
- **Role:** discovery index
- **Source class:** aggregator
- **Claims supported:** C-018
- **Limitations:** Shows the filename in an index but not authoritative authorship.
- **Retrieval handle:** Query `"Graph-Engineering-Athropic-Playbook.pdf"`; result title
  `Exploring Next | Nick Sanders`; the filename appeared in the indexed episode list.

## S-019 — From Loop Engineering to Graph Engineering?

- **URL:** https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c
- **Author / publisher:** Carlos E. Perez / Intuition Machine
- **Published / updated:** 2026-07-18
- **Role:** early extended explainer
- **Source class:** primary
- **Claims supported:** C-015
- **Limitations:** Same-day interpretation, not an empirical result or official definition.

## S-020 — Airflow DAG core concepts

- **URL:** https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html
- **Author / publisher:** Apache Airflow
- **Published / updated:** current docs observed 2026-07-29
- **Role:** engineering ancestor / official documentation
- **Source class:** first-party
- **Claims supported:** C-009
- **Limitations:** General deterministic workflow orchestration, not an agent benchmark.

## S-021 — LangGraph Graph API and persistence

- **URL:** https://docs.langchain.com/oss/python/langgraph/graph-api
- **Author / publisher:** LangChain
- **Published / updated:** current docs observed 2026-07-29
- **Role:** official runtime documentation
- **Source class:** first-party
- **Claims supported:** C-019
- **Limitations:** Documents available primitives, not comparative effectiveness.

## Content signals

All observations below used direct public X original pages in one narrow window. The candidate set
was preselected from a known canonical URL seed list and Web discovery; it is not exhaustive.

## M-001 — Peter Steinberger

- **URL:** https://x.com/steipete/status/2078277297791189132
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Peter Steinberger / @steipete
- **Published at:** 2026-07-18 00:34 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** 3.1m
- **Comments / replies:** 1.2k
- **Reposts / shares:** 388
- **Quotes:** unavailable
- **Likes / reactions:** 7.7k
- **Bookmarks / saves:** 2.8k
- **Signal status:** observed
- **Metric precision:** rounded-ui
- **Comparable set:** seven readable preselected X posts observed in the same minute

## M-002 — Itamar Friedman

- **URL:** https://x.com/itamar_mar/status/1763168555539812407
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Itamar Friedman / @itamar_mar
- **Published at:** 2024-02-29 11:45 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** reply
- **Text access:** complete
- **Views / impressions:** 3.2k
- **Comments / replies:** 3
- **Reposts / shares:** 1
- **Quotes:** unavailable
- **Likes / reactions:** 16
- **Bookmarks / saves:** 6
- **Signal status:** observed
- **Metric precision:** views rounded-ui; reactions exact-ui
- **Comparable set:** same preselected set, but post age differs materially

## M-003 — Mike

- **URL:** https://x.com/michaelmasson55/status/2075913998449701170
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Mike / @michaelmasson55
- **Published at:** 2026-07-11 12:04 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** 69
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Likes / reactions:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** partial
- **Comparable set:** same preselected set
- **Notes:** One additional unlabeled count was visible; it is not assigned to a metric.

## M-004 — Miles Deutscher

- **URL:** https://x.com/milesdeutscher/status/2079692400382103964
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Miles Deutscher / @milesdeutscher
- **Published at:** 2026-07-21 22:18 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** 31.6k
- **Comments / replies:** 17
- **Reposts / shares:** 25
- **Quotes:** unavailable
- **Likes / reactions:** 170
- **Bookmarks / saves:** 214
- **Signal status:** observed
- **Metric precision:** views rounded-ui; reactions exact-ui
- **Comparable set:** same preselected set

## M-005 — Eric Siu

- **URL:** https://x.com/ericosiu/status/2079991948106957131
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Eric Siu / @ericosiu
- **Published at:** 2026-07-22 18:08 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** post
- **Text access:** complete
- **Views / impressions:** 23.2k
- **Comments / replies:** 9
- **Reposts / shares:** 41
- **Quotes:** unavailable
- **Likes / reactions:** 226
- **Bookmarks / saves:** 359
- **Signal status:** observed
- **Metric precision:** views rounded-ui; reactions exact-ui
- **Comparable set:** same preselected set

## M-006 — Paweł Huryn

- **URL:** https://x.com/PawelHuryn/status/2078755464754376719
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Paweł Huryn / @PawelHuryn
- **Published at:** 2026-07-19 08:14 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** quote post
- **Text access:** complete
- **Views / impressions:** 14.8k
- **Comments / replies:** 24
- **Reposts / shares:** 9
- **Quotes:** unavailable
- **Likes / reactions:** 126
- **Bookmarks / saves:** 199
- **Signal status:** observed
- **Metric precision:** views rounded-ui; reactions exact-ui
- **Comparable set:** same preselected set

## M-007 — Codez

- **URL:** https://x.com/0xCodez/status/2080250266851463209
- **Channel:** X
- **Surface:** X original via in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Codez / @0xCodez
- **Published at:** 2026-07-23 11:14 UTC
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** post with linked X Article
- **Text access:** complete for post; partial for linked material
- **Views / impressions:** 478k
- **Comments / replies:** 95
- **Reposts / shares:** 509
- **Quotes:** unavailable
- **Likes / reactions:** 3.2k
- **Bookmarks / saves:** 6.5k
- **Signal status:** observed
- **Metric precision:** rounded-ui
- **Comparable set:** same preselected set

## M-008 — Hamel Husain X Article

- **URL:** https://x.com/HamelHusain/article/2078346425621237935
- **Channel:** X
- **Surface:** X Article via public in-app browser
- **Query / sort:** direct URL
- **Author / handle:** Hamel Husain / @HamelHusain
- **Published at:** reported 2026-07-18; direct timestamp inaccessible
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** article
- **Text access:** inaccessible
- **Views / impressions:** unavailable
- **Comments / replies:** unavailable
- **Reposts / shares:** unavailable
- **Quotes:** unavailable
- **Likes / reactions:** unavailable
- **Bookmarks / saves:** unavailable
- **Signal status:** unavailable
- **Metric precision:** none
- **Proxy basis:** https://www.turingpost.com/p/is-graph-engineering-real-why-everyone-is-talking-about-it,
  https://www.aibuilderclub.com/blog/loop-engineering-guide-2026
- **Comparable set:** excluded

## M-009 — Aaron Francis reply

- **URL:** https://x.com/aarondfrancis/status/2078281677437067773
- **Channel:** X
- **Surface:** X original reply visible on Peter's public post page
- **Query / sort:** direct parent URL
- **Author / handle:** Aaron Francis / @aarondfrancis
- **Published at:** 2026-07-18; exact time unavailable
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** reply
- **Text access:** complete
- **Views / impressions:** 38k
- **Comments / replies:** 9
- **Reposts / shares:** 15
- **Quotes:** unavailable
- **Likes / reactions:** 1k
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** rounded-ui
- **Comparable set:** not ranked; visible reply sample only

## M-010 — Matthew Berman reply

- **URL:** https://x.com/MatthewBerman/status/2078278860991582331
- **Channel:** X
- **Surface:** X original reply visible on Peter's public post page
- **Query / sort:** direct parent URL
- **Author / handle:** Matthew Berman / @MatthewBerman
- **Published at:** 2026-07-18; exact time unavailable
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** reply
- **Text access:** complete
- **Views / impressions:** 45k
- **Comments / replies:** 25
- **Reposts / shares:** 10
- **Quotes:** unavailable
- **Likes / reactions:** 943
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** views rounded-ui; reactions exact-ui
- **Comparable set:** not ranked; visible reply sample only

## M-011 — John Smathers reply

- **URL:** https://x.com/risingtidesdev/status/2078285610914050420
- **Channel:** X
- **Surface:** X original reply visible on Peter's public post page
- **Query / sort:** direct parent URL
- **Author / handle:** John Smathers / @risingtidesdev
- **Published at:** 2026-07-18; exact time unavailable
- **Observed at:** 2026-07-29 15:41 SGT
- **Post type:** reply
- **Text access:** complete
- **Views / impressions:** 35k
- **Comments / replies:** 5
- **Reposts / shares:** 8
- **Quotes:** unavailable
- **Likes / reactions:** 588
- **Bookmarks / saves:** unavailable
- **Signal status:** observed
- **Metric precision:** views rounded-ui; reactions exact-ui
- **Comparable set:** not ranked; visible reply sample only

## Open questions

- What additional origin candidates would a full-archive X MCP search find before 2026-07-04?
- How much does authenticated X `Latest` differ from Web-indexed and preselected candidates?
- What is the primary provenance of `Graph-Engineering-Athropic-Playbook.pdf`?
- Which current metric totals will change materially after 2026-07-29?
- Can quote-post sampling reveal more practitioner implementations rather than teaching content?
- Which graph architectures outperform simpler loops after total cost and recovery are counted?
