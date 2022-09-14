import json
import os


def check_for_secret():
    if os.path.exists('data/secret.json'):
        return load_secret()
    else:
        return create_secret()


def load_secret():
    with open('data/secret.json', 'r') as f:
        secret = json.load(f)
        return secret


def create_secret():
    secret = {
        'bot-token': '',
        'api-token': ''
    }

    print('secret.json not found in data folder! provide your discord bot token, and your xivapi token.')

    secret['bot-token'] = input('bot-token >>> ')
    secret['api-token'] = input('api-token >>> ')

    secret_json = json.dumps(secret)

    with open('data/secret.json', 'w') as f:
        f.write(secret_json)

    return secret
