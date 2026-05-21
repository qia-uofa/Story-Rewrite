```env
TARGET=Rewrite-Summary
```

```targetignore
*
```

You are given:

- **Original story summary:** [summary.md](<env:SOURCE_MASK>/summary.md)
- **Rewrite instructions:** [instructions.md](Input/repo/instructions.md)

Apply every instruction to the story summary. Rewrite it so it describes the *new* version of the story after all transformations have been applied.

Write the rewritten summary to `./rewritten_summary.md`.

## Requirements

- Same narrative scope and level of detail as the original
- Apply **all** transformations from the instructions — skip none
- Internally consistent throughout (if a name changes, it changes everywhere)
- Written in fluid prose

## Rules

- Write **only** to `./rewritten_summary.md`
