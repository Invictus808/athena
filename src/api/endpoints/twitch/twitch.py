#!/usr/bin/env python


"""
api/endpoints/twitch/twitch.py:
    Athena API Twitch endpoint.
"""


from flask import request
from flask_restx import Namespace, Resource

from api import database
from api.models import Command

# Define Twitch endpoint namespace
twitch_endpoint = Namespace(
    name="twitch",
    description="/twitch endpoint used to add, modify, delete, and retrieve chatbot commands.",
    path="/api/twitch",
    # decorators=None,
    validate=True,
    ordered=True,
    # authorizations=None,
)


# Define Twitch endpoint model
# twitch_endpoint_model = twitch_endpoint.model(
#     "Twitch",
#     {
#         "message": fields.String(
#             required=True, description="Message from Twitch endpoint."
#         ),
#         "status": fields.String(
#             required=True, description="Status from Twitch endpoint."
#         ),
#     },
# )


# Define add command endpoint class
class AddCommand(Resource):
    # Define add command endpoint POST
    def post(self):
        data = request.get_json()
        command = data.get("command")
        message = data.get("message")
        user_level = data.get("user_level")
        cooldown = data.get("cooldown")
        alias = data.get("alias")

        database.session.add(
            Command(
                command=command,
                message=message,
                user_level=user_level,
                cooldown=cooldown,
                alias=alias,
            )
        )
        database.session.commit()

        response = {"message": f"The command {command} was successfully added!"}

        return response, 201


twitch_endpoint.add_resource(AddCommand, "/commands/add")
