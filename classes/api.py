import pyxivapi
from classes.item import Item


# TODO: Put in error handling. Check to ensure that item exists before continuing
class API:
    def __init__(self, api_tkn):
        self.client = pyxivapi.XIVAPIClient(api_key=api_tkn)

    def display_help(self):
        with open("data\\help.txt", 'r') as f:
            help_message = f.read()
            return help_message

    async def get_item(self, item_name):
        item = Item(self.client, item_name)
        return item

    async def crafting_recipe(self, item):
        ingredients = await item.get_ingredients()
        amounts = await item.get_quantities()

        recipe = []

        for x in range(8):
            if ingredients['Results'][0][f'ItemIngredient{x}']:
                recipe.append({
                    # This gets the name of each ingredient
                    ingredients['Results'][0][f'ItemIngredient{x}']['Name']:
                    # This gets the quantity of each ingredient
                        amounts['Results'][0][f'AmountIngredient{x}']
                })

        return recipe
