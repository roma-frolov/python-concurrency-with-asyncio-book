# Создание пула процессов

from multiprocessing import Pool
from time import sleep


def say_hello(name: str, delay_seconds: int) -> str:
    sleep(delay_seconds)
    return f"Привет, {name}"


if __name__ == "__main__":
    with Pool() as process_pool:
        hi_jeff = process_pool.apply(say_hello, args=("Jeff", 3))
        print(hi_jeff)
        hi_john = process_pool.apply(say_hello, args=("John", 1))
        print(hi_john)
