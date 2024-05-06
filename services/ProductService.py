from abc import ABC  # Importa la clase ABC desde el módulo abc
from domain.entities.DetailProduct import DetailProduct  # Importa la clase DetailProduct desde el módulo domain.entities
from domain.enums.Category import Category  # Importa la clase Category desde el módulo domain.enums

# Clase abstracta ProductService que hereda de ABC (Abstract Base Class)
class ProductService(ABC):
    # Constructor de la clase
    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos
        self.product = []

    # Método para agregar un producto a la lista
    def Add(self, product: DetailProduct):
        """
        Añade un producto a la lista de productos.

        Parameters:
            product (DetailProduct): El producto a ser añadido.
        """
        self.product.append(product)

    # Método para eliminar un producto de la lista por su índice
    def Delete(self, id: int):
        """
        Elimina un producto de la lista de productos por su índice.

        Parameters:
            id (int): El índice del producto a ser eliminado.
        """
        del self.product[id]

    # Método para editar un producto en la lista por su índice
    def Edit(self, id: str, new_product: DetailProduct):
        """
        Edita un producto en la lista de productos por su índice.

        Parameters:
            id (str): El índice del producto a ser editado.
            new_product (DetailProduct): El nuevo producto que reemplazará al existente.
        """
        self.product[id] = new_product

    # Método para listar todos los productos
    def List(self):
        """
        Lista todos los productos en la lista de productos.
        """
        for i, product in enumerate(self.product):
            # Obtiene el nombre de la categoría del producto usando su número de categoría
            num = product.category
            category = Category.get_category(num)
            # Imprime la información del producto
            print(f"Product {i}| Name: {product.name}, Description: {product.description}, Price: {product.price}, Category: {category.name}")
