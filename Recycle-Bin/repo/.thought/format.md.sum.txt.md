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