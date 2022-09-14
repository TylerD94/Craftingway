class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.saved_items = []

    def add_item(self, item):
        self.saved_items.append(item)
        print([item.item_name for item in self.saved_items])

    def remove_item(self, item):
        if self.saved_items.__contains__(item):
            self.saved_items.remove(item)
            return f"{item} removed from list!"

    def get_list(self):
        msg = ''

        if len(self.saved_items) == 0:
            msg = "No saved items."
        else:
            for x in range(len(self.saved_items)):
                msg += f"Saved item #{x}: {self.saved_items[x].item_name}"

        return msg
