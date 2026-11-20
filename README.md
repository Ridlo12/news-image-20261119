![make.fun](https://make.fun/badge/news-image-20261119.svg)
![Rank](https://make.fun/badge/news-image-20261119/Ridlo12/news-image-20261119/rank.svg)
![Reward](https://make.fun/badge/news-image-20261119/Ridlo12/news-image-20261119/reward.svg)

# news-image-20261119

A newspaper-style infographic of the world on 19 November 2026, built for
the make.fun News Image competition (`news-image-20261119`).

The image tells the day in six stories, with no outside feed needed: the
Trump–Xi–Putin meeting in Shenzhen; the ICJ ruling that Myanmar committed
genocide against the Rohingya — the first genocide ruling against Myanmar,
closing the case over the 2017 military campaign against the Rohingya; the
Anthropic IPO at roughly $81 billion; the release of GTA VI; the US–Iran
war and the Senate's 51–48 vote; and Jeffries as Speaker candidate. The
ICJ headline is the centrepiece: the court's genocide finding is the first
of its kind against Myanmar, and it closes a case that began with the
2017 campaign against the Rohingya.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

`main.py` uses only the Python standard library. It does not draw or
re-render anything: it copies the finished 1024x1024 `entry.png` into the
output directory and checks that the copy has the same size as the source.
Because the program only copies the image, every run writes the exact same
bytes.
