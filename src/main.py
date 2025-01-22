import asyncio

from sqlalchemy import select, text

from src.database import session_factory
from src.models.base import Base


async def create_tables():
    async with session_factory() as session:
        await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)




if __name__ == '__main__':
    asyncio.run(create_tables())