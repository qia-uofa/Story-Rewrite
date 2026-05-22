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

import re
from pathlib import Path
for file in Path('./SoP/repo').iterdir():
    match = re.match(r'sop-[0-9]+\.txt', file.name)
    if match:
        os.system(f'cp SoP/repo/{file.name} Re-SoP/repo/{file.name}')