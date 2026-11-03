from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class User(Base):
    __tablename__ = "User"

    id_user: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    login: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True
    )

    password: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    flashcard_results: Mapped[list["FlashcardResult"]] = relationship(
        "FlashcardResult",
        back_populates="user"
    )

    question_results: Mapped[list["QuestionResult"]] = relationship(
        "QuestionResult",
        back_populates="user"
    )
