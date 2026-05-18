from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select, Update, values

from app.models import Business

ALLOWED_UPDATE_FIELDS = {
    'business_name',
    'avatar_url',
    'google_review_url',
    'yandex_review_url',
    'twogis_review_url',
}

class ProfileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_profile(
        self,
        business_id: int,
    ) -> Business | None:
        result = await self.session.execute(
            Select(Business)
            .where(
                Business.id == business_id
            )
        )

        return result.scalar_one_or_none()

    async def update_profile(
        self,
        business_id: int,
        data: dict,
    ) -> Business:
        filtered_data = {
            key: value
            for key, value in data.items()
            if key in ALLOWED_UPDATE_FIELDS
        }

        if not filtered_data:
            raise ValueError('No valid fields to update')

        stmt = (
            Update(Business)
            .where(Business.id == business_id)
            .values(**filtered_data)
            .returning(Business)
        )

        result = await self.session.execute(stmt)

        await self.session.commit()

        return result.scalar_one()