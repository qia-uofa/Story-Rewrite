## Goal
Create `./out/part-2/scores.json` containing exactly 20 sampled candidate pause points from the provided novel excerpt.

## Approach
- Treat line indices as zero-based, starting from the first visible line of the input file.
- Select candidates spread across the excerpt, including soft paragraph pauses, scene transitions, chapter endings, and emotionally held beats.
- Score each candidate using `score = p_close(i) × p_open(i+1) / 100`.
- Use integer scores for clean JSON output.

## Notes
- Chapter-ending transitions receive the highest scores.
- Mid-scene reflective pauses receive moderate scores.
- Dialogue/action transitions receive lower scores unless they clearly shift focus or time.