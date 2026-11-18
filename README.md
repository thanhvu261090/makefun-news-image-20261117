# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/thanhvu261090/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/thanhvu261090/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A one-page picture of the world's news of **Tuesday 17 November 2026**, drawn as a
newspaper front page: masthead, date banner, and the day's stories as headlines with
short supporting lines, so a viewer who missed the day can tell what happened from
the image alone.

Stories covered (all as reported on 17 November 2026):

- **Lead — Ukraine strikes the Crimean Bridge again** as Russia hits Kyiv's
  crossings: a second attack on the Kerch Bridge in under 24 hours, and Russian
  missiles damage two bridges in Kyiv. Zelenskyy hails "an unprecedented operation".
- **Iran drones target a US radar in Bahrain**: the Revolutionary Guard says it
  struck the radar at Sheikh Isa base; Bahrain says the drones were intercepted
  and no one was hurt.
- **Xi, Trump and Putin to meet in Shenzhen**: China confirms the first three-way
  summit of the three leaders, on Thursday on the sidelines of the APEC meeting.
- **Gaza aid warning as winter closes in**: UN agencies say 1.7 million people are
  still displaced and about 1.4 million face acute hunger; Western states urge
  Israel to open crossings.
- **Cyberattack hits 178 major websites**: malicious code spread through Optimizely
  targeted visitors to the BBC, CNN, Zoom and HSBC, aiming to steal crypto and
  card data.
- **Also today**: Japan scrambles fighter jets after two suspected Russian aircraft
  enter its airspace; Gérard Depardieu pleads guilty to sexual assault and drops
  his appeal; Jay Shah is re-elected chairman of the International Cricket Council.

The image is rendered programmatically (Python + Pillow, DejaVu fonts) at exactly
1024×1024 so every headline is spelled correctly and legible; no AI image
generator was used for the text.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when the variable is
unset). It runs twice and writes the same bytes both times.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
