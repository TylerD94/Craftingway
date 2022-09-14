from classes.user import User


class Users:
    def __init__(self):
        self.users = []

    def get_user(self, user_name):
        for user in self.users:
            if user.user_name == user_name:
                return user

        new_user = User(user_name)
        self.users.append(new_user)
        return new_user
