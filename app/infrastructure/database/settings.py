from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	DB_HOST: str
	DB_PORT: int
	DB_USER: str
	DB_PASSWORD: str
	DB_NAME: str
	DB_DRIVER: str
	
	model_config = SettingsConfigDict(env_file=".env")
	
	@property
	def url_db(self):
		return (f"{self.DB_DRIVER}://{self.DB_USER}:"
		        f"{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
