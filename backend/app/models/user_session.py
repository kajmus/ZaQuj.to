from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class UserSession(Base):
    __tablename__ = "UserSession"

    id_session: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_user: Mapped[int] = mapped_column(
        Integer, ForeignKey("User.id_user"), nullable=False,unique = True
    )
    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.current_timestamp(),
        nullable=False,
    )

    user: Mapped["User"] = relationship("User", back_populates="session")
