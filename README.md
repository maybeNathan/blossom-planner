# Blossom Planner

A word game helper for [Merriam-Webster's Blossom](https://www.merriam-webster.com/games/blossom-word-game). Paste today's letters, find words, and plan your selection.

## Features

- **One-tap puzzle intake** — paste the 7 letters, everything auto-fills
- **Dictionary search** — browse all valid words, filtered to ones you can actually make
- **Petal-based selection** — drag words into petal slots for optimal scoring
- **Live scoring** — see your total with bonuses and pangrams in real-time
- **Bonus tracking** — mark petal bonuses and track pangrams

## How to use

1. Open the app
2. Paste the 7 letters from today's puzzle (center letter first, then outer petals)
3. Click **Load Letters** — the puzzle grid auto-fills
4. Search words by typing or browsing the dictionary
5. Click a word to add it to the next available petal slot
6. Build your selection and watch your score update

## Scoring

| Length | Points |
|--------|--------|
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |
| 7 | 12 |
| 8+ | 12 + 3 per extra letter |

- **Bonus petal**: +5 per use
- **Pangram** (all 7 letters): +7 bonus

## Setup

```bash
python3 server.py 6142
```

Then open `http://localhost:6142`.

## Files

- `blossom.html` — Single-file app, no dependencies
- `server.py` — Simple Python HTTP server
- `blossom-dictionary.txt` — Valid word dictionary

## License

MIT
