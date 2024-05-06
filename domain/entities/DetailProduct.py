
from domain.entities.Product import Product
from domain.enums.Category import Category
class DetailProduct:
    """Clase para representar los detalles de un producto.

    Attributes:
        id (int): El identificador único del detalle del producto.
        product (Product): El producto al que pertenecen estos detalles.
        name (str): El nombre del detalle del producto.
        description (str): La descripción del detalle del producto.
        price (float): El precio del detalle del producto.
        category (Category): La categoría a la que pertenece el detalle del producto.
        stock (int): La cantidad en stock del detalle del producto.
    """

    def __init__(self, id=None, product=None, name=None, description=None, price=None, category=None, stock=None):
        """Inicializa un nuevo objeto DetailProduct.

        Args:
            id (int, optional): El identificador único del detalle del producto.
            product (Product, optional): El producto al que pertenecen estos detalles.
            name (str, optional): El nombre del detalle del producto.
            description (str, optional): La descripción del detalle del producto.
            price (float, optional): El precio del detalle del producto.
            category (Category, optional): La categoría a la que pertenece el detalle del producto.
            stock (int, optional): La cantidad en stock del detalle del producto.
        """
        self.id = id
        self.product = product
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
