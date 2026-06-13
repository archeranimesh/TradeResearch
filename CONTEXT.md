# TradeResearch — Project Context

## Purpose

Analyze YouTube video transcripts to extract trading insights useful for:
- Strategy development (entry/exit rules, filters)
- Performance metrics and measurement techniques
- Risk management ideas
- Trading journal / process / psychology prompts

Secondary purpose: identify and queue anything relevant to the NiftyShield options trading system.

---

## What Exists

```
TradeResearch/
├── CLAUDE.md                    # AI assistant instructions
├── CONTEXT.md                   # this file
├── NIFTYSHIELD_PROFILE.md       # NiftyShield context for relevance assessment
├── pending_niftyshield.md       # cross-project review queue
├── transcripts/                 # raw .txt transcripts (bookmarklet output, <video_id>.txt)
├── findings/                    # structured analysis output, one .md per video
├── knowledge_base/
│   ├── strategies.md            # curated evergreen strategy cards
│   ├── metrics.md               # curated performance metrics and ratios
│   └── journal_prompts.md       # process and psychology observations
└── scripts/
    └── fetch_metadata.py        # fetch video title + channel via YouTube oEmbed API
```

---

## Finding Format (canonical schema)

Every file in `findings/` must follow this exact format:

```markdown
---
video_id: <id>
title: "Video Title"
channel: Channel Name
url: https://www.youtube.com/watch?v=<id>
analyzed: YYYY-MM-DD
niftyshield_relevant: true | false
---

## Summary
2-3 sentences covering what the video is about and its primary trading focus.

## Strategies
- **[Name]:** entry condition / exit condition / filter (quote source if verbatim)

## Metrics & Ratios
- Any measurement technique, ratio, or performance metric mentioned

## Risk Management
- Position sizing rules, stop logic, adjustment triggers

## Journal / Process
- Psychological observations, process habits, mindset frameworks

## NiftyShield Signal
**Relevant:** Yes / No
**Why:** Specific reason tied to NIFTYSHIELD_PROFILE.md (or "N/A")
**Action suggested:** What to do with this finding (or "N/A")
```

---

## Pending NiftyShield Queue Format

Each entry in `pending_niftyshield.md`:

```markdown
## YYYY-MM-DD | [Video Title] — [Channel]
**Signal:** One-line description of the relevant insight
**Finding:** findings/<video_id>.md
**Action:** [ ] What needs to happen next
```

---

## Session Log

| Date | Activity |
|---|---|
| 2026-06-13 | Project initialized |
