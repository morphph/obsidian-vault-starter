# references/ — Content reference library

Curated source material I deliberately **draw on when creating content** — videos,
articles, talks worth returning to for ideas, framings, examples, and angles.

> **Style-template references live elsewhere.** References whose job is to *define a
> video format/style to reproduce* (narration voice + visual system + render target)
> are **not** kept here — they live in the blog2video repo's `templates/` (video style
> template library; one folder per template = `transcript.md` + `visual-style-prompt.md`
> + template card). This folder stays for **material to create content from**.

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

(暂无条目——收录后在此登记。)
