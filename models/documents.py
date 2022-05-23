from __future__ import annotations

from aiogram_utils.mongoengine import Document
from mongoengine import StringField, IntField


class Config(Document):
    sheet_id: str = StringField()
    group_to_forward_id: int = IntField()


class Record(Document):
    date: str = StringField()
    full_name: str = StringField()
    position: str = StringField()
    institution: str = StringField()
    social: str = StringField()
    email: str = StringField()
    tel: str = StringField()
