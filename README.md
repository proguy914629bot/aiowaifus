# aiowaifus
![issues](https://img.shields.io/github/issues/soukyomi/aiowaifus)
![forks](https://img.shields.io/github/forks/soukyomi/aiowaifus)
![stars](https://img.shields.io/github/stars/soukyomi/aiowaifus)
![license](https://img.shields.io/github/license/soukyomi/aiowaifus)

An async ready API wrapper for Waifu.pics written in Python.


Table of Contents
=============
<!--ts-->
  * [Installing](#installing)
  * [Quickstart](#quickstart)
  * [Documentation](#documentation)
  * [License](#license)

## Installing

**Python 3.5.3 or higher is required.**

To install the library, you can just run the following command:
```sh
# Linux/macOS
$ python3 -m pip install -U aiowaifus

# Windows
$ py -3 -m pip install -U aiowaifus
```


## Quickstart

aiowaifus is an API wrapper where you simply say which **category** and 
**type** of image you want, for example:
```py
import asyncio

from aiowaifus import WaifuClient, ImageType

async def main():
    client = WaifuClient()

    # To get a SFW image:
    sfw_waifu = await client.fetch_image('waifu', image_type=ImageType.sfw)

    # To get a NSFW image:
    nsfw_neko = await client.fetch_image('neko', image_type=ImageType.nsfw)

    # To get 30 unique images:
    many_kisses = await client.fetch_many_images('kiss', image_type=ImageType.sfw)

    # Then we close the connection.
    await client.close()

asyncio.run(main())
```

## Documentation

aiowaifus' documentation can be found [here](https://aiowaifus.readthedocs.io/en/latest/).


## License

aiowaifus is protected by MIT license:
```
MIT License

Copyright (c) 2021 Caio Alexandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
