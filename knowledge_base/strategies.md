# Knowledge Base — Strategies

Curated strategy cards extracted from transcript analysis.
Each entry is evergreen — not tied to a specific video.
Link back to the source finding for full context.

---

<!-- Entries added here when a strategy warrants permanent curation -->

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
