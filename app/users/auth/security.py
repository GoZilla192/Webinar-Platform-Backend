from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError, ExpiredSignatureError
from jose.exceptions import JWEInvalidAuth
from passlib.context import CryptContext

from app.settings import Settings  # SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
	"""Hash a password for secure storage."""
	return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
	"""Check a password against its stored hash."""
	return pwd_context.verify(password, password_hash)


def get_access_token(user_id: int, settings: Settings) -> str:
	"""Create a signed access token for a user."""
	now = datetime.now(timezone.utc)
	payload = {
		"sub": str(user_id),
		"exp": int((now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()),
	}
	return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def get_decoded_token(token: str, *, settings: Settings) -> dict:
	"""Decode and validate a signed access token."""
	try:
		return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
	except ExpiredSignatureError as e:
		raise ValueError("Token expired") from e
	except JWEInvalidAuth as e:
		raise ValueError("Invalid token") from e
	except JWTError as e:
		raise ValueError("Invalid authentication") from e
