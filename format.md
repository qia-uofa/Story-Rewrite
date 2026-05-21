## Output Format Rules

1. **Every output must be a file**, enclosed in `<file path="...">...</file>` tags.
   - No raw text, explanations, or code outside of file tags.
   - All paths must start with `./`

2. **Before writing any file, think out loud first** by writing a corresponding thought file:
   - Thought file path: `./.thought/<original/path/file.ext.md>`
   - Example: before `./src/app.py`, write `./.thought/src/app.py.md`
   - The thought file should contain your reasoning: what the file needs to do, design decisions, potential pitfalls, and your approach.

3. **File ordering**: thought file always comes immediately before its corresponding output file.

## Example Output Structure

<file path="./.thought/src/utils.ts.md">
## Goal
Create a utility module for string manipulation.

## Design Decisions
- Export named functions, not a class, for tree-shaking friendliness
- Use TypeScript generics for the pad function to stay flexible

## Potential Pitfalls
- Edge case: empty string input should return empty string, not throw
</file>

<file path="./src/utils.ts">
export function capitalize(s: string): string {
  if (!s) return s;
  return s.charAt(0).toUpperCase() + s.slice(1);
}
</file>

## Strict Rules
- Never output anything outside `<file ...>` tags
- Every non-thought file must have a preceding thought file
- Thought files are Markdown; content files use the appropriate language for their extension
- Paths are relative, always starting with `./`