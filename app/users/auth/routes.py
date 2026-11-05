from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.users.auth.service import AuthService
from app.users.schemas import UserCreateSchema
from app.users.auth.depends import get_auth_service

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreateSchema, svc: Annotated[AuthService, Depends(get_auth_service)]):
	return await svc.create_user(user)


@router.post("/login")
async def login(user: UserCreateSchema, svc: Annotated[AuthService, Depends(get_auth_service)]):
	return await svc.get_jwt_token(user)
