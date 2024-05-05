from abc import ABC, abstractmethod

from domain.entities.User import User

class IMessage(ABC):
     
     @abstractmethod
     def send(self, user: User, message: str):
        pass