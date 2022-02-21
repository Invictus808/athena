#!/usr/bin/env python


"""
manage.py:
    Runs Athena API.
"""


import logging
import logging.config

import yaml
from api import create_app
from flask.cli import FlaskGroup

api_configurations = yaml.safe_load(open("api.cfg", "r"))
logging_configurations = yaml.safe_load(open("logging.cfg", "r"))
logging.config.dictConfig(logging_configurations)
logger = logging.getLogger("base")


def main(**kwargs) -> None:
    logger.info(
        f"{api_configurations['project']} v{api_configurations['version']} by {api_configurations['author']}"
    )
    logger.info(f"{api_configurations['copyright']}")
    logger.debug(
        f"Starting {api_configurations['project']} v{api_configurations['version']}..."
    )
    logger.debug(
        f"Started {api_configurations['project']} v{api_configurations['version']}."
    )

    cli = FlaskGroup(create_app=create_app)
    cli()

    logger.debug(
        f"Stopping {api_configurations['project']} v{api_configurations['version']}..."
    )
    logger.debug(
        f"Stopped {api_configurations['project']} v{api_configurations['version']}."
    )


if __name__ == "__main__":
    main(debug=not api_configurations["production"])
else:
    logger.error(f"{__file__} cannot be imported as a module")
