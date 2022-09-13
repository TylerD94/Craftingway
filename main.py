import bot
import os
import json

if __name__ == '__main__':
    bot_token = ''
    api_token = ''

    if os.path.exists('secret.json'):
        with open('secret.json', 'r') as f:
            lines = json.load(f)
            bot_token = lines['bot-token']
            api_token = lines['api-token']

    bot.start(bot_token, api_token)
