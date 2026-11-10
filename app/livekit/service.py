from livekit import api
from datetime import timedelta

from app.settings import Settings
from app.livekit.schemas import LiveKitTokenRequestSchema, LiveKitTokenResponseSchema


class LiveKitService:
	"""Create access tokens for LiveKit rooms."""
	def __init__(self, settings: Settings):
		"""Initialize the service with application settings."""
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
			.with_name(token_request.name)
			.with_grants(grants)
			.with_ttl(timedelta(minutes=self.settings.LIVEKIT_ACCESS_TOKEN_EXPIRE))
			.to_jwt()
		)
		
		return LiveKitTokenResponseSchema(
			access_token=token,
			wss_url=self.settings.LIVEKIT_URL
		)
