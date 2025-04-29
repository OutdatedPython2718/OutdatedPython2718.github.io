import enum

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import  String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .meta import Base


class EducationType(enum.Enum):
    DEGREE = 'degree'


class Education(Base):
    __tablename__ = "educations"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    type_: Mapped[EducationType] = mapped_column(Enum(EducationType), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    desc: Mapped[str] = mapped_column(String(300), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="educations")

    def __repr__(self) -> str:
        return f"Education(id={self.id!r}, type={self.type_!r}, name={self.name!r}, location={self.location!r}, year={self.year!r}, desc={self.desc!r})"


__all__ = [
    "Education",
]