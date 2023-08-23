from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME

engine = create_async_engine(f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
session = async_sessionmaker(engine, expire_on_commit = False)

Base = declarative_base()


async def get_db():
    db = session()

    try:
        yield db
    finally:
        await db.close()
