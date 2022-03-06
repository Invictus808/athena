#!/usr/bin/env python


"""
conftest.py:
    Athena API test configurations.
"""


import pytest

from api import create_app, database


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("api.configurations.TestingConfiguration")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    database.create_all()
    yield database
    database.session.remove()
    database.drop_all()
