from pydantic import BaseModel


class LiveKitTokenRequestSchema(BaseModel):
	"""Parameters for requesting a LiveKit room token."""
	room_name: str
	is_host: bool
	name: str
	identity: str


class LiveKitTokenResponseSchema(BaseModel):
	"""LiveKit access token and server URL response."""
	access_token: str
	wss_url: str
