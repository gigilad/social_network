from User import User


class UserFactory:
    @staticmethod
    def create_user(username, password, users):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password needs to be between 4 to 8 characters")
        if len(username) == 0:
            raise ValueError("Username cannot be empty")
        if UserFactory.is_username_exists(username, users):
            raise ValueError("User already exists")
        return User(username, password)

    @staticmethod
    def is_username_exists(username, users):
        for user in users:
            if user.get_username() == username:
                return True
        return False