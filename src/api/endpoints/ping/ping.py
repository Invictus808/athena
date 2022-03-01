#!/usr/bin/env python


"""
api/endpoints/ping/ping.py:
    Athena API ping endpoint.
"""


from flask_restx import Namespace, Resource, fields

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


# Define ping endpoint model
ping_endpoint_model = ping_endpoint.model(
    "Ping",
    {
        "message": fields.String(
            required=True, description="Message from ping endpoint."
        ),
        "status": fields.String(
            required=True, description="Status from ping endpoint."
        ),
    },
)


# Define ping endpoint class
class Ping(Resource):
    # Define ping endpoint GET
    @ping_endpoint.marshal_with(ping_endpoint_model)
    @ping_endpoint.response(200, "Successfully pinged endpoint.")
    @ping_endpoint.response(400, "Failed to ping endpoint.")
    def get(self):
        return {"message": "pong", "status": "success"}


# Add ping endpoint class to namespace
ping_endpoint.add_resource(Ping, "")
