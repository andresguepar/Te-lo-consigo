from interfaces.IDataManager import IDataManager

class MassiveDataService(IDataManager):
    def load(self, product):
        print(f"Loading massive quantity of products: {product.name}, {product.description}")