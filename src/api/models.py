#!/usr/bin/env python


"""
api/models.py:
    Athena API models.
"""


from api import database


class Command(database.Model):
    __tablename__ = "commands"
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    command = database.Column(database.String(128), nullable=False)
    message = database.Column(database.String(256), nullable=False)
    user_level = database.Column(database.Integer)
    cooldown = database.Column(database.Integer)
    alias = database.Column(database.String(128), nullable=True)

    def __init__(self, command, message, user_level, cooldown, alias):
        self.command = command
        self.message = message
        self.user_level = user_level
        self.cooldown = cooldown
        self.alias = alias
