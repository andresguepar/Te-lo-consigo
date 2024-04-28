from abc import ABC
import model.User as User

class AdminService (ABC):
    def __init__(self):

        self.user = []

    def Add(self, user: User):

        self.user.append(user)

    def Delete(self, id: int):
        del self.user[id]

    def Edit(self, id: str, new_user: User):
        self.user[id] = new_user

    def List(self):
        for i, user in enumerate(self.user):
            print(f"User {i}: {user.name}, {user.phone} {user.email}")

