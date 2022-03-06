#!/usr/bin/env python


"""
unit/test_configurations.py:
    Test for Athena API configurations.
"""


import os


def test_development_config(test_app):
    # given
    test_app.config.from_object("api.configurations.DevelopmentConfiguration")

    # then
    assert test_app.config["SECRET_KEY"] == "secret_key"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")


def test_testing_config(test_app):
    # given
    test_app.config.from_object("api.configurations.TestingConfiguration")

    # then
    assert test_app.config["SECRET_KEY"] == "secret_key"
    assert test_app.config["TESTING"]
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )


def test_production_config(test_app):
    # given
    test_app.config.from_object("api.configurations.ProductionConfiguration")

    # then
    assert test_app.config["SECRET_KEY"] == "secret_key"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
