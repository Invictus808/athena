#!/usr/bin/env python


"""
api/configurations.py:
    Athena API API module.
"""


class BaseConfiguration:
    TESTING = False


class DevelopmentConfiguration(BaseConfiguration):
    pass


class TestingConfiguration(BaseConfiguration):
    TESTING = True


class ProductionConfiguration(BaseConfiguration):
    pass
