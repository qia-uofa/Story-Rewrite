env_block = """
```env
TARGET=SOP
```
"""

import os
import sys
from pathlib import Path
from lips.utils.parse_build_files import env_from_build_file

_, env = env_from_build_file(env_block)

split_repo = Path("Split/repo")   # SOURCE — parts live here; we also stage temp files here

# ── Collect parts ────────────────────────────────────────────────────────────
parts = sorted(
    p for p in split_repo.iterdir()
    if p.name.startswith("part_") and p.suffix == ".txt"
)

if not parts:
    print("[summarize] ERROR: No part_NNN.txt files found in Split/repo/")
    print("           Run 'lips build split.md Input' first.")
    sys.exit(1)

print(f"[summarize] {len(parts)} parts found — summarising sequentially.")

for i, part_path in enumerate(parts):
    num = f"{i:03d}"
    print(f"\n[summarize] Part {num}  ({part_path.name}) ...")

    # Stage current part and its index into the source repo so the LLM can read them
    (split_repo / "_current_part.txt").write_text(
        part_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (split_repo / "_current_num.txt").write_text(num, encoding="utf-8")

    ret = os.system("lips build summarize-part Split")
    if ret != 0:
        print(f"[summarize] ERROR: failed on part {num} (exit {ret})")
        sys.exit(ret)

    print(f"[summarize] ✓  SOP/repo/{num}.md")

# ── Cleanup temp files from source repo ─────────────────────────────────────
for tmp in ("_current_part.txt", "_current_num.txt"):
    p = split_repo / tmp
    if p.exists():
        p.unlink()

print(f"\n[summarize] Done — {len(parts)} summaries written to SOP/repo/")
