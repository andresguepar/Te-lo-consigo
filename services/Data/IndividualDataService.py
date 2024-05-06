from interfaces.IDataManager import IDataManager  # Importa la interfaz IDataManager desde el módulo interfaces

# Clase IndividualDataService que implementa la interfaz IDataManager
class IndividualDataService(IDataManager):
    # Método load que carga un producto individualmente
    def load(self, product):
        """
        Carga un producto individualmente.

        Parameters:
            product: El producto a ser cargado.
        """
        print(f"Loading by individual product: {product.name}, {product.description}")
