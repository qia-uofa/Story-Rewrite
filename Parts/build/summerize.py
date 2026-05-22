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


from pathlib import Path
for file in Path('./Parts/repo').iterdir():
    os.system(f'FILE={file.name} lips build summerize-part Parts')