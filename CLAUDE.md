# TradeResearch — AI Assistant Instructions

> Auto-loaded at session start. Every step is mandatory.

---

## Purpose

This project analyzes YouTube video transcripts to extract trading insights, strategies, metrics,
and journal prompts. When a finding is relevant to the NiftyShield trading system, it is flagged
and queued for cross-project review.

---

## Pre-Task Protocol

### Step 1 — Read context files first

Before analyzing any transcript, read:
- `CONTEXT.md` — current project state
- `NIFTYSHIELD_PROFILE.md` — what NiftyShield needs (required to assess relevance)

State `CONTEXT.md ✓` and `NIFTYSHIELD_PROFILE.md ✓` in your first response.

### Step 2 — Identify the transcript

Transcripts are in `transcripts/` as `<video_id>.txt` (e.g., `2175knd26Yw.txt`).
Before analyzing, fetch video metadata using `scripts/fetch_metadata.py <video_id>` to get
the title and channel name. If metadata fetch fails, proceed with video ID as title.

### Step 3 — Analyze and produce finding

Output a finding file at `findings/<video_id>.md` using the exact format defined in
`CONTEXT.md`. Do not deviate from the schema — downstream tooling depends on it.

### Step 4 — Cross-project queue

If `niftyshield_relevant: true`, append a one-liner to `pending_niftyshield.md` immediately
after writing the finding. Never skip this step.

### Step 5 — Update knowledge base (when warranted)

If a finding contains a strategy, metric, or journal prompt that is evergreen (not
video-specific), add it to the appropriate file in `knowledge_base/`. This is judgment-driven —
not every finding warrants a knowledge base entry.

---

## Rules

- **Never modify** `NIFTYSHIELD_PROFILE.md` during analysis. Update it only when explicitly asked.
- **Never write** to NiftyShield's folder directly. The bridge is `pending_niftyshield.md` only.
- **Always use** the structured finding format. Freeform prose findings are not acceptable.
- **Transcripts are read-only.** Never edit or delete files in `transcripts/`.
- If a transcript is too long for a single pass, chunk it and synthesize findings at the end.

---

## File Map

| File | Purpose |
|---|---|
| `CONTEXT.md` | Project state, finding format spec |
| `NIFTYSHIELD_PROFILE.md` | NiftyShield context — what to flag as relevant |
| `pending_niftyshield.md` | Cross-project queue for manual review |
| `transcripts/<id>.txt` | Raw transcript input from bookmarklet |
| `findings/<id>.md` | Structured analysis output per video |
| `knowledge_base/strategies.md` | Curated strategy cards |
| `knowledge_base/metrics.md` | Curated performance metrics |
| `knowledge_base/journal_prompts.md` | Process and psychology observations |
| `scripts/fetch_metadata.py` | Fetch video title + channel from video ID |
