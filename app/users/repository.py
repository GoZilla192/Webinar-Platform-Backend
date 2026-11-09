from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from app.users.auth.exceptions import UserAlreadyExists
from app.users.models import User


class UserRepository:
	"""Persist and retrieve user records."""
	def __init__(self, db_session: AsyncSession):
		"""Initialize the repository with a database session."""
		self.db_session = db_session
	
	async def create_user(self, user: User) -> User:
		"""Save a user and raise if its email is already registered."""
		self.db_session.add(user)
		
		try:
			await self.db_session.flush()
			await self.db_session.commit()
		except IntegrityError:
			raise UserAlreadyExists
		
		return user
	
	async def get_user_by_email(self, email: str) -> User | None:
		"""Return the user with this email, or ``None`` if absent."""
		res = await self.db_session.execute(
			select(User).where(User.email == email)
		)
		return res.scalar_one_or_none()
