<file path="./.thought/prompt.md.md">
## Goal
Transform the original story-modification prompt into a prompt for modifying a lore-book instead of the story itself.

## Design Decisions
- Preserve all original intentions: replace characters with characters from *The Boys*, replace world-building with *Invincible*, and preserve the original plot-line.
- Adapt wording so the target artifact is a lore-book: entries, factions, locations, timelines, powers, relationships, terminology, and continuity notes.
- Add technical details to ensure the modified lore-book remains internally consistent, structured, and useful as a reference document.
- Avoid adding new creative directives that conflict with the original prompt.

## Potential Pitfalls
- The original phrase "charactors" is misspelled; correct it to "characters" while preserving meaning.
- A lore-book does not contain prose scenes in the same way as a story, so "preserve the plot-line" must be reframed as preserving the underlying chronology, causal chain, arcs, and event structure documented by the lore-book.
- Ensure replacement of world-building with *Invincible* does not erase plot continuity or relationships that are required to preserve the original storyline.
</file>

<file path="./prompt.md">
Modify the lore-book of the original story according to the following requirements:

- Replace the characters of the lore-book with characters from *The Boys*.
- Replace the world-building, setting logic, power structures, cosmology, institutions, factions, and genre assumptions of the lore-book with the world-building of *Invincible*.
- Preserve the plot-line of the original story as represented in the lore-book.

Technical requirements:

1. Treat the input as a lore-book, not as prose narrative.
   - Update character entries, faction entries, location entries, timeline entries, terminology, relationship notes, power-system notes, and continuity references.
   - Do not rewrite the story as scenes or chapters.
   - Maintain the lore-book’s reference-document function.

2. Character replacement:
   - Substitute original character roles, relationships, conflicts, and narrative functions with appropriate characters from *The Boys*.
   - Preserve each original role’s purpose in the plot-line, even when the replacement character’s personality, powers, affiliation, or moral alignment requires adjustment to fit.
   - Update aliases, biographies, motivations, powers, weaknesses, affiliations, and relationship mappings accordingly.
   - Ensure all character references are renamed and made consistent throughout the lore-book.

3. World-building replacement:
   - Rebuild the setting using the world-building framework of *Invincible*.
   - Update references to governments, superhero organizations, alien civilizations, cosmic threats, power scaling, technology, public superhero culture, media presence, and institutional structures so they align with *Invincible*.
   - Replace incompatible original setting details with *Invincible*-style equivalents while preserving their function in the plot-line.
   - Ensure the lore-book’s rules for powers, combat, public knowledge, secrecy, and large-scale threats are internally consistent.

4. Plot-line preservation:
   - Preserve the original story’s major events, chronology, causal structure, conflicts, revelations, betrayals, alliances, escalations, climaxes, and resolutions as documented in the lore-book.
   - Do not remove, reorder, or substantially alter core plot beats unless a technical adaptation is necessary to fit the new characters or *Invincible* world-building.
   - When adaptation is necessary, keep the same narrative function and consequence as the original plot beat.

5. Continuity and consistency:
   - Ensure every changed entry remains consistent with every other changed entry.
   - Update cross-references, timelines, terminology, group memberships, power descriptions, locations, and historical notes.
   - Remove or revise contradictions created by the character and world-building substitutions.
   - Preserve the lore-book’s original structure where possible, while improving clarity and technical precision.

6. Output expectations:
   - Produce a complete revised lore-book prompt/instruction set suitable for transforming the original lore-book.
   - Keep the transformed lore-book grounded in the preserved plot-line while fully reflecting *The Boys* characters and *Invincible* world-building.
</file>