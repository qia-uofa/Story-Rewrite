## Goal
Create `./out/part-1/scores.json` containing scored candidate pause points from the provided novel snippet.

## Approach
- Treated line indices as zero-based, beginning with the title line.
- Selected 10 candidate pauses spread across the available excerpt, including chapter boundaries, scene transitions, reflective beats, and strong emotional/dialogue beats.
- Scored each candidate by estimating how strongly the current line closes a unit and how strongly the following line opens a new unit, then using `score = p_close * p_open / 100`.

## Notes
- Chapter boundaries receive the strongest scores.
- Cliffhangers or emotionally significant beats that continue directly into the next line receive moderate scores rather than perfect scores.
- Scores are rounded to whole numbers for JSON readability.