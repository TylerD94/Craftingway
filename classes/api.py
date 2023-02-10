import os

import pyxivapi
from classes.item import Item


# TODO: Put in error handling. Check to ensure that item exists before continuing
class API:
    def __init__(self):
        self.client = pyxivapi.XIVAPIClient(api_key=os.environ.get("XIVAPI_KEY"))

    async def get_item(self, item_name):
        item = Item(self.client, item_name)
        return item


