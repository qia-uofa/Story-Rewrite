env_block = """
```env
TARGET=Output
CONTEXT_WINDOW=3
```
"""

import os
import sys
from pathlib import Path
from lips.utils.parse_build_files import env_from_build_file

_, env = env_from_build_file(env_block)

CONTEXT_WINDOW   = int(env.get("CONTEXT_WINDOW", "3"))
rewrite_sop_repo = Path("Rewrite-SOP/repo") # SOURCE — rewritten summaries + temp staging
split_repo       = Path("Split/repo")        # cross-stage — original parts for style reference
output_repo      = Path("Output/repo")       # cross-stage — read constructed sections for context

# ── Collect rewritten summaries ──────────────────────────────────────────────
rewritten_summaries = sorted(
    p for p in rewrite_sop_repo.iterdir()
    if p.name[0].isdigit() and p.suffix == ".md"
)
original_parts = sorted(
    p for p in split_repo.iterdir()
    if p.name.startswith("part_") and p.suffix == ".txt"
)

if not rewritten_summaries:
    print("[construct] ERROR: No rewritten summaries in Rewrite-SOP/repo/")
    print("            Run 'lips build rewrite.py SOP' first.")
    sys.exit(1)

print(f"[construct] {len(rewritten_summaries)} sections to construct (context window: {CONTEXT_WINDOW}).\n")

constructed = []  # completed section paths, for rolling context

for i, summary_path in enumerate(rewritten_summaries):
    num = f"{i:03d}"
    orig_path = original_parts[i] if i < len(original_parts) else None
    print(f"[construct] Section {num} ...")

    # Stage inputs into the source repo (Rewrite-SOP/repo/)
    (rewrite_sop_repo / "_current_summary.md").write_text(
        summary_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    orig_text = orig_path.read_text(encoding="utf-8") if orig_path else ""
    (rewrite_sop_repo / "_current_original.txt").write_text(orig_text, encoding="utf-8")
    (rewrite_sop_repo / "_current_num.txt").write_text(num, encoding="utf-8")

    # Build rolling context from last CONTEXT_WINDOW constructed sections
    context_sections = []
    for prev in constructed[-CONTEXT_WINDOW:]:
        context_sections.append(
            f"## Previous Section {prev.stem}\n\n"
            + prev.read_text(encoding="utf-8")
        )
    context_text = (
        "\n\n---\n\n".join(context_sections)
        if context_sections
        else "(No previous sections yet — this is the opening of the story.)"
    )
    (rewrite_sop_repo / "_context.md").write_text(context_text, encoding="utf-8")

    ret = os.system("lips build construct-part Rewrite-SOP")
    if ret != 0:
        print(f"[construct] ERROR: failed on section {num} (exit {ret})")
        sys.exit(ret)

    out = output_repo / f"{num}.txt"
    if out.exists():
        constructed.append(out)
        print(f"[construct] ✓  Output/repo/{num}.txt")
    else:
        print(f"[construct] WARNING: {num}.txt was not produced.")

# ── Cleanup temp files from source repo ─────────────────────────────────────
for tmp in ("_current_summary.md", "_current_original.txt", "_current_num.txt", "_context.md"):
    p = rewrite_sop_repo / tmp
    if p.exists():
        p.unlink()

# ── Assemble final story ─────────────────────────────────────────────────────
print("\n[construct] Assembling final story ...")
section_files = sorted(
    p for p in output_repo.iterdir()
    if p.name[0].isdigit() and p.suffix == ".txt"
)
sections = [p.read_text(encoding="utf-8") for p in section_files]
final    = "\n\n---\n\n".join(sections)
(output_repo / "story.txt").write_text(final, encoding="utf-8")

print(f"[construct] Done — {len(sections)} sections, {len(final):,} characters.")
print(f"            Output: Output/repo/story.txt")
