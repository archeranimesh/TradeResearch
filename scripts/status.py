"""TradeResearch pipeline status — shows processed and pending transcripts.

Compares transcripts/ against findings/ to determine processing state.
For pending transcripts, fetches YouTube metadata via oEmbed.

Usage:
    python scripts/status.py              # full report
    python scripts/status.py --pending    # pending only (no metadata fetch for processed)
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
TRANSCRIPTS_DIR = ROOT / "transcripts"
FINDINGS_DIR = ROOT / "findings"
OEMBED_BASE = "https://www.youtube.com/oembed"

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def fetch_metadata(video_id: str) -> dict | None:
    """Fetch title and channel via YouTube oEmbed. Returns None on failure."""
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    params = urllib.parse.urlencode({"url": video_url, "format": "json"})
    try:
        with urllib.request.urlopen(f"{OEMBED_BASE}?{params}", timeout=10) as r:
            data = json.loads(r.read().decode())
        return {
            "title": data.get("title", "Unknown"),
            "channel": data.get("author_name", "Unknown"),
            "url": video_url,
        }
    except Exception:
        return None


def get_ids(directory: Path, suffix: str) -> set[str]:
    return {p.stem for p in directory.glob(f"*{suffix}")}


def reading_time_estimate(video_id: str) -> str:
    """Rough transcript size → estimated video length."""
    path = TRANSCRIPTS_DIR / f"{video_id}.txt"
    if not path.exists():
        return ""
    size = path.stat().st_size
    # ~1000 chars/min of speech is a rough approximation
    minutes = size // 1000
    return f"~{minutes}min" if minutes else "<1min"


def main() -> None:
    parser = argparse.ArgumentParser(description="TradeResearch pipeline status")
    parser.add_argument(
        "--pending", action="store_true", help="Show pending transcripts only"
    )
    parser.add_argument(
        "--no-fetch", action="store_true", help="Skip YouTube metadata fetch"
    )
    args = parser.parse_args()

    transcript_ids = get_ids(TRANSCRIPTS_DIR, ".txt")
    finding_ids = get_ids(FINDINGS_DIR, ".md")

    # Remove .gitkeep if present
    finding_ids.discard(".gitkeep")

    processed = transcript_ids & finding_ids
    pending = transcript_ids - finding_ids
    orphaned = finding_ids - transcript_ids  # findings with no transcript (manual or deleted)

    print(f"\n{BOLD}TradeResearch — Pipeline Status{RESET}")
    print(f"{'─' * 50}")
    print(f"  Transcripts : {len(transcript_ids)}")
    print(f"  Processed   : {GREEN}{len(processed)}{RESET}")
    print(f"  Pending     : {YELLOW}{len(pending)}{RESET}")
    if orphaned:
        print(f"  Orphaned    : {RED}{len(orphaned)}{RESET}  (findings without transcripts)")
    print(f"{'─' * 50}\n")

    if not args.pending and processed:
        print(f"{BOLD}✓ Processed{RESET}")
        for vid in sorted(processed):
            finding_path = FINDINGS_DIR / f"{vid}.md"
            mtime = finding_path.stat().st_mtime
            from datetime import datetime
            analyzed = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            print(f"  {GREEN}●{RESET} {vid}  (analyzed {analyzed})")
        print()

    if pending:
        print(f"{BOLD}⏳ Pending{RESET}")
        for vid in sorted(pending):
            est = reading_time_estimate(vid)
            if args.no_fetch:
                print(f"  {YELLOW}○{RESET} {vid}  [{est}]")
            else:
                meta = fetch_metadata(vid)
                if meta:
                    title = meta["title"][:65] + "…" if len(meta["title"]) > 65 else meta["title"]
                    print(f"  {YELLOW}○{RESET} {vid}  [{est}]")
                    print(f"       {title}")
                    print(f"       {meta['channel']}")
                else:
                    print(f"  {YELLOW}○{RESET} {vid}  [{est}]  (metadata unavailable)")
        print()

    if orphaned:
        print(f"{BOLD}{RED}⚠ Orphaned findings (no transcript){RESET}")
        for vid in sorted(orphaned):
            print(f"  {RED}?{RESET} {vid}")
        print()

    # Summary line
    total = len(transcript_ids)
    if total == 0:
        print("No transcripts found. Drop .txt files into transcripts/ to get started.\n")
    elif not pending:
        print(f"{GREEN}All transcripts processed.{RESET}\n")
    else:
        pct = int(len(processed) / total * 100)
        print(f"Progress: {len(processed)}/{total} ({pct}%)\n")


if __name__ == "__main__":
    main()
