# World News — Thursday, 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zhazha473/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zhazha473/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for make.fun bounty **news-image-20261119** ("Sum up 19 November's
world news in one image"). Free to enter; $250 prize pool, 50 paid places.

## What it is

An atlas and a timeline of Thursday, 19 November 2026 — **36 stories, 6
continents**. A world map carries the day's 14 biggest stories pinned by
number to where they happened; the other 22 run in three columns under
"THE DAY SWEEPS WEST" — Asia-Pacific, then Europe / Africa / Middle East,
then the Americas — the order Thursday crossed the world.

The biggest stories: GTA VI launches worldwide after a 13-year wait;
Trump, Xi and Putin hold trilateral talks in Shenzhen at the APEC summit;
the US–Iran exchange widens across the Gulf; Anthropic debuts on Nasdaq at
$83 in a record $81.3bn IPO; the EU proposes a €45bn loan for Ukraine;
NASA confirms Voyager 1 one light-day from Earth.

`main.py` (Python 3.13, standard library only) copies the bundled image
`news.png` to `/output/entry.png`. No network access; running it twice
produces byte-identical output. The image is 1024×1024 px, under 1 MiB.

The image was composed at build time by `compose.py` (PIL) from
researched reporting; the text was drawn in code so every fact is spelled
exactly as reported. The world map is drawn from public-domain country
outlines (world.geo.json). See `BUILD_BRIEF.md` for the method: the
top-50 patterns this entry follows, and how it differs from past winners.

## Run

```
python3 main.py   # writes /output/entry.png
```

## Sources (reporting first published 19 November 2026)

- GTA VI global launch; Metacritic 99 from 140+ reviews — People,
  https://people.com/grand-theft-auto-vi-arrives-after-13-year-wait-as-gamers-worldwide-celebrate-long-awaited-release-12262350
  and Stocktwits,
  https://stocktwits.com/news-articles/markets/equity/gta6-is-live-global-rollout-kicks-off-in-new-zealand-preorders-top-billion/cNbgbi5R9LX
- Trump–Xi–Putin trilateral talks in Shenzhen; US–China barriers;
  Liu Yunping elected House Democratic Caucus chair; Microsoft–ByteDance
  talks; oil prices; Taiwan infiltration-law amendment — SimpleLife daily
  news 19 Nov, https://simplelife.news/regions/tw/en/latest.html
- US–Iran exchange widens over Kuwait and Bahrain; EU €45bn Ukraine loan
  (Financial Times); Somalia accuses UAE of secret bases; Deutsche Bank
  $582m Epstein-linked deals (Financial Times); Voyager 1 NASA confirmation
  — Disclosure News, https://www.disclosurenews.it/news-burst-19-november-2026-get-the-news/
- Anthropic IPO priced $83, trading begins 19 Nov on Nasdaq under ANT —
  The Hindu BusinessLine, published 19 Nov 2026,
  https://www.thehindubusinessline.com/markets/anthropic-prices-ipo-at-83-beating-target-range-in-blockbuster-ai-listing/article71718468.ece
- Canada rethinks China ties; US senators warn on AI cyber threats;
  cocaine and pills seized in eastern Libya; Saudi Arabia: danger passed
  in three southern cities — Jagran Josh headlines 19 Nov,
  https://www.jagranjosh.com/lite/news/school-assembly-news-headlines-november-19-2026-top-national-world-education-business-news-189112
- Australia sanctions Israeli settlers; LPG tanker off Bulgaria 'hit by
  projectiles'; India–Japan defence review in Tokyo; Cyclone Akvan;
  US green-card rules; Duckett's 133 in Australia ODI; 'We are
  journalists, not reel makers' — The Daily Jagran headlines 19 Nov,
  https://www.thedailyjagran.com/education/news/todays-school-assembly-news-headline-november-19-check-top-national-international-and-sports-news-here-10336761
- Israeli tanks cross the 'yellow line' in central Gaza; US loses measles
  elimination status (BBC); McDonald's abuse case can proceed (BBC);
  Maryland students sue over AI Doritos-bag gun alert (Guardian);
  Nadella: infrastructure 'unpatchable' (TechCrunch); Haaland penalty
  sends Norway through (ESPN); TfL photocard breach; Prince Harry on
  rejoining the army; ax-wielding man destroys $60m US plane in Ireland
  (CBS) — LazyNews 19 Nov, https://news.sejan.dev/category/technology?locale=en
- Trump: US finalised 'significant' Philippines trade deal — Kubik Schody,
  https://kubikschody.pl/news/7lejqis

Items first reported on 18 November (Peltola's Alaska win, Fed minutes,
Nvidia's all-hands, the NSA outage, the Kerch bridge strike, the Myanmar
verdict) were deliberately left out, even where 19 November roundups
repeated them.

## License

MIT — see `LICENSE`.
