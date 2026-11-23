# The World in One Day — 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/nofrizal05/makefun-news-23nov/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/nofrizal05/makefun-news-23nov/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the make.fun competition **news-image-20261123**: "Sum up
23 November's world news in one image" ($100, entries close 2026-11-25 07:00 WIB).

Bounty page: https://make.fun/bounty/news-image-20261123

A hero-led newspaper front page (1024×1024) for Monday, 23 November 2026:

- **Lead story — Climate talks collapse.** COP31 in Antalya ends without a
  climate pact after two weeks and two days of overtime — the longest COP
  ever — because the final draft never mentions fossil fuels. The UN chief
  calls it "deeply disappointing".
- **Drone hits Kyiv region building** — at least 14 people missing,
  President Zelenskiy says.
- **Hormuz conflict at a crucial stage** — the Iran–US war engulfs Saudi
  Arabia and Bahrain; a coalition intercepts a Houthi missile.
- **Factory fire in Indonesia** — 7 dead, 50 missing.
- **South Korea minister quits over AI exam cheating** — education chief
  Choi Kyo-jin resigns after anti-cheating measures cause chaos.
- **Nepal PM meets Modi in Delhi** — Balendra Shah on a state visit.
- **India pile up a record 720/9d** in the Wellington Test against
  New Zealand.
- Footer strip: Lisbon marches over living costs, UN talks on lethal AI
  weapons continue, Mexico seizes 'El Chapo Isidro' (11 killed), Russian
  cargo ship still burning off Finland, ICJ rules Myanmar committed
  genocide against the Rohingya, Waymo pulls driverless taxis off US
  freeways.

## How it works

`main.py` is Python standard library only (`hashlib`, `os`, `shutil`,
`struct`, `pathlib`): it validates the shipped `entry.png` (PNG signature,
1024×1024 IHDR dimensions, under 1 MiB) and copies it to
`MAKEFUN_OUTPUT_DIR` (default `/output`), then verifies the copy's SHA-256
against the expected hash. A corrupt or swapped asset fails loudly instead
of scoring silently.
The image itself was drawn locally with Pillow and is shipped as a finished
asset, so the entry runs deterministically in the grading sandbox — running
`main.py` twice writes byte-identical output.

## Verify locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png  # identical
file /tmp/out1/entry.png                            # 1024x1024 PNG, < 1 MiB
```
