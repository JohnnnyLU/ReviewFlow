from fastapi import HTTPException, status

# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

# DB models
from app.models import Business

# Pydantic schemas
from app.schemas import BusinessSchema

class BusinessRepository:
    async def get_exist_business(
        self,
        session: AsyncSession,
        email: str
    ) -> Business | None:
        result = await session.execute(
            select(Business).where(
                Business.email == email
            )
        )
        return result.scalar_one_or_none()

    async def register(
        self,
        session: AsyncSession,
        business_schema: BusinessSchema,
        password_hash: str,
    ):
        business = await self.get_exist_business(session, business_schema.email)

        if business:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Business already exists"
            )

        business = Business(
            business_name=business_schema.business_name,
            email=business_schema.email,
            password_hash=password_hash,
        )

        session.add(business)

        try:
            await session.commit()
            await session.refresh(business)

        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The name already exists'
            )
        return business
