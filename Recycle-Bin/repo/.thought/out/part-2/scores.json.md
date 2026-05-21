## Goal
Create `./out/part-2/scores.json` containing sampled natural pause-point scores from the provided excerpt.

## Approach
I treated line indices as the visible line numbers in `window.txt`, using boundaries after the indexed line and before the next line. I selected pause points spread across the excerpt, emphasizing chapter boundaries, scene transitions, letter/list endings, and shifts from one interaction or location to another.

## Scoring Notes
- Chapter transitions receive the highest scores because the preceding line closes a major unit and the next line opens a new one.
- Scene shifts and completed mini-scenes receive moderately high scores.
- Boundaries after documents/lists or dialogue exchanges are scored lower when the next line continues the same broader narrative thread.