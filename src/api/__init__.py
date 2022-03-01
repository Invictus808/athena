#!/usr/bin/env python


"""
api/__init__.py:
    Athena API api module.
"""


import logging
import logging.config
import os

import yaml
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

api_configurations = yaml.safe_load(open("api.cfg", "r"))
logging_configurations = yaml.safe_load(open("logging.cfg", "r"))
logging.config.dictConfig(logging_configurations)
logger = logging.getLogger("base")


# Instantiate the database
logger.debug("Intantiating database...")
database = SQLAlchemy()
logger.debug("Instantiated database.")


# Instantiate API
def create_app():
    # Instantiate the application
    logger.debug("Instantiating Flask application...")
    app = Flask(__name__)
    logger.debug("Instantiated Flask application.")

    # Set configurations
    logger.debug("Setting configurations...")
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    logger.debug(f"Using: {app_settings}")
    logger.debug("Set configurations.")

    # Set up database with API
    logger.debug("Setting up database with application...")
    database.init_app(app)
    logger.debug("Set database with application.")

    api = Api(
        app=app,
        version=api_configurations["version"],
        title=api_configurations["project"],
        description=api_configurations["copyright"],
        contact=api_configurations["maintainer"],
        contact_email=api_configurations["email"],
        doc="/api",
        default_swagger_filename="athena.json",
    )

    from .endpoints import ping_endpoint

    api.add_namespace(ping_endpoint)

    # Shell context for the Flask CLI
    @app.shell_context_processor
    def ctx():

        return {
            "app": app,
            # 'database': database,
        }

    return app
