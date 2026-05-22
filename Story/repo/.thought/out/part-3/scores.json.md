## Goal
Create `./out/part-3/scores.json` containing exactly 20 sampled natural pause-point scores.

## Approach
I treated line indices as zero-based and chose candidates spread across the snippet, including chapter/title transitions, time jumps, scene shifts, and softer reflective pauses. For each candidate, I estimated how strongly the current line closes a unit and how strongly the next line opens a new unit, then used `score = p_close * p_open / 100`.

## Notes
Stronger scores are assigned to chapter boundaries and major scene resets. Medium scores are assigned to time/location shifts or reflective beats. Lower scores are used for softer paragraph-level pauses where the same narrative thread continues.