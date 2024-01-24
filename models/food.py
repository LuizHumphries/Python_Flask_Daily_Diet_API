import datetime
from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from database import db

class Food(db.Model):
    """Default Table Model For Food insertion"""
    id: Mapped[int] = mapped_column(primary_key=True) #unique
    name: Mapped[str] #Non Nullable
    description: Mapped[str] #Non Nullable
    time: Mapped[datetime.datetime] #Non Nullable
    diet: Mapped[bool] #Non Nullable

    