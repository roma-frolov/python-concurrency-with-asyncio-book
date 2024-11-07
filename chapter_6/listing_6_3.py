# Асинхронное получение результатов от пула процессов

from multiprocessing import Pool
from time import sleep


def say_hello(name: str, delay_seconds: int) -> str:
    sleep(delay_seconds)
    return f"Привет, {name}"


if __name__ == "__main__":
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=("Jeff", 3,))
        hi_john = process_pool.apply_async(say_hello, args=("John", 2,))
        print(hi_jeff.get())
        print(hi_john.get())
