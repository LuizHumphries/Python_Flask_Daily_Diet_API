import datetime
from sqlalchemy.orm import Mapped
from database import db

class Food(db.Model):
    """Default Table Model For Food insertion"""
    id: Mapped[int] = db.Column(db.Integer, primary_key=True) #unique
    name: Mapped[str] = db.Column(db.String(80), nullable=False) #Non Nullable
    description: Mapped[str] = db.Column(db.String(120), nullable=False) #Non Nullable
    calories: Mapped[int] = db.Column(db.Float, nullable=False) #Non Nullable
    diet: Mapped[bool] = db.Column(db.Boolean,default=False, nullable=False) #Non Nullable
    time: Mapped[datetime.datetime] = db.Column(db.DateTime(timezone=True), nullable=False) #Non Nullable

    