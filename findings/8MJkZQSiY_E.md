---
video_id: 8MJkZQSiY_E
title: "How This Trader Trades Options For Long-Term Wealth | Options Trading #Face2Face with Naresh Kusunam"
channel: Learn Stock Market 1M+
url: https://www.youtube.com/watch?v=8MJkZQSiY_E
analyzed: 2026-06-13
niftyshield_relevant: true
---

## Summary

Interview with Naresh Kusunam — an Indian-origin, US-based options seller who runs a ~$10M hedge fund trading S&P 500 and US large-cap options. He transitioned from buy-and-hold to pure options selling (99% of capital in options), achieving consistent profitability since June 2021 (4 losing months out of 55). The video covers six distinct options-selling strategies with backtested parameters, a clear DTE/delta framework, and a strict pre-trade risk discipline. All strategies are mechanically translatable to NSE index options with minor adaptations.

---

## Strategies

**1. Naked Put Selling (Core Strategy)**
- **90 DTE version:** Sell 15-delta put; stop loss = 2x credit received
- **30 DTE version:** Sell 30-delta put (15 delta insufficient credit at 30 DTE); stop loss = 2x credit
- Best candidates: trending-up indices (QQQ, Netflix); avoid high-vol single stocks
- Live demo on QQQ: sold 611 put (~3% OTM, 25 DTE) for $611 credit; BP required ~$8,000; ROC ~7.6% per trade
- **Hedge fund laddering:** Enter 2 contracts/week over 12 weeks for 90-DTE cycle — diversifies time-risk so a single drop doesn't stop out the full book

**2. Jade Lizard (Bullish + No Upside Risk)**
- Sell 30-delta put (~30 DTE) + sell a narrow call credit spread (5-wide, near ATM)
- Combined credit (~$988–$1,000) > call spread width ($500) → zero upside risk
- No additional margin in US vs. naked put alone; the call spread margin offsets
- Use when mildly bullish and confident stock won't gap up significantly

**3. Ratio Call Spread (Bearish Directional)**
- 1:3 version: Buy 1 call (ATM/slightly OTM), sell 3 calls (5-wide OTM)
- 32 DTE, QQQ example: credit ~$1,265; BP ~$17,000; ROC 7.44% / annualized ~85%
- 1:2 version (lower margin): credit $525; BP ~$9,000; ROC 5.83% / annualized ~66%
- 1:3:2 version: buy further OTM calls to partially hedge; reduces BP from $17k to ~$11k
- Use for bearish plays around earnings (named: Palantir, Nvidia); no adjustments, pre-set stop

**4. Short Strangle (Neutral / Range-Bound)**
- 30 DTE, 30-delta on both sides (15 delta only for 45–90 DTE)
- QQQ example (626 spot, 32 DTE): sold 609P / 641C; credit $1,456; BP ~$8,000–$9,000; ROC 17% / annualized ~200%
- Stop loss: 2x total credit received ($2,912 max loss)
- **Avoid on high-volatility single stocks** (explicitly: do not strangle Tesla)
- Best candidates: index ETFs (QQQ), liquid large-caps with mean-reverting behavior

**5. Poor Man's Covered Call (PMCC)**
- Buy 70-delta call (~30 DTE long leg), then sell ATM (~50 delta) next-day expiry call daily
- Example: QQQ 619C (70D, $1,880 cost) + sell QQQ 626C (50D, next day, $276 credit) daily
- Goal: accumulate daily credits to recover long call cost over 30 days, then net profit
- Active management: close short leg daily; let long leg run; if short call ITM, close both and reset

**6. Rolling Put Diagonal (Mirror of PMCC)**
- Buy 30-DTE ATM put as long leg; sell next-day ATM put daily against it
- Pair with PMCC to create a market-neutral daily income structure
- Used as core of fund's "value-added monthly index" with reduced drawdown vs. S&P 500

---

## DTE / Delta Framework (Backtested)

| DTE | Delta | Strategy |
|---|---|---|
| 90 DTE | 15 delta | Put selling (longer theta capture) |
| 45 DTE | 15 delta | Put selling (transition zone) |
| 30 DTE | 30 delta | Put selling, strangles, PMCC |
| Daily (0–1 DTE) | 50 delta (ATM) | PMCC short leg, rolling put diagonal |

Rationale: "Theta decay happens heavily from 45 days to [expiry]. When we are doing within the 30 days, we have to go like 30 delta. Backtesting showed that."

