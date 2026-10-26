from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.infrastructure.database.settings import Settings

settings = Settings()

engine = create_async_engine(settings.url_db)

AsyncSessionFactory = async_sessionmaker(engine)


async def get_db_session() -> AsyncSession:
	async with AsyncSessionFactory() as session:
		yield session
