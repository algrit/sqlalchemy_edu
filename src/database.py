from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engine = create_async_engine(url=settings.DB_URL,
                             echo=True,
                             pool_size=5,
                             max_overflow=5)

session_factory = async_sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
