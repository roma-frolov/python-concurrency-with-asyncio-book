import asyncio
from utils import delay, async_timed


async def positive_integers_async(until: int):
    for i in range(1, until):
        await delay(i)
        yield  i


@async_timed
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f"Получено число {number}")


asyncio.run(main())
