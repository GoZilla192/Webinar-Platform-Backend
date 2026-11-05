from app.exceptions.auth import UserDoesntExists, PasswordIncorrect, UserAlreadyExists
from app.settings import Settings
from app.users.repository import UserRepository
from app.users.schemas import UserCreateSchema, UserReadSchema
from app.users.models import User
from app.users.auth.security import hash_password, verify_password, get_access_token


class AuthService:
	def __init__(self, user_repository: UserRepository, settings: Settings):
		self.user_repository = user_repository
		self.settings = settings
	
	async def create_user(self, user_schema: UserCreateSchema):
		user = await self.user_repository.create_user(
			User(email=user_schema.email, password=hash_password(user_schema.password))
		)
		
		return UserReadSchema(id=user.id, email=user.email)
	
	async def get_jwt_token(self, user_schema: UserCreateSchema):
		user = await self.user_repository.get_user_by_email(user_schema.email)
		if not user:
			raise UserDoesntExists
		if not verify_password(user_schema.password, user.password):
			raise PasswordIncorrect
		
		return get_access_token(user.id, self.settings)
