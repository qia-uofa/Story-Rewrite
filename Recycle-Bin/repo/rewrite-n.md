```env
TARGET=Re-Parts
ALIAS=main
```
```sourceignore
*
!resop-*.txt
!part-<env:n>.txt
```
```targetignore
*
```

You are presented the <env:n>-th part of a story in `part-<env:n>.txt`. 

You are presented the rewritten summary of parts (ReSoP) `resop-*.txt`. 

Your task is to rewrite the <env:n>-th part of the story `part-<env:n>.txt` as a re-construction from `resop-<env:n>.txt`. Take other ReSoP as contexts to make the story consistant. 

 Write your output at `./repart-<env:n>.txt`