# Knowledge Base — Strategies

Curated strategy cards extracted from transcript analysis.
Each entry is evergreen — not tied to a specific video.
Link back to the source finding for full context.

---

<!-- Entries added here when a strategy warrants permanent curation -->

---
tags: [options-selling, strangle, iron-condor, strike-selection, backtesting, delta-neutral]
source: findings/8MJkZQSiY_E.md
added: 2026-06-13
---

## DTE / Delta Framework for Options Selling (Backtested)

**Source:** [findings/8MJkZQSiY_E.md](../findings/8MJkZQSiY_E.md)

The correct delta to sell depends on DTE — using the same delta across all timeframes is a common error. Backtesting on US index ETFs (QQQ/S&P 500) shows:

| DTE | Delta | Use Case |
|---|---|---|
| 90 DTE | 15 delta | Put selling — longer theta capture, smaller position per trade |
| 45 DTE | 15 delta | Transition zone — put selling |
| 30 DTE | 30 delta | Put selling, strangles, PMCC anchor leg |
| 0–1 DTE | 50 delta (ATM) | PMCC daily short leg, rolling put diagonal |

**Why 30 delta at 30 DTE:** "Theta decay happens heavily from 45 days to [expiry]. When we are doing within the 30 days, we have to go like 30 delta. Backtesting showed that." — 15 delta at 30 DTE generates insufficient credit to make the trade worthwhile after stop-loss sizing.

**Why 15 delta at 90 DTE:** Gives enough credit while maintaining a large OTM buffer. The longer time window allows delta to erode naturally without requiring a large initial delta exposure.

**NSE adaptation:** Nifty's primary cycle is monthly expiry (~30 DTE). Use 30 delta PE for put selling and 30 delta on both sides for strangles. For the rare 90-DTE equivalent (far monthly), shift to 15 delta.

---
tags: [options-selling, strangle, adjustment, risk-management, index-options]
source: findings/8MJkZQSiY_E.md
added: 2026-06-13
---

## Jade Lizard — Zero Upside Risk Strangle Variant

**Source:** [findings/8MJkZQSiY_E.md](../findings/8MJkZQSiY_E.md)

**Construction:**
1. Sell 30-delta put (~30 DTE) — generates bulk of the credit
2. Add: sell a call credit spread (5-wide, near ATM) — generates additional premium
3. Ensure: total credit received > call spread width → upside risk = zero

**Example (QQQ):** Sell 30D put for ~$770 + sell 5-wide CE spread for ~$230 = $1,000 total credit. Call spread max loss = $500. Since $1,000 > $500, upside gap cannot create a net loss.

**Margin:** In the US, no additional margin vs. naked put — the call spread margin offsets. Verify NSE treatment: short CE spread margin may differ from US, but logic holds if total credit > spread width.

**When to use:** Mildly bullish but wanting to monetize the upside (vs. pure put selling). Do not use if you expect a large gap-up — the call spread will be deep ITM but capped, while the total structure still profits.

---

---
tags: [ai-workflow, automation, knowledge-management, screening]
source: findings/2175knd26Yw.md
added: 2026-06-13
---

## AI Second Brain Architecture (Claude Code + Obsidian)

**Source:** [findings/2175knd26Yw.md](../findings/2175knd26Yw.md)

