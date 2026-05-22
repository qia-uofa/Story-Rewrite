env_block = """
```env
TARGET=Re-Parts
ALIAS=main
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)

import re
import os
from pathlib import Path

for file in Path('./Re-SoP/repo').iterdir():
    match = re.match(r'resop-([0-9]+)\.txt', file.name)
    if match:
        n = match.group(1)
        if not(int(n) in [3,4]):
            continue
        with open(f'Re-Parts/repo/part-{n}.txt') as f:
            content = f.read()
        chars = len(content)
        lines = len(content.split('\n'))
        os.system(f'n={n} CHARS={chars} LINES={lines} lips build rewrite-n Re-SoP')