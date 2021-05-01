from aiowaifus import WaifuClient, ImageType
import asyncio
import logging


async def main():
    logging.basicConfig(level=logging.DEBUG)

    client = WaifuClient()

    image = await client.fetch_image('waifu', image_type=ImageType.sfw)
    print(image)

    images = await client.fetch_many_images('waifu', image_type=ImageType.sfw)
    print(images)

    await client.close()


asyncio.run(main())
