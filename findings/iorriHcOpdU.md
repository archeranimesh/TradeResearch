---
video_id: iorriHcOpdU
title: "1% Risk, 5x Reward? 🤯 Ratio Spread se Expiry Day Income | Live Demo (Nifty/Sensex) | Theta Gainers"
channel: Theta Gainers
url: https://www.youtube.com/watch?v=iorriHcOpdU
analyzed: 2026-06-28
niftyshield_relevant: true
---

## Summary

A deep-dive on expiry day trading using double-sided ratio spreads on Nifty/Sensex index options. The presenter demonstrates a mechanical, rules-based approach to selling premium on expiry day by constructing a balanced ratio spread, holding it through close, and enforcing a strict 1% max loss rule. Backtested across 8 expiries (April–June 2026, including war-volatility period); showed 5 wins, 1 loss, 2 breakeven.

---

## Strategies

**Double-Sided Ratio Spread (Expiry Day Income)**

- **Entry:** 9:25–9:30 AM on expiry day; identify ATM strike
- **Buy leg:** 1 call + 1 put at ATM (e.g., ₹135 put, ₹180 call)
- **Sell leg:** Divide each buy premium by 3, multiply by 3
  - Example: buy 135 → 135÷3 = 45 → sell 3 legs at ~45 premium
  - Example: buy 180 → 180÷3 = 60 → sell 3 legs at ~60 premium
- **Ratio:** 1:3 on each side (total 8 legs: 1 buy call, 3 sell call, 1 buy put, 3 sell put)
- **Hold:** Until 3:27 PM close or until 1% max loss triggered
- **Exit:** Immediate exit at 1% loss; no discretion

**Structure Logic:** Creates a "Batman" or straddle-shaped payoff on each side with steep loss boundaries and wide breakeven range (~1.2–1.5% total, e.g., ±6.6% on each side for a specific example).

**Profit Profile:**
- Max theoretical profit: uncapped above/below boundaries, but on expiry day typically capped by time decay
- Realized profit: consistently ~0.7–1.4% on margin (average 1%)
- Breakeven range: 1.2–1.5% total market move

---

## Metrics & Ratios

- **Win rate:** 5/6 expiries profitable (83%); tested across war-volatility period (April–June 2026)
- **Average ROI on margin:** ~0.9–1% per expiry (varies 0.2–1.5% depending on IV and conditions)
- **Max loss per expiry:** 1% of margin (fixed discipline rule)
- **Recovery rule:** If 1% is lost on an expiry, the next expiry's 1% win is insufficient to recover; expect 2-week drawdown if broken
- **Margin deployed:** ~₹6.5 lakh on expiry day (SEBI mandates higher margin on expiry); non-expiry setup would require ~₹3.5–4 lakh
- **Frequency:** Nifty (Tuesday) + Sensex (Thursday) = 2 trades/week possible

---

## Risk Management

- **Fixed 1% stop loss (non-negotiable):** Exit immediately when unrealized loss reaches 1% of margin; no discretion, no averaging
- **Why 1%:** Ratio spreads short vega aggressively; if volatility expands or price moves hard against position, losses accelerate. Staying in a losing trade risks wiping 2 weeks of gains
- **Holding time:** Full day (9:27 AM to 3:27 PM close) if position remains profitable or within 1% loss
- **Greeks exposure:**
  - Vega: Short (selling 3 legs per side = aggressive vol short). Volatility expansion hurts. Mitigated by holding to expiry when vol decay accelerates
  - Theta: Long (massively positive on expiry day). Every 15 min of theta decay drives profit
  - Delta: Near-neutral at entry; converges to intrinsic by close
- **Adjustment:** None shown. Strategy is hold-to-expiry with a hard 1% exit
- **Contingency:** If 1% loss is hit, accept it; do NOT re-enter on same expiry. Wait for next expiry cycle

---

## Journal / Process

- **Discipline > Direction:** No chart analysis, no bias, no market view. Strategy is agnostic to up/down/sideways. Entry is time-based (9:27 AM) and mechanical (divide by 3, multiply by 3). Credibility comes from systematic execution
- **Profit is not the goal; loss prevention is:** "Our only control is the loss side. Profit is not in our hands." The trader monitors 1% loss obsessively; profit outcome varies (0.2%–1.5%) and is secondary
- **Holding discipline:** "Very holding style… must not be lured. Exit only at 1% loss." Requires stomach to watch position fluctuate and resist the temptation to take early profit or panic-exit
- **Context awareness:** Video tested during India-Ukraine war volatility period. System still profitable 5/6 times. Normal low-vol environments expected to show even better consistency
- **Behavioral insight:** "Market tries to trap the OI built over weeks. That's our edge." On expiry, large OI creates pressure; ratio spread captures this via time decay + gamma edge between ATM buys and OTM sells

---

## NiftyShield Signal

**Relevant:** Yes

**Why:** 
1. **Options selling strategy** directly aligned with NiftyShield's core focus (short strangles, iron condors); ratio spread is an exotic cousin with edge on expiry day
2. **Entry timing** (expiry day, 9:27 AM) is index-specific NSE knowledge
3. **Strike selection** (ATM + ratio to OTM) is mechanical and data-driven
4. **Greeks management** (explicit vega/theta/delta discussion) matches NiftyShield's framework
5. **Delta-neutral hedging** (ATM long legs hedge the short selling legs)
6. **Win rate & P&L metrics** (83% 5/6 expiries, ~1% ROI/margin) provide empirical validation even under stressed vol
7. **Risk management** (hard 1% loss rule, no averaging) is portable risk discipline
8. **Index-specific edge** (Nifty Tuesday, Sensex Thursday, SEBI expiry margin impact) is NSE-native knowledge
9. **Backtesting across expiries** (8 historical examples with actual P&L shown) de-risks the strategy vs. simulated claims

**Action suggested:** 
- [ ] Extract the "divide premium by 3, multiply by 3" rule and test on BankNifty expiries for strike selection calibration
- [ ] Audit the 1% loss rule against NiftyShield's current position-sizing framework (does it align with per-trade % risk?)
- [ ] Verify whether ratio spread's vega-short profile can be hedged or toned down (e.g., 1:2 ratio instead of 1:3) without sacrificing ROI
- [ ] Backtest against recent June 2026 expirations to confirm the 83% win rate holds post-war period
- [ ] Compare margin efficiency: at ₹6.5 lakh margin for 1% ROI (~₹6.5k profit), is this capital-efficient vs. alternative spreads?

---

## Notes for Follow-up

- **Video quality:** Live simulator walkthrough with 8 historical expiry replays; excellent pedagogical clarity for mechanical reproducibility
- **Limitations not discussed:** Single-lot examples; real scaling (10+ lots) and slippage impact unknown
- **Upside:** Expiry day consolidation hypothesis is empirically validated (M-shape, N-shape, trending all work within range); no chart dependency reduces discretion
- **Caveat:** 1% margin loss on a ₹6.5 lakh deployment = ₹6.5k loss, recoverable in 1 win, but psychological impact of back-to-back loss-then-win cycles may test discipline
