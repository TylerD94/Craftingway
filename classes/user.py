class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.saved_items = [None, None, None, None, None]

    def add_item(self, item):
        for saved_item in self.saved_items:
            if saved_item is None:
                self.saved_items[saved_item] = item
                return f"{item} added to list!"
            else:
                return "Saved items list full!"

    def remove_item(self, item):
        if self.saved_items.__contains__(item):
            self.saved_items.remove(item)
            return f"{item} removed from list!"

    def get_list(self):
        msg = ''
        for item in self.saved_items:
            if item is None:
                break
            else:
                msg += f"{item}\n"
        return msg
