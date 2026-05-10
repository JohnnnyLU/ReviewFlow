from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database_helper import Base

class Business(Base):
    __tablename__ = 'business'

    id:            Mapped[int] = mapped_column(Integer, primary_key=True)
    business_name: Mapped[str] = mapped_column(String)
    email:         Mapped[str] = mapped_column(String, unique=True, nullable=True)
    password_hash: Mapped[str | None] = mapped_column(String, nullable=True)

    google_id:     Mapped[str | None] = mapped_column(
        String,
        unique=True,
        nullable=True,
        index=True,
    )

    auth_provider: Mapped[str] = mapped_column(
        String(50),
        default="credentials",
    )