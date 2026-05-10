from fastapi import APIRouter

#routers
from .routes.auth import router as auth_router
from .routes.google import router as google_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
api_router.include_router(google_router, prefix='/google', tags=['Google'])
