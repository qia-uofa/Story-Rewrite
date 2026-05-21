```env
TARGET=SOP
```

```targetignore
*
```

```sourceignore
part_*
index.md
```

Read from `<env:SOURCE_MASK>/`:

- `_current_part.txt` — the story segment to summarise
- `_current_num.txt` — three-digit index of this part (e.g. `002`)

Write a **detailed narrative summary** to `./<content of _current_num.txt>.md`.

## What the summary must cover

- **Main events** — everything that happens, in narrative order
- **Characters** — who appears, what they do, key lines of dialogue
- **Setting & atmosphere** — where and when, mood and tone
- **Emotional beats** — tension, relief, surprise, grief
- **Plot-critical details** — revelations, decisions, foreshadowing, planted clues
- **Continuity hooks** — how this segment connects to what came before and after

## Quality bar

Detailed enough that a skilled writer could reconstruct the scene without reading the original. Reads as a reference document, not a blurb.

## Rules

- Write **only** to `./<three-digit number>.md`
- Do **not** modify `_current_part.txt` or `_current_num.txt`
