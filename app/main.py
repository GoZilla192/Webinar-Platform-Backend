from fastapi import FastAPI

from app.livekit.routes import router as livekit_router
from app.auth.routes import router as auth_router

app = FastAPI()
app.include_router(livekit_router)
app.include_router(auth_router)
