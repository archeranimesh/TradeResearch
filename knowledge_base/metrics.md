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

---
tags: [risk-management, metrics, edge-calculation, process]
source: findings/fPFOXqmzJp8.md
added: 2026-06-13
---

## Drawdown Recovery Asymmetry — Why Capital Preservation Beats Return Maximization

**Source:** [findings/fPFOXqmzJp8.md](../findings/fPFOXqmzJp8.md)

Losses require disproportionately larger gains to recover. The math is not symmetric:

| Drawdown | Recovery needed to break even |
|---|---|
| 10% | 11% |
| 25% | 33% |
| 50% | 100% |
| 75% | 300% |

A 50% drawdown requires doubling the remaining capital — effectively starting over. At 75% most traders quit, which makes the math academic.

**The practical implication:** The expected return from a trade is not the only relevant number. The cost of a large loss is not its face value — it is the lost compounding opportunity on the base capital, plus the psychological cost of the recovery grind, plus the risk of quitting before recovery. This makes max drawdown the most important metric for survival, more important than annual return.

**For NiftyShield:** Unlimited-loss positions (short strangles without defined exits) can produce 75%+ drawdowns in gap events. The 2x credit stop from the options-selling KB entry exists precisely because a single unbounded loss can produce an unrecoverable drawdown at standard sizing. Pre-define stops before entry; never rely on "it'll come back."

---

---
tags: [backtesting, metrics, automation, process]
source: findings/4TTb0f9fk1U.md
added: 2026-06-13
---

## Indicator Warm-Up Bars — Backtest Validity Requirement

**Source:** [findings/4TTb0f9fk1U.md](../findings/4TTb0f9fk1U.md)

Any indicator that uses a rolling window N requires N bars of data before it produces a valid value. If a backtest starts before those N bars are available, the indicator output is garbage — effectively a random number — and the first N signals of the backtest are unreliable.

**Rule:** Always prepend `N` warm-up bars before the backtest start date. These bars are used only to seed indicator state; no trades are generated during warm-up.

**Common examples:**
| Indicator | Window | Warm-up bars needed |
|---|---|---|
| SMA(200) | 200 days | 200 daily bars (~10 months) |
| ATR(20) | 20 days | 20 bars |
| RSI(14) | 14 bars | 14 bars + initial smoothing period |
| BB(20,2) | 20 bars | 20 bars |

**Practical fix:** Pull an additional 1.5× of the largest indicator window as pre-data from a secondary source (e.g., Yahoo Finance), concatenate before the primary data feed, calculate all indicators over the full series, then slice to the actual backtest start date before evaluating signals.

**Detection:** If early backtest trades have an anomalously high win rate vs the rest of the sample, warm-up contamination is a likely cause — the indicator was still converging.
