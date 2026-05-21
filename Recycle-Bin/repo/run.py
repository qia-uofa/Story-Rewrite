env_block = """
```env
TARGET=Input
```
"""

import os
import sys
from lips.utils.parse_build_files import env_from_build_file

_, env = env_from_build_file(env_block)

# ── Pipeline steps: (build-script, stage-path) ──────────────────────────────
STEPS = [
    # (build-script,      source-stage)     arrow → TARGET inside each build file
    ("split.md",          "Input"),          # Input        → Split
    ("summarize.py",      "Split"),          # Split        → SOP
    ("compress.md",       "SOP"),            # SOP          → SOS
    ("lorebook.md",       "SOP"),            # SOP          → Lorebook
    ("rewrite.md",        "SOS"),            # SOS          → Rewrite-Summary
    ("rewrite.md",        "Lorebook"),       # Lorebook     → Rewrite-Lorebook
    ("rewrite.py",        "SOP"),            # SOP          → Rewrite-SOP
    ("construct.py",      "Rewrite-SOP"),    # Rewrite-SOP  → Output
]

BAR = "=" * 62

def run(script, stage):
    cmd = f"lips build {script} {stage}"
    print(f"\n{BAR}")
    print(f"  {cmd}")
    print(BAR)
    return os.system(cmd)


print(f"\n{BAR}")
print("  Story-Rewrite Pipeline — starting")
print(BAR)

for script, stage in STEPS:
    code = run(script, stage)
    if code != 0:
        print(f"\n[ERROR] '{script}' on '{stage}' failed (exit {code}).")
        sys.exit(code)

print(f"\n{BAR}")
print("  Pipeline complete!")
print("  Find your story in:  Output/repo/story.txt")
print(BAR + "\n")
