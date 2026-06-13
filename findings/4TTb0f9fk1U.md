---
video_id: 4TTb0f9fk1U
title: "I Tested Larry Connors' Famous Trading Strategy (Does It Still Work?)"
channel: Unbiased Trading
url: https://www.youtube.com/watch?v=4TTb0f9fk1U
analyzed: 2026-06-13
niftyshield_relevant: false
---

## Summary

The video backtests Larry Connors' "Double Seven" mean-reversion strategy — a three-rule equity system that has held up out-of-sample since its 2008 publication. It also covers the full workflow of using Claude Code to build a backtest, volatility-based position sizing, and the practical delta between a backtest script and a production live algo.

## Strategies

- **Double Seven (Connors):** Entry — instrument must be above 200-day SMA AND close at a 7-day low → buy. Exit — while long, close at a 7-day high → sell. No stop-loss, no profit target. Pure mean-reversion within a trend filter.
  - Tested on SPY, QQQ, Gold over 5 years (2020–2026), $100K capital.
  - Equal sizing results: 49% total return, 75% average win rate, 16% max drawdown, 0.58 Sharpe, 180 trades, ~8-day avg hold.
  - Volatility sizing results: 57% total return, 74% win rate, 15% max drawdown, 0.69 Sharpe.
  - Win rates by symbol: SPY 76%, QQQ 71%, Gold 77%.
  - Notably unchanged from original 2008 parameters — all out-of-sample since then.

## Metrics & Ratios

- **Sharpe context:** 0.5–1.0 is realistic for daily equity/futures strategies; crypto can run higher. Retail expectation of 2–3 Sharpe is unrealistic for non-HFT.
- **Warm-up bars:** When using a 200-day SMA, backtest needs 200 bars of data before the first signal can be valid. Missing this inflates early signals with garbage indicator values. Solution: prepend 1.5 years of additional historical data as warm-up before the target period.
- **Slippage assumption used:** 5 pips per side, zero commissions (Public.com sponsor).

## Risk Management

- **Volatility-based sizing (ATR method):** Risk a fixed dollar amount per trade ($2,000 in the example) scaled by 3×ATR(20) stop at entry. This normalizes dollar risk across instruments with different volatility profiles (e.g., QQQ vs SPY) and improved both return and Sharpe vs equal sizing.
- **Equal sleeve sizing:** Each instrument gets a fixed capital allocation (1/N); each sleeve compounds independently. Simpler but ignores inter-instrument volatility differences.

## Journal / Process

- **Signal logic is 10% of the work; plumbing is 90%.** When transitioning a backtest to a live algo, the five non-obvious requirements are: (1) broker module wrapping account/portfolio/order endpoints, (2) replace bar loop with a scheduler running just before EOD close, (3) treat broker position state as source of truth — not local code state, (4) persist all trade state to disk (JSON) for crash recovery, (5) safety rails: market-hours guard, double-order prevention on restart, kill switch on drawdown breach, logging every fill/rejection, partial-fill handling logic.
- **Vague prompts → hidden bugs.** When prompting an AI coding tool, provide a style reference (existing working code) plus extremely explicit rule statements. Ambiguity pushes assumption-making into the model.
- **Order submission timing tradeoffs for EOD strategies:** (a) submit at ~15:58 — close enough to theoretical close price, most liquid; (b) submit post-close in extended hours — exact signal but less liquid; (c) submit at next day's open — gap risk. Option (a) generally preferred for size.

## NiftyShield Signal

**Relevant:** No  
**Why:** The Double Seven strategy is a pure equity mean-reversion system with no options component. Backtesting methodology tips (warm-up bars, volatility sizing) are generic and already well-understood. The live algo transition checklist is solid systems engineering but not options-specific.  
**Action suggested:** N/A
