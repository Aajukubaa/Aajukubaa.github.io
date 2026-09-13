#!/usr/bin/env python3
"""
Fetches live Chess.com data and writes it to chess-data.json at the repo
root. The site's JavaScript reads that file directly (same-origin —
no browser CORS involved), because Chess.com's public API does not
reliably support CORS for direct browser fetch() calls, which is why
the dashboard was always failing to load when it tried to hit
api.chess.com straight from the page.

Run automatically by .github/workflows/build.yml (on every relevant
push, and on a schedule so ratings/games stay fresh even without a
push). Can also be run manually:

    pip install -r requirements.txt
    python fetch_chess_data.py
"""
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

USERNAME = "Aajukubaa"  # hardcoded per request
# Chess.com asks API consumers to identify themselves in the User-Agent;
# requests without one are more likely to get blocked with a 403.
HEADERS = {
    "User-Agent": (
        "AajukubaaPortfolioSite/1.0 (+https://aajukubaa.github.io; "
        "contact: kabirbhuchar@gmail.com)"
    )
}
OUTPUT_FILE = Path(__file__).parent / "chess-data.json"
MAX_GAMES = 10
MAX_MONTHS_BACK = 3  # keep looking back if the latest month or two are thin


def fetch_json(url: str) -> dict:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


def fetch_stats() -> dict:
    return fetch_json(f"https://api.chess.com/pub/player/{USERNAME.lower()}/stats")


def fetch_recent_games() -> list:
    archives = fetch_json(
        f"https://api.chess.com/pub/player/{USERNAME.lower()}/games/archives"
    ).get("archives", [])

    games = []
    for archive_url in reversed(archives[-MAX_MONTHS_BACK:]):
        month_games = fetch_json(archive_url).get("games", [])
        games.extend(g for g in month_games if g.get("pgn"))
        if len(games) >= MAX_GAMES:
            break

    games.sort(key=lambda g: g.get("end_time", 0), reverse=True)
    return games[:MAX_GAMES]


def main() -> None:
    data = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "username": USERNAME,
        "stats": None,
        "recent_games": [],
        "error": None,
    }

    errors = []
    try:
        data["stats"] = fetch_stats()
    except Exception as exc:  # noqa: BLE001 - want this to degrade gracefully, not crash CI
        errors.append(f"stats fetch failed: {exc}")

    try:
        data["recent_games"] = fetch_recent_games()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"games fetch failed: {exc}")

    if errors:
        data["error"] = "; ".join(errors)

    OUTPUT_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE} ({OUTPUT_FILE.stat().st_size:,} bytes)")
    if errors:
        print("Completed with errors:", data["error"])


if __name__ == "__main__":
    main()
