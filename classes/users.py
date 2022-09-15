from classes.user import User


class Users:
    def __init__(self):
        self.user_list = []

    def get_user(self, user_name):
        for user in self.user_list:
            if user.user_name == user_name:
                return user

        new_user = User(user_name)
        self.user_list.append(new_user)
        return new_user