---

## Metrics & Ratios

- Monthly win rate since June 2021: **~93%** (4 losing months / 55 months)
- Monthly return target: **1–2% per month** → ~25% CAGR
- During Trump tariff drop (market –17%): portfolio **+6%**
- Strangle ROC example: **17%/trade, ~200% annualized** (on margin, QQQ 30 DTE)
- Put sell ROC example: **7.6%/trade, ~111% annualized** (QQQ 25 DTE)
- Account minimum for unrestricted trading (US PDT rule): **$25,000**
- Consistent strategy outperforms high-variance strategy over 10 years at same average CAGR: "$500,000 more" — modeled with 30% average CAGR, smooth vs. volatile equity curves

---

## Risk Management

- **2x stop loss rule (universal):** Max loss = 2x credit received. Applied to every strategy. "Either I want to make $1,456 or have a loss of $2,800."
- **2–3% portfolio max loss per day:** Hard cap on daily drawdown across the full book.
- **No adjustments / no rolling:** "I never adjusted any trade. It makes absolutely no sense." Pre-decide the stop; if hit, exit and re-enter fresh.
- **No position marriages:** Cut losers mechanically; do not hold through hope.
- **Index circuit breaker as passive hedge:** QQQ/SPX halt at 7% intraday drop, limiting tail risk for index put sellers.
- **Pre-trade decisions only:** "Decisions have to be made pre-trade, not while the trade is running and definitely not when it is going against you."
- **Ladder entries (fund approach):** 2 contracts/week over 12 weeks for 90-DTE puts — avoids full stop-out on a single down day.
- **Think in percentages, never dollars:** Prevents loss aversion / position-sizing errors during drawdowns.

---

## Journal / Process

- **Post-market ritual:** Deliberate disconnect — wife asks "what is S&P today?"; answer is "I don't know." Maintains emotional separation from P&L after close.
- **Daily schedule:** 1 hour backtesting + 2 hours podcast/content. Trading is secondary to preparation.
- **Two years in isolation:** Before launching fund, spent two years with zero public presence to achieve consistency — the vanity of teaching before mastering is a real edge killer.
- **Bruce Lee principle (directly quoted):** "I fear not the man who practiced 10,000 kicks once, but I fear the person who practices that one kick 10,000 times." — Master one strategy before expanding.
- **Social accountability:** Maintains Discord group with peer traders; "trading is such a boring job, you have nobody to pat on."
- **Probability-first framing:** Selling 30-delta = 70% win probability per trade. Selling 1SD put = 83% win. The edge is in repetition, not prediction.
- **Market is never wrong:** "Whatever the market is doing, you are not there to double guess." Accept price, manage the position.
- **Loss framing:** "When a big loss happens to me, I keep thinking, oh, we could have bought like a Ferrari... but you have to always think in terms of the percentages."

---

## NiftyShield Signal

**Relevant:** Yes

**Why:** Direct overlap on NiftyShield's core framework across multiple strategies. Per-strategy fit assessment:

| Strategy | NSE Fit | Notes |
|---|---|---|
| Put Selling | ✅ Direct | 30 DTE / 30 delta maps to Nifty monthly expiry; 2x stop immediately adoptable |
| Short Strangle | ✅ Direct | Core NiftyShield territory; validate 2x stop vs. current adjustment logic |
| Jade Lizard | ✅ Worth exploring | Extracts extra credit from upside; verify NSE margin treatment for CE spread |
| Ratio Call Spread | ⚠️ Situational | Usable on event days (RBI, Budget); prefer 1:2 over 1:3 to limit gap-up risk |
| PMCC | 🔲 Deferred | Requires 0 DTE liquidity; evaluate fit to Indian expiry structure separately |
| Rolling Put Diagonal | 🔲 Deferred | Same 0 DTE liquidity constraint; evaluate alongside PMCC for Indian context |

**Action suggested:**
1. Backtest 30 DTE / 30 delta Nifty strangle with 2x-credit stop — does it survive weekly gap events (RBI, Budget, expiry)?
2. Evaluate Jade Lizard on Nifty: sell 30D PE + sell narrow CE spread ATM; verify NSE SPAN margin treatment vs. naked PE alone.
3. Model ratio call spread for Nifty event days — size with 1:2 ratio, pre-set stop, no adjustments.
4. Revisit PMCC + rolling put diagonal for Indian context — assess Tuesday/Thursday expiry liquidity as a proxy for 0 DTE legs.
