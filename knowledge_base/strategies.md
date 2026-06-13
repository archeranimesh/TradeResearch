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
