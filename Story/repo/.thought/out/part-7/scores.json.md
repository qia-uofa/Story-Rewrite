## Goal
Write pause-point scores for part 7 to `./out/part-7/scores.json`.

## Approach
The provided excerpt is short, so I treated each sentence or natural clause-level unit as a line-like scoring unit in order to produce exactly 20 candidate pause points spread across the snippet. I scored pauses between consecutive units, using higher scores for exits, shifts in speaker/focus, and completed emotional beats, and lower scores for intra-sentence continuations or dependent clauses.

## Potential Pitfalls
- The source excerpt as printed has fewer physical newline-separated lines than the required 20 candidates, so the indices here correspond to sequential natural reading units rather than the visible wrapped lines.
- Pauses inside Hermione’s long dialogue are mostly weak because they continue the same speaker and thought.