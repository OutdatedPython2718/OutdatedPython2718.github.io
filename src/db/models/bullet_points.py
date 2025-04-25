from sqlalchemy import ForeignKey
from sqlalchemy import  String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .meta import Base


class BulletPoint(Base):
    __tablename__ = "bullet_points"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    desc: Mapped[str] = mapped_column(String(500), nullable=False)

    experience_id: Mapped[int] = mapped_column(ForeignKey("experiences.id"))
    experience: Mapped["Experience"] = relationship(back_populates="bullet_points")

    def __repr__(self) -> str:
        return f"BulletPoint(id={self.id!r}, desc={self.desc!r})"


__all__ = [
    "BulletPoint",
]