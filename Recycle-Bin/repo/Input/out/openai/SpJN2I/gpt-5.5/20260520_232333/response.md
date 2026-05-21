<file path="./.thought/output.txt.md">
## Goal
Determine the line number `n` where the text prefix from line 1 through `n` forms a meaningful, complete unit without cutting off a sentence or thought.

## Reasoning
The first three lines are title/chapter heading lines. The first actual narrative paragraph is line 4, beginning with “Mr. and Mrs. Dursley...” and ending as a complete sentence. Including lines 1 through 4 gives the title, chapter heading, section heading, and a complete opening narrative paragraph.

## Decision
Use `n = 4`.
</file>
<file path="./output.txt">4</file>