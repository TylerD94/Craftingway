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


@bot.command(name='craft', description='Returns crafting recipe')
async def craft(ctx, *args):
    msg = Messages(ctx, api, users, *args)
    await msg.lookup_item()


@bot.command(name='additem', description="Adds item to user's saved-items list")
async def add_item(ctx, *args):
    msg = Messages(ctx, api, users, *args)
    await msg.add_item()


@bot.command(name='removeitem', description="Removes item from user's saved-items list")
async def remove_item(ctx, *args):
    msg = Messages(ctx, api, users, *args)
    await msg.remove_item()


@bot.command(name='saveditems', description="Sends a message with the user's saved-items list")
async def saved_items(ctx):
    msg = Messages(ctx, api, users)
    await msg.saved_items()


@bot.command(name='info', description='Sends a help message')
async def help(ctx):
    msg = Messages(ctx, api, users)
    await msg.help()


def start(bot_tkn, api_tkn):
    global api
    global users
    api = API(api_tkn)
    users = Users()
    bot.run(bot_tkn)
