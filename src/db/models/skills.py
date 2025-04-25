import enum

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import  String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .meta import Base


class SkillType(enum.Enum):
    PROG_LANG = 'programing language'
    TOOL = 'tool'
    ACHIEVE = 'achievement'


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    type_: Mapped[SkillType] = mapped_column(Enum(SkillType), nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    desc: Mapped[str] = mapped_column(String(300), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="skills")

    def __repr__(self) -> str:
        return f"Skill(id={self.id!r}, type={self.type_!r}, name={self.name!r}, desc={self.desc!r})"


__all__ = [
    "Skill",
]