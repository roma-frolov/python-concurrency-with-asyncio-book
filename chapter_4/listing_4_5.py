# Использование спискового включения для создания и ожидания задач

import asyncio
from utils import async_timed, delay


@async_timed
async def main():
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


asyncio.run(main())