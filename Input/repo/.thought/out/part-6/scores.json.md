## Goal
Create `./out/part-6/scores.json` containing exactly 20 sampled pause-point scores for the provided novel excerpt.

## Approach
- Treat line indices as 1-based, matching the natural reading of “line i” and “line i+1.”
- Select candidate pause points spread across the excerpt, favoring places where dialogue turns, characters enter or exit, topics shift, or narration transitions.
- Score each candidate using `score(i) = p_close(i) × p_open(i+1) / 100`.

## Candidate Scoring Notes
- Line 1 closes the opening window-reflection beat before the compartment action starts.
- Lines 10, 20, 30, 37, 48, 57, 64, 68, 69, 75, and 97 are relatively strong pauses because they mark exits, completed exchanges, topic shifts, or quiet transitions.
- Lines 24, 41, 53, 78, 81, 89, and 90 are softer pauses where the scene continues but the focus changes.
- Line 4 is a moderate pause before the twins re-enter the exchange.

## Potential Pitfalls
- Avoid selecting the final line because there is no following line for `p_open(i+1)`.
- Avoid incomplete-sentence cuts as high-value pauses.
- Keep exactly 20 JSON entries.