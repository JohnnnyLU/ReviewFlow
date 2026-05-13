from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import RatingCreate, NegativeFeedbackCreate
from app.services import ReviewService

from app.api.deps import get_review_service, get_db

router = APIRouter(prefix="/review")

@router.post("/{token}/rating")
async def process_rating(
    token: str,
    data: RatingCreate,
    session: AsyncSession = Depends(get_db),
    service: ReviewService = Depends(get_review_service)
):
    return await service.process_rating(session, token, data)

@router.post("/{token}/negative-feedback")
async def create_negative_feedback(
    token: str,
    data: NegativeFeedbackCreate,
    session: AsyncSession = Depends(get_db),
    service: ReviewService = Depends(get_review_service)
):
    return await service.create_negative_feedback(session, token, data)
