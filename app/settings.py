from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	"""Application settings loaded from environment variables."""
	LIVEKIT_URL: str
	LIVEKIT_API_KEY: str
	LIVEKIT_API_SECRET: str
	LIVEKIT_ACCESS_TOKEN_EXPIRE: int = 20
	
	SECRET_KEY: str
	ALGORITHM: str
	ACCESS_TOKEN_EXPIRE_MINUTES: int
	COOKIE_NAME: str = "token"
	
	DB_HOST: str
	DB_PORT: int
	DB_USER: str
	DB_PASSWORD: str
	DB_NAME: str
	DB_DRIVER: str = "postgresql+asyncpg"
	
	model_config = SettingsConfigDict(env_file=".env", extra="ignore")
	
	@property
	def url_db(self):
		"""Build the async SQLAlchemy database URL."""
		return (f"{self.DB_DRIVER}://{self.DB_USER}:"
		        f"{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
