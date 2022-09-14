class Item:
    def __init__(self, client, item_name):
        self.client = client
        self.item_name = item_name

    async def get_item(self):
        item = await self.client.index_search(
            name=self.item_name,
            indexes=["Recipe"],
            columns=[
                "ItemIngredient0",
                "ItemIngredient1",
                "ItemIngredient2",
                "ItemIngredient3",
                "ItemIngredient4",
                "ItemIngredient5",
                "ItemIngredient6",
                "ItemIngredient7",
                "ItemIngredient8"
            ]
        )

        return item

    async def get_crafting_materials(self):
        materials = await self.client.index_search(
            name=self.item_name,
            indexes=["Recipe"],
            columns=[
                "AmountIngredient0",
                "AmountIngredient1",
                "AmountIngredient2",
                "AmountIngredient3",
                "AmountIngredient4",
                "AmountIngredient5",
                "AmountIngredient6",
                "AmountIngredient7"
            ]
        )

        return materials
