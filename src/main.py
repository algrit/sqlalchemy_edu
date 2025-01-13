import asyncio

from sqlalchemy import select, text

from src.database import session_factory


async def get_123():
    async with session_factory() as session:
        res = await session.execute(text("SELECT 1,2,3"))
        print(res.first())




if __name__ == '__main__':
    asyncio.run(get_123())