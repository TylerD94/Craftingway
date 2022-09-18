import bot
import classes.secret as secret


if __name__ == '__main__':
    bot.start(**secret.check_for_secret())
