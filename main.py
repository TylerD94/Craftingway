import bot
import classes.secret as secret


def run():
    s = secret.check_for_secret()
    bot.start(s['bot-token'], s['api-token'])


if __name__ == '__main__':
    run()
