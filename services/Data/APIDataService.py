from interfaces.IDataManager import IDataManager

class APIDataService(IDataManager):
    def load(self, product):
        print(f"Loading the product: {product.name}, {product.description} by the API")