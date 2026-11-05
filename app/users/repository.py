from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from app.exceptions.auth import UserAlreadyExists
from app.users.schemas import UserCreateSchema
from app.users.models import User


class UserRepository:
	def __init__(self, db_session: AsyncSession):
		self.db_session = db_session
	
	async def create_user(self, user: User) -> User:
		self.db_session.add(user)
		
		try:
			await self.db_session.flush()
			await self.db_session.commit()
		except IntegrityError:
			raise UserAlreadyExists
		
		return user
	
	async def get_user_by_email(self, email: str) -> User | None:
		res = await self.db_session.execute(
			select(User).where(User.email == email)
		)
		return res.scalar_one_or_none()
