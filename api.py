import pyxivapi
from item import Item


# TODO: Put in error handling. Check to ensure that item exists before continuing
class API:
    def __init__(self, api_tkn):
        self.client = pyxivapi.XIVAPIClient(api_key=api_tkn)

    def display_help(self):
        with open("data\\help.txt", 'r') as f:
            help_message = f.read()
            return help_message

    async def get_crafting_recipe(self, item_name):
        item = Item(self.client, item_name)
        ingredients = await item.get_item()
        amounts = await item.get_crafting_materials()

        recipe = []

        for x in range(8):
            if ingredients['Results'][0][f'ItemIngredient{x}']:
                recipe.append({
                    ingredients['Results'][0][f'ItemIngredient{x}']['Name']: amounts['Results'][0][f'AmountIngredient{x}']
                })

        return recipe
