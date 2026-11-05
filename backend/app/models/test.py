from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Test(Base):
    __tablename__ = "Test"
    __table_args__ = (
        CheckConstraint("mode IN ('fiszki', 'abcd')", name="ck_test_mode"),
    )

    id_testu: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_user: Mapped[int] = mapped_column(
        Integer, ForeignKey("User.id_user"), nullable=False
    )
    mode: Mapped[str] = mapped_column(Text, nullable=False)
    started_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), nullable=False
    )
    finished_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="tests")
    results: Mapped[list["Result"]] = relationship("Result", back_populates="test")
