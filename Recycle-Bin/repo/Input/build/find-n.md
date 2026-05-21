```env
TARGET=Input
```
```sourceignore
out
.thought
story
```
```targetignore
*
```

You are given a snippet of text from a novel. Your task is to sample candidate pause points, score them, and write the scores to `./<env:OUTPATH>`.

A natural pause point is a line where the reader could naturally stop and reflect — a moment of rest, transition, or shift in scene, tone, or focus.

Scoring system (0 to 100):
- p_close(i): how much does line i feel like the end of a unit?
    100 — scene ends, emotional beat resolves, character exits, chapter-like finality
     75 — strong closing tone, trailing silence, a held breath
     50 — soft stop, paragraph ends but narrative thread continues
     25 — mid-action, mid-dialogue, mid-description
      0 — sentence is incomplete or cuts off abruptly
- p_open(i+1): how much does line i+1 feel like the start of a unit?
    100 — new scene, new character, time jump, location change, fresh narrative thread
     75 — tonal shift, new paragraph with new focus
     50 — continuation with slight reorientation
     25 — direct continuation of prior sentence or action
      0 — mid-sentence or dependent clause
- score(i) = p_close(i) × p_open(i+1) / 100

Strategy — follow these steps in order:

Step 1 — Sample candidates:
  Read through the text and identify exactly <env:k> candidate pause points spread across the text.

Step 2 — Score each candidate:
  For each candidate i, compute p_close(i) and p_open(i+1) using the scoring system above, then compute score(i).

Step 3 — Write output:
  Write the scores as a JSON file to ./<env:OUTPATH> in this exact format:
    {
        "<line_index>": <score>,
        "<line_index>": <score>,
        ...
    }
  where keys are line indices as strings and values are scores from 0 to 100.
  Do not include any explanation or extra text in the file, only valid JSON.