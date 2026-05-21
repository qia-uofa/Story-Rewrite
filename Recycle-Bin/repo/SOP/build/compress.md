```env
TARGET=SOS
```

```targetignore
*
```

Read all sub-summary files from `<env:SOURCE_MASK>/` in order — named `000.md`, `001.md`, `002.md`, etc.

Synthesise a single, comprehensive **Story Summary** and write it to `./summary.md`.

## What the summary must contain

- **Narrative arc** — the complete story from opening to resolution, in prose
- **Primary characters** — who they are and how they change across the whole story
- **Central themes** — the ideas and questions the story explores
- **Major turning points** — the key events that shift the story's direction
- **Climax and resolution** — what the story builds to and how it ends

## Quality bar

Fluid, readable prose (not bullet points). Several paragraphs. A standalone document — someone who has never read the story should come away with a clear, accurate picture of the whole work.

## Rules

- Write **only** to `./summary.md`
