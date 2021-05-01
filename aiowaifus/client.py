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
import aiohttp
from typing import List

from .http import HTTPClient
from .enums import ImageType
from .errors import InvalidCategory, InvalidImageType


__all__ = ('WaifuClient',)


class WaifuClient:
    '''Represents a client session with Waifu.pics.

    Parameters
    ----------
    loop: Optional[:class:`asyncio.AbstractEventLoop`]
        The abstract event loop to use for asynchronous operations. Defaults
        to ``None``, in which case the default event loop is used via
        :func:`asyncio.get_event_loop()`.
    connector: :class:`aiohttp.BaseConnector`
        The connector to use connection pooling.
    '''
    def __init__(self, *, loop: asyncio.AbstractEventLoop = None, **kwargs):
        loop = loop or asyncio.get_event_loop()
        connector = kwargs.pop('connector', None)
        
        self.http = HTTPClient(loop=loop, connector=connector)

    def _parse_arguments(self, category: str, image_type: ImageType):
        if not isinstance(image_type, ImageType):
            raise InvalidImageType()

        if category not in self.http.POSSIBLE_ENDPOINTS[image_type]:
            raise InvalidCategory()

    async def fetch_image(self, category: str, *, image_type: ImageType) -> str:
        '''Fetches a single image from Waifu.pics.

        Parameters
        ----------
        category: :class:`str`
            The category of the image. To check the full list, check :ref:`list_of_categories`.
        image_type: :class:`ImageType`
            The type of the image.

        Returns
        -------
        :class:`str`
            The requested image URL.
        '''
        self._parse_arguments(category, image_type)

        path = f'/{image_type.value}/{category}'
        r = await self.http.request('GET', path)

        return r['url']

    async def fetch_many_images(self, category: str, *, image_type: ImageType, exclude: List[str] = []):
        '''Fetches 30 unique images from Waifu.pics.

        Parameters
        ----------
        category: :class:`str`
            The category of the image. To check the full list, check :ref:`list_of_categories`.
        image_type: :class:`ImageType`
            The type of the image.
        exclude: list[:class:`str`]
            A list of images to be not included in the response,
            by default it is ``[]``.

        Returns
        -------
        List[:class:`str`]
            The requested list of images.
        '''
        self._parse_arguments(category, image_type)

        body = {'exclude': exclude}
        path = f'/many/{image_type.value}/{category}'
        r = await self.http.request('POST', path, body)

        return r['files']

    async def close(self):
        '''Closes the client session.'''
        await self.http.close()
