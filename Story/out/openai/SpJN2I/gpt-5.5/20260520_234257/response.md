<file path="./.thought/output.txt.md">
## Goal
Determine the largest `n` such that the text from line 1 through line `n` forms one meaningful, complete narrative paragraph.

## Reasoning
The first line is a complete, coherent paragraph introducing the Dursleys on the morning the story begins. It ends cleanly at a newline and does not cut off mid-sentence or mid-thought.

Line 2 begins a separate paragraph about the owl passing the window, so including it would no longer make lines 1 through `n` a single narrative paragraph. Therefore the largest valid `n` is 1.
</file>

<file path="./output.txt">
1</file>