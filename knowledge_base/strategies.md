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
