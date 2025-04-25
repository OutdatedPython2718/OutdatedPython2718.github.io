import datetime
from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

from .custom_types import TZDateTime

DATABASE_URL = 'sqlite:///ashen-casuals.db'

datetimetz = Annotated[datetime.datetime, mapped_column(TZDateTime())]

# provide echo as true to enable loggin to stdout
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)