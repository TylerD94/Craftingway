import bot
import os
import json

if __name__ == '__main__':
    bot_token = ''
    api_token = ''

    # TODO: Move this into a class all of its own
    # TODO: Make functionality that if secret.json doesn't exist, a new file can be created taking in the needed API tokens
    # TODO: Create a nicer message template
    # TODO: Implement search for gathering locations of materials

    if os.path.exists('secret.json'):
        with open('secret.json', 'r') as f:
            lines = json.load(f)
            bot_token = lines['bot-token']
            api_token = lines['api-token']

    bot.start(bot_token, api_token)
