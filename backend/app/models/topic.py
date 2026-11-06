from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Topic(Base):
    __tablename__ = "Temat"

    id_temat: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    id_category: Mapped[int] = mapped_column(
        Integer, ForeignKey("Kategoria.id_category"), nullable=False
    )

    category: Mapped["Category"] = relationship(
        "Category", back_populates="topics"
    )
    questions: Mapped[list["ABCDQuestion"]] = relationship(
        "ABCDQuestion", back_populates="topic"
    )
