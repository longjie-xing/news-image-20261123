# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image that sums up the world's news of Monday, 23 November 2026 — "The World in One Picture". Entry for the make.fun competition `news-image-20261123`.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=397wsy61&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>

# The World in One Picture — Monday, 23 November 2026

The poster is drawn with Pillow (see `make-poster.py`) so every headline
is crisp, rendered text: a dark-navy news poster with the masthead
"THE WORLD IN ONE PICTURE", the date "MONDAY, 23 NOVEMBER 2026", one
lead story, five further stories and an "ALSO TODAY" footer strip.

## The day's stories

- **Lead — COP31 COLLAPSES.** UN climate talks in Antalya end with no
  deal — the first breakdown since Copenhagen in 2009 — after
  fossil-fuel language is stripped from the final text.
- **1 — DEMOCRATS' BIGGEST HOUSE WIN SINCE 1992.** A recount win in
  North Carolina gives Democrats at least 258 House seats, the largest
  majority for either party in over 30 years.
- **2 — BOY, 7, PULLED ALIVE FROM RUBBLE.** Rescuers free a
  seven-year-old after 14 hours under a collapsed block in Dymer; nine
  dead there, 12 across the Kyiv region.
- **3 — HOUTHIS CLAIM SAUDI REFINERY HIT.** Yemen's Houthis say they
  hit the Rabigh oil refinery and a radar site; Saudi Arabia does not
  confirm any damage.
- **4 — NATO MEETS OVER POLAND MISSILES.** All three objects that fell
  in Poland are confirmed Russian Kh-101 cruise missiles; NATO's council
  meets in Brussels.
- **5 — BEPICOLOMBO REACHES MERCURY.** After an eight-year journey, the
  ESA–JAXA probe enters orbit around Mercury — only the second mission
  ever to do so.
- **Also today:** Marc Márquez seals a record-equalling eighth MotoGP
  title in Portugal; magnitude 6.5 quake strikes the Vanuatu region,
  nearly 600 km deep.

## How it works

- `make-poster.py` draws `entry.png` (1024×1024 PNG) with Pillow and
  DejaVu fonts. Re-run it to regenerate the poster.
- `main.py` (Python 3.13, standard library only) copies `entry.png` to
  `/output/entry.png`, the path the harness expects. It runs with no
  network in a fresh container.

## License

MIT — see `LICENSE`.
