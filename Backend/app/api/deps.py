from fastapi import Depends

from app.core.database_helper import db_helper

from app.repositories import BusinessRepository

from app.services import AuthService, JWTService

from app.core.config import settings

async def get_db():
    return db_helper.get_scoped_session()

#repositories

def get_business_repositories() -> BusinessRepository:
    return BusinessRepository()

#services

def get_auth_service(
    business_repo: BusinessRepository = Depends(get_business_repositories)
) -> AuthService:
    return AuthService(business_repo)

def get_jwt_service():
    return JWTService