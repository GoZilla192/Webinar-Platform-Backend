from fastapi import Depends

from app.livekit.service import LiveKitService
from app.settings import Settings


def get_livekit_settings() -> Settings:
	"""Provide application settings to LiveKit dependencies."""
	return Settings()


def get_livekit_service(
		settings: Settings = Depends(get_livekit_settings)
) -> LiveKitService:
	"""Construct the LiveKit service for the current request."""
	return LiveKitService(settings=settings)
