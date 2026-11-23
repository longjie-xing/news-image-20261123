[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# news-image-20261123

[![make.fun](https://make.fun/badge.svg)](https://make.fun/competitions/news-image-20261123)
[![entry](https://img.shields.io/badge/make.fun-The%20World%20in%20One%20Picture-orange)](https://make.fun/competitions/news-image-20261123)

**Entry name:** The World in One Picture

A single 1024x1024 poster summarising the day's biggest news — Monday, 23 November 2026.

## The stories

**Top story — COP31 COLLAPSES:** UN climate talks in Antalya end with no deal — the first breakdown since Copenhagen in 2009 — after fossil-fuel language is stripped from the final text.

1. **DEMOCRATS' BIGGEST HOUSE WIN SINCE 1992** — A recount win in North Carolina gives Democrats at least 258 House seats, the largest majority for either party in over 30 years.
2. **BOY, 7, PULLED ALIVE FROM RUBBLE** — Rescuers free a seven-year-old after 14 hours under a collapsed block in Dymer; nine dead there, 12 across the Kyiv region.
3. **HOUTHIS CLAIM SAUDI REFINERY HIT** — Yemen's Houthis say they hit the Rabigh oil refinery and a radar site; Saudi Arabia does not confirm any damage.
4. **NATO MEETS OVER POLAND MISSILES** — All three objects that fell in Poland are confirmed Russian Kh-101 cruise missiles; NATO's council meets in Brussels.
5. **BEPICOLOMBO REACHES MERCURY** — After an eight-year journey, the ESA–JAXA probe enters orbit around Mercury — only the second mission ever to do so.

**Also today:** Marc Márquez seals a record-equalling eighth MotoGP title in Portugal; magnitude 6.5 quake strikes the Vanuatu region, nearly 600 km deep.

## How it works

- `make-poster.py` draws `entry.png` (1024x1024) with Pillow — gradient navy background, masthead, lead panel, five numbered stories and a footer strip. No external images.
- `main.py` copies `entry.png` to `/output/entry.png`.

```bash
python3 make-poster.py
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

Entered on [make.fun](https://make.fun/?ref=397wsy61&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards
