import discord
from discord.ext.commands import Bot
from api import API

intents = discord.Intents.all()
bot = Bot(command_prefix="!", intents=intents)
api = None


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.startswith("!"):
        await call_api(message, message.content[1:])
    else:
        return


async def call_api(message, item):
    result = await api.get_ingredients(item)
    await send_message(message, result)


async def send_message(message, result):
    msg = ''
    for d in result:
        for key in d:
            value = d[key]
            msg += f'{key}: {value} required.\n'
    await message.channel.send(msg)


def start(BOT, api_tkn):
    global api
    api = API(api_tkn)
    bot.run(BOT)
