from sqlalchemy import Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class QuestionResult(Base):
    __tablename__ = "Wynik_Pytania"

    id_wyniku: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    id_user: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("User.id_user"),
        nullable=False
    )

    id_pytanie: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("Pytanie_ABCD.id_pytanie"),
        nullable=False
    )

    boolean_answer: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="question_results"
    )

    question: Mapped["ABCDQuestion"] = relationship(
        "ABCDQuestion",
        back_populates="results"
    )
