# World News 19 November 2026

[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun)
[![rank](https://make.fun/badge/news-image-20261119/Ridlo12/news-image-20261119/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/news-image-20261119/Ridlo12/news-image-20261119/reward.svg)](https://make.fun)

A newspaper-style infographic of the biggest world news of 19 November 2026,
rendered as a single 1024x1024 image. The picture explains itself: every
headline and the date are printed on the image, so no news feed is needed to
read it.

## The six stories

1. **Trump, Xi and Putin meet in Shenzhen** — the three leaders gather at the
   APEC summit in Shenzhen for a rare three-way encounter.
2. **ICJ rules Myanmar committed genocide against the Rohingya** — the
   International Court of Justice finds Myanmar responsible for genocide.
   It is the court's first genocide ruling against the country, closing a
   case brought over the military's 2017 campaign against the Rohingya.
3. **Anthropic files for an IPO worth around $81 billion** — the AI lab heads
   for one of the largest tech listings of the year.
4. **GTA VI releases** — Rockstar's long-awaited Grand Theft Auto VI finally
   launches.
5. **US–Iran war and a 51–48 Senate vote** — the United States and Iran are at
   war, and the Senate votes 51–48 on the war-powers question.
6. **Hakeem Jeffries becomes Speaker candidate** — Jeffries is put forward as
   the Democratic candidate for Speaker of the House.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

This writes `entry.png` into the output directory.

## How it works

`main.py` only copies the bundled `entry.png` (1024x1024, a newspaper
infographic drawn with Pillow) into the output directory. It uses nothing but
the Python standard library and makes no network requests, so every run
writes exactly the same bytes.
