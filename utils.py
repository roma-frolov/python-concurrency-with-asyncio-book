import asyncio
import functools
import time
from typing import Callable, Any


async def delay(delay_seconds: int) -> int:
    print(f'Засыпаю на {delay_seconds} секунд.')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} секунд закончился.')

    return delay_seconds


def async_timed():
    def wrapper(function: Callable) -> Callable:
        @functools.wraps(function)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Выполняется "{function.__name__}" с args: {args}; kwargs: {kwargs}')
            start = time.time()

            try:
                return await function(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'"{function.__name__}" завершилась за {total:.4f} с')

        return wrapped
    return wrapper
