#!/usr/bin/env python


"""
functional/test_ping.py:
    Test for Athena API Twitch endpoint.
"""


import json


def test_add_command(test_app, test_database):
    # given
    client = test_app.test_client()

    # when
    response = client.post(
        "/api/twitch/commands/add",
        data=json.dumps(
            {
                "command": "gg",
                "message": "good game",
                "user_level": 4,
                "cooldown": 10,
                "alias": None,
            }
        ),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    # then
    assert response.status_code == 201
    assert "The command gg was successfully added!" in data["message"]
