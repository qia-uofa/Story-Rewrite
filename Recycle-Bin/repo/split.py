env_block = """
```env
TARGET=Split
N=10000
```
"""
import os
import time
import sys
from lips.utils.parse_build_files import env_from_build_file
_, env = env_from_build_file(env_block)

