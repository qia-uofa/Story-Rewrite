env_block = """
```env
TARGET=Re-SoP
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)

from pathlib import Path
sop = ''
files = [file for file in sorted(Path('./SoP/repo').iterdir()) if file.is_file]
for i,file in enumerate(files):
    if file.is_file():
        print(file)
        with open(file, 'r', encoding='utf-8') as f:
            sop += f'## Part {i}\n\n{f.read()}\n\n'
with open('./Re-SoP/repo/resop.txt', 'w', encoding='utf-8') as f:
    f.write(sop)