from .db import engine
from .models import *

models.Base.metadata.create_all(bind=engine)