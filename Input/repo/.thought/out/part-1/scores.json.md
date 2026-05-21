## Goal
Create `./out/part-1/scores.json` containing exactly 20 sampled candidate pause points from the provided novel excerpt, with each candidate scored according to `p_close(i) * p_open(i+1) / 100`.

## Approach
I treated the excerpt as a sequence of lines and selected pause points distributed across the visible text, favoring chapter boundaries, scene transitions, emotional beats, and moments where the next line begins a fresh unit. Strong chapter endings and new chapter openings receive the highest scores; softer paragraph or tonal transitions receive moderate scores.

## Design Decisions
- Use line indices as JSON string keys.
- Use integer scores for clarity.
- Include exactly 20 candidate pause points.
- Prioritize spread across Chapters One through Five rather than clustering around only chapter breaks.

## Potential Pitfalls
- Line indexing depends on the exact source line segmentation; I used the line breaks as presented in the printed repository content.
- Some candidates are softer pauses rather than full scene breaks, so their scores are intentionally lower than chapter transitions.