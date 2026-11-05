from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status

from app.users.auth.service import AuthService
from app.exceptions.auth import UserAlreadyExists, UserDoesntExists, PasswordIncorrect
from app.users.schemas import UserCreateSchema
from app.users.auth.depends import get_auth_service

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/signup",
             status_code=status.HTTP_201_CREATED,
             responses={
		             201: {
			             "description": "Created",
		             },
		             409: {
			             "description": "Email already registered",
		             },
		         },
)
async def signup(user: UserCreateSchema, svc: Annotated[AuthService, Depends(get_auth_service)]):
	try:
		return await svc.create_user(user)
	except UserAlreadyExists:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Email already registered"
		)


@router.post("/login", responses={
		             200: {
			             "description": "OK",
		             },
		             401: {
			             "description": "Credentials incorrect",
		             },
		         },
)
async def login(user: UserCreateSchema, svc: Annotated[AuthService, Depends(get_auth_service)]):
	try:
		return await svc.get_jwt_token(user)
	except (UserDoesntExists, PasswordIncorrect):
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Credentials incorrect"
		)
