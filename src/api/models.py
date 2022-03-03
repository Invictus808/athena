#!/usr/bin/env python


"""
api/models.py:
    Athena API models.
"""


from sqlalchemy.sql import func

from api import database


class User(database.Model):
    __tablename__ = "users"
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    username = database.Column(database.String(128), nullable=False)
    email = database.Column(database.String(128), nullable=False)
    active = database.Column(database.String(128), default=True, nullable=False)
    created_date = database.Column(
        database.DateTime, default=func.now(), nullable=False
    )

    def __init__(self, username, email):
        self.username = username
        self.email = email
