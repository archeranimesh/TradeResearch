# Pending — NiftyShield Review Queue

Items flagged as relevant to NiftyShield during transcript analysis.
Review periodically. Check the box when actioned. Carry decisions into NiftyShield's TODOS.md or BACKTEST_PLAN.md.

---

<!-- New entries appended below by analysis pipeline -->

## 2026-06-13 | How This Trader Trades Options For Long-Term Wealth | #Face2Face with Naresh Kusunam — Learn Stock Market 1M+
**Signal:** Backtested DTE/delta framework (30 DTE / 30 delta for strangles) + 2x stop loss rule + Jade Lizard with no upside risk + laddering entry approach over weekly sub-expiries — all directly portable to NiftyShield.
**Finding:** findings/8MJkZQSiY_E.md
**Action:**
- [ ] Backtest 30 DTE / 30 delta Nifty strangle with 2x-credit stop loss — does it survive weekly gap events (RBI, Budget, earnings)?
- [ ] Evaluate Jade Lizard on Nifty: sell 30D PE + sell narrow CE spread ATM; verify NSE margin treatment vs. naked PE
- [ ] Model laddering entry: 1 lot/week over 4 weeks targeting monthly expiry cycle — does time-diversification reduce max drawdown meaningfully?

## 2026-06-13 | How This Trader Built a Mark Minervini-Style AI Trading System — Learn Stock Market 1M+
**Signal:** Two portable ideas: (1) dump Zerodha options P&L export into Claude to get edge numbers + return-on-margin baseline for NiftyShield review; (2) Claude Code + Obsidian offline vault as architecture for NiftyShield's research KB and automation layer.
**Finding:** findings/2175knd26Yw.md
**Action:**
- [ ] Run trade-data-dump prompt on last 3 months of NiftyShield options P&L (Zerodha tradebook export) — get win rate, avg credit, avg loss, return on margin
- [ ] Evaluate Claude Code + Obsidian vault setup for NiftyShield research KB
- [ ] Review Kaparthi's LLM wiki on GitHub as vault instruction scaffold

## 2026-06-13 | The Options Strategy That Lets Traders Sleep Peacefully !! #Face2Face with Vaibhav Shinde — Learn Stock Market 1M+
**Signal:** Fixed-premium short straddle on Nifty/Sensex DT1+DT0 with cost-based SL migration — concrete implementation (₹75 premium, 50% SL, break-even leg migration, 3:15 exit) plus redundant OTM hedging philosophy and Monte Carlo capital-sizing workflow.
**Finding:** findings/VFRHrYtkr6o.md
**Action:**
- [ ] Backtest fixed-premium (₹75 analog) vs ATM straddle entry on Nifty DT0 — does normalized premium produce tighter max-drawdown distribution?
- [ ] Implement cost-based SL migration: when one leg stops out, surviving leg SL moves to entry price (break-even)
- [ ] Run Monte Carlo on NiftyShield backtest P&L series via ChatGPT — use 90th percentile max drawdown to size capital buffer, not historical max
- [ ] Audit pledged NiftyBees margin haircut assumption vs current SEBI rules (equity MF haircut may differ from ETF)

## 2026-06-28 | 1% Risk, 5x Reward? Ratio Spread se Expiry Day Income — Theta Gainers
**Signal:** Double-sided ratio spreads (1:3 buy:sell on ATM ±OTM) deployed exclusively on expiry day with hard 1% max-loss discipline. Backtested 8 expiries (April–June 2026), 83% win rate (5 profits, 1 loss, 2 breakeven), consistent ~1% ROI on ₹6.5L margin. Vega-short, theta-long profile with Greeks explicitly managed; no chart analysis. Directly portable strike-selection and risk-management rules.
**Finding:** findings/iorriHcOpdU.md
**Action:**
- [ ] Extract "divide premium by 3, multiply by 3" ratio rule — backtest on BankNifty expiries to confirm strike-selection calibration
- [ ] Stress-test 1% loss rule against NiftyShield's current per-trade % risk framework — does it align or conflict?
- [ ] Backtest ratio 1:2 (instead of 1:3) to lower vega short without sacrificing ROI; measure max drawdown trade-off
- [ ] Verify 83% win rate on post-June 2026 expirations (war-volatility period may not repeat; test on normal vol)
- [ ] Capital efficiency audit: ₹6.5k profit on ₹6.5L margin = 0.1% per expiry net of loss cases; compare to alternative spreads (strangles, condors, naked) for ROI/margin ratio
