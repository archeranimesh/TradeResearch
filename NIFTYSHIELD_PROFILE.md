# NiftyShield Profile — Cross-Project Relevance Guide

> This file tells TradeResearch what NiftyShield needs.
> Update this file when NiftyShield's strategy focus changes.
> Never modify during transcript analysis.

---

## What NiftyShield Is

An automated options trading system for NSE (Indian markets) focused on:
- **Options selling** on Nifty / BankNifty (short strangles, iron condors)
- **Delta-neutral position management** with real-time Greeks monitoring
- **Demand/supply zone analysis** for entry timing (price action based)
- **NiftyBees ETF** pledged as margin collateral
- **Backtesting** against expired NSE option contract data

---

## Flag as Relevant If the Video Covers:

### Strategy
- Options selling strategies (short strangle, iron condor, short straddle, jade lizard, etc.)
- Entry filters using IV Rank / IV Percentile / HV vs IV comparison
- Demand and supply zone identification, especially for index instruments
- Multi-timeframe analysis for entry confirmation
- Delta-neutral setup or adjustment techniques
- Strike selection methodology for selling options

### Adjustments & Management
- Rolling rules (when to roll, to what strike, to what expiry)
- Delta hedging or gamma scalping techniques
- Position sizing relative to portfolio / margin
- Adjustment triggers (delta breach, loss threshold, DTE rules)

### Risk Management
- Max loss per trade / per week / portfolio-level stops
- Theta decay curves and how to exploit them
- Margin management and capital allocation for options selling

### Metrics & Measurement
- Win rate, P&L per day, return on margin
- Sharpe / Sortino adapted for options selling
- IV rank thresholds and historical performance
- Expected value calculations for premium selling

### Indian Market Specific
- NSE options microstructure, liquidity at strikes
- Weekly vs monthly expiry strategy differences (Nifty expiry is Tuesday)
- SEBI margin rules impact on position sizing
- BankNifty vs Nifty behavior differences

---

## Do NOT Flag:
- Pure equity/stock picking strategies
- Crypto, forex, or US-market-only content (unless the concept is directly portable)
- Fundamental analysis, DCF, valuation frameworks
- Scalping or intraday equity strategies
- Content that only covers basics already well understood (e.g., "what is an option")
