from abc import ABC, abstractmethod

from model.User import User

class IMessage(ABC):
     
     @abstractmethod
     def send(self, user: User, message: str):
        pass