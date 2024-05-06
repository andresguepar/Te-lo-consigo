from abc import ABC, abstractmethod
from domain.entities.User import User

class IMessage(ABC):
    """Interfaz para definir métodos de envío de mensajes."""

    @abstractmethod
    def send(self, user: User, message: str):
        """Método abstracto para enviar un mensaje a un usuario.

        Args:
            user (User): El usuario al que se enviará el mensaje.
            message (str): El mensaje que se enviará.

        Raises:
            NotImplementedError: Si el método no está implementado en la clase derivada.
        """
        pass
