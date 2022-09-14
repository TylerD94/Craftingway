import discord
from discord.ext.commands import Bot
from classes.api import API
from classes.user import User

intents = discord.Intents.all()
bot = Bot(command_prefix="!", intents=intents)
users = []


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await check_command(message)


async def check_command(message):
    user = get_user(message.author)

    if message.content.startswith("!lookup "):  # Looks up an item by name, needs check for if item doesn't exist
        await lookup_item(message)
    elif message.content.startswith("!additem "):  # Adds item to user's saved items list
        await send_message(message, user.add_item(await api.get_item(message.content[9:])))
    elif message.content.startswith("!removeitem "):  # Removes item from user's saved items list
        await send_message(message, user.remove_item(message.content[12:]))
    elif message.content.startswith("!saveditems"):  # Displays user's saved items list
        await send_message(message, user.get_saved_items())
    elif message.content.startswith("!help"):  # Displays help text
        await send_message(message, api.display_help())
    else:
        return


def get_user(user_name):
    for user in users:
        if user.user_name == user_name:
            return user

    new_user = User(user_name)
    users.append(new_user)
    return new_user


async def lookup_item(message):
    item = await api.get_item(message.content[8:])
    recipe = await api.crafting_recipe(item)
    msg = create_recipe_message(recipe)
    await send_message(message, msg)


def create_recipe_message(recipe):
    msg = ''
    for d in recipe:
        for key in d:
            value = d[key]
            msg += f'{key}: {value} required.\n'
    return msg


async def send_message(message, response):
    await message.channel.send(response)


def start(bot_tkn, api_tkn):
    global api
    api = API(api_tkn)
    bot.run(bot_tkn)
