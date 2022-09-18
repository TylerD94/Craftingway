class Item:
    def __init__(self, client, item_name):
        self.client = client
        self.item_name = item_name

    async def get_recipe(self):
        recipe = await self.client.index_search(
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
                "ItemIngredient8",
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

        recipe_dict = self.crafting_recipe(recipe)
        return self.create_recipe_message(**recipe_dict)

    def crafting_recipe(self, recipe):
        recipe_dict = {}

        for x in range(8):
            if recipe['Results'][0][f'ItemIngredient{x}']:
                recipe_dict.update({
                    # This gets the name of each ingredient
                    recipe['Results'][0][f'ItemIngredient{x}']['Name']:
                    # This gets the quantity of each ingredient
                        recipe['Results'][0][f'AmountIngredient{x}']
                })
        return recipe_dict

    def create_recipe_message(self, **recipes):
        msg = ''
        for recipe in recipes:
            msg += f'{recipe}: {recipes[recipe]} required.\n'

        return msg
