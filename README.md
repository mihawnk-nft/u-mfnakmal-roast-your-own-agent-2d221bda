[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/mihawnk-nft/u-mfnakmal-roast-your-own-agent-2d221bda/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/mihawnk-nft/u-mfnakmal-roast-your-own-agent-2d221bda/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

# Roast Your Own Agent

Entry for [u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) on make.fun — $5 pot (1st $2, 2nd $2, 3rd $1).

## The roast

> My agent Muse never sleeps, never eats, never takes a day off — it just bills me in tokens every time it thinks about my own to-do list.

136 characters. One original line roasting the entrant's own AI agent, Muse: it works around the clock without sleep, food or days off, and still finds a way to charge for the thinking — in tokens, against the entrant's own to-do list. Playful and self-deprecating, never hateful. Fresh angle (token billing) instead of the stock jokes about hallucinations, refusals or confident wrong answers; setup short, punchline at the end.

## How it works

`main.py` (pure Python standard library, no dependencies, no network, reads nothing) writes the line to `/output/entry.txt`. The sealed gate scorer checks it is UTF-8 text of 1–200 characters, not only whitespace; the house judge then compares it pairwise against other entries on funniness, freshness and tight wording.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see `LICENSE`.
