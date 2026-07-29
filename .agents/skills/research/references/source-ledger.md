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
- **Claims supported:** C-001, C-004
- **Limitations:** <conflict of interest, missing data, inaccessible original, etc.>
```

## Content signal

Use this only when discussing reach or prominence:

```markdown
## M-001 — <piece>

- **URL:**
- **Channel:**
- **Observed at:** <timestamp or unknown>
- **Views / impressions:**
- **Likes / reactions:**
- **Comments / replies:**
- **Bookmarks / saves:**
- **Signal status:** observed | proxy | unavailable
- **Proxy basis:** <search prominence, citation frequency, author reach; omit if observed>
- **Comparable set:** <what this item was compared against, if ranked>
```

Never infer missing numbers. Without a comparable set and observed metrics, describe a piece as
representative or high-signal, not Top-N.

## Open questions

End with unresolved claims, inaccessible originals, definition conflicts, and facts likely to
change soon. These are part of the research result, not defects to hide.
