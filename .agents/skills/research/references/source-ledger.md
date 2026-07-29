# Source ledger

Keep verification detail here so `report.md` can remain readable.

## Research boundary

```markdown
# Source Ledger: <topic>

> as_of: <YYYY-MM-DD>
> channels searched: <list>
> primary search languages: <list>
> important access limits: <paywalls, unavailable metrics, blocked pages>
```

## Claim record

Create one record for every load-bearing or contested claim:

```markdown
## C-001 — <short claim>

- **Claim:** <exact proposition used in the report>
- **Kind:** definition | origin | timeline | mechanism | metric | comparison | synthesis
- **Status:** verified | probable | disputed | unsupported
- **Time sensitivity:** low | medium | high
- **Primary source:** <canonical URL or none found>
- **Supporting sources:** <URLs>
- **Counter-evidence:** <URLs or search result>
- **Search boundary:** <what was checked before using first/only/best>
- **Operational contract:** <surface, minimum version, prerequisites, provider/plan/beta limits,
  or not applicable>
- **Used in report:** <section>
- **Notes:** <what the sources actually establish>
```

`verified` means the cited evidence directly supports the proposition. Multiple secondary sources
repeating the same claim do not make it verified.

## Source record

Record sources that materially shape the report:

```markdown
## S-001 — <title>

- **URL:** <canonical URL>
- **Author / publisher:**
- **Published / updated:**
- **Role:** originator | official | amplifier | explainer | practitioner | critic
- **Source class:** primary | first-party | independent analysis | community | aggregator
- **Affiliation / dependency:** <employer, vendor, sponsor, customer, investor, evaluation access,
  or none found>
- **Evidence chain:** <other items that repeat the same underlying test, interview, or release>
- **Claims supported:** C-001, C-004
- **Limitations:** <conflict of interest, missing data, inaccessible original, etc.>
```

## Content signal

Use this only when discussing reach or prominence:

```markdown
## M-001 — <piece>

- **URL:**
- **Channel:**
- **Surface:** <original page, connector/API, search card, or third-party snapshot>
- **Query / sort:** <query and Latest/Top, direct URL, or not applicable>
- **Author / handle:**
- **Published at:**
- **Observed at:** <timestamp with timezone or unknown>
- **Post type:** <post, reply, quote, thread, article, video, etc.>
- **Text access:** complete | partial | inaccessible
- **Views / impressions:**
- **Likes / reactions:**
- **Comments / replies:**
- **Reposts / shares:**
- **Quotes:**
- **Bookmarks / saves:**
- **Signal status:** observed | proxy | unavailable
- **Metric precision:** exact-ui | rounded-ui | partial | none
- **Proxy basis:** <search prominence, citation frequency, author reach; omit if observed>
- **Comparable set:** <what this item was compared against, if ranked>
```

`observed` requires a direct original surface or first-party API result and an observation time.
A search card, third-party snapshot, snippet, or another author's retelling is `proxy`. A blank
or hidden metric is `unavailable`, not zero. Preserve rounded UI strings such as `3.1M`; do not
convert them into invented exact counts.

Never infer missing numbers. Rank only within an explicit, comparably observed set using the same
metric and observation window. Otherwise describe a piece as representative, discourse-shaping,
or high-signal rather than Top-N.

## Open questions

End with unresolved claims, inaccessible originals, definition conflicts, and facts likely to
change soon. These are part of the research result, not defects to hide.
