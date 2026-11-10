from fastapi import APIRouter, Depends

from app.livekit.schemas import LiveKitTokenRequestSchema
from app.livekit.service import LiveKitService
from app.livekit.depends import get_livekit_service

router = APIRouter(tags=["LiveKit Server"])


@router.post("/get-livekit-token")
async def get_livekit_token(
		token_request: LiveKitTokenRequestSchema,
		livekit_service: LiveKitService = Depends(get_livekit_service)
):
	"""Return a signed token for joining a LiveKit room."""
	return livekit_service.get_token(token_request)
