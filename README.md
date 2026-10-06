# Blossom Planner

A word game planner for the daily [Blossom](https://www.merriam-webster.com/games/blossom-word-game) puzzle.

## What it does

Paste the day's 7 letters, find all valid words from the dictionary, and plan your word selection across the 6 petals — with correct scoring, bonus tracking, and pangram detection.

## How to use

1. Open the app (see links below)
2. Paste the 7 letters into the intake textarea (center letter first, then outer petals)
3. Click **Load Letters** — fills the grid
4. Type to search words, or click any word from the dictionary search to add it
5. Click words to place them into petal slots for scoring

## Scoring (correct Blossom rules)

| Length | Points |
|--------|--------|
| 4 letters | 2 |
| 5 letters | 4 |
| 6 letters | 6 |
| 7 letters | 12 |
| 8+ letters | 12 + 3 per extra letter |

- **Bonus petal**: +5 points each use
- **Pangram** (uses all 7 letters): +7 bonus

## Deployment

### Tailscale (jeff-lab)
- URL: `https://jeff-lab.tail40ed1d.ts.net`
- Server: `server.py` (Python HTTP, serves static files + dictionary)
- Dictionary: `blossom-dictionary.txt`

### Self-host
```bash
python3 server.py 6142
```
Then open `http://localhost:6142` or `http://<your-ip>:6142`.

## Tech

Single HTML file, no dependencies, no build step. Python `http.server` for hosting.

## License

MIT
