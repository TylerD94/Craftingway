import json
import os


def get_secret():
    secret = {
        'bot-token': os.environ.get("CRAFTINGWAY_API_KEY"),
        'api-token': os.environ.get("XIVAPI_KEY")
    }

    return secret

