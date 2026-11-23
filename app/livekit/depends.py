from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.livekit.service import LiveKitService
from app.livekit.repository import LiveKitRepository
from app.infrastructure.database.accessor import get_db_session
from app.settings import Settings


def get_livekit_settings() -> Settings:
	"""Provide application settings to LiveKit dependencies."""
	return Settings()


def get_livekit_repository(
		db_session: AsyncSession = Depends(get_db_session)
) -> LiveKitRepository:
	return LiveKitRepository(db_session=db_session)


def get_livekit_service(
		settings: Settings = Depends(get_livekit_settings),
		repository: LiveKitRepository = Depends(get_livekit_repository)
) -> LiveKitService:
	"""Construct the LiveKit service for the current request."""
	return LiveKitService(settings=settings, repository=repository)
