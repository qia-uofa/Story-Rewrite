<file path="./.thought/format.md.sum.txt.md">
## Goal
Summarize the contents of `format.md` into a concise text file.

## Design Decisions
- Capture the core requirements: all outputs must be files, thought files must precede content files, path rules, and ordering constraints.
- Keep the summary short and clear.
- Use plain text because the target file extension is `.txt`.

## Potential Pitfalls
- Avoid adding content outside file tags.
- Ensure the thought file immediately precedes the requested output file.
- Use paths starting with `./`.
</file>

<file path="./format.md.sum.txt">
format.md defines strict output formatting rules. Every response must consist only of file blocks using <file path="...">...</file> tags, with all paths starting with ./.

Before writing any non-thought file, a corresponding Markdown thought file must be written under ./.thought/ using the original file path plus .md. The thought file should explain the goal, design decisions, pitfalls, and approach, and it must appear immediately before the file it describes.

The rules also require that no raw text appear outside file tags, thought files use Markdown, content files use the appropriate language for their extension, and every non-thought file must have a preceding thought file.
</file>