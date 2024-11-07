import asyncio

from chapter_5.database_connection import connect


async def main():
    connection = await connect()
    version = connection.get_server_version()
    print(f"Подключено! Версия Postgres равна {version}")
    await connection.close()


asyncio.run(main())