**Setup:**
1. Install Obsidian (free, offline). Create a vault folder.
2. Install Claude Code (Pro/Max plan required). Point it at the vault folder.
3. Paste [Kaparthi's LLM wiki](https://github.com/karpathy/llm.md) as the instruction scaffold — tells Claude how to structure the vault.
4. Ingest sources: YouTube transcripts (Chrome extension or copy-paste), PDFs, GitHub repo links, images, audio transcripts. Use the command `ingest [source]` in Claude Code.

**How it works:** Claude Code uses Obsidian as an offline memory bank (wiki folder + raw folder). Each ingested source is parsed and added to a knowledge graph of `.md` files. Claude does NOT search the web — it only reasons over the vault contents. The graph grows incrementally; contradicted information gets replaced.

**Automation patterns built on top:**
- Slash commands (`/fetch`, `/rs [ticker]`) for daily data retrieval
- Session-ID based scraping of authenticated web dashboards (MarketSmith, Chartink screeners)
- Telegram bot integration for daily alert delivery
- TradingView Chrome extension for RS overlays
- Routines (scheduled commands) for end-of-day scans

**Portability:** The vault is a folder. Copy it to any machine with Claude Code installed and the full knowledge graph is immediately available.

**NiftyShield use case:** Build a NiftyShield-specific vault ingesting NSE options literature, SEBI margin rules, IV seasonality data, adjustment rule documentation, and backtesting results. Query it with natural language instead of relying on web search or memory.

---

---
tags: [options-selling, strangle, strike-selection, risk-management, nse, index-options]
source: findings/VFRHrYtkr6o.md
added: 2026-06-13
---

## Fixed-Premium Selling — IV-Normalized Risk Control

**Source:** [findings/VFRHrYtkr6o.md](../findings/VFRHrYtkr6o.md)

Instead of selling the ATM straddle/strangle (where premium varies with IV), sell the specific strike priced near a fixed target premium (e.g., ₹75 for Nifty, ₹225 for Sensex). This normalizes max-loss-per-day across different IV regimes.

**Why ATM fails for risk management:**
- High IV day: ATM call sells at ₹300 → 30% SL = ₹90 loss per leg
- Low IV day: ATM call sells at ₹70 → 30% SL = ₹21 loss per leg
- The per-trade risk swings 4× without any change in position size

**Fixed-premium approach:**
- Select the strike whose market price is closest to ₹75 (Nifty) each morning
- 50% SL = ₹37.5 loss per leg, every day, regardless of IV environment
- Max-drawdown distribution is tighter → easier to size capital correctly

**Entry:** Post 9:15 open candle, between 9:20–9:30 AM. Two lots staggered (9:22 and 9:29) for time diversification within the same strike.

**Instruments:** Nifty DT1+DT0 (Monday+Tuesday), Sensex DT1+DT0 (Thursday+Friday) = 8 opportunities/month.

**Rationale:** Near-expiry theta decay is maximum on DT0/DT1. Restricting to the final 1–2 days captures peak theta while minimizing overnight gap exposure (intraday only, all positions closed by 3:15 PM).

**Backtest results (₹6L margin, Aug 2023 – Feb 2025):** 60% win rate, avg monthly profit ₹15,700, max drawdown ₹23K (~4%), max single-day loss ~1.7%, pre-tax ROI ~26% on total capital (pledged MF + cash).

---

---
tags: [risk-management, position-sizing, backtesting, metrics, automation]
source: findings/4TTb0f9fk1U.md
added: 2026-06-13
---

## ATR-Based Volatility Position Sizing

**Source:** [findings/4TTb0f9fk1U.md](../findings/4TTb0f9fk1U.md)

Scale position size by realized volatility (ATR) so that every trade risks the same dollar amount regardless of instrument. Eliminates the systematic over-exposure to high-volatility instruments that equal-sleeve sizing creates.

**Formula:**
```
position_size = risk_per_trade / (atr_multiplier × ATR(N))
risk_per_trade = fixed dollar amount (e.g., ₹2,000 or $2,000)
atr_multiplier = stop distance in ATR units (e.g., 3)
ATR(N) = N-day average true range (typically N=20)
```

**Outcome vs equal sizing (Double Seven strategy, same signals):**
- Total return: +57% vs +49%
- Max drawdown: 15% vs 16%
- Sharpe: 0.69 vs 0.58

**Why it works:** QQQ can be 2–3× more volatile than SPY on a given day. Equal sleeves implicitly over-bet on the volatile instrument. ATR sizing normalizes to equal risk-per-trade across instruments, which is the correct unit of exposure for a strategy tested on mixed-volatility assets.

**NSE adaptation:** Directly applicable to Nifty vs BankNifty sizing in NiftyShield. BankNifty ATR is typically 1.5–2× Nifty ATR. Using equal lots on both instruments over-exposes the portfolio to BankNifty drawdowns. ATR-normalize lot counts relative to a fixed notional risk per position.

---
tags: [options-selling, adjustment, risk-management, strangle, index-options]
source: findings/VFRHrYtkr6o.md
added: 2026-06-13
---

## Cost-Based SL Migration — Protecting the Surviving Leg

**Source:** [findings/VFRHrYtkr6o.md](../findings/VFRHrYtkr6o.md)

When running a straddle or strangle, the two legs are managed independently but with a conditional linkage: if one leg is stopped out, the surviving leg's stop loss is immediately moved to its entry price (break-even).

**Mechanics:**
1. Sell call at ₹100 (SL at ₹150 = 50%) + sell put at ₹100 (SL at ₹150 = 50%)
2. Market rallies → call hits ₹150, call leg closed, loss = ₹50
3. Immediately: put SL moved from ₹150 to ₹100 (entry price)
4. Worst-case net loss now capped at ₹50 (one leg only), not ₹100

**Why this works:** After a directional move sufficient to stop one leg, the market often continues. Keeping the surviving leg's SL at the original level (₹150) risks a second full loss; moving it to cost eliminates further loss on that leg. Net result: single-leg max-loss instead of double-leg max-loss on worst-case days.

**Execution requirement:** Must be automatable — human reaction time is too slow on fast moves. The SL migration must be a conditional algo rule: "IF call_leg_status = stopped THEN put_leg_SL = put_leg_entry_price."

**Contrast with 2x-credit SL rule:** The 2x-credit rule (from [strategies.md](strategies.md)) applies a single combined SL to the whole position. Cost-based migration applies per-leg SLs with a conditional linkage. Both can coexist: set individual leg SLs, with the overall position also subject to a combined loss cap.

---

---
tags: [options-selling, delta-neutral, strike-selection, expiry-specific, risk-management, nse, index-options, backtesting]
source: findings/iorriHcOpdU.md
added: 2026-06-28
---

## Double-Sided Ratio Spread — Expiry Day Premium Income (1:3 Buy:Sell)

**Source:** [findings/iorriHcOpdU.md](../findings/iorriHcOpdU.md)

A mechanical options-selling structure deployed exclusively on expiry day that combines delta-neutral hedging (long ATM) with aggressive theta capture (short 3× the OTM).

**Construction (9:25–9:30 AM entry, expiry day only):**

1. **Identify ATM strike** — the 50-delta call/put (strikes are typically even 100-point intervals on Nifty/Sensex)
2. **Buy legs:** 1 call + 1 put at ATM premium (e.g., call ₹180, put ₹135)
3. **Sell legs:** Divide each buy premium by 3, then sell 3 legs at that target price
   - Call: ₹180 ÷ 3 = 60 → sell 3 calls at ~60 (or closest market price ~67)
   - Put: ₹135 ÷ 3 = 45 → sell 3 puts at ~45 (or closest market price ~46)
4. **Payoff profile:** Forms a "Batman" or double-straddle shape; steep loss boundaries at 1.2–1.5% up/down from ATM on either side

**Greeks management:**
- **Vega:** Strongly short (3 short legs per side = high volatility sensitivity). Mitigated by holding to expiry when IV collapse accelerates. Risky if taken pre-expiry.
- **Theta:** Strongly positive. Peak on expiry day; every 15 min of time decay drives profit.
- **Delta:** Near-neutral at entry; converges to intrinsic by 3:27 PM close.

**Exit rules:**
- **Profit:** No target. Let theta run through close (3:27 PM) or exit early if comfortable. Realized profit typically 0.7–1.4% on deployed margin.
- **Loss:** Hard 1% stop loss on margin deployed. Exit immediately upon hitting 1% unrealized loss. Zero discretion; no averaging, no hope.

**Reason for hard 1% rule:** If 1% loss is taken, the next expiry's 1% profit is insufficient to fully recover (2-week recovery cycle). Loss management is the only controllable variable; profit is a secondary outcome of time decay.

**Backtesting (NSE Nifty/Sensex, April–June 2026):**
- 8 consecutive expiries tested (war-volatility period)
- Win rate: 83% (5 profitable, 1 loss, 2 breakeven)
- Avg ROI per expiry: ~0.9–1.4% on margin (highly consistent)
- Margin deployed: ~₹6.5 lakh on expiry day (SEBI mandates higher margin on expiry vs. non-expiry)
- Tradeable 2×/week: Nifty (Tuesday) + Sensex (Thursday)

**Why expiry day works:**
- Market consolidates in ~1–1.5% range historically (M-shape, N-shape, or trending; all profitable within the breakeven range)
- OI built over weeks creates pressure to pin strikes or trap traders; theta captures this via time decay
- No chart reading required; structure is agnostic to direction

**Execution requirement:** Fully mechanical entry (time + ATM + divide/multiply by 3); holding discipline (1% SL or to close); no discretion or bias. Backtesting shows consistency even under high-vol/war conditions.

**Caveats:**
- Tested only on index (Nifty/Sensex). Scaling to 10+ lots and slippage impact unknown.
- Single-lot examples; psychological cost of loss-then-recovery cycles (1% loss + 1% win) may test discipline.
- Capital efficiency: ₹6.5k profit on ₹6.5L margin = ~0.1% net ROI per expiry after loss cases; compare to alternative spreads (strangles, condors) for competitive positioning.
- Vega-short profile is aggressive; works only on expiry day when IV collapse offsets. Pre-expiry deployment is high-risk.
