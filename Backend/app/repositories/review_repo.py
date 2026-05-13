# SQLAlchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# DB models
from app.models import Review


class ReviewRepository:
    async def create(
        self,
        session: AsyncSession,
        review: Review,
    ) -> Review:
        session.add(review)

        await session.commit()
        await session.refresh(review)

        return review