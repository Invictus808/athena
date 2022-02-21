#!/usr/bin/env python


"""
api/endpoints/ping/ping.py:
    Athena API ping endpoint.
"""


# Third-party imports
# from flask import Blueprint
from flask_restx import Namespace, Resource

ping_endpoint = Namespace(
    name="ping",
    description="/ping endpoint used to test reachability of the Athena API.",
    path="/api/ping",
    # decorators=None,
    validate=True,
    ordered=True,
    # authorizations=None,
)


class Ping(Resource):
    def get(self):
        return {"message": "pong", "status": "success"}


ping_endpoint.add_resource(Ping, "")
