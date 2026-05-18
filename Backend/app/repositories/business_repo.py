# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# DB models
from app.models import Business

class BusinessRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(
            self,
            business_id: int,
    ) -> Business | None:
        result = await self.session.execute(select(Business).where(Business.id==business_id))
        return result.scalar_one_or_none()

    async def get_by_email(
            self,
            email: str,
    ) -> Business | None:
        result = await self.session.execute(select(Business).where(Business.email == email))

        return result.scalar_one_or_none()

    async def get_by_token(
            self,
            token: str,
    ) -> Business | None:
        result = await self.session.execute(select(Business).where(Business.token == token))

        return result.scalar_one_or_none()

    async def get_by_google_id(
        self,
        google_id: str,
    ):
        query = select(Business).where(Business.google_id == google_id)

        result = await self.session.execute(query)

        return result.scalar_one_or_none()

    async def register(
            self,
            business: Business,
    ) -> Business:
        self.session.add(business)

        await self.session.commit()
        await self.session.refresh(business)

        return business

    async def create_google_user(
        self,
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

        self.session.add(business)

        await self.session.commit()
        await self.session.refresh(business)

        return business
