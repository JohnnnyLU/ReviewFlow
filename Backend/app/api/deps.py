from fastapi import Depends

from app.core.database_helper import db_helper

from app.repositories import BusinessRepository

from app.services import AuthService, JWTService


async def get_db():
    print(db_helper.get_scoped_session())
    return db_helper.get_scoped_session()


#repositories

def get_business_repositories() -> BusinessRepository:
    return BusinessRepository()

#services

def get_jwt_service() -> JWTService:
    return JWTService()

def get_auth_service(
    business_repo: BusinessRepository = Depends(get_business_repositories),
    jwt_service: JWTService = Depends(get_jwt_service),
) -> AuthService:
    return AuthService(business_repo, jwt_service)

