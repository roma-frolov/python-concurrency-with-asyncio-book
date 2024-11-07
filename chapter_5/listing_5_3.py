import asyncio

from chapter_5.database_connection import connect
from chapter_5.listing_5_2 import CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, CREATE_PRODUCT_COLOR_TABLE, \
    CREATE_PRODUCT_SIZE_TABLE, CREATE_SKU_TABLE, COLOR_INSERT, SIZE_INSERT


async def main():
    connection = await connect()
    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        COLOR_INSERT,
        SIZE_INSERT,
    ]
    print("Создаётся база данных product...")

    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print("База данных product создана!")
    await connection.close()

asyncio.run(main())
