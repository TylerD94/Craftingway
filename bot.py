import discord
from discord.ext.commands import Bot
from classes.api import API
from classes.messages import Messages
from classes.users import Users

intents = discord.Intents.all()
bot = Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = Messages(message, api, users)
    await msg.new_message()


def start(bot_tkn, api_tkn):
    global api
    global users
    api = API(api_tkn)
    users = Users()
    bot.run(bot_tkn)
