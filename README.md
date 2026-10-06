# Blossom Planner

A helper for [Merriam-Webster's Blossom](https://www.merriam-webster.com/games/blossom-word-game), the daily word puzzle.

## What it does

Blossom gives you 7 letters (center + 6 petals) and you need to find 12 words. This app lets you:

- Paste today's 7 letters once and have everything auto-populate
- Search the full dictionary for valid words you can form
- Organize words into petal slots for optimal scoring
- See your total score with live updates

## How to use

1. Open the app
2. Paste the 7 letters into the textarea (center first, then petals)
3. Click **Load Letters** — the grid auto-fills
4. Type in the word search to filter, or browse the dictionary
5. Click a word to add it to the next available petal slot
6. Build your selection and track your score

## Scoring

| Word length | Points |
|-------------|--------|
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |
| 7 | 12 |
| 8+ | 12 + 3 per extra letter |

- **Bonus petal**: +5 each use
- **Pangram** (all 7 letters): +7 bonus

## Setup

```bash
python3 server.py 6142
```

Then open `http://localhost:6142`.

## Files

- `blossom.html` — Single-file app (HTML + CSS + JS, no dependencies)
- `server.py` — Python HTTP server
- `blossom-dictionary.txt` — Valid word dictionary

## License

MIT
