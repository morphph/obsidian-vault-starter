# Claude Daily-Fetch Source Verification (2026-04-18)

Conversation log: tested all candidate sources for daily Anthropic/Claude newsletter ingestion.

## Method
- Websites: WebFetch
- X handles: Playwright MCP (`browser_navigate` → page title parse)

## Verified websites (WebFetch ✅)
- anthropic.com/news
- anthropic.com/engineering
- anthropic.com/transparency *(later dropped — policy/compliance, off-topic for product newsletter)*
- claude.com/blog (JS-rendered but content visible)
- claude.com/cowork
- support.claude.com/.../release-notes
- platform.claude.com/docs/en/release-notes
- platform.claude.com/docs/en/about-claude/models/overview
- platform.claude.com/docs/en/claude-code
- status.claude.com *(later dropped — incident feed)*
- github.com/anthropics/claude-code/releases.atom
- github.com/anthropics/claude-code/raw/refs/heads/main/CHANGELOG.md

## Failed
- docs.claude.com/* → redirects to platform.claude.com/docs/* (use canonical)
- github.com/.../CHANGELOG.md (blob URL) → HTML wrapper hides content (use `raw/refs/heads/main/...`)
- ALL x.com/* via WebFetch → HTTP 402 (X blocks unauthenticated fetches)

## Verified X handles (Playwright ✅)
Page titles confirm both handle and display name:
- @AnthropicAI → "Anthropic"
- @DarioAmodei → "Dario Amodei" *(later dropped — vision essays, not product)*
- @jackclarkSF → "Jack Clark" *(later dropped — policy/safety focus)*
- @mikeyk → "Mike Krieger" (CPO)
- @claudeai → "Claude"
- @alexalbert__ → "Alex Albert" (DevRel) — note: trailing **double** underscore
- @bcherny → "Boris Cherny"
- @_catwu → "cat" (Cat Wu) — note: leading underscore
- @trq212 → "Thariq"
- @felixrieseberg → "Felix Rieseberg"

## Filtering decision
Dropped 4 sources (policy/vision/incidents) as low-signal for a model/product/dev-feature newsletter:
- anthropic.com/transparency
- @DarioAmodei
- @jackclarkSF
- status.claude.com

## Final count
9 websites · 8 X accounts · 1 RSS feed = **18 sources**
