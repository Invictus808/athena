#!/usr/bin/env python


"""
api/configurations.py:
    Athena API API module.
"""


import os


class BaseConfiguration:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfiguration(BaseConfiguration):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfiguration(BaseConfiguration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfiguration(BaseConfiguration):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
