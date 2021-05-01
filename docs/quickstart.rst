.. _quickstart:

Quickstart
==========
Welcome to the aiowaifus' documentation.

Basic Concepts
--------------
aiowaifus is an API wrapper where you simply say which **category** and 
**type** of image you want, for example:

.. code-block:: python3

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
