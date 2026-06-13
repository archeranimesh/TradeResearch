# Knowledge Base — Journal & Process Prompts

Curated trading psychology, process habits, and journal prompts from transcript analysis.
Link back to the source finding for full context.

---

<!-- Entries added here when a prompt warrants permanent curation -->

---
tags: [process, psychology, risk-management, options-selling]
source: findings/8MJkZQSiY_E.md
added: 2026-06-13
---

## Pre-Trade Decision Protocol — No In-Trade Decisions

**Source:** [findings/8MJkZQSiY_E.md](../findings/8MJkZQSiY_E.md)

"Decisions have to be made pre-trade, not while the trade is running and definitely not when it is going against you."

Before entering any position, write down:
1. Entry conditions (why this trade, why now)
2. Max loss (2x credit for premium selling)
3. Exit condition if wrong (stop trigger, no exceptions)
4. What "winning" looks like (close at X% profit, or hold to expiry)

Once the trade is live, the only permitted action is executing the pre-written plan. No adjustments, no rolling, no "let me see if it comes back." The moment you deviate under stress, you are trading on emotion, not edge.

**Journal prompt:** "If I had to write my exit rule for this trade before I entered it, what would it say? Did I follow it exactly? If not, what changed — and was that change evidence-based or emotional?"

---
tags: [process, psychology, journaling]
source: findings/8MJkZQSiY_E.md
added: 2026-06-13
---

## Post-Market Disconnect Ritual

**Source:** [findings/8MJkZQSiY_E.md](../findings/8MJkZQSiY_E.md)

Naresh deliberately disconnects from market price after the close. His wife asks "What is S&P today?" — his answer is always "I don't know." Not because he doesn't track performance, but because obsessing over mark-to-market after hours produces no edge and increases anxiety.

**The distinction:** Know your P&L at the end of day (review positions, check Greeks). But do not watch CNBC, check futures, or refresh the brokerage app after market hours. The market will do what it does; your decisions were made pre-trade.

**For NSE traders:** Nifty futures trading after 3:30 PM is noise. Your Nifty options positions are closed for the day. Reviewing OI data or charts after close for tomorrow's setup is acceptable; checking SGX Nifty every 20 minutes at night is not.

**Journal prompt:** "How many minutes after market close did I spend monitoring positions or checking prices? What decision did that enable that I couldn't have made before the next open?"

---

---
tags: [edge-calculation, journaling, metrics, automation, nse]
source: findings/2175knd26Yw.md
added: 2026-06-13
---

## Trade Data Dump — Edge Numbers + Time-to-Goal

**Source:** [findings/2175knd26Yw.md](../findings/2175knd26Yw.md)

Export broker console data (Zerodha: Reports → Tradebook, filter by date range) and paste into a Claude session with this prompt:

> "Here is my trade export. Tell me: total trades, win rate, average winner, average loser, profit factor, and edge ratio. Then project: at this performance rate, starting from ₹[X] capital, how long to reach ₹[Y]? Show assumptions."

**Why it works:** Forces quantitative self-assessment without manual journaling. The forward projection is the key output — if the number is too large (e.g. 7 years), it forces a system-level rethink (position sizing, strategy selection) rather than tactical tweaks.

**For options (NiftyShield adaptation):** Use the same prompt on options P&L exports. Key metrics to request: avg credit collected per strangle, win rate (expired worthless), avg loss on breached positions, return on margin deployed. Ask Claude to compute annualized return on margin as the primary KPI.

**Cadence:** Run monthly. Compare period-over-period to detect drift in edge.

---

---
tags: [process, psychology, edge-calculation, journaling]
source: findings/2175knd26Yw.md
added: 2026-06-13
---

## Three S's — Strategy vs Setup vs System

**Source:** [findings/2175knd26Yw.md](../findings/2175knd26Yw.md)

Most trading education stops at Strategy (entry/exit rules). Fewer teach Setup (pattern identification). Almost none teach System (treating trading as a repeatable business process with metrics, reviews, and consistent position sizing).

**Journal prompt:** "Am I losing because my strategy is wrong, or because I don't have a system? What would I need to measure to know the difference?"

Real consistency only comes at the System level. If results are inconsistent, the bottleneck is almost always System — not Strategy.

---

---
tags: [process, psychology, edge-calculation, metrics]
source: findings/VFRHrYtkr6o.md
added: 2026-06-13
---

## Losing Streaks Are Expected — Statistical Literacy for Systematic Traders

**Source:** [findings/VFRHrYtkr6o.md](../findings/VFRHrYtkr6o.md)

A 60% win rate does NOT guarantee alternating wins and losses. In any finite sample, clustering of losses is mathematically inevitable. At 60% win rate over 2.5 years:
- 4 consecutive losses: occurred 3 times
- 5 consecutive losses: occurred once

"People say that in every 5 trades, 3 should be profitable and 2 should be loss-making. But statistically, that number 5 is very small — it is irrelevant. You should look at how the edge performs over 100 trades."

**Why this matters:** Most traders abandon a working strategy during a losing streak, precisely when they should be doing nothing. The correct response to a losing streak within an otherwise valid strategy is to verify: (a) execution was correct, (b) market conditions haven't shifted regime, (c) you're inside the expected statistical distribution. If yes to all three: continue.

