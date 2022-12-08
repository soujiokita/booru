# Booru
Python bindings for Booru imageboards

<a href="http://sinkaroid.github.io/booru"><img align="right" src="https://cdn.discordapp.com/attachments/952117487166705747/961124440400351232/mataa.png" width="400"></a>

- [Booru](#booru)
  - [Features](#features)
  - [This library vs. the Competition](#this-library-vs-the-competition)
    - [Benchmark quick tests](#benchmark-quick-tests)
  - [Usage](#usage)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Quick example](#quick-example)
      - [search](#search)
      - [get image](#get-image)
    - [Advanced example](#advanced-example)
      - [Armored search](#armored-search)
      - [Gacha-like](#gacha-like)
      - [Import you want to use](#import-you-want-to-use)
  - [Documentation](#documentation)
  - [Legal](#legal)  



<div align="center">

<a href="https://sinkaroid.github.io/booru"><img src="https://github.com/sinkaroid/booru/actions/workflows/docs.yml/badge.svg"></a>
<a href="https://github.com/sinkaroid/booru/actions/workflows/api.yml"><img src="https://github.com/sinkaroid/booru/actions/workflows/api.yml/badge.svg"></a>
<a href="https://codeclimate.com/github/sinkaroid/booru/maintainability"><img src="https://api.codeclimate.com/v1/badges/c334d91994d1d84b8d7d/maintainability" /></a>

Python bindings for the imageboards.
It is takes a much more functionalities to interacts with ease, and fully extendable. Making your API request significantly tidier and easier to comprehend

<b>
<a href="https://github.com/sinkaroid/booru/blob/master/CONTRIBUTING.md">Contributing</a> •
<a href="https://sinkaroid.github.io/booru">Documentation</a> •
<a href="https://github.com/sinkaroid/booru/issues/new/choose">Report Issues</a>
</b>
</div>

---

## Features
- Handle 19 different booru
- Minimalist dependencies
- Gacha-like built-in
- Documented and tested
- Easy to use, check your intelisense
- Support arranged, shuffle or raw data returns
- Out of the box, JSON friendly with fully extendable
- Armored-search, resolved safety tags concerns

## This library vs. the Competition

This benchmark search 100 items from each booru sites and returns the average response time  
Speed or perfomace may not accurate because internet connection or server response.
- **Stable**: fully functional | **Partial**: limited features | **Triage**: has some issues

- 🎲 Support random | 🕹️ Support gacha | 🎨 Extract images | 🛡️ Armored-search


### Benchmark quick tests

| Booru                                       | Status                                                                                                                                                   | Random | Tags block | Tags finder     | Get images     | Gacha     |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ----- | ----- | ----- | 
| [Gelbooru](https://gelbooru.com/)           | [![status](https://github.com/soujiokita/booru/workflows/Gelbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/gel.yml)            | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Danbooru](https://danbooru.donmai.us/)     | [![status](https://github.com/soujiokita/booru/workflows/Danbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/danbo.yml)  | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Rule34](https://rule34.xxx)                | [![status](https://github.com/soujiokita/booru/workflows/Rule34/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/r34.yml)        | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Realbooru](https://realbooru.com/)         | [![status](https://github.com/soujiokita/booru/workflows/Realbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/real.yml)       | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Tbib](https://tbib.org/)                   | [![status](https://github.com/soujiokita/booru/workflows/Tbib/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/tbib.yml)   | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Xbooru](https://xbooru.com/)               | [![status](https://github.com/soujiokita/booru/workflows/Xbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/xbo.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Safebooru](https://safebooru.org/)         | [![status](https://github.com/soujiokita/booru/workflows/Safebooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/safe.yml)   | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Yandere](https://yande.re/)                | [![status](https://github.com/soujiokita/booru/workflows/Yandere/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/yande.yml)   | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Lolibooru](https://lolibooru.moe/)         | [![status](https://github.com/soujiokita/booru/workflows/Lolibooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/loli.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Konachan](https://konachan.com/)           | [![status](https://github.com/soujiokita/booru/workflows/Konachan/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/kona.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Konachan.net](https://konachan.net/)       | [![status](https://github.com/soujiokita/booru/workflows/KonachanNet/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/konanet.yml) | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Hypnohub](https://hypnohub.net/)           | [![status](https://github.com/soujiokita/booru/workflows/Hypnohub/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/hypno.yml)  | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [E621](https://e621.net/)                   | [![status](https://github.com/soujiokita/booru/workflows/E621/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/e6.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [E926](https://e926.net/)                   | [![status](https://github.com/soujiokita/booru/workflows/E926/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/e9.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [Derpibooru](https://derpibooru.org/)       | [![status](https://github.com/soujiokita/booru/workflows/Derpibooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/derpi.yml)   | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [Furbooru](https://furbooru.org/)           | [![status](https://github.com/soujiokita/booru/workflows/Furbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/fur.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [ATFbooru](https://booru.allthefallen.moe/) | [![status](https://github.com/soujiokita/booru/workflows/ATFbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/atf.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Behoimi](http://behoimi.org/)              | [![status](https://github.com/soujiokita/booru/workflows/Behoimi/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/behoi.yml)   | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [Paheal](https://rule34.paheal.net/)        | [![status](https://github.com/soujiokita/booru/workflows/Paheal/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/paheal.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 

## Usage
This lib should be run in async context, and it's recommended to use [asyncio](https://docs.python.org/3/library/asyncio.html)

### Prerequisites
<table>
	<td><b>NOTE:</b> Python 3.7 or above</td>
</table>

### Installation
It's fairly simple to install booru

🚀from PyPI:

    pip install booru

🚀from pipenv:

    pipenv install booru

Or from this repository!

### Quick example
#### search

```py
(method) search: (tags: str, limit: int = 100, page: int = 1, random: bool = True, gacha: bool = False) -> Coroutine
```  
> All the parameters are optional, except for `query` which is required.

```py
import asyncio
import booru

async def main():
    gel = booru.Gelbooru()
    res = await gel.search(query="cat_girl", limit=50)
    print(res) ## unresolve
    print(booru.resolve(res)) ## resolved

asyncio.run(main())
```
The final step you must resolve them to works with data. See [#Unresolved JSON](#unresolved-json)  
Authorization is always optional! but if you fill it you should define through specific import

```py
from booru import Gelbooru

gel = Gelbooru(api_key="API_KEY_HERE", user_id="USER_ID_HERE")
## do with gel
```



<details>
<summary>Returns</summary>

```js
[
  {
    "change": 1649210419,
    "created_at": "Tue Apr 05 21:00:19 -0500 2022",
    "creator_id": 6498,
    "directory": "41/bd",
    "file_url": "https://img3.gelbooru.com/images/41/bd/41bdc5a29a49dc5a06127bbd6b3ae506.jpg",
    "has_children": "false",
    "has_comments": "false",
    "has_notes": "false",
    "height": 1200,
    "id": 7110275,
    "image": "41bdc5a29a49dc5a06127bbd6b3ae506.jpg",
    "md5": "41bdc5a29a49dc5a06127bbd6b3ae506",
    "owner": "danbooru",
    "parent_id": 0,
    "post_locked": 0,
    "post_url": "https://gelbooru.com/index.php?page=post&s=view&id=7110275",
    "preview_height": 250,
    "preview_url": "https://img3.gelbooru.com/thumbnails/41/bd/thumbnail_41bdc5a29a49dc5a06127bbd6b3ae506.jpg",
    "preview_width": 176,
    "rating": "safe",
    "sample": 0,
    "sample_height": 0,
    "sample_url": "",
    "sample_width": 0,
    "score": 3,
    "source": "https://twitter.com/hdd_social_marv/status/1443591478182305793",
    "status": "active",
    "tags": "1girl animal_ears black_hair bra cat_ears cat_girl cat_tail closed_mouth fishnet_legwear fishnets flower hair_flower hair_ornament hair_rings hairband heart heart_hands heart_tail high_school_dxd highres kuroka_(high_school_dxd) lingerie lipstick long_hair looking_at_viewer makeup multiple_tails nekomata official_art panties purple_lips see-through slit_pupils solo standing tail thighhighs underwear white_bra white_panties yellow_eyes",
    "title": "",
    "width": 849
  },
  {
    "change": 1649210414,
    "created_at": "Tue Apr 05 21:00:14 -0500 2022",
    "creator_id": 6498,
    "directory": "06/3d",
    "file_url": "https://img3.gelbooru.com/images/06/3d/063df68a0cdc6e25c95856c8663b904a.jpg",
    "has_children": "false",
    "has_comments": "false",
    "has_notes": "false",
    "height": 1200,
    "id": 7110270,
    "image": "063df68a0cdc6e25c95856c8663b904a.jpg",
    "md5": "063df68a0cdc6e25c95856c8663b904a",
    "owner": "danbooru",
    "parent_id": 0,
    "post_locked": 0,
    "post_url": "https://gelbooru.com/index.php?page=post&s=view&id=7110270",
    "preview_height": 250,
    "preview_url": "https://img3.gelbooru.com/thumbnails/06/3d/thumbnail_063df68a0cdc6e25c95856c8663b904a.jpg",
    "preview_width": 176,
    "rating": "safe",
    "sample": 0,
    "sample_height": 0,
    "sample_url": "",
    "sample_width": 0,
    "score": 3,
    "source": "https://twitter.com/hdd_social_marv/status/1443591478182305793",
    "status": "active",
    "tags": "1girl all_fours animal_ears black_hair blush bra breasts cat_ears cat_girl cat_tail cleavage fishnet_legwear fishnets flower food hair_flower hair_ornament hair_rings hairband happy_birthday heart heart_hands heart_tail high_school_dxd highres jewelry kuroka_(high_school_dxd) lingerie lipstick long_hair looking_at_viewer makeup multiple_tails naughty_face necklace nekomata official_art panties purple_lips seductive_smile see-through slit_pupils smile solo tail thighhighs underwear white_bra white_panties yellow_eyes",
    "title": "",
    "width": 849
  }
] // 50
```
</details>

#### get image
If you just rely on images only, Yes so there's no need to do any pesky list comprehension hacks

```py
(method) get_image: (query: str, block: str = '', limit: int = 100, page: int = 1) -> Coroutine
```  
> Same as `search` but return only the image list / array

<details>
<summary>Returns</summary>

```js
[
  "https://img3.gelbooru.com/images/c4/d6/c4d6a75f5e0f70ee292392324384b1a1.png",
  "https://img3.gelbooru.com/images/11/02/110258561e75cb1a13de395d5b8ec327.jpeg",
  "https://img3.gelbooru.com/images/58/b8/58b8850696b685b7d02d512de1293e3d.png",
  "https://img3.gelbooru.com/images/0f/e8/0fe85b5c0436169e69c4b8a5d04e91ff.jpeg",
  "https://img3.gelbooru.com/images/bc/df/bcdf09e175c80967d9a948a80eff1444.jpeg",
  "https://img3.gelbooru.com/images/11/38/1138be490058d8afbd9f4ca9465db8fd.jpeg",
  "https://img3.gelbooru.com/images/bf/97/bf97954e8fcd6dd8d14778f23e50fee2.jpeg",
  "https://img3.gelbooru.com/images/40/6b/406b2d883b8cb5b5dbf9ecb05a41da2f.png",
  "https://img3.gelbooru.com/images/82/c0/82c01eb16f3b366c1c5ca3bb2d940a74.jpeg",
  "https://img3.gelbooru.com/images/88/7b/887bc5925c49e62215af29209a2f766b.png"
] //and more
```
</details>

### Advanced example
Here some more advanced examples of using this library.

####  Armored search
Armored-search built-in resolved safety tags concerns, TLDR:

The disgusting query you want to block, For example You want to search 'ahegao' but dont want to gets 'futanari'.

```py
async def get():
    gel = booru.Gelbooru()
    res = await gel.search(query="ahegao", limit=50, block="futanari")
    print(res)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
```
Multiple block separated by (space), check the benchmark table not all booru support this stuff.
> PS: booru is user generated content, there is always the slight possibility that posts not tagged accordingly.

#### Gacha-like
Just like gacha, fill this if you're clown, `gacha=True` will return a random single post.

#### Import you want to use
This library built with separated classes, If you want to use specific booru, For example you can import it:

```py
from booru import Rule34
some_booru = Rule34()

## do something
```

#### Shuffle the whole dictionary
For default, the lib return a random dict, to gets a raw data and disable set 'random' param with `False`

## Unresolved JSON
Instead arbitrary object, This library designed to be neat and clean returns, although it must be reparsed to the string first, that's why [`booru.resolve()`](https://sinkaroid.github.io/booru/utils/parser.html#booru.utils.parser.resolve) exist.  

Let's see an example:

```py
async def main():
    gel = booru.Gelbooru()
    res = await gel.search(query="cat_girl", limit=50)
    print(res) ## unresolve
    print(booru.resolve(res)) ## resolved

asyncio.run(main())
```
- Unresolve: meant is better and neat dictionaries returns instead arbitrary JSON structure
- Resolved: bad structure, arbitary indent, unsorting but it is resolved and ready to extends works with JSON

## Documentation
The documentation can be found https://sinkaroid.github.io/booru

## Limitations
- Respect the ratelimit, there is a hard limit of 100 posts per request.
- Curently the object returns is not consistent, every dict is different structure.
- More than just searching (Comming soon)
- `'charmap' codec can't encode characters`
  - It's raised when the dict contains non-ascii characters, then your console can't parse them, use real console don't Git-bash.
- All mocking tests run without api keys
  -  login properties may not same it all, If you encounter this misleading please open an issue like [#1](https://github.com/sinkaroid/booru/issues/1)

## Acknowledgements
- This project logo was peeked from [pandas](https://github.com/pandas-dev/pandas) with jokes in mind.

## Legal
This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel
like this tool deserves an attribution, mention it. It won't hurt anybody
