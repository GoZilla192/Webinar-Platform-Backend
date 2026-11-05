from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.settings import Settings
from app.users.repository import UserRepository
from app.users.auth.service import AuthService
from app.infrastructure.database.accessor import get_db_session


def get_user_settings():
	return Settings()


def get_user_repository(db_session: AsyncSession = Depends(get_db_session)):
	return UserRepository(db_session=db_session)


def get_auth_service(
		repo: UserRepository = Depends(get_user_repository),
		settings: Settings = Depends(get_user_settings)
):
	return AuthService(user_repository=repo, settings=settings)
