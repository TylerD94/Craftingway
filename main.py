import bot
import os
import classes.secret as secret

def run():
    if os.path.exists('data/secret.json'):
        bot_token, api_token = secret.load_secret()
        bot.start(bot_token, api_token)
    else:
        print("No secret.json file found in data folder!")
        # Set up functionality to create secret.json




if __name__ == '__main__':
    run()

