import discord
from discord.ext.commands import Bot
from api import API

intents = discord.Intents.all()
bot = Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.startswith("!lookup "):  # Looks up an item by name, needs check for if item doesn't exist
        await call_api(message, message.content[8:])
    elif message.content.startswith("!help"):
        await send_help_message(message)
    else:
        return


async def call_api(message, item):
    recipe = await api.get_crafting_recipe(item)
    await send_recipe_message(message, recipe)


async def send_help_message(message):
    await message.channel.send(api.display_help())


async def send_recipe_message(message, result):
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
