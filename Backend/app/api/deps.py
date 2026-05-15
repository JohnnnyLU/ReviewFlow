from typing import Optional

from fastapi import Depends, Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database_helper import db_helper
from app.repositories import BusinessRepository, ReviewRepository, ProfileRepository
from app.services import AuthService, JWTService, ReviewService, ProfileService


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error, scheme_name="JWT")

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        credentials = await super().__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication scheme."
                )
            return credentials.credentials
        return None

oauth2_scheme = JWTBearer()

# db

async def get_db():
    return db_helper.get_scoped_session()

# repositories

def get_business_repository() -> BusinessRepository:
    return BusinessRepository()

def get_review_repository() -> ReviewRepository:
    return ReviewRepository()

def get_profile_repository(session: AsyncSession = Depends(get_db)) -> ProfileRepository:
    return ProfileRepository(session)

# services

def get_jwt_service() -> JWTService:
    return JWTService()

def get_auth_service(
    business_repo: BusinessRepository = Depends(get_business_repository),
    jwt_service: JWTService = Depends(get_jwt_service),
) -> AuthService:
    return AuthService(business_repo, jwt_service)

def get_review_service(
    review_repo: ReviewRepository = Depends(get_review_repository),
    business_repo: BusinessRepository = Depends(get_business_repository),
) -> ReviewService:
    return ReviewService(review_repo, business_repo)

def get_profile_service(
    profile_repo: ProfileRepository = Depends(get_profile_repository),
) -> ProfileService:
    return ProfileService(profile_repo)

# JWT
async def get_current_business(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_db),
    jwt_service: JWTService = Depends(get_jwt_service),
    repo: BusinessRepository = Depends(get_business_repository),
):
    payload = jwt_service.decode_token(token)

    business_id = payload.get("sub")

    business = await repo.get_by_id(session, int(business_id))

    if not business:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return business