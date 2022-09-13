import pyxivapi


# TODO: Put in error handling. Check to ensure that item exists before continuing
class API:
    def __init__(self, api_tkn):
        self.api_tkn = api_tkn
        self.client = pyxivapi.XIVAPIClient(api_key=self.api_tkn)

    def display_help(self):
        help_message = '!lookup "ITEM NAME": Allows you to look up the recipe for an item by name.\n' \
                       '!help: Displays this help message.'
        return help_message

    async def get_ingredients(self, item_name):
        recipe = await self.client.index_search(
            name=item_name,
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
        amounts = await self.client.index_search(
            name=item_name,
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

        ingredients = []
        print(recipe)

        for x in range(8):
            if recipe['Results'][0][f'ItemIngredient{x}']:
                print(recipe['Results'][0][f'ItemIngredient{x}'])
                ingredients.append({
                    recipe['Results'][0][f'ItemIngredient{x}']['Name']: amounts['Results'][0][f'AmountIngredient{x}']
                })

        return ingredients
