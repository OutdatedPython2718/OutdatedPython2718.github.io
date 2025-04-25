from typing import List 

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .meta import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)

    educations: Mapped[List["Education"]] = relationship()
    experiences: Mapped[List["Experience"]] = relationship()
    skills: Mapped[List["Skill"]] = relationship()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, full_name={self.first_name!r} {self.last_name!r}, email={self.email!r}, phone={self.phone!r})"


__all__ = [
    "User",
]