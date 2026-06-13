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
