from interfaces.IDataManager import IDataManager  # Importa la interfaz IDataManager desde el módulo interfaces

# Clase APIDataService que implementa la interfaz IDataManager
class APIDataService(IDataManager):
    # Método load que carga un producto utilizando la API
    def load(self, product):
        """
        Carga el producto utilizando la API.

        Parameters:
            product: El producto a ser cargado.
        """
        print(f"Loading the product: {product.name}, {product.description} by the API")
