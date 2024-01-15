# Неправильное использование блокирующего API как сопрограммы

import asyncio

import requests

from utils import (
    async_timed,
)


@async_timed
async def get_request_status_code(url: str):
    return requests.get(url).status_code


@async_timed
async def main():
    url = 'https://www.example.com/'
    first_task = asyncio.create_task(get_request_status_code(url))
    second_task = asyncio.create_task(get_request_status_code(url))

    await first_task
    await second_task


asyncio.run(main())
