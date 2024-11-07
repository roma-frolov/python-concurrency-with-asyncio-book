import asyncio

from chapter_5.database_connection import connect


async def main():
    connection = await connect()
    query = "SELECT product_id, product_name FROM product"
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()

asyncio.run(main())
