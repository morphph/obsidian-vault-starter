---
name: emerge
description: "⚠️ Heavy command. 60-day scan to surface unnamed patterns and implicit theories. Best in a fresh session."
---

# Emerge — Surface What You Haven't Said Yet

Look across the vault for patterns, theories, and directions that you keep circling around but have never explicitly named.

## Step 0: Session Health Check

Before doing anything else, assess the current session:
- If the conversation already has more than 10 messages, warn:
  "⚠️ /emerge reads a lot of vault content. Recommend running in a fresh session for best results. Continue anyway? [yes / new session]"
- If fresh, proceed directly.

## Steps

1. Read ALL daily build logs from the past 60 days.
2. Read all files in ideas/, projects/, and references/.

3. Analyze for:
   - **Recurring themes** across unrelated contexts
   - **Unresolved [[links]]** mentioned repeatedly but never created — these are latent concepts
   - **#idea clusters** around common themes
   - **Repeated phrases or concepts** never formally defined
   - **Implicit theories** — beliefs revealed by decisions, not explicitly stated
   - **Direction signals** — where attention keeps drifting

4. For each discovered pattern:
   - **Name** — give it a clear, memorable name
   - **Evidence** — which specific build logs or notes show this
   - **Why it matters** — implications for projects or thinking
   - **Suggestion** — should this become an ideas/ note? A project? A reference?

5. Write to `agent-output/emerge-{date}.md`

6. In the terminal, show the top 3 findings with brief summaries.

## Important
- Show things I DON'T already know. Discovery, not confirmation.
- Ground every finding in specific vault content.
- Don't invent patterns. If data is thin, say so.
- Write to agent-output/ only.
