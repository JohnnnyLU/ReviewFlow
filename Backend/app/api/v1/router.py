from fastapi import APIRouter

#routers
from .routes.auth import router as auth_router
from .routes.google import router as google_router
from .routes.review import router as review_router
from .routes.profile import router as profile_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
api_router.include_router(google_router, prefix='/google', tags=['Google'])
api_router.include_router(review_router, tags=['Review'])
api_router.include_router(profile_router, prefix='/profile', tags=['Profile'])