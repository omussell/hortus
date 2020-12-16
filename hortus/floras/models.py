# Standard Library
from enum import Enum
from typing import Optional

# 3rd-party
import databases
import orm
import sqlalchemy
from classifications.models import Classification
from classifications.models import ClassificationBase
from db.base import database
from db.base import metadata
from pydantic import BaseModel

# sqlalchemy


class Flora(orm.Model):
    __tablename__ = "flora"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=True)
    classification = orm.ForeignKey(Classification)
    name = orm.String(max_length=100)
    # completed = orm.Boolean(default=False)


# pydantic


class FloraBase(BaseModel):
    classification: ClassificationBase
    name: str
    # completed: Optional[bool]

    class Config:
        orm_mode = True


class FloraCreate(FloraBase):
    pass


class FloraRead(FloraBase):
    id: int


class FloraUpdate(FloraBase):
    id: int


class FloraDelete(FloraBase):
    id: int
