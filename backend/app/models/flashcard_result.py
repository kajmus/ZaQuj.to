from sqlalchemy import Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class FlashcardResult(Base):
    __tablename__ = "Wynik_Fiszki"

    id_wyniku: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    id_user: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("User.id_user"),
        nullable=False
    )

    id_fiszka: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Pytanie_Fiszka.id_fiszka"),
        nullable=False
    )

    boolean_answer: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="flashcard_results"
    )

    flashcard: Mapped["Flashcard"] = relationship(
        "Flashcard",
        back_populates="results"
    )
