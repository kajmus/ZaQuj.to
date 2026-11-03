from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class ABCDQuestion(Base):
    __tablename__ = "Pytanie_ABCD"

    id_pytanie: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    id_fiszka: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Pytanie_Fiszka.id_fiszka"),
        nullable=False
    )

    correct_answer: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    wrong_answer_1: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    wrong_answer_2: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    wrong_answer_3: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    flashcard: Mapped["Flashcard"] = relationship(
        "Flashcard",
        back_populates="questions"
    )

    results: Mapped[list["QuestionResult"]] = relationship(
        "QuestionResult",
        back_populates="question"
    )
