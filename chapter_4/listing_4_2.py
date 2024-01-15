# Отправка веб-запроса с помощью aiohttp

import asyncio
import aiohttp

from chapter_4 import fetch_status
from utils import async_timed


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com/'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')


asyncio.run(main())
