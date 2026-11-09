from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import Settings

settings = Settings()

engine = create_async_engine(settings.url_db)

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)


async def get_db_session() -> AsyncSession:
	"""Yield a database session for a request."""
	async with AsyncSessionFactory() as session:
		yield session
