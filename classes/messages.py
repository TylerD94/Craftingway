class Messages:
    def __init__(self, context, api, users, *item_name):
        self.context = context
        self.content = self.define_content(item_name)
        self.api = api
        self.users = users
        self.user = self.users.get_user(self.context.author)

    def define_content(self, item_names):
        content = ''

        for item_name in item_names:
            content += f'{item_name} '

        return content

    async def lookup_item(self):
        item = await self.api.get_item(self.content)
        recipe = await item.get_recipe()
        await self.send_message(recipe)

    async def add_item(self):
        item = await self.api.get_item(self.content)
        await self.send_message(self.user.add_item(item))

    async def remove_item(self):
        await self.send_message(self.user.remove_item(self.content))

    async def saved_items(self):
        await self.send_message(self.user.get_saved_items())

    async def send_message(self, response):
        await self.context.channel.send(response)
