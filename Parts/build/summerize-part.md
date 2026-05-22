```env
TARGET=SoP
```
```sourceignore
*
!<env:FILE>
```
```targetignore
*
```

Read the content of <env:FILE> and summerize it. 

Write the output at './<env:OUT>'.