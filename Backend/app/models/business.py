from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database_helper import Base


class Business(Base):
    __tablename__ = 'business'

    id:            Mapped[int] = mapped_column(primary_key=True)
    business_name: Mapped[str] = mapped_column(String)
    email:         Mapped[str] = mapped_column(String, unique=True)
    password_hash: Mapped[str] = mapped_column(String)