<file path="./.thought/out/part-2/scores.json.md">
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
</file>

<file path="./out/part-2/scores.json">
{
  "14": 42,
  "18": 53,
  "35": 33,
  "52": 42,
  "60": 49,
  "70": 60,
  "76": 56,
  "99": 60,
  "103": 100,
  "110": 53,
  "128": 54,
  "160": 60,
  "176": 64,
  "194": 60,
  "228": 95,
  "300": 56,
  "355": 53,
  "372": 100,
  "465": 49,
  "493": 49
}
</file>