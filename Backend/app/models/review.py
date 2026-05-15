from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Enum as SqlEnum,
    DateTime,
    func,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.core.database_helper import Base
from app.schemas.review import ReviewSubject


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    business_id: Mapped[int] = mapped_column(ForeignKey("business.id", ondelete="CASCADE"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)

    subject: Mapped[ReviewSubject | None] = mapped_column(SqlEnum(ReviewSubject), nullable=True)
    situation: Mapped[str | None] = mapped_column(String(500), nullable=True)
    contact: Mapped[str | None] = mapped_column(String(128), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    business: Mapped["Business"] = relationship(
        back_populates="reviews"
    )