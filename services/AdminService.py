from abc import ABC  # Importa la clase ABC desde el módulo abc
from domain.entities.User import User  # Importa la clase User desde el módulo domain.entities

# Clase abstracta AdminService que hereda de ABC (Abstract Base Class)
class AdminService(ABC):
    # Constructor de la clase
    def __init__(self):
        # Inicializa una lista vacía para almacenar los usuarios
        self.user = []

    # Método para agregar un usuario a la lista
    def Add(self, user: User):
        """
        Añade un usuario a la lista de usuarios.

        Parameters:
            user (User): El usuario a ser añadido.
        """
        self.user.append(user)

    # Método para eliminar un usuario de la lista por su índice
    def Delete(self, id: int):
        """
        Elimina un usuario de la lista de usuarios por su índice.

        Parameters:
            id (int): El índice del usuario a ser eliminado.
        """
        del self.user[id]

    # Método para editar un usuario en la lista por su índice
    def Edit(self, id: str, new_user: User):
        """
        Edita un usuario en la lista de usuarios por su índice.

        Parameters:
            id (str): El índice del usuario a ser editado.
            new_user (User): El nuevo usuario que reemplazará al existente.
        """
        self.user[id] = new_user

    # Método para listar todos los usuarios
    def List(self):
        """
        Lista todos los usuarios en la lista de usuarios.
        """
        for i, user in enumerate(self.user):
            # Imprime la información del usuario
            print(f"User {i}: {user.name}, {user.phone}, {user.email}")


