## Goal
Create `./out/part-5/scores.json` containing exactly 20 sampled candidate pause points from the provided novel excerpt.

## Approach
- Treat line indices as zero-based, matching typical text-processing conventions.
- Select candidates spread across the excerpt rather than clustered in one scene.
- Favor paragraph endings, scene transitions, character entrances/exits, shifts in topic, and reflective beats.
- Compute each score as `p_close(i) × p_open(i+1) / 100`.

## Notes
The chosen points include chapter-opening transition, the move from the Dursleys to King's Cross, entrance to Platform Nine and Three-Quarters, the train departure, Ron and Harry's first conversation, the food-cart scene, the Chocolate Frog/card sequence, Neville and Hermione's entrance, and Hermione's exit.