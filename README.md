[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# news-image-20261123

[![make.fun](https://make.fun/badge.svg)](https://make.fun/competitions/news-image-20261123)
[![entry](https://img.shields.io/badge/make.fun-The%20World%20in%20One%20Picture-orange)](https://make.fun/competitions/news-image-20261123)

**Entry name:** The World in One Picture

A single 1024x1024 poster summarising the day's biggest news — Monday, 23 November 2026.

## The stories

**Top story — COP31 COLLAPSES:** EU and UK reject the final text — no mention of fossil fuels — as the longest climate summit in history ends with no deal, the first breakdown since Copenhagen in 2009.

1. **DEMOCRATS' BIGGEST HOUSE WIN SINCE 1992** — A recount confirms Chuck Hubbard's 330-vote win over Virginia Foxx in North Carolina, giving Democrats at least 258 House seats — the largest majority in over 30 years.
2. **BOY, 7, PULLED ALIVE FROM RUBBLE** — Davyd survives nearly 14 hours under a collapsed block in Dymer; 11 dead there, 15 across the Kyiv region. A 79-year-old woman is also rescued alive.
3. **24 KILLED IN INDONESIA FACTORY FIRE** — A blaze guts a candy factory in Cikande; about 30 workers are still missing as rescuers search the unstable wreckage. DNA tests may take weeks.
4. **HOUTHIS CLAIM SAUDI REFINERY HIT** — Yemen's Houthis say they hit the Rabigh oil refinery and a radar site; Saudi Arabia does not confirm any damage.
5. **NATO MEETS OVER POLAND MISSILES** — All three objects that fell in Poland are confirmed Russian Kh-101 cruise missiles; NATO's council meets in Brussels.

**Also today:** BepiColombo enters orbit around Mercury after an eight-year journey; Marc Márquez seals a record-equalling eighth MotoGP title in Portugal.

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
