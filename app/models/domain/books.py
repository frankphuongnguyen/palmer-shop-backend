import datetime
from typing import Optional

from app.models.domain.rwmodel import RWModel
from app.models.common import IDModelMixin, DateTimeModelMixin


class Book(IDModelMixin, DateTimeModelMixin, RWModel):
    name: str
    genre: str
    released_date: datetime.datetime

