<file path="./.thought/output.txt.md">
## Goal
Determine the largest `n` such that the text from line 1 through line `n` forms a meaningful, complete narrative paragraph starting at the first line.

## Reasoning
The first line is a complete narrative paragraph about the Dursleys' secret and their fear of the Potters being discovered. It is self-contained, coherent, and ends at a newline without cutting off a sentence or thought.

The second line begins a new paragraph with a new scene-setting transition: "When Mr. and Mrs. Dursley woke up..." Including it would start another paragraph rather than extending the first one.

Therefore, the largest valid `n` is 1.
</file>

<file path="./output.txt">
1</file>