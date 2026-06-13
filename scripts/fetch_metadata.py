"""Fetch YouTube video metadata (title, channel) from a video ID via oEmbed API.

Usage:
    python scripts/fetch_metadata.py <video_id>
    python scripts/fetch_metadata.py 2175knd26Yw

Output (JSON to stdout):
    {"video_id": "...", "title": "...", "channel": "...", "url": "..."}
"""

import json
import sys
import urllib.request
import urllib.parse
import urllib.error


_OEMBED_BASE = "https://www.youtube.com/oembed"


def fetch_metadata(video_id: str) -> dict:
    """Fetch title and channel for a YouTube video ID via oEmbed.

    Args:
        video_id: The YouTube video ID (e.g., "2175knd26Yw").

    Returns:
        Dict with keys: video_id, title, channel, url.

    Raises:
        ValueError: If video_id is empty.
        urllib.error.URLError: If the network request fails.
        RuntimeError: If the API returns unexpected data.
    """
    if not video_id:
        raise ValueError("video_id must not be empty")

    video_url = f"https://www.youtube.com/watch?v={video_id}"
    params = urllib.parse.urlencode({"url": video_url, "format": "json"})
    request_url = f"{_OEMBED_BASE}?{params}"

    with urllib.request.urlopen(request_url, timeout=10) as response:
        data = json.loads(response.read().decode())

    title = data.get("title")
    channel = data.get("author_name")

    if not title or not channel:
        raise RuntimeError(f"Unexpected oEmbed response: {data}")

    return {
        "video_id": video_id,
        "title": title,
        "channel": channel,
        "url": video_url,
    }


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/fetch_metadata.py <video_id>", file=sys.stderr)
        sys.exit(1)

    video_id = sys.argv[1].strip()

    try:
        result = fetch_metadata(video_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code}: video not found or private", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
