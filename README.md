# Blossom Planner

A helper for the daily [Blossom](https://www.merriam-webster.com/games/blossom-word-game) puzzle by Merriam-Webster. Plan your word selection and maximize your score.

## What it does

Blossom is a daily word game where you're given 7 letters (center + 6 petals) and need to form 12 words. This planner lets you:

- Enter the day's puzzle letters once and have everything auto-populate
- Search the dictionary for all valid words that use your letters
- Organize words across the 6 petals for optimal scoring
- See your total score in real-time with correct Blossom rules

## Features

- **Puzzle intake**: Paste the 7 letters once, app fills the config grid
- **Auto-suggestions**: Type to search, filtered to words you can actually form
- **Selection panel**: Organize words by petal letter, click to add
- **Drag-and-drop**: Drag words from the list into petal slots
- **Live scoring**: See points, bonuses, and pangrams as you build your selection
- **Dictionary search**: Browse the full reference dictionary

## Scoring

| Word length | Points |
|-------------|--------|
| 4 letters | 2 |
| 5 letters | 4 |
| 6 letters | 6 |
| 7 letters | 12 |
| 8+ letters | 12 + 3 per extra letter |

**Bonuses:**
- Bonus petal: +5 points each time you use it
- Pangram (uses all 7 letters): +7 bonus points

## How to use

1. Open the app
2. Paste the 7 letters from today's puzzle (center letter first, then outer petals)
3. Click **Load Letters** — the grid auto-fills
4. Type in the word input to search, or browse the dictionary
5. Click a word to add it to the next available petal slot
6. Build your selection and track your score

## Setup

### Quick start (Tailscale)

The app runs on Tailscale via funnel:

```
https://jeff-lab.tail40ed1d.ts.net
```

### Self-host

```bash
python3 server.py 6142
```

Then open `http://localhost:6142`.

## Files

- `blossom.html` — Single-file app (HTML + CSS + JS, no dependencies)
- `server.py` — Simple Python HTTP server
- `blossom-dictionary.txt` — Reference dictionary for valid words

## Tech

- Single HTML file, no build step, no dependencies
- Python `http.server` for hosting
- Responsive layout, works on desktop and mobile

## License

MIT
