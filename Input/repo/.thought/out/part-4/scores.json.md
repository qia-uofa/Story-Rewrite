## Goal
Create `./out/part-4/scores.json` containing exactly 20 sampled candidate pause points from the provided novel excerpt.

## Approach
I treated line indices as 1-based physical lines in the printed `window.txt` excerpt. I selected pause points that are spread across the snippet and favor transitions such as chapter/title boundaries, completed actions, scene shifts, arrivals/departures, and changes in conversational focus.

## Scoring
For each selected line `i`, I estimated:
- `p_close(i)` based on how much the line feels like an ending or resting point.
- `p_open(i+1)` based on how much the following line feels like a new start.
- `score = p_close * p_open / 100`.

Strong chapter/scene boundaries received the highest scores, while softer paragraph or conversational transitions received moderate scores.