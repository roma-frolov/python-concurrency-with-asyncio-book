import asyncio

from utils import (
    delay,
    async_timed,
)


@async_timed()
async def _delay(*args, **kwargs):
    return await delay(*args, **kwargs)


@async_timed()
async def main():
    first_task = asyncio.create_task(_delay(5))
    second_task = asyncio.create_task(_delay(5))

    await first_task
    await second_task


asyncio.run(main())
