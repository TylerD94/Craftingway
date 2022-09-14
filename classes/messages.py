class Messages:
    def __init__(self, message, api, users):
        self.message = message
        self.api = api
        self.users = users

    async def new_message(self):
        user = self.users.get_user(self.message.author)
        content = self.message.content

        if content.startswith("!lookup "):  # Looks up an item by name, needs check for if item doesn't exist
            await self.lookup_item()
        elif content.startswith("!additem "):  # Adds item to user's saved items list
            await self.send_message(user.add_item(await self.api.get_item(content[9:])))
        elif content.startswith("!removeitem "):  # Removes item from user's saved items list
            await self.send_message(user.remove_item(content[12:]))
        elif content.startswith("!saveditems"):  # Displays user's saved items list
            await self.send_message(user.get_saved_items())
        elif content.startswith("!help"):  # Displays help text
            await self.send_message(self.api.display_help())
        else:
            return

    async def lookup_item(self):
        item = await self.api.get_item(self.message.content[8:])
        recipe = await self.api.crafting_recipe(item)
        msg = item.create_recipe_message(recipe)
        await self.send_message(msg)

    async def send_message(self, response):
        await self.message.channel.send(response)
