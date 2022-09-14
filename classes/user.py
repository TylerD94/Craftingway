class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.saved_items = []

    def add_item(self, item):
        self.saved_items.append(item)
        return f"Added {item.item_name} to saved items."

    def remove_item(self, item_name):
        for item in self.saved_items:
            if item.item_name == item_name:
                self.saved_items.remove(item)
                return f"Removed {item_name} from saved items."

        return f"{item_name} not found."

    def get_saved_items(self):
        msg = ''

        if len(self.saved_items) == 0:
            msg = "No saved items."
        else:
            for x in range(len(self.saved_items)):
                msg += f"Saved item #{x}: {self.saved_items[x].item_name}\n"

        return msg
