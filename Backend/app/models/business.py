import secrets

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database_helper import Base


class Business(Base):
    __tablename__ = 'business'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    business_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    password_hash: Mapped[str | None] = mapped_column(String, nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String, nullable=True)

    google_id: Mapped[str | None] = mapped_column(String, unique=True, nullable=True, index=True,)
    auth_provider: Mapped[str] = mapped_column(String(50), default="credentials",)

    token: Mapped[str] = mapped_column(unique=True, default=lambda: secrets.token_urlsafe(16))

    google_review_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    yandex_review_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    twogis_review_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="business",
        cascade="all, delete-orphan",
    )