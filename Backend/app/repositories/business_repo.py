# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# DB models
from app.models import Business
from app.core.config import settings


class BusinessRepository:
    async def get_exist_business(
            self,
            email: str,
            session: AsyncSession,
) -> Business | None:
        result = await session.execute(
            select(Business).where(Business.email == email)
        )
        return result.scalar_one_or_none()

    async def create_sso_user(
            self,
            email: str,
            provider: str,
            provider_id: str,
            session: AsyncSession,
) -> Business:
        business_data = {
            "email": email,
            f"{provider}_id": provider_id,
        }
        new_business = Business(**business_data)
        session.add(new_business)
        await session.commit()
        await session.refresh(new_business)

        return new_business

    async def link_sso_provider(
            self,
            provider: str,
            provider_id: str,
            business: Business,
            session: AsyncSession,
) -> Business:
        setattr(business, f"{provider}_id", provider_id)

        session.add(business)
        await session.commit()
        await session.refresh(business)

        return business

    async def create(
            self,
            session: AsyncSession,
            business: Business,
    ) -> Business:
        session.add(business)
        await session.commit()
        await session.refresh(business)

        return business

