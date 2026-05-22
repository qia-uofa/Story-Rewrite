env_block = """
```env
TARGET=SoP
ALIAS=main
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)

import re
from pathlib import Path
for file in Path('./Parts/repo').iterdir():
    match = re.match(r'part-[0-9]+\.txt', file.name)
    if match:
        os.system(f'FILE={file.name} OUT={re.sub('part','sop',file.name)} lips build summerize-part Parts')