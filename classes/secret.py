import json


def load_secret():
    with open('data/secret.json', 'r') as f:
        lines = json.load(f)
        return lines['bot-token'], lines['api-token']


def create_secret():
    return
    # TODO: Build functionality to create secret.json file.
