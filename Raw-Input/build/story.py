env_block = """
```env
TARGET=Story
N=1000
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)

import re
N = int(env['N'])

with open(f'Raw-Input/repo/story.txt', 'r', encoding='utf-8') as f:
    content = f.read().split('\n\n')
    content = list(map(lambda line: re.sub('\n',' ',line) , content))

with open(f'Input/repo/story.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(content[:N]))

os.system(f'lips build {env["TARGET"]}')