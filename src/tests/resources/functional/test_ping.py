#!/usr/bin/env python


"""
functional/test_ping.py:
    Test for Athena API ping endpoint.
"""


# Built-in imports
import json


def test_ping(test_app):
    # given
    client = test_app.test_client()

    # when
    response = client.get("/api/ping")
    data = json.loads(response.data.decode())

    # then
    assert response.status_code == 200
    assert data["message"] == "pong"
    assert data["status"] == "success"
