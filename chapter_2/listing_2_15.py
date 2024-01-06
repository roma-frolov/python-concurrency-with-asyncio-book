import asyncio

from utils import delay


def make_request() -> asyncio.Future:
    future = asyncio.Future()
    asyncio.create_task(set_future_value(future, 123))

    return future


async def set_future_value(future: asyncio.Future, value: int) -> None:
    # Подождать 1 секунду перед установкой значения в Future
    await delay(1)
    future.set_result(value)


async def main():
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())
