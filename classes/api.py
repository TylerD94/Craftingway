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


