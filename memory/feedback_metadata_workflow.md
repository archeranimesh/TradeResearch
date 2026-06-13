---
name: feedback_metadata_workflow
description: User runs fetch_metadata.py locally and pastes the JSON output at the start of analysis sessions
metadata:
  type: feedback
---

User runs `python3 scripts/fetch_metadata.py <video_id>` locally (sandbox has no internet) and pastes the resulting JSON before asking for transcript analysis. Wait for that metadata JSON before writing the finding — do not infer channel name from transcript content.

**Why:** The sandbox cannot reach youtube.com (403 Forbidden). The transcript header contains the title but not the channel name, which can be wrong if guessed.

**How to apply:** At the start of any transcript processing session, if metadata JSON hasn't been provided yet, remind the user to run the script and paste the output before proceeding to write `findings/<video_id>.md`.
