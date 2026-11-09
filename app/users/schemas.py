from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
	"""Credentials used to create or authenticate a user."""
	email: EmailStr
	password: str


class UserReadSchema(BaseModel):
	"""Public user details returned by the API."""
	id: int
	email: EmailStr
