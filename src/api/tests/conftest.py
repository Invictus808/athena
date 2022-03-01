#!/usr/bin/env python


"""
conftest.py:
    Athena API test configurations.
"""


import pytest

from api import create_app


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("api.configurations.TestingConfiguration")
    with app.app_context():
        yield app
