```env
TARGET=Output
```

```targetignore
*
```

```sourceignore
*.md
*.txt
```

You are writing one section of the new story. Read from `<env:SOURCE_MASK>/`:

- `_current_summary.md` — the rewritten sub-summary: every event in this section
- `_current_original.txt` — the original story segment (voice and style reference)
- `_current_num.txt` — three-digit section number (e.g. `004`)
- `_context.md` — the most recently constructed sections (for narrative continuity)

Also read:

- [rewritten_lorebook.md](Rewrite-Lorebook/repo/rewritten_lorebook.md) — canonical names, places, and facts for the new story

## Task

Write a fully realised, polished story section in prose.

1. **Follow `_current_summary.md` exactly** — every event, action, and beat must appear
2. **Flow from `_context.md`** — the opening must read naturally after the previous sections
3. **Match the style of `_current_original.txt`** — same voice, point of view, sentence rhythm, pacing
4. **Respect `rewritten_lorebook.md`** — all proper nouns and facts must match

Write the section to `./<content of _current_num.txt>.txt`.

## Quality bar

This is the **final output** of the pipeline — polished, publication-ready prose. Not an outline. Not a summary. Complete, vivid, well-paced narrative fiction.

## Rules

- Write **only** to `./<three-digit-number>.txt`
- Do **not** modify any input files
