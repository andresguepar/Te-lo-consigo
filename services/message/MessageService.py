from abc import ABC

from interfaces.IMessage import IMessage

class MessageService:
    def __init__(self, message: IMessage):
        self.message = message

    def send_notification(self, user, message):
        self.message.send(user, message)
