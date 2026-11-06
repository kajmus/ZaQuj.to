from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Result(Base):
    __tablename__ = "Wynik"
    __table_args__ = (
        UniqueConstraint("id_testu", "id_pytanie", name="uq_wynik_test_pytanie"),
    )

    id_wyniku: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_testu: Mapped[int] = mapped_column(
        Integer, ForeignKey("Test.id_testu"), nullable=False
    )
    id_pytanie: Mapped[int] = mapped_column(
        Integer, ForeignKey("Pytanie_ABCD.id_pytanie"), nullable=False
    )
    boolean_answer: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    selected_answer: Mapped[str | None] = mapped_column(Text, nullable=True)
    answered_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    test: Mapped["Test"] = relationship("Test", back_populates="results")
    question: Mapped["ABCDQuestion"] = relationship(
        "ABCDQuestion", back_populates="results"
    )
