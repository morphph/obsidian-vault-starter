---
name: log
description: Quick daily build log capture with auto-linking. Prompts for what you built, what surprised you, and what's next. Writes to today's daily note, then auto-suggests [[wiki links]].
---

# Daily Build Log Capture + Auto-Link

You are helping vfan quickly capture a daily build log entry. This should be fast and low-friction.

## Steps

### Part 1: Capture

1. Get today's date in YYYY-MM-DD format.

2. Check if `daily/{date}.md` already exists.
   - If yes, you'll append to it.
   - If no, you'll create it with the header `# {date}`.

3. Ask me these three questions ONE AT A TIME (wait for each answer before asking the next):
   - "What did you build or work on today?"
   - "Anything surprising or worth noting?"
   - "What's the plan for tomorrow?"

4. Take my answers and format them as a build log entry:
   - Add `## Build Log` section header (if not already present in the file)
   - Format each answer as bullet points
   - If I mention something that sounds like an idea or future possibility, add `#idea` tag
   - If I mention being stuck or blocked, add `#blocker` tag
   - If I mention a surprising discovery, add `#learning` tag

### Part 2: Auto-Link

5. Before writing, scan the formatted entry for link opportunities:
   - **Project names:** LoreAI, blog2video
   - **Existing vault notes:** scan file names in ideas/, references/, projects/ for matches
   - **Concepts from CLAUDE.md:** check the linking conventions section for known concepts
   - Wrap detected names/concepts in [[double brackets]]

6. Show me the formatted entry WITH the suggested links highlighted:
   ```
   Ready to write to daily/{date}.md:
   
   ## Build Log
   - worked on [[blog2video]] narration pacing, Kimi K2.5 handles ZH better than expected
   - #learning Chinese content needs different narrative structure for [[blog2video]]
   - #idea test [[LoreAI]] AEO with llms.txt

   ## Tomorrow
   - continue with narration module

   New links suggested: [[blog2video]], [[LoreAI]]
   
   Write this? [yes / edit / cancel]
   ```

7. Wait for confirmation. If "edit", let me modify before writing.

8. Write the entry to `daily/{date}.md` (append if file exists).

9. Give me a one-line summary:
   "✅ Logged to daily/{date}.md — X items, Y links, Z tags."

## Important
- Keep it fast. Don't over-format. Bullet points are fine.
- Chinese-English mixing is normal. Don't standardize language.
- If I give very short answers, that's fine. Don't ask me to elaborate.
- NEVER write to any file outside of daily/.
- Don't over-link. Only suggest links that are genuinely useful and likely to appear in other notes.
- Follow CLAUDE.md linking conventions: link projects and own concepts, NOT generic terms like AI or Python.
