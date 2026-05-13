from fastapi import APIRouter

#routers
from .routes.auth import router as auth_router
from .routes.google import router as google_router
from .routes.business import router as business_router
from .routes.review import router as review_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
api_router.include_router(google_router, prefix='/google', tags=['Google'])
api_router.include_router(business_router, tags=['Business'])
api_router.include_router(review_router, tags=['Review'])