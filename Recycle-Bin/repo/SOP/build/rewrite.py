env_block = """
```env
TARGET=Rewrite-SOP
CONTEXT_WINDOW=3
```
"""

import os
import sys
from pathlib import Path
from lips.utils.parse_build_files import env_from_build_file

_, env = env_from_build_file(env_block)

CONTEXT_WINDOW   = int(env.get("CONTEXT_WINDOW", "3"))
sop_repo         = Path("SOP/repo")         # SOURCE — summaries live here; stage temp files here too
rewrite_sop_repo = Path("Rewrite-SOP/repo") # TARGET — completed rewrites land here (for context)

# ── Collect original summaries ───────────────────────────────────────────────
summaries = sorted(
    p for p in sop_repo.iterdir()
    if p.name[0].isdigit() and p.suffix == ".md"
)

if not summaries:
    print("[rewrite-sop] ERROR: No summary files in SOP/repo/")
    print("              Run 'lips build summarize.py Split' first.")
    sys.exit(1)

print(f"[rewrite-sop] Rewriting {len(summaries)} summaries (context window: {CONTEXT_WINDOW}).\n")

rewritten = []  # completed rewrite paths, for rolling context

for i, summary_path in enumerate(summaries):
    num = f"{i:03d}"
    print(f"[rewrite-sop] {num}.md ...")

    # Stage current summary and index into source repo
    (sop_repo / "_current_summary.md").write_text(
        summary_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (sop_repo / "_current_num.txt").write_text(num, encoding="utf-8")

    # Build rolling context from the last CONTEXT_WINDOW completed rewrites
    context_sections = []
    for prev in rewritten[-CONTEXT_WINDOW:]:
        context_sections.append(
            f"## Rewritten Summary {prev.stem}\n\n"
            + prev.read_text(encoding="utf-8")
        )
    context_text = (
        "\n\n---\n\n".join(context_sections)
        if context_sections
        else "(No previous rewritten summaries yet — this is the first.)"
    )
    (sop_repo / "_context.md").write_text(context_text, encoding="utf-8")

    ret = os.system("lips build rewrite-part SOP")
    if ret != 0:
        print(f"[rewrite-sop] ERROR: failed on {num} (exit {ret})")
        sys.exit(ret)

    out = rewrite_sop_repo / f"{num}.md"
    if out.exists():
        rewritten.append(out)
        print(f"[rewrite-sop] ✓  Rewrite-SOP/repo/{num}.md")
    else:
        print(f"[rewrite-sop] WARNING: {num}.md was not produced.")

# ── Cleanup temp files from source repo ─────────────────────────────────────
for tmp in ("_current_summary.md", "_current_num.txt", "_context.md"):
    p = sop_repo / tmp
    if p.exists():
        p.unlink()

print(f"\n[rewrite-sop] Done — {len(rewritten)}/{len(summaries)} summaries rewritten.")
