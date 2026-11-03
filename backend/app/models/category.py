from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Category(Base):
    __tablename__ = "Kategoria"

    id_category: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    flashcards: Mapped[list["Flashcard"]] = relationship(
        "Flashcard",
        back_populates="category"
    )
