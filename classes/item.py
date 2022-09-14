class Item:
    def __init__(self, client, item_name):
        self.client = client
        self.item_name = item_name

    async def get_ingredients(self):
        ingredients = await self.client.index_search(
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

        return ingredients

    async def get_quantities(self):
        quantities = await self.client.index_search(
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

        return quantities

    def create_recipe_message(self, recipe):
        msg = ''
        for d in recipe:
            for key in d:
                value = d[key]
                msg += f'{key}: {value} required.\n'
        return msg