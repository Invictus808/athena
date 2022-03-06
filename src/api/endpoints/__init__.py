#!/usr/bin/env python


"""
api/endpoints/__init__.py:
    Athena API endpoints module.
"""


from .ping import ping_endpoint
from .twitch import twitch_endpoint

ping_endpoint = ping_endpoint
twitch_endpoint = twitch_endpoint
