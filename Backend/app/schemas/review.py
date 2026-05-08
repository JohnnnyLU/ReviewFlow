from pydantic import BaseModel, Field, model_validator

from enum import Enum

class ReviewSubject(str, Enum):
    BAD_SERVICE = "bad_service"
    LONG_WAIT = "long_wait"
    HIGH_PRICE = "high_price"
    BAD_SUPPORT = "bad_support"
    HARD_TO_USE = "hard_to_use"
    OTHER = "other"

class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    subject: ReviewSubject | None = None
    situation: str | None = Field(None, min_length=5, max_length=500)
    contact: str | None = Field(None, max_length=128)

    @model_validator(mode="after")
    def validate_low_rating_feedback(self):
        if self.rating < 4:
            if not self.subject:
                raise ValueError("Subject is required for ratings below 4")

            if not self.situation:
                raise ValueError("Situation is required for ratings below 4")

        return self