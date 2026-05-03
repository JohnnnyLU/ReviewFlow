# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# DB models
from app.models import Business

class BusinessRepository:
    async def get_exist_business(
        self,
        session: AsyncSession,
        email: str
    ) -> Business | None:
        result = await session.execute(
            select(Business).where(Business.email == email)
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        session: AsyncSession,
        business: Business
    ) -> Business:
        session.add(business)
        await session.commit()
        await session.refresh(business)
        print('COMMIT DONE')
        return business

