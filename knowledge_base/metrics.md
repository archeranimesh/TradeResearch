# Knowledge Base — Metrics & Ratios

Curated performance metrics and measurement techniques from transcript analysis.
Link back to the source finding for full context.

---

<!-- Entries added here when a metric warrants permanent curation -->

---
tags: [risk-management, options-selling, strangle, iron-condor, metrics]
source: findings/8MJkZQSiY_E.md
added: 2026-06-13
---

## 2x Credit Stop Loss — Universal Options Selling Rule

**Source:** [findings/8MJkZQSiY_E.md](../findings/8MJkZQSiY_E.md)

Set max loss per position at exactly 2x the credit received at entry. Pre-decided before entering the trade.

**Examples from 30-DTE trades:**
- Strangle credit = $1,456 → stop at $2,912 loss
- Put sell credit = $611 → stop at $1,222 loss

**Rationale:** At 30-delta, ~70% of trades win. A 2x stop means win:loss ratio is 1:2. With 70% win rate: EV = 0.70 × (+$1) – 0.30 × (–$2) = +$0.10 per unit. Positive expected value, mechanically enforced.

**What not to do:** No rolling to avoid the stop. No adjusting strikes. "I never adjusted any trade. It makes absolutely no sense. Either you have to cut the losses." Adjusting delays the loss but increases total exposure to a losing position.

**NSE adaptation:** The 2x rule works on Nifty strangles as-is. The main risk is overnight/gap events (RBI surprise, global crash) that can jump through the stop. Use intraday stop monitoring; do not rely on GTC stop orders for options in illiquid expiries.
