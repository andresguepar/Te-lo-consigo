from interfaces.IDataManager import IDataManager  # Importa la interfaz IDataManager desde el módulo interfaces

# Clase MassiveDataService que implementa la interfaz IDataManager
class MassiveDataService(IDataManager):
    # Método load que carga una cantidad masiva de productos
    def load(self, product):
        """
        Carga una cantidad masiva de productos.

        Parameters:
            product: El producto a ser cargado.
        """
        print(f"Loading massive quantity of products: {product.name}, {product.description}")
