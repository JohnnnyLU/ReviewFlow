# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# DB models
from app.models import Business

class BusinessRepository:
    async def get_by_email(
            self,
            session: AsyncSession,
            email: str,
    ) -> Business | None:
        result = await session.execute(select(Business).where(Business.email == email))

        return result.scalar_one_or_none()

    async def get_by_google_id(
        self,
        session: AsyncSession,
        google_id: str,
    ):
        query = select(Business).where(Business.google_id == google_id)

        result = await session.execute(query)

        return result.scalar_one_or_none()

    async def register(
            self,
            session: AsyncSession,
            business_name: str,
            email: str,
            password_hash: str,
    ) -> Business:
        business = Business(
            business_name=business_name,
            email=email,
            password_hash=password_hash,
            google_id=None,
            auth_provider="credentials",
        )

        session.add(business)

        await session.commit()
        await session.refresh(business)

        return business

    async def create_google_user(
        self,
        session: AsyncSession,
        email: str,
        google_id: str,
        business_name: str,
    ) -> Business:
        business = Business(
            email=email,
            google_id=google_id,
            business_name=business_name,
            auth_provider="google",
        )

        session.add(business)

        await session.commit()
        await session.refresh(business)

        return business
