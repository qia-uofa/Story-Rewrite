```env
TARGET=Timestamps
```

```sourceignore
story.txt
ans.json
```
```targetignore
*
```
You are given a snippet of text from a novel. Your task is to find a line number `n` and write it to `./output.txt`.

Rules:
- Split the text into lines (by newline character)
- Find `n` such that lines 1 through n represent a natural pause point in the narrative
- A natural pause point is where:
  - The story reaches a moment of rest, transition, or shift in scene/tone/focus
  - The reader could naturally stop and reflect
- Write only the integer `n` to `./output.txt`, nothing else