import bot
import os
import classes.secret as secret

def run():
    if os.path.exists('data/secret.json'):
        bot_token, api_token = secret.load_secret()
        bot.start(bot_token, api_token)
    else:
        bot_token, api_token = secret.create_secret()
        bot.start(bot_token, api_token)

if __name__ == '__main__':
    run()

