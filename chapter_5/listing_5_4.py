import asyncpg
import asyncio

from asyncpg import Record

from chapter_5.database_connection import connect


async def main():
    connection = await connect()
    await connection.execute("INSERT INTO brand VALUES (DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES (DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: list[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f"id: {brand['brand_id']}, name: {brand['brand_name']}")

    await connection.close()

asyncio.run(main())
