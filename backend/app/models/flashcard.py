from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Flashcard(Base):
    __tablename__ = "Pytanie_Fiszka"

    id_fiszka: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    id_category: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Kategoria.id_category"),
        nullable=False
    )

    text_answer: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="flashcards"
    )

    questions: Mapped[list["ABCDQuestion"]] = relationship(
        "ABCDQuestion",
        back_populates="flashcard"
    )

    results: Mapped[list["FlashcardResult"]] = relationship(
        "FlashcardResult",
        back_populates="flashcard"
    )
