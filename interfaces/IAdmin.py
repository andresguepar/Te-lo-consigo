from abc import ABCMeta, abstractmethod

class IAdmin(metaclass=ABCMeta):
    """Interfaz para definir operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para la administración."""

    @abstractmethod
    def Add(self):
        """Método abstracto para agregar un elemento."""
        pass

    @abstractmethod
    def Delete(self):
        """Método abstracto para eliminar un elemento."""
        pass

    @abstractmethod
    def Edit(self):
        """Método abstracto para editar un elemento."""
        pass

    @abstractmethod
    def List(self):
        """Método abstracto para listar todos los elementos."""
        pass
