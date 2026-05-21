```env
TARGET=Rewrite-Lorebook
```

```targetignore
*
```

You are given:

- **Original lorebook:** [lorebook.md](<env:SOURCE_MASK>/lorebook.md)
- **Rewrite instructions:** [instructions.md](Input/repo/instructions.md)

Apply every instruction to every section of the lorebook. Rewrite it so it serves as the canonical reference for the *new*, rewritten story.

Write the rewritten lorebook to `./rewritten_lorebook.md`.

## Requirements

- Apply transformations to **all sections**: Characters, Locations, Timeline, Relationships, Objects & Artifacts, Themes & Motifs
- If a name changes, update every mention across all sections
- If the setting changes, update all location and timeline entries
- The rewritten lorebook must be **fully self-consistent** — no contradictions between sections

## Purpose

This rewritten lorebook is the source of truth for every subsequent stage (Rewrite-SOP, Output). Make it precise and complete.

## Rules

- Write **only** to `./rewritten_lorebook.md`