**Journal prompt:** "Am I in a losing streak because my strategy has stopped working, or because I haven't given it enough trades to express its edge? How many trades have I taken since I last updated my win-rate estimate? Is this streak inside or outside the expected statistical range?"

**Algo corollary:** Systematic traders should pre-compute the expected maximum losing streak for their win rate and sample size before going live. For 60% win rate, max losing streak of 5 in 100 trades is approximately expected. Seeing it live should not be a surprise.

---

---
tags: [process, psychology, automation, ai-workflow]
source: findings/VFRHrYtkr6o.md
added: 2026-06-13
---

## AI as Trading Coach — Emotion Processing During Drawdowns

**Source:** [findings/VFRHrYtkr6o.md](../findings/VFRHrYtkr6o.md)

Trading is often a socially isolated activity. Family and friends either don't understand or actively discourage it. During drawdowns, the natural instinct is to discuss the situation — but most available peers are also loss-making traders giving biased, emotion-driven advice.

**The AI coaching use case:** Build a custom GPT persona with your trading system rules, risk parameters, and psychological tendencies. When facing emotional challenges (drawdown, urge to deviate from algo, MTM anxiety), use it as a first-response sounding board before taking any action.

**Specific example:** Trader was checking P&L every 30 minutes during market hours despite no actionable information. Custom GPT reminded him: "Your job as a systematic trader is about execution (input), not P&L (output). Day-to-day MTM is statistically irrelevant — look at it over the long-term window you designed for."

**System prompt for trading buddy GPT:**
```
You are my trading coach. I am a systematic algorithmic options seller on NSE. 
My system: [describe your strategy, risk rules, algo framework].
My known psychological weaknesses: [list them].
When I describe a situation, help me evaluate it from the perspective of a disciplined systematic trader — not from an emotional perspective. 
Ask me: "Is this within your pre-defined system rules? If yes, do nothing. If no, what rule does it violate and why?"
```

**Personas for learning:** Store expert personas (Rob Carver, Perry Kaufman, etc.) as separate system prompts. Upload book chapters or papers and ask the persona to explain it as a mentor to a practitioner-level student. Faster than re-reading; produces applied explanations rather than academic ones.

---
tags: [process, psychology, journaling, edge-calculation]
source: findings/fPFOXqmzJp8.md
added: 2026-06-13
---

## Trade Grading Matrix — Process Over Outcome

**Source:** [findings/fPFOXqmzJp8.md](../findings/fPFOXqmzJp8.md)

Grade every trade on two axes: outcome (win/loss) and execution (followed process / broke rules). This produces four cells:

| | Followed Process | Broke Rules |
|---|---|---|
| **Win** | Good trade ✓ | **Dangerous trade ⚠** |
| **Loss** | Good trade ✓ | Bad trade ✗ |

The cell to watch is the dangerous trade: a win taken while breaking rules. The brain records this as evidence that rule-breaking works, creating a reinforcement loop that surfaces later at worse sizing or worse market conditions. A rule-breaking win is more damaging to long-term edge than a rule-breaking loss.

**Practical application:** In your post-trade journal, score every trade on the 2x2, not just whether it was profitable. If you accumulate more than 2–3 "dangerous trades" in a week, that's a process-level alert — the rules may be too restrictive (in which case update the rules), or you're drifting under P&L pressure (in which case reduce size).

**Journal prompt:** "Was this trade in the top-left or top-right cell? If top-right: what rule did I break? What would I need to believe for that break to be justified? Is that belief in my trading plan?"

---

---
tags: [process, automation, ai-workflow, metrics]
source: findings/4TTb0f9fk1U.md
added: 2026-06-13
---

## The 10/90 Rule — Signal Logic vs Production Plumbing

**Source:** [findings/4TTb0f9fk1U.md](../findings/4TTb0f9fk1U.md)

"The signal logic is normally 10% of the actual work. The other 90% is going to be plumbing, reconciling, and things like that that most people don't think of when transitioning something from a back test to a live algo."

The five production-readiness requirements that are absent from every backtest:

1. **Broker module** — wrap account balance, open positions, order status, order placement, and order cancellation into clean functions. Never call raw broker API from signal logic.
2. **EOD scheduler** — replace the bar loop with a cron/scheduler that runs once per bar period, fetches only the latest incremental data, evaluates signals, and submits orders.
3. **Broker as source of truth** — on every run, reconcile local position state against broker-reported positions. Assume your code is wrong; the broker is right.
4. **Persist state to disk** — write all trade records, fill prices, and entry timestamps to a JSON or SQLite file. Algo must be crash-recoverable and restart-safe.
5. **Safety rails** — market-hours guard, double-order prevention on restart, drawdown-based kill switch, full logging of every order event, partial-fill handling policy.

**Journal prompt for systematic traders:** "If my algo crashed tonight and restarted tomorrow morning, would it correctly know its current position, prevent duplicate orders, and resume without human intervention? Which of these five requirements is my current weakest link?"

**NSE adaptation:** Add NSE-specific rails — SEBI margin checks before order submission, expiry-day position close triggers, and alerts for illiquid strikes that may cause partial fills at wide spreads.
