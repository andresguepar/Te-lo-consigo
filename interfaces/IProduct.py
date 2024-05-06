from abc import abstractmethod, ABCMeta  # Importa las clases abstractas ABCMeta y abstractmethod desde el módulo abc

# Clase abstracta IProduct con metaclass ABCMeta para definir una clase abstracta
class IProduct(metaclass=ABCMeta):
    # Método abstracto para agregar un producto
    @abstractmethod
    def Add(self):
        """
        Método abstracto para agregar un producto.
        """
        pass

    # Método abstracto para eliminar un producto
    @abstractmethod
    def Delete(self):
        """
        Método abstracto para eliminar un producto.
        """
        pass

    # Método abstracto para editar un producto
    @abstractmethod
    def Edit(self):
        """
        Método abstracto para editar un producto.
        """
        pass

    # Método abstracto para listar productos
    @abstractmethod
    def List(self):
        """
        Método abstracto para listar productos.
        """
        pass
