from domain.enums.Category import Category

class Product:
    """Clase para representar un producto.

    Attributes:
        id (int): El identificador único del producto.
        name (str): El nombre del producto.
        category (Category): La categoría a la que pertenece el producto.
    """

    def __init__(self, id=None, name=None, category=None):
        """Inicializa un nuevo objeto Producto.

        Args:
            id (int, optional): El identificador único del producto.
            name (str, optional): El nombre del producto.
            category (Category, optional): La categoría a la que pertenece el producto.
        """
        self.id = id
        self.name = name
        self.category = category