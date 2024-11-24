from sqlalchemy import Integer, String, Enum
from sqlalchemy.orm import mapped_column, Mapped

from app.adapters.sqlalchemy_db.models import Base
from app.application import models

import enum


class BookStatus(str, enum.Enum):
    AVAILABLE = "в наличии"
    ISSUED = "выдана"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[BookStatus] = mapped_column(Enum(BookStatus), default=BookStatus.AVAILABLE)

    def to_dto(self) -> models.Book:
        return models.Book(
            id=self.id,
            title=self.title,
            author=self.author,
            year=self.year,
            status=self.status
        )
