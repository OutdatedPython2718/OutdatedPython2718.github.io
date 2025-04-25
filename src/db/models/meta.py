from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


__all__ = [
    "Base",
]