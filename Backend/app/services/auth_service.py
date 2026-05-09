from datetime import timedelta, datetime, UTC

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.schemas import BusinessSchema
from app.core.security import hash_password, verify_password
from app.models import Business

from .jwt_service import JWTService
from app.repositories import BusinessRepository
from app.schemas import TokenResponse


class AuthService:
    def __init__(
            self,
            business_repo: BusinessRepository,
            jwt_service: JWTService
    ):
        self.business_repo = business_repo
        self.jwt_service = jwt_service

    async def login(
        self,
        email: str,
        password: str,
        session: AsyncSession,
    ):
        business = await self.business_repo.get_exist_business(session, email)

        if not business or not verify_password(plain_password=password, hashed_password=business.password_hash):
            raise ValueError('Invalid credentials')

        payload = {"sub": str(business.id)}

        access_token = self.jwt_service.create_access_token(payload)
        refresh_token = self.jwt_service.create_refresh_token(payload)

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def register(
            self,
            session: AsyncSession,
            business_schema: BusinessSchema,
    ) -> Business:
        existing_business = await self.business_repo.get_exist_business(
            session, business_schema.email
        )
        if existing_business:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Business already exists'
            )

        password_hash = hash_password(business_schema.password)

        business = Business(
            business_name=business_schema.business_name,
            email=business_schema.email,
            password_hash=password_hash
        )

        try:
            return await self.business_repo.create(session, business)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Business name already exists'
            )