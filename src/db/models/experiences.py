import enum
from typing import List 

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import  String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .meta import Base


class ExperienceType(enum.Enum):
    PROFESS = 'professional'
    PERSONAL = 'personal'


class Experience(Base):
    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    type_: Mapped[ExperienceType] = mapped_column(Enum(ExperienceType), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    employeer: Mapped[str] =  mapped_column(String(100), nullable=True)
    start_year: Mapped[int] = mapped_column(Integer, nullable=False)
    end_year: Mapped[int] = mapped_column(Integer, nullable=True)

    bullet_points: Mapped[List["BulletPoint"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="experiences")

    def __repr__(self) -> str:
        return f"Experience(id={self.id!r}, type={self.type_}, name={self.name!r}, start={self.start_year!r}, end={self.end_year!r})"


__all__ = [
    "Experience",
]