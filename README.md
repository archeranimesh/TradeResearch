# TradeResearch

A Cowork project for analyzing YouTube video transcripts to extract trading insights,
strategies, metrics, and journal prompts. Flags anything relevant to the NiftyShield
options trading system for cross-project review.

---

## How It Works

1. Your bookmarklet saves a YouTube transcript as `<video_id>.txt` into `transcripts/`
2. You open this project in Cowork and ask Claude to analyze the transcript
3. Claude produces a structured finding in `findings/<video_id>.md`
4. If relevant to NiftyShield, Claude appends an entry to `pending_niftyshield.md`
5. You periodically review `pending_niftyshield.md` and decide what to carry into NiftyShield

---

## Workflow

### Step 1 — Save the transcript

Your bookmarklet handles this. For a video at:
```
https://www.youtube.com/watch?v=2175knd26Yw
```
It saves the transcript as:
```
transcripts/2175knd26Yw.txt
```

### Step 2 — Fetch video metadata (optional but recommended)

Before asking Claude to analyze, get the video title and channel name:

```bash
python scripts/fetch_metadata.py 2175knd26Yw
```

Output:
```json
{
  "video_id": "2175knd26Yw",
  "title": "How I Trade Iron Condors",
  "channel": "OptionAlpha",
  "url": "https://www.youtube.com/watch?v=2175knd26Yw"
}
```

No dependencies — uses Python stdlib only. Requires internet access.

### Step 3 — Ask Claude to analyze

Open this project in Cowork and say:

> Analyze transcript `2175knd26Yw`

Claude will:
- Read `CONTEXT.md` and `NIFTYSHIELD_PROFILE.md`
- Read `transcripts/2175knd26Yw.txt`
- Fetch metadata if not already provided
- Write a structured finding to `findings/2175knd26Yw.md`
- Append to `pending_niftyshield.md` if relevant to NiftyShield

### Step 4 — Review the finding

```
findings/2175knd26Yw.md
```

The finding contains: summary, strategies, metrics, risk management notes, journal prompts,
and a NiftyShield Signal section explaining whether and why it is relevant.

---

## Cross-Project Flow (NiftyShield)

### How items are flagged

Every finding has a `niftyshield_relevant` field in its frontmatter. When `true`, Claude
appends an entry to `pending_niftyshield.md` in this format:

```markdown
## 2026-06-13 | How I Trade Iron Condors — OptionAlpha
**Signal:** IV rank entry filter — waits for IVR >40 before selling strangles
**Finding:** findings/2175knd26Yw.md
**Action:** [ ] evaluate against BankNifty historical IV data
```

### How to review the queue

Open `pending_niftyshield.md` periodically. For each unchecked item, decide:

| Decision | What to do |
|---|---|
| Worth backtesting | Add to NiftyShield's `BACKTEST_PLAN.md` or `TODOS.md` |
| Worth noting as a decision | Add to NiftyShield's `DECISIONS.md` |
| Interesting but not urgent | Leave checked, revisit later |
| Not applicable after reading | Mark `[x]` and add a one-line note why |

Mark the checkbox `[x]` once actioned so the queue stays clean.

### What to carry into NiftyShield

Never copy raw finding text directly. Synthesize:
- A strategy → goes into NiftyShield's `BACKTEST_PLAN.md` as a hypothesis to test
- A metric → goes into NiftyShield's `TODOS.md` as a measurement to implement
- A risk rule → goes into NiftyShield's `DECISIONS.md` after council review if significant
- A journal prompt → goes into NiftyShield's knowledge base or personal trading journal

### Updating the relevance profile

If NiftyShield's strategy focus shifts (new instruments, new adjustment rules, new expiry
structure), update `NIFTYSHIELD_PROFILE.md` in this project so future flagging stays accurate.

---

## Knowledge Base

When a finding contains something evergreen — not specific to one video — Claude adds it to:

| File | What goes here |
|---|---|
| `knowledge_base/strategies.md` | Reusable strategy cards with entry/exit/filter rules |
| `knowledge_base/metrics.md` | Performance metrics, ratios, measurement techniques |
| `knowledge_base/journal_prompts.md` | Psychology, process habits, reflection questions |

These files accumulate over time and become a personal trading knowledge base.

---

## File Reference

| File | Purpose |
|---|---|
| `CLAUDE.md` | AI instructions — do not edit unless changing protocol |
| `CONTEXT.md` | Project state and canonical finding format |
| `NIFTYSHIELD_PROFILE.md` | What NiftyShield needs — update when strategy shifts |
| `pending_niftyshield.md` | Cross-project queue — review periodically |
| `transcripts/<id>.txt` | Raw transcript input — read-only |
| `findings/<id>.md` | Structured analysis output per video |
| `scripts/fetch_metadata.py` | Fetch title + channel for a video ID |

---

## Notes

- `transcripts/` is gitignored — transcripts stay local only
- No external dependencies — `fetch_metadata.py` uses Python stdlib
- The only file you write to in NiftyShield is its `TODOS.md`, `BACKTEST_PLAN.md`, or `DECISIONS.md` — never write directly to NiftyShield from this project
