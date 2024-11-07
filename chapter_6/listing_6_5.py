# Исполнители пула процессов в сочетании с asyncio

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial


def count(count_to: int) -> int:
    start = time.time()
    counter = 0

    while counter < count_to:
        counter += 1

    end = time.time()
    print(f"Закончен подсчет до {count_to} за время {end-start}")

    return counter


async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        numbers = [1, 3, 5, 22, 100_000_000]
        calls: list[partial[int]] = [partial(count, num) for num in numbers]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))

        results = await asyncio.gather(*call_coros)

        for result in results:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())