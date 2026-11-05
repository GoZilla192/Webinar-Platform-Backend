from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
	email: EmailStr
	password: str


class UserReadSchema(BaseModel):
	id: int
	email: EmailStr
