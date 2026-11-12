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

    tests: Mapped[list["Test"]] = relationship(
        "Test",
        back_populates="user"
    )

    session: Mapped["UserSession"] = relationship(
        "UserSession", 
        back_populates="user", 
            uselist=False)
