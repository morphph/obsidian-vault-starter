# X community evidence

Use this protocol only when X materially carries a topic's origin, spread, definition,
practitioner evidence, or criticism.

## Route by capability

1. Discover whether a dedicated X connector, API, or MCP supports the required read operation.
2. If available, prefer the official X MCP or another first-party API with read-only credentials
   and the minimum tool allowlist.
3. Otherwise use an available browser surface for read-only observation of X search and original
   post pages. Load and follow the applicable browser-control skill.
4. Use public web search to discover canonical X URLs when native search is unavailable.
5. Use third-party snapshots only as `proxy`.

As of 2026-07-29, X documents a hosted X MCP at `https://api.x.com/mcp`, commonly reached through
the official `xurl mcp` bridge. It requires an X Developer app and underlying X API access; it is
not a free data channel. Recheck the [official X MCP documentation](https://docs.x.com/tools/mcp)
before configuration because authentication, capabilities, limits, and billing can change.

For research, expose only operations needed to search and read posts, users, counts, trends, or
news. Do not enable publishing, likes, follows, bookmarks, direct messages, or account-management
tools. Never place credentials in the research workspace, report, ledger, chat, or tracked config.

Browser work is also read-only: do not like, follow, repost, reply, bookmark, or inspect cookies,
local storage, passwords, session stores, or account attributes.

## Build reproducible query families

Choose only the families the question needs:

- exact term: `"<term>"`;
- chronology: `"<term>" since:<date> until:<date>` using `Latest`;
- origin counter-search: move `until:` earlier than the current earliest candidate;
- definitions: `"<term>" means` and `"<term>" is`;
- named source: `from:<handle> "<term>"`;
- practice: `"<term>" built`, `production`, `github`, or `using`;
- criticism: `"<term>" hype`, `nothing new`, `state machine`, `bullshit`, or a
  topic-appropriate counterphrase;
- disambiguation: pair the term with each adjacent meaning;
- replies and quotes: inspect a small sample around load-bearing posts.

Do not use a personalized feed as the sample. Use `Latest` for chronology and `Top` only to find
candidates. Record query, sort, date boundary, and how many candidates were reviewed. Search
ranking is not engagement data and does not establish Top-N.

Suggested evidence budgets, not report quotas:

- `quick`: 3 query families and 6–10 original posts;
- `standard`: about 6 query families and 15–25 original posts;
- `deep`: 8–12 query families and 30–50 original posts, plus sampled replies or quotes.

Stop early when additional posts repeat the same source chain or no longer change the discourse
map. Record important negative findings such as no production examples found.

## Capture original observations

For every post that carries a claim or content signal, record in `source-ledger.md`:

```markdown
- **URL:** <canonical post URL>
- **Surface:** X original via browser | X connector/API | X search card | third-party snapshot
- **Query / sort:** <query> · Latest | Top | direct URL
- **Author / handle:**
- **Published at:**
- **Observed at:** <timestamp with timezone>
- **Post type:** post | reply | quote | thread | article
- **Text access:** complete | partial | inaccessible
- **Views / impressions:** <displayed value or unavailable>
- **Comments / replies:** <displayed value or unavailable>
- **Reposts / shares:** <displayed value or unavailable>
- **Quotes:** <displayed value or unavailable>
- **Likes / reactions:** <displayed value or unavailable>
- **Bookmarks / saves:** <displayed value or unavailable>
- **Signal status:** observed | proxy | unavailable
- **Metric precision:** exact-ui | rounded-ui | partial | none
- **Comparable set:** <explicit set or none>
```

Preserve displayed strings such as `3.1M` and label them `rounded-ui`. Do not silently convert
them to exact numbers. Empty or hidden values are `unavailable`, not zero.

Use `observed` only for the original X page or first-party API result seen at the recorded time.
Search cards, snippets, screenshots reported by others, and third-party archives are `proxy`.

## Reconstruct discourse without amplifying bias

- Separate originator, amplifier, definer, practitioner, institutional adopter, and critic.
- Trace reposts and repeated claims to their common source instead of counting them as independent
  confirmation.
- Search support and criticism separately.
- Compare `Latest` findings with candidates surfaced by `Top`.
- Treat follower size and engagement as reach signals, never factual authority.
- Account for post age before comparing cumulative metrics.
- Counter-search every `first`, `invented`, `viral`, `most`, or `top` claim.
- Find the primary artifact behind screenshots, PDFs, benchmarks, or supposed official studies.
- Describe sampled replies and quotes as discourse evidence, not representative public opinion.
- State that platform ranking, region, language, deleted posts, and access state constrain the
  sample.

## Degrade honestly

- If native X search requires authentication, try another already available authorized surface
  only when browser-routing rules permit it. Otherwise ask for login in an interactive run or
  mark the lane incomplete.
- Direct public post pages may still permit original-body and metric observation even when search
  is blocked; verify each one rather than assuming.
- If a connector lacks credentials, costs money, or exposes unsafe write scopes, do not configure
  it silently. Continue with the next route.
- On rate limits or UI failures, stop repeated refreshes, retain completed observations, and mark
  the remainder `unavailable`.
- Third-party material may discover an original URL but cannot be upgraded into primary evidence.
- If direct X access does not materially improve the evidence, say so; do not add posts merely to
  justify the channel.
