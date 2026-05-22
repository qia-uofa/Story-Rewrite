env_block = """
```env
TARGET=Parts
ALIAS=main
N=500
k=20
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)


i = 0
N = int(env['N'])
k = int(env['k'])

import re
import json
import math
import random
from pathlib import Path

with open(f'Input/repo/story.txt', 'r', encoding='utf-8') as f:
    content = f.read().split('\n')

l = len(content)
count = 1
while (i < l):
    n = min(i + N, l)
    window = content[i:n]
    
    root = Path('Input/repo/')
    out = Path(f'./out/part-{count}')
    
    (root/out).mkdir(parents=True, exist_ok=True)

    
    with open(root/out/'window.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(window))
    with open(root/'window.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(window))
		
    os.system(f'OUTPATH={out/"scores.json"} N={N} k={k} lips build find-n Input')
    

    with open(root/out/'scores.json', 'r', encoding='utf-8') as f:
        scores = json.load(f)

    # Step 1 — likelihood via softmax
    vals = list(scores.values())
    exp_vals = [math.exp(v) for v in vals]
    Z_soft = sum(exp_vals)
    likelihood = {k: math.exp(v) / Z_soft for k, v in scores.items()}

    # Step 2 — Gaussian prior centered at middle of window
    mean = N / 2
    std = N / 4
    def gaussian(i):
        return math.exp(-0.5 * ((i - mean) / std) ** 2)

    prior = {k: gaussian(int(k)) for k in scores}

    # Step 3 — unnormalized posterior
    unnorm = {k: likelihood[k] * prior[k] for k in scores}

    # Step 4 — normalize posterior
    Z = sum(unnorm.values())
    posterior = {k: v / Z for k, v in unnorm.items()}

    # Step 5 — sample from posterior distribution
    keys = list(posterior.keys())
    probs = [posterior[k] for k in keys]
    d = int(random.choices(keys, weights=probs, k=1)[0])
    
    with open(f'Parts/repo/part-{count}.txt', 'w', encoding='utf-8') as f:
         f.write('\n'.join(window[:d]))
    count += 1
    i += d
    time.sleep(2)