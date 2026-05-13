from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import ReviewRepository, BusinessRepository

from app.schemas import (
    RatingCreate,
    PositiveFeedbackResponse,
    NegativeFeedbackResponse,
    NegativeFeedbackCreate,
    FeedbackSavedResponse,
)

from app.models import Review


class ReviewService:
    def __init__(
        self,
        review_repo: ReviewRepository,
        business_repo: BusinessRepository,
    ):
        self.review_repo = review_repo
        self.business_repo = business_repo

    async def process_rating(
        self,
        session: AsyncSession,
        token: str,
        data: RatingCreate,
    ) -> PositiveFeedbackResponse | NegativeFeedbackResponse:
        review_link = await self.business_repo.get_by_token(session, token) #Business

        if not review_link:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )

        if data.rating >= 4:
            await self.review_repo.create(
                session=session,
                review=Review(
                    business_id=review_link.id,
                    rating=data.rating,
                    subject=None,
                    situation=None,
                    contact=None,
                )
            )
            return PositiveFeedbackResponse(
                type="positive",
                message="Thank you for your positive feedback",
                business_links={
                    'google': review_link.google_review_url,
                    'yandex': review_link.yandex_review_url,
                    '2gis': review_link.twogis_review_url,
                },
            )
        else:
            return NegativeFeedbackResponse(
                type="negative",
                message="We're very sorry. Please let us know what disappointed you",
                required_fields=["subject", "situation", "contact"],
            )

    async def create_negative_feedback(
        self,
        session: AsyncSession,
        token: str,
        data: NegativeFeedbackCreate,
    ):
        review_link = await self.business_repo.get_by_token(session, token)

        if not review_link:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )

        await self.review_repo.create(
            session=session,
            review=Review(
                business_id=review_link.id,
                rating=data.rating,
                subject=data.subject,
                situation=data.situation,
                contact=data.situation,
            ),
        )

        return FeedbackSavedResponse(
            success=True,
            message="Thank you. We'll try to do better",
        )
