---
name: connect
description: "Find hidden connections between two concepts or projects. Usage: /connect [concept1] [concept2]. Medium weight — session check included."
---

# Connect — Cross-Domain Bridge Finder

Take two concepts, projects, or domains and find meaningful connections between them.

## Step 0: Session Health Check

If the conversation has more than 15 messages, suggest a fresh session.
Otherwise proceed.

## Arguments
Parse $ARGUMENTS to extract two concepts, e.g.:
`/connect blog2video AEO`
`/connect Xiaohongshu email-subscribers`

## Steps

1. **Search for both concepts** across the vault:
   - File names, content, [[links]]
   - Use Obsidian CLI if available: `obsidian search query="{concept}"` and `obsidian backlinks file="{concept}"`
   - Also search related terms and synonyms

2. **Map neighborhoods:**
   For each concept: all mentioning files, linked files, surrounding themes.

3. **Find bridges:**
   - Files mentioning BOTH concepts
   - Shared links (connected to both)
   - Thematic overlaps in build logs
   - Indirect paths through the link graph

4. **Generate 3-5 bridges** — meaningful, not superficial.
   Each bridge:
   - What the connection is (grounded in vault content)
   - Why it's interesting or non-obvious
   - One actionable suggestion

5. Write full report to `agent-output/connect-{concept1}-{concept2}-{date}.md`

6. Show bridges in terminal + mention report location.

## Important
- Connections should be genuinely interesting, not obvious.
- Ground every connection in actual vault content.
- If one/both concepts barely appear in the vault, say so honestly.
- Write to agent-output/ only.
