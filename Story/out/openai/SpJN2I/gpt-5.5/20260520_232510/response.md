<file path="./.thought/output.txt.md">
## Goal
Find the largest line number `n` such that the prefix from line 1 through line `n` forms a meaningful, complete narrative paragraph and does not cut off a sentence or thought.

## Reasoning
The text begins with the book title, chapter label, and chapter title on lines 1–3. Line 4 is the first actual narrative paragraph, and it is self-contained: it introduces the Dursleys and ends with a complete sentence. Including line 5 would start a new paragraph, so the prefix would no longer be a single narrative paragraph unit.

## Decision
Use `n = 4`.
</file>
<file path="./output.txt">
4
</file>