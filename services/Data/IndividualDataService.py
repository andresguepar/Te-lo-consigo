from interfaces.IDataManager import IDataManager

class IndividualDataService(IDataManager):
    def load(self, product):
        print(f"Loading by individual product: {product.name}, {product.description}")