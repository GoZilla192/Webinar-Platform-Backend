from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	SECRET_KEY: str
	ALGORITHM: str
	ACCESS_TOKEN_EXPIRE_MINUTES: int
	COOKIE_NAME: str = "token"
	
	model_config = SettingsConfigDict(env_file=".env", extra="ignore")
