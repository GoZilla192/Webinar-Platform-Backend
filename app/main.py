from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.livekit.routes import router as livekit_router
from app.auth.routes import router as auth_router

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=False,
	allow_methods=["GET", "POST", "DELETE", "PUT", "PATCH", "OPTIONS"],
	allow_headers=["Authorization", "Content-Type"],
)
app.include_router(livekit_router)
app.include_router(auth_router)
