from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Business
from app.schemas import BusinessSchema
from app.core.security import hash_password, verify_password

class AuthService:
    def __init__(self, business_repo):
        self.business_repo = business_repo

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