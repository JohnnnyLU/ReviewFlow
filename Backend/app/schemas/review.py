from pydantic import BaseModel, Field

from enum import Enum

class ReviewSubject(str, Enum):
    BAD_SERVICE = "bad_service"
    LONG_WAIT = "long_wait"
    HIGH_PRICE = "high_price"
    BAD_SUPPORT = "bad_support"
    HARD_TO_USE = "hard_to_use"
    OTHER = "other"

class RatingCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)

class NegativeFeedbackCreate(BaseModel):
    rating: int = Field(..., ge=1, le=3)
    subject: ReviewSubject
    situation: str | None = Field(..., min_length=5, max_length=500)
    contact: str | None = Field(..., min_length=5, max_length=128)

class PositiveFeedbackResponse(BaseModel):
    type: str = 'positive'
    message: str
    business_links: dict[str, str | None]

class NegativeFeedbackResponse(BaseModel):
    type: str = 'negative'
    message: str
    required_fields: list[str]

class FeedbackSavedResponse(BaseModel):
    success: bool = True
    message: str