---
name: ideas
description: "⚠️ Heavy command. Deep 30-day vault scan → cross-project idea report. Best run in a fresh session. Takes 5-10 min."
---

# Ideas Generation — Cross-Project Deep Scan

Perform a comprehensive scan of the vault to generate actionable ideas.

## Step 0: Session Health Check

Before doing anything else, assess the current session:
- If the conversation already has more than 10 messages, warn the user:
  "⚠️ This is a heavy command that reads a lot of vault content. You already have significant conversation history in this session. For best results, I recommend running /ideas in a fresh session. Continue anyway? [yes / new session]"
- If the session is fresh or short, proceed directly.

## Steps

1. **Load all context:**
   - Read CLAUDE.md
   - Read ALL project context files in projects/
   - Read ALL daily build logs from the past 30 days
   - Read all files in ideas/
   - Read all files in references/

2. **Structural analysis** (use Obsidian CLI if available):
   - `obsidian orphans` — files with no links to/from other files
   - `obsidian search query="- [ ]"` — incomplete tasks
   - `obsidian backlinks` for key project files — most connected?
   - Unresolved [[links]] — concepts mentioned but never developed
   - #idea tags not yet graduated
   - #blocker tags still open

3. **Pattern detection:**
   - Themes appearing across multiple projects?
   - Time spent on undocumented activities?
   - Connections between projects not explicitly linked?
   - Contradictions between project strategies?
   - Tools or workflows mentioned repeatedly but not built?

4. **Generate report** — write to `agent-output/ideas-report-{date}.md`:

```markdown
# Ideas Report — {date}

## Vault Health
- Daily logs analyzed: X (date range)
- Active projects: X
- Orphan files worth noting: [list]
- Unresolved links (latent interests): [list]
- Stale #blockers (>7 days old): [list]

## Cross-Project Connections
[Connections between projects I might not be seeing.
Each: what the connection is + specific action.]

## Tools to Build
[Based on work patterns — specific, not vague.
Not "a dashboard" but "a command that does X because you keep doing Y manually."]

## Ideas Worth Developing
[Ideas from build logs that deserve standalone notes.
Each: original context + why interesting + suggested next step.]

## Patterns I Haven't Named
[Themes I keep circling around.
Each: a suggested name + one-paragraph description.]

## Top 5 Actions — Do Now
[Most impactful things to do this week, ranked.]
```

5. After writing, give a 3-sentence summary in the terminal.
   Then: "Full report → agent-output/ideas-report-{date}.md"

## Important
- Write to agent-output/ only. NEVER to daily/, ideas/, or projects/.
- Be specific and actionable. No abstract advice.
- Ground findings in actual vault content.
- If vault data is thin (<2 weeks of logs), say so and suggest building more history first.
