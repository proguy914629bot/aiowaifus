'''
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
'''

import asyncio
import logging
from typing import Optional

import aiohttp

from .enums import ImageType
from .errors import InvalidCategory


__all__ = ('HTTPClient',)


log = logging.getLogger(__name__)


class HTTPClient:
    BASE_URL = 'https://waifu.pics/api'

    POSSIBLE_ENDPOINTS = {
        ImageType.sfw: [
            'waifu', 'neko',
            'shinobu', 'megumin',
            'bully', 'cuddle',
            'cry', 'hug',
            'awoo', 'kiss',
            'lick', 'pat',
            'smug', 'bonk',
            'yeet', 'blush',
            'smile', 'wave',
            'highfive', 'handhold',
            'nom', 'bite',
            'glomp', 'kill',
            'slap', 'happy',
            'wink', 'poke',
            'dance', 'cringe',
            'blush'
        ],
        ImageType.nsfw: [
            'waifu', 'neko',
            'trap', 'blowjob'
        ]
    }

    def __init__(self, loop, connector):
        self.client = aiohttp.ClientSession(connector=connector, loop=loop)

    async def get(self, path, **kwargs):
        url = self.BASE_URL + path
        
        async with self.client.get(url, **kwargs) as r:
            log.debug(f'GET {url} has returned code {r.status}.')
            return await r.json()

    async def close(self):
        await self.client.close()
