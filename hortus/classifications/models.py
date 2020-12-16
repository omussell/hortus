# Standard Library
from enum import Enum
from typing import Optional

# 3rd-party
import databases
import orm
import sqlalchemy
from db.base import database
from db.base import metadata
from pydantic import BaseModel

# sqlalchemy


class Classification(orm.Model):
    __tablename__ = "classification"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=True)
    name = orm.String(max_length=100)


# pydantic


class ClassificationEnum(str, Enum):
    vegetable = "vegetable"
    shrub = "shrub"
    tree = "tree"


class ClassificationBase(BaseModel):
    name: ClassificationEnum

    class Config:
        orm_mode = True


class ClassificationCreate(ClassificationBase):
    pass


class ClassificationRead(ClassificationBase):
    id: int


class ClassificationUpdate(ClassificationBase):
    id: int


class ClassificationDelete(ClassificationBase):
    id: int
