```env
TARGET=Re-SoP
ALIAS=main
```
```sourceignore
*
!relore.md
```
```targetignore
*
!sop-*.txt
```

`re-lore.md` is the rewritten lore-book of the original story.

`sop-*.txt` are summary of parts of the original story. 

Your task is to produce a `resop-*.txt` for each `sop-*.txt`. 

The content of each output file should be the rewritten SoP of its original SoP, based of the rewritten lore-book `re-lore.md`.