# references/ — Content reference library

Curated source material I deliberately **draw on when creating content** — videos,
articles, talks worth returning to for ideas, framings, examples, and angles.

## How this differs from `raw/`

| | `raw/` | `references/` |
|---|---|---|
| Purpose | Sources to **ingest into the wiki** knowledge base | Material to **create content from** |
| Flow | `/ingest` → fans out into `wiki/` pages | Browsed by hand while drafting; feeds `/draft` |
| Shape | Flat pile of files | One folder per source |
| Owner | Human curates, LLM reads | Human curates, LLM helps capture |

A source can be both — ingest it into the wiki *and* keep a reference card here if
it's a recurring creative touchstone. They serve different jobs.

## Structure

```
references/
└── <slug>/
    ├── README.md      ← note card (source, why it's a reference, takeaways, content angles)
    ├── transcript.txt ← clean text (for video/audio sources)
    └── captions.srt   ← original timed captions (optional)
```

## Note card conventions

- **Frontmatter**: `title`, `source`, `type` (youtube/article/talk/…), `author`, `published`, `captured`, `tags`.
- **Why it's a reference** — what makes this worth keeping (the reusable part).
- **Key takeaways / claims** — the substance, in my own words.
- **Content angles** — concrete ideas this could seed for my own writing.

## Capturing a YouTube reference

```bash
# clean transcript + timed captions via yt-dlp
yt-dlp --no-update --skip-download --write-auto-subs \
       --sub-langs "en-orig,en" --convert-subs srt \
       -o "%(title)s.%(ext)s" "<url>"
```

Then de-dupe the rolling auto-captions into a clean `transcript.txt` and write the note card.

## Index

- [[sean-agent-harness-loop-engineering/README|Sean — AI Agent Harness & Loop Engineering (19 min)]] — cleanest plain-language frame for harness / loop / eval / RAG
