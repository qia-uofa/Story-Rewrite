```env
TARGET=Rewrite-SOP
```

```targetignore
*
```

```sourceignore
*.md
```

You are rewriting one sub-summary. Read from `<env:SOURCE_MASK>/`:

- `_current_summary.md` — the original sub-summary to rewrite
- `_current_num.txt` — three-digit part number (e.g. `003`)
- `_context.md` — the most recently rewritten sub-summaries (narrative continuity)

Also read:

- [rewritten_lorebook.md](Rewrite-Lorebook/repo/rewritten_lorebook.md) — canonical names, places, facts for the new story
- [instructions.md](Input/repo/instructions.md) — the rewrite instructions

## Task

Rewrite `_current_summary.md` so it describes this part of the **new, rewritten story**.

Apply all relevant instructions. Use `rewritten_lorebook.md` as the authoritative reference for all proper nouns and facts. Ensure the narrative flows naturally from the context in `_context.md`.

Write the rewritten sub-summary to `./<content of _current_num.txt>.md`.

## Requirements

- Same level of detail as the original sub-summary
- All instructions applied
- All proper nouns consistent with the rewritten lorebook
- Narrative continuity with `_context.md`

## Rules

- Write **only** to `./<three-digit-number>.md`
- Do **not** modify `_current_summary.md`, `_current_num.txt`, or `_context.md`
