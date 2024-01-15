# Использование asyncio.as_completed

import asyncio
from aiohttp import ClientSession
from utils import async_timed, delay
from chapter_4 import fetch_status


async def _fetch_status(*args, delay_seconds: int, **kwargs):
    await delay(delay_seconds)

    return await fetch_status(*args, **kwargs)


@async_timed
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com/'
        fetchers = [
            _fetch_status(session, url, delay_seconds=1),
            _fetch_status(session, url, delay_seconds=1),
            _fetch_status(session, url, delay_seconds=10),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())