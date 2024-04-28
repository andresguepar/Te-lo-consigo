
from interfaces.IMessage import IMessage


class ShowInScreen(IMessage):
     def send(self, user, message):
        print(f"User {user}: {message}")