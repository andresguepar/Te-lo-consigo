from abc import ABC  # Importa la clase ABC desde el módulo abc
from interfaces.IDataManager import IDataManager  # Importa la interfaz IDataManager desde el módulo interfaces
from domain.entities.DetailProduct import DetailProduct  # Importa la clase DetailProduct desde el módulo domain.entities

# Clase DataService
class DataService:
    # Constructor de la clase
    def __init__(self, product: IDataManager):
        """
        Inicializa un objeto DataService.

        Parameters:
            product (IDataManager): El gestor de datos utilizado para cargar los productos.
        """
        self.product = product

    # Método para cargar datos utilizando el gestor de datos proporcionado
    def load_data(self, product: DetailProduct):
        """
        Carga datos utilizando el gestor de datos proporcionado.

        Parameters:
            product (DetailProduct): El producto a ser cargado.
        """
        self.product.load(product)
