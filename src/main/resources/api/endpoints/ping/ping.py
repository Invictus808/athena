#!/usr/bin/env python


"""
api/endpoints/ping/ping.py:
    Athena API ping endpoint.
"""


from flask_restx import Namespace, Resource

# Define ping endpoint namespace
ping_endpoint = Namespace(
    name="ping",
    description="/ping endpoint used to test reachability of the Athena API.",
    path="/api/ping",
    # decorators=None,
    validate=True,
    ordered=True,
    # authorizations=None,
)


# Define ping endpoint class
class Ping(Resource):
    # Define ping endpoint GET
    def get(self):
        return {"message": "pong", "status": "success"}


# Add ping endpoint class to namespace
ping_endpoint.add_resource(Ping, "")
