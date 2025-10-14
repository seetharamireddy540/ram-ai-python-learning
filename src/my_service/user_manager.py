
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def authenticate(self, username, password):
        return username in self.users and self.users[username] == password