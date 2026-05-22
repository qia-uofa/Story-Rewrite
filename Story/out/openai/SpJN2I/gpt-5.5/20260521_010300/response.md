<file path="./.thought/out/part-2/n.txt.md">
## Goal
Find a natural pause point in the provided narrative and write the corresponding line number to `./out/part-2/n.txt`.

## Approach
I split the text by newline and looked for a point where the narrative reaches rest or transition. The strongest natural pause is the end of Chapter One, immediately before the `CHAPTER TWO` heading begins.

## Decision
Line 109 is the final paragraph of Chapter One, closing the scene with Harry asleep on the doorstep and people toasting him. Line 110 starts Chapter Two, so line 109 is the best stopping point.
</file>

<file path="./out/part-2/n.txt">109</file>