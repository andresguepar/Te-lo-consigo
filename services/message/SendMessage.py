
from interfaces.IMessage import IMessage


class SendMessage(IMessage):
    def send(self, user, message):
        print(f"Sending email to {user}: {message}")