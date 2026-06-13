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

---

---
tags: [backtesting, risk-management, metrics, edge-calculation, options-selling]
source: findings/VFRHrYtkr6o.md
added: 2026-06-13
---

## Monte Carlo for Capital Buffer Sizing

**Source:** [findings/VFRHrYtkr6o.md](../findings/VFRHrYtkr6o.md)

Historical max drawdown from backtest is the best-case scenario for drawdown, not the expected one — it is path-dependent and reflects only the single sequence of trades that actually occurred. A strategy with historical max drawdown of ₹23K could produce ₹50K drawdown under a different (equally plausible) sequence.

**Monte Carlo approach:**
1. Export daily P&L series from backtest
2. Upload to ChatGPT with prompt: "Run 1000 Monte Carlo simulations on this P&L series by randomly shuffling the sequence. Give me: (a) median max drawdown, (b) 90th percentile max drawdown, (c) 99th percentile max drawdown."
3. Size your capital buffer to cover the 90th percentile max drawdown, not the historical max

**Why 90th percentile:** The 99th percentile often includes extreme compounded sequences that are statistically valid but practically very rare. The 90th percentile is a reasonable "stress scenario" — happens roughly once per 10 comparable strategy lifetimes.

**Practical example:** If historical max drawdown = ₹23K but Monte Carlo 90th percentile = ₹45K, hold ₹45K in cash buffer (or 2–2.5× as a further margin of safety), not ₹23K.

**Tool:** ChatGPT Code Interpreter handles this without specialized software. Paste P&L as a column of numbers or upload CSV.

**Companion metric — standard deviation of daily P&L:** Ask ChatGPT to also compute the standard deviation of daily returns. The ±1 SD range (covering ~68% of days) tells you what "normal" looks like — useful for not overreacting to individual bad days within the normal distribution.
