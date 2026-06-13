# Knowledge Base — Journal & Process Prompts

Curated trading psychology, process habits, and journal prompts from transcript analysis.
Link back to the source finding for full context.

---

<!-- Entries added here when a prompt warrants permanent curation -->

---

---
tags: [edge-calculation, journaling, metrics, automation, nse]
source: findings/2175knd26Yw.md
added: 2026-06-13
---

## Trade Data Dump — Edge Numbers + Time-to-Goal

**Source:** [findings/2175knd26Yw.md](../findings/2175knd26Yw.md)

Export broker console data (Zerodha: Reports → Tradebook, filter by date range) and paste into a Claude session with this prompt:

> "Here is my trade export. Tell me: total trades, win rate, average winner, average loser, profit factor, and edge ratio. Then project: at this performance rate, starting from ₹[X] capital, how long to reach ₹[Y]? Show assumptions."

**Why it works:** Forces quantitative self-assessment without manual journaling. The forward projection is the key output — if the number is too large (e.g. 7 years), it forces a system-level rethink (position sizing, strategy selection) rather than tactical tweaks.

**For options (NiftyShield adaptation):** Use the same prompt on options P&L exports. Key metrics to request: avg credit collected per strangle, win rate (expired worthless), avg loss on breached positions, return on margin deployed. Ask Claude to compute annualized return on margin as the primary KPI.

**Cadence:** Run monthly. Compare period-over-period to detect drift in edge.

---

---
tags: [process, psychology, edge-calculation, journaling]
source: findings/2175knd26Yw.md
added: 2026-06-13
---

## Three S's — Strategy vs Setup vs System

**Source:** [findings/2175knd26Yw.md](../findings/2175knd26Yw.md)

Most trading education stops at Strategy (entry/exit rules). Fewer teach Setup (pattern identification). Almost none teach System (treating trading as a repeatable business process with metrics, reviews, and consistent position sizing).

**Journal prompt:** "Am I losing because my strategy is wrong, or because I don't have a system? What would I need to measure to know the difference?"

Real consistency only comes at the System level. If results are inconsistent, the bottleneck is almost always System — not Strategy.
