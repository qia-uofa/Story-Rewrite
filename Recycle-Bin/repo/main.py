env_block = """
```env
TARGET=Timestamps
N=50
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)


i = 0
N = int(env['N'])

import re, json


with open(f'Input/repo/story.txt', 'r', encoding='utf-8') as f:
    content = f.read().split('\n')

l = len(content)
count = 1
while (i < l):
    n = min(i + N, l)
    window = content[i:n]
    
    with open(f'Input/repo/context.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(window))

    os.system(f'lips build split Input')
    
    with open(f'Timestamps/repo/output.txt', 'r', encoding='utf-8') as f:
        d = int(f.read())
        
    with open(f'Input/repo/part-{count}.txt', 'w', encoding='utf-8') as f:
         f.write('\n'.join(window[:d]))
    count += 1
    i += d
    
    
    
    
    
    
    
    