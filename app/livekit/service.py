from livekit import api
from datetime import timedelta
import uuid

from app.settings import Settings
from app.livekit.schemas import LiveKitTokenRequestSchema, LiveKitTokenResponseSchema
from app.livekit.repository import LiveKitRepository
from app.livekit.exceptions import RoomDoesntExist
from app.auth.security import get_decoded_token


class LiveKitService:
	"""Create access tokens for LiveKit rooms."""
	
	def __init__(self, settings: Settings, repository: LiveKitRepository):
		"""Initialize the service with application settings."""
		self.repository = repository
		self.settings = settings
	
	def get_token(self, token_request: LiveKitTokenRequestSchema) -> LiveKitTokenResponseSchema:
		"""Create a room token with permissions from the request."""
		grants = api.VideoGrants(
			room_join=True,
			room=token_request.room_name,
			can_publish=token_request.is_host,
			can_subscribe=True,
		)
		
		token = (
			api.AccessToken(self.settings.LIVEKIT_API_KEY, self.settings.LIVEKIT_API_SECRET)
			.with_identity(token_request.identity)
			# .with_name(token_request.name) Do I need it?
			.with_grants(grants)
			.with_ttl(timedelta(minutes=self.settings.LIVEKIT_ACCESS_TOKEN_EXPIRE))
			.to_jwt()
		)
		
		return LiveKitTokenResponseSchema(
			access_token=token,
			wss_url=self.settings.LIVEKIT_URL
		)
	
	async def create_room(self, jwt_token: str) -> LiveKitTokenResponseSchema:
		"""Create room, make token request and return token response"""
		
		decoded_token = get_decoded_token(token=jwt_token, settings=Settings())
		user_id = int(decoded_token['sub'])
		
		room_id = await self.repository.create_room(user_id=user_id)
		token_request = LiveKitTokenRequestSchema(
			room_name=room_id,
			is_host=True,
			identity=f"{user_id}"
		)
		
		return self.get_token(token_request)
	
	async def get_room_token(self, room_id: str) -> LiveKitTokenResponseSchema:
		"""Check if room exists, make token request and return token response"""
		if (await self.repository.is_room_exist(room_id=room_id)) is False:
			raise RoomDoesntExist
		
		token_request = LiveKitTokenRequestSchema(
			room_name=room_id,
			is_host=False,
			identity=f"{uuid.uuid4()}"
		)
		
		return self.get_token(token_request)
