from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class QuestionProgress(Base):
    __tablename__ = "QuestionProgress"
    __table_args__ = (
        UniqueConstraint("id_user", "id_question", name="uq_question_progress_user_question"),
    )

    id_progress: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_user: Mapped[int] = mapped_column(
        Integer, ForeignKey("User.id_user"), nullable=False
    )
    id_question: Mapped[int] = mapped_column(
        Integer, ForeignKey("Pytanie_ABCD.id_pytanie"), nullable=False
    )
    last_is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    last_answered_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="question_progress")
    question: Mapped["ABCDQuestion"] = relationship(
        "ABCDQuestion", back_populates="user_progress"
    )
