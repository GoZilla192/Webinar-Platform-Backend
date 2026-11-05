from fastapi import Depends

from app.livekit.service import LiveKitService
from app.settings import Settings


def get_livekit_settings() -> Settings:
	"""
	For FastAPI Dependency Injection mechanism
	If I will change LiveKitSetting, I will change this function only
	"""
	return Settings()


def get_livekit_service(
		settings: Settings = Depends(get_livekit_settings)
) -> LiveKitService:
	return LiveKitService(settings=settings)
