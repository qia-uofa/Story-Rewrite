```env
TARGET=Re-Parts
```
```sourceignore
*
!resop-*.txt
!relore.md
```
```targetignore
*
!part-<env:n>.txt
```

You are presented the <env:n>-th part of a story in `part-<env:n>.txt`. 

You are presented the rewritten summary of parts (ReSoP) `resop-*.txt`. 

You are presented the rewritten lore-book `relore.md`. 



Your task is to rewrite the <env:n>-th part of the story `part-<env:n>.txt` as a re-construction from `resop-<env:n>.txt`. Take other ReSoP as contexts to make the story consistant. 


The temperature determines how much you are allowed to diverge from the original sentence structure. 0 means you must keep all the sentences the same and only change necessary parts. 10 means you don't have to preserve any sentence structure. 

The temperature for this task is <env:TEMP>.

The length of the text you are supposed to produce is <env:CHARS> characters.

The number of lines you are supposed to produce is <env:LINES>.

Write your output at `./repart-<env:n>.txt`