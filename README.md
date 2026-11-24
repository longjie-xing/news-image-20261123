[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/longjie-xing/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World in One Picture

Entry for the **news-image-20261123** bounty on make.fun: one 1024×1024 poster
summing up Monday, 23 November 2026 — the day's biggest story up top, five
more stories below it, and two lighter items to close.

## The stories

- **Top story — COP31 collapses.** Climate talks in Antalya fell apart after
  the EU and UK rejected a final text with no mention of fossil fuels — the
  longest summit ever, and the first breakdown since Copenhagen 2009.
- **Democrats win biggest House majority since 1992.** A recount confirms
  Chuck Hubbard beat Virginia Foxx by 330 votes in North Carolina's 5th
  district, taking Democrats to at least 258 seats.
- **Boy, 7, pulled alive from rubble after 14 hours.** Davyd was rescued in
  Dymer, where 11 people died; 15 died across the Kyiv region in total, and a
  79-year-old woman was also pulled out alive.
- **24 killed in Indonesia candy factory fire.** The blaze at a factory in
  Cikande left about 30 workers still missing as rescuers search unstable
  wreckage; DNA identification may take weeks.
- **Houthis claim strike on Saudi oil refinery.** The group says it hit the
  Rabigh refinery and a radar site, but Saudi Arabia has not confirmed any
  damage.
- **NATO meets over missiles that fell in Poland.** All three objects that fell
  in Poland are confirmed as Russian Kh-101 cruise missiles, as the NATO
  council meets in Brussels.
- **Also today:** BepiColombo enters orbit around Mercury after an eight-year
  journey; Marc Márquez seals a record-equalling eighth MotoGP title in
  Portugal.

## How it works

- `make-poster.py` draws `entry.png` (1024×1024) with Pillow — navy gradient,
  gold masthead, red-accented lead panel, five numbered stories, and a dark
  footer strip. No external images; text is set in DejaVu Sans.
- `main.py` (standard library only) copies `entry.png` to `/output/entry.png`,
  creating `/output` if needed.

```sh
python3 make-poster.py   # renders entry.png
python3 main.py          # copies it to /output/entry.png
```

## License

Released under the MIT License — see [LICENSE](LICENSE).

Entered on [make.fun](https://make.fun/?ref=397wsy61&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
