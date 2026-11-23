from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from typing import Annotated

from app.livekit.service import LiveKitService
from app.livekit.depends import get_livekit_service
from app.livekit.exceptions import RoomDoesntExist
from app.auth.security import bearer_schema

router = APIRouter(prefix="/room", tags=["LiveKit Server"])


@router.post("/create")
async def create_room(
		token: Annotated[HTTPAuthorizationCredentials, Depends(bearer_schema)],
		livekit_service: LiveKitService = Depends(get_livekit_service)
):
	return await livekit_service.create_room(token.credentials)


@router.get("/token/{room_id}", responses={
	200: {
		"description": "OK",
	},
	404: {
		"description": "Room not found",
	},
}, )
async def get_room_token(
		room_id: str,
		livekit_service: LiveKitService = Depends(get_livekit_service)
):
	try:
		return await livekit_service.get_room_token(room_id=room_id)
	except RoomDoesntExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Room not found"
		)
